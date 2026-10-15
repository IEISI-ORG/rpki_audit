import csv
import glob
import json
import os
from collections import Counter, defaultdict
import rov_utils

# Single source of truth — defined in rov_utils.py
TIER_1_FIREWALL        = rov_utils.TIER_1_ASNS
IS_NON_TRANSIT         = rov_utils.NON_TRANSIT_ASNS
RATIO                  = rov_utils.PROVIDER_RATIO
CONFIRM_REGIONS        = rov_utils.RRC_CONFIRM_REGIONS
IXP_PRUNE_THRESHOLD    = rov_utils.CONE_QUALITY_THRESHOLD  # 5.0 %
EVIDENCE_REQUIRED      = rov_utils.EVIDENCE_REQUIRED_ASNS
UP_RANK_MAX_RATIO      = rov_utils.PATH_UP_RANK_MAX_RATIO
TOP_DOWN_MAX_PASSES    = 10
STUB_RATIO_MIN_REGIONS = rov_utils.STUB_RATIO_MIN_REGIONS

# Export evidence bits per ordered pair (x, c), from bgp-extractor's exports.csv:
# x passed the route it learned from c on to another AS (beyond the collector end of the path),
# and that AS was a Tier 1 (x not), per address family.
EV_BEYOND_4, EV_BEYOND_6, EV_T1_4, EV_T1_6 = 1, 2, 4, 8
EV_BEYOND = EV_BEYOND_4 | EV_BEYOND_6
EV_T1 = EV_T1_4 | EV_T1_6


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_scraped_metadata() -> dict:
    print("    - Loading ASN data from packed file...")
    data = rov_utils.load_all_asn_data()
    return {
        asn: {'name': d.get('name', 'Unknown'), 'cc': d.get('cc', 'XX'), 'cone': d.get('cone_size', 0)}
        for asn, d in data.items()
    }


def _find_collector_files() -> list[tuple[str, str]]:
    """
    Return [(rrc_name, filepath)] for every relationships.csv found under
    output/rrcNN/.  Falls back to the legacy single-file path if no
    per-collector directories exist.
    """
    files = []
    for rrc_name in rov_utils.RRC_COLLECTORS:
        path = os.path.join(rov_utils.DIR_RRC, rrc_name, "relationships.csv")
        if os.path.exists(path):
            files.append((rrc_name, path))

    if not files:
        legacy = rov_utils.FILE_RELATIONSHIPS
        if os.path.exists(legacy):
            print(f"    [!] No per-collector directories found; falling back to {legacy}")
            files.append(("rrc00", legacy))
        else:
            print(f"    [!] No relationship files found. Run bgp-extractor first.")
    return files


def load_multi_collector_relationships() -> tuple[dict, dict, dict]:
    """
    Load adjacency data from all available RRC collectors.

    Returns
    -------
    adj : {asn: set(neighbour_asns)}   — combined undirected adjacency (union)
    degrees : {asn: int}               — degree in the combined graph
    link_regions : {(min_asn, max_asn): set(region_str)}
        Set of geographic regions that independently observed this link.
        A link confirmed by both EU and APAC collectors is strong transit evidence;
        a link seen only from a single EU collector is suspect IXP peering.

    Multi-collector rationale
    -------------------------
    rrc00 at Amsterdam and rrc23 at Singapore are at completely different IXPs.
    A route-server adjacency fabricated at AMS-IX will NOT appear in Singapore
    BGP dumps.  A *real* transit link (e.g. Cogent → small stub) propagates
    globally and shows up in ALL collectors.

    The IXP route-server problem (RFC 7947 path stripping) cannot be detected
    by valley-free analysis alone because stripped paths look identical to
    transit paths.  Cross-regional confirmation is the primary defence;
    the excl_pct pruning pass below is the secondary backstop.
    """
    collector_files = _find_collector_files()
    if not collector_files:
        return None, None, None

    adj = defaultdict(set)
    link_regions: dict[tuple, set] = defaultdict(set)

    rrc_meta = rov_utils.RRC_COLLECTORS

    for rrc_name, filepath in collector_files:
        region = rrc_meta.get(rrc_name, {}).get("region", rrc_name)
        location = rrc_meta.get(rrc_name, {}).get("location", rrc_name)
        count = 0
        with open(filepath) as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) < 3:
                    continue
                as1, as2 = int(row[0]), int(row[1])
                adj[as1].add(as2)
                adj[as2].add(as1)
                link_regions[tuple(sorted((as1, as2)))].add(region)
                count += 1
        print(f"      {rrc_name} ({location}): {count:,} relationship rows")

    degrees = {asn: len(nbrs) for asn, nbrs in adj.items()}
    n_confirmed = sum(1 for regions in link_regions.values() if len(regions) >= CONFIRM_REGIONS)
    print(f"    - Combined: {len(degrees):,} ASNs, {len(link_regions):,} unique links")
    print(f"      Cross-regional confirmed (≥{CONFIRM_REGIONS} regions): {n_confirmed:,} links")
    return adj, degrees, link_regions


