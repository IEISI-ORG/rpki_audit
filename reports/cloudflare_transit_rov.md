# Cloudflare (AS13335) as a transit provider, and its RPKI filtering

2026-10-15. Why this matters: `rov_utils.NON_TRANSIT_ASNS` lists AS13335. Both the path inference and
the degree rules skip non-transit ASes, so Cloudflare's customers get no provider. Windcave AS131168,
Ministry of Education AS24318, TVNZ AS37999, Northpower AS131254 and Inland Revenue AS136990 are all
`PROVIDER UNKNOWN (In BGP)` for this reason. RIS sees Windcave only behind 13335, in all five
collectors. Across the audit, 383 of the 744 PROVIDER UNKNOWN ASes have Cloudflare as a neighbour,
and 356 have no other neighbour. Evidence snapshot: `data/snapshots/cloudflare_rov_2026-10-15/`
(local, not in git).

## 1. Cloudflare carries other networks' routes (it is a transit provider)

- **Cloudflare's documentation:** Magic Transit customers announce their own prefixes through Cloudflare,
  either with their own ASN or with AS13335. "Provide all IP prefixes you plan to onboard, along with
  the ASNs from which you will advertise them" and "If you do not own an ASN, you can use the
  Cloudflare Customer ASN (AS13335)"
  ([Advertise prefixes](https://developers.cloudflare.com/magic-transit/how-to/advertise-prefixes/)).
  Cloudflare passes those routes on to its own transit providers: "Our transit providers require the
  LOA so they can accept the routes we advertise on your behalf"
  ([Get started](https://developers.cloudflare.com/magic-transit/get-started/)). "Cloudflare advertises
  the customer's protected IP prefixes to the Internet from all of Cloudflare's global data centers"
  ([Protect data center networks](https://developers.cloudflare.com/reference-architecture/diagrams/network/protect-data-center-networks/)).
- **Our data:** the rrc00 RIS dump of 2026-10-11 has 285,408 distinct routes where 13335 is mid-path
  and another AS is the origin. That is 6,597 prefixes from 1,025 origin ASes. CAIDA's 20261001
  relationships independently list Cloudflare as provider for 1,011 ASes. For Windcave, Cloudflare
  passes the route on to Tier 1s (GTT 3257, NTT 2914, PCCW 3491, among others).

## 2. Cloudflare filters RPKI-invalid routes

- "We have fully deployed Origin Validation on all our BGP sessions with our peers and signed our
  prefixes." Louis Poinsignon, Cloudflare blog, 17 April 2020
  ([Is BGP Safe Yet?](https://blog.cloudflare.com/is-bgp-safe-yet-rpki-routing-security-initiative/)).
  The 2018 announcement said Cloudflare had "started deploying active filtering by using RPKI for
  routing decisions" and was "progressively moving towards enforcing strict validation of RPKI signed
  routes everywhere" ([RPKI details](https://blog.cloudflare.com/rpki-details/)).
- Cloudflare's own isbgpsafeyet.com data lists itself as `cloud, signed + filtering, safe`
  ([operators.csv](https://raw.githubusercontent.com/cloudflare/isbgpsafeyet.com/master/data/operators.csv)).
- **What isn't in writing:** none of these sources names transit sessions or customer sessions
  separately ("BGP sessions with our peers"), and none gives a date later than 2020 for the
  deployment. I found no current Cloudflare policy page on the subject.

## 3. The test prefix is the intended exception

Cloudflare announces 103.21.244.0/24 and 2606:4700:7000::/48 as deliberately invalid, from its data
centres and IX connections, so that other networks can test their filtering: "Both these prefixes
should be considered invalid and should not be routed by your provider"
([Is BGP Safe Yet?](https://blog.cloudflare.com/is-bgp-safe-yet-rpki-routing-security-initiative/)).
Cloudflare originates these itself, so they don't appear among the routes in section 4.

## 4. Check: are the routes Cloudflare passes on for others RPKI-valid?

RFC 6811 validation of the 285,408 routes (6,597 prefixes) from section 1, against rpki-client's VRPs
of 2026-10-15 07:41 UTC (`cf_validate.py` in the snapshot):

| RPKI state | routes | prefixes |
|---|---|---|
| valid | 155,585 | 3,663 |
| not found (no ROA) | 129,730 | 2,931 |
| invalid | 93 | 3 |

The three invalid prefixes:

| prefix | origin | covering ROA | why invalid |
|---|---|---|---|
| 156.236.84.0/24 | AS198990 | 156.236.84.0/24 max /24, AS17561 | ROA names a different AS |
| 162.158.71.0/24 | AS132892 (Cloudflare's own second ASN) | 162.158.64.0/21 max /21, AS132892 | /24 longer than the ROA's maxLength |
| 31.57.60.0/24 | AS213563 | 31.57.60.0/22 max /24, AS834 | ROA names a different AS |

So 3 of 6,597 prefixes (0.05%) are invalid, one of them Cloudflare's own address space. Both
customer cases fit routes that Cloudflare originates on a customer's behalf (Magic Transit / BYOIP)
rather than receives over BGP. Import-side ROV doesn't check those. This is an inference, not
something Cloudflare states. Caveat: the VRPs are 4 days newer than the dump, so a ROA that changed
in between would show here wrongly.

**Answer:** Cloudflare is a transit provider for about a thousand networks. It says in writing that it
drops RPKI-invalid routes on its BGP sessions, and its own test prefix is the deliberate exception.
The routes it carries for customers are 99.95% not invalid (valid or no ROA). The remaining 3 prefixes
look like customer or own announcements that it originates, not routes it learned.

## 5. What it means for the audit verdict

Inbound traffic to a Magic Transit customer arrives via Cloudflare. Outbound traffic, which is what
ROV protects, depends on the customer's setup: "You have two options for your Magic Transit
implementation: ingress traffic or ingress and egress traffic"
([About](https://developers.cloudflare.com/magic-transit/about/)). Without egress, return traffic uses
Direct Server Return: "route it natively out of the data center and onto the Internet, bypassing
Cloudflare network"
([Protect data center networks](https://developers.cloudflare.com/reference-architecture/diagrams/network/protect-data-center-networks/)).
With Cloudflare-leased IPs, Egress is switched on automatically
([Get started](https://developers.cloudflare.com/magic-transit/get-started/)). BGP doesn't show which
mode a customer uses. A customer on Magic Transit Egress is protected by Cloudflare's filtering. An
ingress-only customer is protected only if its own egress provider filters.

## 6. Change made (2026-10-15)

AS13335 has been removed from `rov_utils.NON_TRANSIT_ASNS` and from `constants.go isNonTransit()`. It stays
in `HARDCODED_SECURE`, with the reasons above. Our measurements can't test Cloudflare: the Atlas
invalid beacon is its own deliberately invalid prefix, and APNIC sees few end users there.
- Graph: Cloudflare gets 1,023 direct customers (CAIDA: 1,011). Of the 38 networks with signed ASPA
  that now have Cloudflare as a provider, 34 list AS13335 in their own ASPA. Overall ASPA precision
  is 94.4% (was 94.5%) and recall 60.1% (was 59.9%).
- Audit: PROVIDER UNKNOWN 744 → 368; 372 ASes move to STUB: PASSIVE (Clean Pipe), among them
  Windcave, Ministry of Education, TVNZ, Northpower and Inland Revenue. Per section 5, PASSIVE is right
  for customers on Magic Transit Egress and too generous for ingress-only ones. BGP can't tell them
  apart. **Decision (Terry, 2026-10-15):** PASSIVE is accepted as reasonable, because at least a
  Magic Transit customer's inbound traffic arrives through Cloudflare's filtering.
- `cone-calculator` (degree rules, rrc00 only) now gives Cloudflare an audit cone of 18,878 (was 0).
  That tool still uses the old degree ratio, so the figure is likely inflated by Cloudflare's peering
  degree (TODO: bring cone-calculator in line with the path inference).

Sources checked 2026-10-15.
