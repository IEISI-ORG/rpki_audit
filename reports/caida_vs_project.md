# CAIDA AS relationships vs the rpki_audit topology

2026-10-14. CAIDA serial-2 `as-rel2` and `ppdc-ases` for 20261001. Our topology is built
from RIPE RIS dumps of 2026-10-11 from five collectors: rrc00, rrc14, rrc19, rrc23 and rrc24.
The signed ASPA records are `data/aspa_real.json`, dated 2026-10-07: 3,421 networks.
CAIDA is treated as a second opinion to test, not as ground truth.

## Summary

1. **Our topology and CAIDA's disagree most on the largest networks.**
   - Our Tier 1 cones are 1.3 to 16 times CAIDA's. For example, NTT is 69,002 here and
     23,297 in CAIDA; Deutsche Telekom is 68,757 and 4,312.
   - We miss customers of mid-sized and NZ networks. Spark AS4648 has 48 here and 118 in
     CAIDA.
   - Our phantom pruning removes some real providers entirely. Angola Cables and EdgeUno
     have no customers here; CAIDA gives each about 4,000.
2. **Where the two disagree and there is evidence, CAIDA is usually right.**
   - Against signed ASPA, 90.2% of CAIDA's provider labels are correct, against 69.7% of
     ours.
   - In observed route exports, 98–99% of CAIDA's provider→customer labels are confirmed.
3. **CAIDA's one systematic error is Hurricane Electric (AS6939) over IPv6.**
   - In IPv4, HE's peer links behave as peering: 7,159 only pass the peer's routes down,
     and 3 pass them up.
   - In IPv6 the same links behave as transit: 4,435 pass the peer's routes up to HE's
     own providers and peers, and 2 don't.
   - CAIDA gives one label per AS pair, and that label matches IPv4. Our extractor mixes
     both address families, which is why our HE cone is 68,421 against CAIDA's 22,110.
4. **ASPA will curb HE's IPv6 model only gradually, and only for networks that leave HE
   off their ASPA.**
   - An ASPA record has a single provider list covering IPv4 and IPv6.
   - So a network that relies on HE for IPv6 reach and lists it as a provider also
     authorises HE to pass its IPv4 routes upward.
   - Today, 250 of the 5,586 non-customer origins whose IPv6 routes HE sends upward would
     have those routes rejected by a network that validates ASPA. A further 300 list HE,
     which makes the leak valid. The remaining 5,036 have no ASPA, so their routes are
     kept. See section 4.

## 1. Where the two topologies differ

Full tables are in `reports/caida_crosscheck.md` (`caida_crosscheck.py`). Each row below is
one of our link rules, compared with CAIDA's label for the same AS pair:

| our rule | links | CAIDA: same provider→customer | CAIDA: peer | CAIDA: transit (we dropped it) |
|---|---|---|---|---|
| ratio_4x | 123,534 | 82% | 8% | – |
| pruned (phantom backstop, dropped) | 78,779 | – | 73% | 6% |
| peer (ratio below 4x, dropped) | 30,187 | – | 22% | **67%** |
| tier1 | 28,751 | 96% | 3% | – |
| ratio_8x (seen in one region) | 17,367 | **18%** | 65% | – |

The remainder of each row is links CAIDA doesn't have.

What these numbers mean for our code:

- `ratio_8x` is wrong about four times out of five. Links seen in only one region are
  mostly IX peering.
- The `peer` rule drops 20,220 links that CAIDA labels as transit. A degree ratio can't
  detect a customer that is about the same size as its provider. This causes the NZ
  undercount:

  | AS | ours | CAIDA |
  |---|---|---|
  | Feenix | 55 | 161 |
  | Spark | 48 | 118 |
  | One NZ AS9500 | 4 | 41 |
  | Voyager | 10 | 33 |

- Vetta Group AS64073 goes the other way: its cone is 928 here and 32 in CAIDA. That is an
  IX phantom the pruning missed.
- Phantom pruning is all-or-nothing per provider. Angola Cables, EdgeUno and Durand end up
  with a cone of 0.
- Cloudflare AS13335 is in our non-transit list, but CAIDA sees it as a provider for 1,011
  networks.
- **Tier 1 list:** it now has the 18 ASes that form a complete mesh of observed links with
  no CAIDA provider (`TESTED_TIER1`, set 2026-10-14). Nine ASes have been removed:
  1273, 4134, 4637, 4809, 4837, 6939, 7922, 9808 and 9929. Even so, the remaining Tier 1
  cones are 1.3 to 16 times CAIDA's, because their peers' customers get counted as theirs.