def load_exports(base_dir: str = "output") -> dict | None:
    """{(x, c): EV_* bits} from every <base_dir>/rrc*/exports.csv; None if there are none."""
    files = sorted(glob.glob(os.path.join(base_dir, "rrc*", "exports.csv")))
    if not files:
        return None
    ev: dict = defaultdict(int)
    for path in files:
        with open(path) as f:
            reader = csv.reader(f)
            next(reader, None)
            for x, c, af, _paths, beyond, to_t1 in reader:
                bits = 0
                if int(beyond):
                    bits |= EV_BEYOND_6 if af == "6" else EV_BEYOND_4
                if int(to_t1):
                    bits |= EV_T1_6 if af == "6" else EV_T1_4
                ev[(int(x), int(c))] |= bits
    return dict(ev)


def load_triples(base_dir: str = "output") -> dict | None:
    """{x: {(y, c, af)}} from every <base_dir>/rrc*/triples.csv (x passed the route it learned
    from c on to y); None if there are none."""
    files = sorted(glob.glob(os.path.join(base_dir, "rrc*", "triples.csv")))
    if not files:
        return None
    tr: dict = defaultdict(set)
    for path in files:
        with open(path) as f:
            next(f, None)
            for line in f:
                af, y, x, c = line.rstrip("\n").split(",")
                tr[int(x)].add((int(y), int(c), int(af)))
    return dict(tr)


# ---------------------------------------------------------------------------
# Path-based (top-down) inference
# ---------------------------------------------------------------------------

def transit_degrees(triples: dict) -> dict:
    """{x: number of distinct neighbours on either side of x where x is mid-path}."""
    return {x: len({y for y, _, _ in ts} | {c for _, c, _ in ts}) for x, ts in triples.items()}


def rank_positions(nodes, td: dict, degrees: dict) -> dict:
    """{asn: position}, top first: Tier 1s, then transit degree, degree, ASN."""
    order = sorted(nodes, key=lambda a: (a not in TIER_1_FIREWALL, -td.get(a, 0), -degrees.get(a, 0), a))
    return {a: i for i, a in enumerate(order)}


def _reaches(down: dict, src: int, dst: int) -> bool:
    """True when dst is in src's customer cone (so dst -> src would close a loop)."""
    seen, stack = {src}, [src]
    while stack:
        for n in down.get(stack.pop(), ()):
            if n == dst:
                return True
            if n not in seen:
                seen.add(n)
                stack.append(n)
    return False


def infer_top_down(triples: dict, pos: dict, td: dict) -> dict:
    """{provider: {customers}} from path triples, AS Rank style.

    x provides c when x passed c's route on to an AS y that is x's provider or a Tier 1: valley-free
    routing only exports customer routes up and across, and a Tier 1 is never a customer, so it
    is x's provider or peer. Tier 1s and non-transit ASes are never customers; an
    EVIDENCE_REQUIRED_ASNS member counts IPv4 triples only.
    Pass 0 visits ASes in rank order and accepts only c ranked below x: x's providers rank above
    x, so they are known when x is visited, and the graph is loop-free by construction. Later
    passes repeat until nothing changes, also accepting c ranked above x when c's transit degree
    is at most UP_RANK_MAX_RATIO times x's; every edge after pass 0 is checked for loops.
    """
    provs: dict = defaultdict(set)
    down: dict = defaultdict(set)
    order = sorted(pos, key=pos.get)
    last = len(pos)
    rejected = set()
    for npass in range(TOP_DOWN_MAX_PASSES):
        added = 0
        for x in order:
            if x in IS_NON_TRANSIT or x not in triples:
                continue
            px = provs.get(x, ())
            for y, c, af in triples[x]:
                if c in TIER_1_FIREWALL or c in IS_NON_TRANSIT or c == x or c in down.get(x, ()):
                    continue
                if x in EVIDENCE_REQUIRED and af != 4:
                    continue
                if y not in TIER_1_FIREWALL and y not in px:
                    continue
                up = pos.get(c, last) < pos[x]
                if npass == 0:
                    if up:
                        continue
                elif (x, c) in rejected:
                    continue
                elif up and td.get(c, 0) > UP_RANK_MAX_RATIO * max(td.get(x, 0), 1):
                    continue
                elif _reaches(down, c, x):
                    rejected.add((x, c))
                    continue
                provs[c].add(x)
                down[x].add(c)
                added += 1
        if not added:
            break
    return down


# ---------------------------------------------------------------------------
# IXP phantom pruning
# ---------------------------------------------------------------------------

def _build_providers_of(downstream_map: dict) -> dict:
    providers_of = defaultdict(set)
    for provider, customers in downstream_map.items():
        for c in customers:
            providers_of[c].add(provider)
    return providers_of


def _prune_ixp_phantoms(downstream_map: dict, tier1_set: set) -> tuple[int, int]:
    """
    Secondary defence: remove non-T1 providers whose captive-customer fraction
    is below IXP_PRUNE_THRESHOLD.

    This catches any phantoms that slipped through the multi-collector check —
    for example, links that appear in two European collectors but are still
    local to European IXPs.

    See the docstring in build_topology() for the full explanation of why
    the valley-free algorithm cannot detect IXP phantoms.
    """
    providers_of = _build_providers_of(downstream_map)
    excl_map: dict[int, float] = {}
    for provider, customers in downstream_map.items():
        if provider in tier1_set or not customers:
            continue
        total = len(customers)
        captive = sum(1 for c in customers if len(providers_of.get(c, set())) <= 2)
        excl_map[provider] = captive / total * 100.0

    phantoms = {p for p, pct in excl_map.items() if pct < IXP_PRUNE_THRESHOLD}
    removed_links = removed_providers = 0
    for provider in phantoms:
        n = len(downstream_map.get(provider, []))
        if n:
            downstream_map[provider] = []
            removed_links += n
            removed_providers += 1
    return removed_providers, removed_links


# ---------------------------------------------------------------------------
# Per-link inference rule
# ---------------------------------------------------------------------------

def infer_link(as1: int, as2: int, degrees: dict, link_regions: dict) -> tuple:
    """(provider, customer, rule) for one observed link; provider is None when dropped.

    rule names the step that decided: non_transit, t1_t1, tier1, ratio_4x,
    peer or single_region. caida_crosscheck.py uses the rule to attribute disagreements.
    """
    # Rule 1: Non-transit exclusion
    if as1 in IS_NON_TRANSIT or as2 in IS_NON_TRANSIT:
        return None, None, "non_transit"

    # Rule 2: Tier-1 affirmative override (always provider of non-T1)
    t1_as1, t1_as2 = as1 in TIER_1_FIREWALL, as2 in TIER_1_FIREWALL
    if t1_as1 and t1_as2:
        return None, None, "t1_t1"
    if t1_as1:
        return as1, as2, "tier1"
    if t1_as2:
        return as2, as1, "tier1"

    # Rule 3: Cross-regional degree-ratio. A link seen from fewer than CONFIRM_REGIONS
    # regions is never transit by ratio: the 8x rule it used to get was mostly IX peering
    # (18% CAIDA agreement; dropping it lifted provider precision vs ASPA 69.7% -> 83.7%).
    d1, d2 = degrees[as1], degrees[as2]
    n_regions = len(link_regions.get(tuple(sorted((as1, as2))), set()))
    lopsided = d1 > d2 * RATIO or d2 > d1 * RATIO
    if n_regions < CONFIRM_REGIONS:
        return None, None, "single_region" if lopsided else "peer"
    if d1 > d2 * RATIO:
        return as1, as2, "ratio_4x"
    if d2 > d1 * RATIO:
        return as2, as1, "ratio_4x"
    return None, None, "peer"