## 2. Who is right: signed ASPA

An ASPA record is the network's own signed list of its providers. It is the only ground
truth here, but it covers just 2.8% of networks: 2,634 of the 3,421 are stubs, and it says
nothing about peering.

| | networks covered | provider precision | provider recall |
|---|---|---|---|
| CAIDA | 2,694 | 90.2% (5,922 / 6,563) | 63.7% (5,922 / 9,301) |
| ours | 2,907 | 69.7% (5,438 / 7,807) | 52.5% (5,438 / 10,356) |

CAIDA disagrees with ASPA on 1,150 links. Section 3 tests which side the paths support.

- **641 links:** CAIDA labels X as a provider of C, but C's ASPA doesn't list X.
- **509 links:** C's ASPA lists X as a provider, but CAIDA labels the link peering. HE is
  X in 230 of these.

**AS0 records.** 65 networks publish an AS0-only ASPA, which declares no providers.
- 6 of them are on our Tier 1 list (174, 1299, 3257, 3320, 6830, 7018), which is
  independent confirmation.
- 18 are IX route servers, and none of those is in our non-transit list yet (TODO).

## 3. Who is right: observed exports

**Method.** Take a RIS path ending `… Y X C`, where C is the origin. Then X passed C's
route to Y.
- If Y is X's provider or peer, valley-free routing means C is X's customer, or the
  export is a route leak.
- **Strict test:** Y is in the tested Tier 1 clique and X is not. This uses no CAIDA data.
- **Via label test:** CAIDA labels Y as X's provider or peer. This leans on CAIDA's
  label for a different link, so it is reported separately.
- "Only passed down" means C's route was seen going only to X's CAIDA-labelled customers.
  That fits any relationship.

The data is 4.5 million distinct last-three-hop triples from the five dumps, tagged by
address family. Script: `caida_export_test.py` (tests: `tests/test_caida_export.py`).

| test | address family | provider (strict) | provider (via label) | only passed down | not seen |
|---|---|---|---|---|---|
| A. CAIDA p2c, missing from C's ASPA | v4 | 131 | 207 | 7 | 296 |
| | v6 | 41 | 62 | 4 | 534 |
| B. in C's ASPA, CAIDA p2p | v4 | 5 | 40 | 258 | 206 |
| | v6 | 199 | 48 | 12 | 250 |
| B, X = HE only | v4 | 1 | 0 | 215 | 14 |
| | v6 | 176 | 25 | 0 | 29 |
| C. all CAIDA p2p links tested | v4 | 78 | 5,337 | 37,792 | – |
| | v6 | 1,192 | 5,259 | 12,860 | – |
| C, X = HE only | v4 | 3 | 0 | 7,159 | – |
| | v6 | 1,054 | 3,381 | 2 | – |
| D. all CAIDA p2c links tested | v4 | 81,450 | 72,899 | 1,533 | – |
| | v6 | 26,595 | 25,394 | 814 | – |

Each row is counted separately for IPv4 and IPv6, so a link seen in both families appears
in both rows.

What the rows show:
- **A:** where the paths show anything, they support CAIDA in 338 of 345 IPv4 cases. Those
  networks have providers they haven't put in their ASPA.
- **B:** in IPv4, these "providers" mostly behave as peers (258 of 303 seen). In IPv6 they
  mostly behave as providers (247 of 259). HE accounts for most of both. The networks
  signed HE as a provider because it is their IPv6 transit, and ASPA has no way to say
  "IPv6 only".
- **C:** in IPv4, 78 of 43,207 CAIDA peer links (0.2%) fail the strict test. In IPv6,
  1,192 of 19,311 fail, and 1,054 of those 1,192 are HE.
  - The via-label column flags many more links. It can double-count a single CAIDA error,
    so treat it as a lead to check, not a verdict.
- **D:** CAIDA's provider→customer labels are confirmed by upward exports in 99% of tested
  IPv4 links and 98% of IPv6 links. The strict test alone confirms 81,450 IPv4 and 26,595 IPv6
  links; the rest rely on CAIDA's label for the next link.

**Verdict on CAIDA.**
- Its provider→customer labels can be used as an input.
- Its peer labels are reliable except for HE over IPv6. There, HE acts as the provider of
  its "peers", which matches what Terry describes from operating experience: HE sends its
  full IPv6 table to all peers and customers, including remote IX sessions.