def build_graph(adj: dict, degrees: dict, link_regions: dict, evidence: dict | None,
                triples: dict | None = None, never_providers: set = frozenset()) -> tuple:
    """(downstream {provider: [customers]}, labels {pair: (provider, customer, rule)}).

    With export evidence (bgp-extractor exports.csv), after infer_link:
      restored           a dropped single_region / peer link becomes p2c when a Tier 1 export
                         shows it in one direction only and the provider has the larger degree.
                         Every non-Tier-1 p2c edge then points up the degree order and no edge
                         enters a Tier 1, so the graph stays loop-free.
      pruned             a p2c link with a non-Tier-1 provider that is never passed beyond the
                         collector end of a path (only seen next to the collector: IX phantom).
      evidence_required  provider in EVIDENCE_REQUIRED_ASNS without an IPv4 Tier 1 export.
    Without evidence (old extractor output), falls back to _prune_ixp_phantoms; links it removes
    are labelled pruned.

    With path triples (bgp-extractor triples.csv), the result of the above is only a fallback:
      path         p2c from infer_top_down. Replaces the Tier 1 override and the degree ratio.
      ratio_4x / restored
                   kept only for an AS that path evidence gives no provider, when the provider
                   ranks above it and the link closes no loop.
      tier1        kept when the customer is a stub (never seen mid-path), AS Rank step 9:
                   97% CAIDA-same on the 11 Oct dumps. A stub has no customers, so no cone nests.
      ratio_stub   a ratio_4x link to a stub seen from >= STUB_RATIO_MIN_REGIONS collector regions
                   (item 4: signed ASPA 132/7), unless the provider is in never_providers (IXP ASNs).
      unconfirmed  any other link the rules above would have made p2c.
    """
    labels = {}
    for a, nbrs in adj.items():
        for b in nbrs:
            pair = (min(a, b), max(a, b))
            if pair not in labels:
                labels[pair] = infer_link(a, b, degrees, link_regions)

    if evidence is None:
        down = defaultdict(list)
        for p, c, _ in labels.values():
            if p is not None:
                down[p].append(c)
        kept = {p: set(cs) for p, cs in down.items()}
        _prune_ixp_phantoms(down, TIER_1_FIREWALL)
        after = {p: set(cs) for p, cs in down.items()}
        for pair, (p, c, rule) in labels.items():
            if p is not None and c in kept.get(p, ()) and c not in after.get(p, ()):
                labels[pair] = (p, c, "pruned")
        if triples is None:
            return down, labels
    else:
        for (a, b), (p, c, rule) in list(labels.items()):
            if p is None and rule in ("single_region", "peer"):
                ab, ba = evidence.get((a, b), 0) & EV_T1, evidence.get((b, a), 0) & EV_T1
                if bool(ab) != bool(ba):
                    pr, cu = (a, b) if ab else (b, a)
                    if degrees[pr] > degrees[cu]:
                        labels[(a, b)] = (pr, cu, "restored")

        down = defaultdict(list)
        for pair, (p, c, rule) in labels.items():
            if p is None:
                continue
            if p not in TIER_1_FIREWALL:
                ev = evidence.get((p, c), 0)
                if not ev & EV_BEYOND:
                    labels[pair] = (p, c, "pruned")
                    continue
                if p in EVIDENCE_REQUIRED and not ev & EV_T1_4:
                    labels[pair] = (p, c, "evidence_required")
                    continue
            down[p].append(c)
    if triples is None:
        return down, labels

    td = transit_degrees(triples)
    pos = rank_positions(set(adj) | set(triples), td, degrees)
    edges = infer_top_down(triples, pos, td)
    has_provider = {c for cs in edges.values() for c in cs}
    last = len(pos)
    for p, cs in edges.items():
        for c in cs:
            labels[(min(p, c), max(p, c))] = (p, c, "path")
    for pair, (p, c, rule) in sorted(labels.items()):
        if p is None or rule in ("path", "pruned", "evidence_required"):
            continue
        providerless = (rule in ("ratio_4x", "restored") and c not in has_provider
                        and pos.get(p, last) < pos.get(c, last))
        tier1_stub = rule == "tier1" and td.get(c, 0) == 0
        ratio_stub = (rule == "ratio_4x" and td.get(c, 0) == 0 and p not in never_providers
                      and len(link_regions.get(pair, ())) >= STUB_RATIO_MIN_REGIONS)
        if (providerless or tier1_stub or ratio_stub) and not _reaches(edges, c, p):
            edges[p].add(c)
            if ratio_stub and not providerless:
                labels[pair] = (p, c, "ratio_stub")
        else:
            labels[pair] = (None, None, "unconfirmed")
    return defaultdict(list, {p: sorted(cs) for p, cs in edges.items() if cs}), labels


# ---------------------------------------------------------------------------
# Main topology builder
# ---------------------------------------------------------------------------

def build_topology():
    """
    Build the provider→customer directed graph from RIPE RIS BGP dumps.

    Uses data from multiple geographically diverse RRC collectors so that
    IXP route-server adjacencies (which are local to one IXP fabric) can be
    distinguished from genuine transit relationships (which appear globally).

    Rule priority (cone-calculator.go has rules 1, 2 and the 4× ratio, on rrc00 only):
      1. Non-transit exclusion  (RIRs, root servers, IXP route servers)
      2. Tier-1 affirmative override
      3. Cross-regional degree-ratio:
           ≥ CONFIRM_REGIONS regions see the link → use RATIO (4×)
           < CONFIRM_REGIONS regions            → never transit (dropped)
      4. Export evidence (build_graph): restore confirmed links, prune links only seen at the
         collector end, EVIDENCE_REQUIRED_ASNS need IPv4 Tier 1 exports
    With path triples (triples.csv), rules 2-4 only give providers to ASes that the top-down
    path inference (infer_top_down) leaves without one; see build_graph.
    """
    print("[*] Building Topology from RIPE RIS (Multi-Collector)...")

    meta_map = load_scraped_metadata()
    print(f"    - Loading collector data...")
    adj, degrees, link_regions = load_multi_collector_relationships()
    if not adj:
        return

    evidence = load_exports()
    if evidence is None:
        print("    [!] No exports.csv from bgp-extractor (old binary?): falling back to "
              "provider-level phantom pruning.")
    else:
        print(f"    - Export evidence: {len(evidence):,} directed links")
    triples = load_triples()
    if triples is None:
        print("    [!] No triples.csv from bgp-extractor (old binary?): using the degree rules "
              "(Tier 1 override, degree ratio) without path inference.")
    else:
        print(f"    - Path triples: {sum(map(len, triples.values())):,} for {len(triples):,} ASes")
    downstream_map, labels = build_graph(adj, degrees, link_regions, evidence, triples)

    rules = Counter(rule for _, _, rule in labels.values())
    kept = sum(len(cs) for cs in downstream_map.values())
    print(f"    - Graph built: {len(labels):,} links, {kept:,} kept as transit.")
    for rule, n in rules.most_common():
        print(f"      {rule:<18} {n:>9,}")

    # Save
    with open(os.path.join(rov_utils.DIR_DATA, "downstream_graph.json"), 'w') as f:
        json.dump(downstream_map, f)

    new_asns = 0
    for asn in degrees:
        if asn not in meta_map:
            meta_map[asn] = {'name': 'Unknown (RIS)', 'cc': 'XX', 'cone': 0}
            new_asns += 1
    with open(os.path.join(rov_utils.DIR_DATA, "asn_meta.json"), 'w') as f:
        json.dump(meta_map, f)

    print(f"    - Added {new_asns} unscraped ASNs to metadata.")
    print("[+] Topology saved to 'data/downstream_graph.json'")


if __name__ == "__main__":
    build_topology()