## 4. Will ASPA stop HE's leaky IPv6 model?

**How the check works.** Under ASPA verification (draft-ietf-sidrops-aspa-verification-28):
- A network receiving a route from a peer or a customer applies *upstream* verification.
  Every hop has to be customer→provider.
- When HE passes origin C's route to its own provider or peer Y, Y checks the hop C→HE
  against C's ASPA, with three possible outcomes:

| C's ASPA | outcome at Y (if Y validates) |
|---|---|
| lists HE | Valid: the leak is authorised |
| exists but omits HE (or is AS0-only) | Invalid: Y drops the route |
| none | Unknown: kept |

Routes HE passes to its own customers get *downstream* verification, which allows one
sideways hop at the top of the path, so they stay valid.

**One provider list for both address families.** The ASPA profile
(draft-ietf-sidrops-aspa-profile-29) has a single provider set with no address family. The
verification draft states the consequence: the provider set "contains the union of
Providers ... for both IPv4 and IPv6 unicast". A network that uses HE as its IPv6 transit
must list HE, and that also makes HE's IPv4 exports of its routes valid.

**What happens today.** These are origins whose routes HE passes to its own providers or
peers (the same tests as section 3), sorted by the origin's ASPA:

| address family | CAIDA's label for C–HE | origins | ASPA omits HE → dropped | ASPA lists HE → valid | no ASPA → kept |
|---|---|---|---|---|---|
| v6 | peer or no link | 5,586 | 250 | 300 | 5,036 |
| v6 | HE is C's provider | 1,295 | 3 | 97 | 1,195 |
| v4 | peer or no link | 7 | 0 | 1 | 6 |
| v4 | HE is C's provider | 2,173 | 1 | 121 | 2,051 |

**What this means for the IPv6 leak:**
- **Where it would stop it:** 250 origins, 4.5%, have signed an ASPA that leaves HE out. A
  network that validates ASPA would drop HE's upward copy of their IPv6 routes. That
  number grows as more networks publish ASPA.
- **Where it legitimises it:** 300 origins list HE. For them the leak is authorised in
  both families, even though in IPv4 HE behaves as their peer (section 3, row B).
- **Most origins:** 5,036 have no ASPA, so nothing changes.
- **The effect needs both sides.** The origin has to publish an ASPA, and the network
  receiving the route from HE (its providers and peers) has to validate. This report has
  no data on which networks validate today.

**Answer:** yes, in time, but only network by network. Each HE peer will eventually have to
choose:
- **List HE:** this keeps the IPv6 reach HE gives it and authorises HE to propagate its
  routes in both families.
- **Leave HE off:** validating networks then drop HE's leaked copies of its routes.

ASPA doesn't stop the model as such. It makes each peer state whether HE is its provider.

## 5. Changes for our code (all in TODO.md)

1. **Build the topology per address family, or IPv4 only for verdicts.**
   - `bgp-extractor.go` reads AS paths and ignores the prefix field, so HE's IPv6 transit
     inflates its IPv4 cone.
   - The Atlas audit test is IPv4; IPv6 results are kept out of verdicts.
2. **Use CAIDA's p2c labels as an input where our rules drop or reverse the link.** CAIDA is
   98–99% confirmed by exports and 90% by ASPA. Don't use CAIDA's p2p labels for HE over IPv6.
3. **Fix our weak rules:**
   - replace `ratio_8x` and the all-or-nothing phantom pruning;
   - add the 18 AS0 route servers to the non-transit list once each is confirmed in
     PeeringDB;
   - take Cloudflare out of the non-transit list.
4. **Recompute the Tier 1 cones** without counting peers' customers. They are 1.3 to 16
   times CAIDA's.

## Limits

- **Route leaks:** passing a route upward is also what a leak looks like. For HE, the
  networks' own ASPA records say it acts as their provider, so the distinction doesn't
  change the conclusion.
- **Coverage:** our five collectors see 289k links. CAIDA has 398k peer links we never see,
  and the export test covers only origins whose last three hops appear in our dumps.
- **Skewed ASPA sample:** ASPA signers are mostly small networks. An ASPA may also list
  backup or planned providers.
- **Single snapshots:** each source is one dump (RIS 11 Oct, CAIDA October, ASPA 7 Oct).

## Reproduce

```
python3 caida_crosscheck.py                    # section 1, reports/caida_crosscheck.md
python3 caida_export_test.py --extract         # sections 3-4; triples to output/triples/ (~15 min)
```
