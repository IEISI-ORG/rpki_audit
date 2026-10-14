# NZ beacon baseline (2026-10-14)

Every connected RIPE Atlas probe in the country pinged and traced two valid/invalid beacon pairs. **cf** = Cloudflare (most networks get its invalid route straight from Cloudflare); **ris** = RIPE NCC RIS beacons AS12654 (few upstreams carry the invalid route, so failing to reach it usually means it was never offered).

Measurement IDs: v4: ping:cf_valid=222576137, ping:cf_invalid=222576138, ping:ris_valid=222576139, ping:ris_invalid=222576142, trace:cf_valid=222576143, trace:cf_invalid=222576145, trace:ris_valid=222576146, trace:ris_invalid=222576147; v6: ping:cf_valid=222576157, ping:cf_invalid=222576159, ping:ris_valid=222576160, ping:ris_invalid=222576161, trace:cf_valid=222576163, trace:cf_invalid=222576165, trace:ris_valid=222576166, trace:ris_invalid=222576167

## IPv4: 115 probes
- cf: invalid-unreachable 24, no-data 4, reaches-invalid 87
- ris: invalid-unreachable 111, no-data 4

| AS | name | probes | cf reach invalid | ris reach invalid | ris stop ASNs | verdict | APNIC | ROVista |
|---|---|---|---|---|---|---|---|---|
| 64073 | Vetta Group | 28 | 28/28 | 0/28 | 174 64073 | PARTIAL: VULNERABLE (Mixed) | 0.0 | 0.0 |
| 56030 | Voyager Internet Ltd. | 14 | 14/14 | 0/14 | 56030 | VULNERABLE (Atlas Verified) | 0.0 | 0.0 |
| 55850 | Mercury NZ Limited | 8 | 8/8 | 0/8 | 55850 | REGRESSED | 0.09 | 100.0 |
| 23655 | 2degrees Networks Limited | 7 | 0/7 | 0/7 | 4826 9790 23655 | ACTIVE (Atlas Verified) | 97.61 | 0.0 |
| 9790 | Two Degrees Networks Limited | 7 | 0/7 | 0/7 | 4826 9790 | ACTIVE (Atlas Verified) | 99.52 | 0.0 |
| 4771 | Spark New Zealand Trading Lt | 6 | 5/5 | 0/5 | 4771 | VULNERABLE (Atlas Verified) | 0.03 | 100.0 |
| 9500 | One New Zealand Group Limite | 6 | 6/6 | 0/6 | 9500 | PARTIAL: VULNERABLE (Mixed) | 0.11 | 0.0 |
| 138398 | Prodigi Technology Services  | 3 | 3/3 | 0/3 | 136557 | PARTIAL: VULNERABLE (Mixed) | -1.0 | 0.0 |
| 140220 | Sky Network Television Ltd | 2 | 0/2 | 0/2 | 9790 | STUB: VOLATILE | 98.82 | -1.0 |
| 14593 | SpaceX Starlink | 2 | 2/2 | 0/2 | 7578 | VULNERABLE (Atlas Verified) | 19.51 | 100.0 |
| 16509 | Amazon.com, Inc. | 2 | 0/2 | 0/2 |  | ACTIVE (Atlas Verified) | 99.74 | 100.0 |
| 18199 | Worldnet Services Limited | 2 | 2/2 | 0/2 | 135069 | STUB: VULNERABLE | 0.0 | 0.0 |
| 24324 | Kordia Limited | 2 | 2/2 | 0/2 | 24324 | VULNERABLE (Atlas Verified) | 0.0 | 0.0 |
| 4049 | CELLO GROUP LIMITED | 2 | 2/2 | 0/2 | 55850 | PARTIAL: VULNERABLE (Mixed) | 1.21 | 0.0 |
| 45177 | Devoli | 2 | 2/2 | 0/2 | 4637 | REGRESSED | 0.13 | 100.0 |
| 61138 | Zappie Host LLC | 2 | 0/1 | 0/1 | 174 | PARTIAL: VULNERABLE (Mixed) | -1.0 | 100.0 |
| 131583 | WIZwireless Limited | 1 | 1/1 | 0/1 | 131583 | STUB: VULNERABLE | 0.0 | 0.0 |
| 132003 | Network Research Lab | 1 | 0/1 | 0/1 | 23905 | NOT ROUTED | -1.0 | -1.0 |
| 132255 | PrimoWireless Ltd | 1 | 1/1 | 0/1 | 132255 | STUB: VULNERABLE | 0.0 | 0.0 |
| 132588 | Yrless Ltd | 1 | 0/1 | 0/1 | 9790 | STUB: VOLATILE | -1.0 | -1.0 |
| 133075 | Telesmart Limited | 1 | 1/1 | 0/1 | 135069 | STUB: VOLATILE | -1.0 | 100.0 |
| 133950 | Hoopla Hosting Limited | 1 | 1/1 | 0/1 | 7578 | STUB: VULNERABLE | -1.0 | -1.0 |
| 134220 | Lightwire LTD | 1 | 1/1 | 0/1 | 45177 | STUB: VULNERABLE | -1.0 | 0.0 |
| 137257 | Localhost Limited | 1 | 1/1 | 0/1 | 137257 | STUB: VULNERABLE | -1.0 | -1.0 |
| 152586 | Kuroit | 1 | 0/1 | 0/1 | 174 | PARTIAL: VULNERABLE (Mixed) | -1.0 | -1.0 |
| 153375 | Cover Communications Limited | 1 | 1/1 | 0/1 | 64073 | STUB: VULNERABLE | -1.0 | -1.0 |
| 17705 | InSPire Net Ltd | 1 | 0/0 | 0/0 |  | INCONSISTENT | 13.07 | 0.0 |
| 24398 | Auckland University of Techn | 1 | 1/1 | 0/1 | 24398 | STUB: VULNERABLE | -1.0 | -1.0 |
| 38064 | InternetNZ (.nz tld) | 1 | 1/1 | 0/1 | 4637 | STUB: VULNERABLE | -1.0 | -1.0 |
| 38299 | REANNZ Corporate | 1 | 0/1 | 0/1 | 38299 | STUB: VOLATILE | -1.0 | -1.0 |
| 45131 | REANNZ Head Office | 1 | 0/0 | 0/0 |  | NOT ROUTED | -1.0 | -1.0 |
| 45475 | Amuri Net | 1 | 0/1 | 0/1 | 9790 | DISPUTED | 25.0 | 100.0 |
| 58631 | Vista Group (NZ) Limited | 1 | 1/1 | 0/1 | 45177 | STUB: VULNERABLE | -1.0 | -1.0 |
| 58666 | Vorco | 1 | 1/1 | 0/1 | 9790 | PARTIAL: VULNERABLE (Mixed) | -1.0 | 0.0 |
| 64095 | Blue Reach Services Limited | 1 | 1/1 | 0/1 | 135069 | STUB: VULNERABLE | 0.0 | 0.0 |
| 9245 | COMPASS NZ | 1 | 1/1 | 0/1 | 9245 | DISPUTED | 100.0 | 0.0 |

## IPv6: 67 probes
- cf: invalid-unreachable 15, no-data 6, no-valid 1, reaches-invalid 45
- ris: invalid-unreachable 60, no-data 6, no-valid 1

| AS | name | probes | cf reach invalid | ris reach invalid | ris stop ASNs | verdict | APNIC | ROVista |
|---|---|---|---|---|---|---|---|---|
| 64073 | Vetta Group | 17 | 15/15 | 0/15 | 174 | PARTIAL: VULNERABLE (Mixed) | 0.0 | 0.0 |
| 56030 | Voyager Internet Ltd. | 9 | 9/9 | 0/9 | 56030 | VULNERABLE (Atlas Verified) | 0.0 | 0.0 |
| 55850 | Mercury NZ Limited | 7 | 7/7 | 0/7 | 55850 | REGRESSED | 0.09 | 100.0 |
| 9790 | Two Degrees Networks Limited | 7 | 0/7 | 0/7 | 4826 9790 | ACTIVE (Atlas Verified) | 99.52 | 0.0 |
| 138398 | Prodigi Technology Services  | 3 | 3/3 | 0/3 | 174 | PARTIAL: VULNERABLE (Mixed) | -1.0 | 0.0 |
| 14593 | SpaceX Starlink | 2 | 1/2 | 0/2 | 137409 | VULNERABLE (Atlas Verified) | 19.51 | 100.0 |
| 23655 | 2degrees Networks Limited | 2 | 0/2 | 0/2 | 4826 23655 | ACTIVE (Atlas Verified) | 97.61 | 0.0 |
| 4049 | CELLO GROUP LIMITED | 2 | 2/2 | 0/2 | 55850 | PARTIAL: VULNERABLE (Mixed) | 1.21 | 0.0 |
| 61138 | Zappie Host LLC | 2 | 0/1 | 0/1 | 174 | PARTIAL: VULNERABLE (Mixed) | -1.0 | 100.0 |
| 133075 | Telesmart Limited | 1 | 1/1 | 0/1 | 135069 | STUB: VOLATILE | -1.0 | 100.0 |
| 133950 | Hoopla Hosting Limited | 1 | 1/1 | 0/1 | 63956 | STUB: VULNERABLE | -1.0 | -1.0 |
| 134220 | Lightwire LTD | 1 | 0/0 | 0/0 |  | STUB: VULNERABLE | -1.0 | 0.0 |
| 152586 | Kuroit | 1 | 0/1 | 0/1 | 174 | PARTIAL: VULNERABLE (Mixed) | -1.0 | -1.0 |
| 16509 | Amazon.com, Inc. | 1 | 0/1 | 0/1 |  | ACTIVE (Atlas Verified) | 99.74 | 100.0 |
| 17705 | InSPire Net Ltd | 1 | 0/0 | 0/0 |  | INCONSISTENT | 13.07 | 0.0 |
| 18199 | Worldnet Services Limited | 1 | 1/1 | 0/1 | 135069 | STUB: VULNERABLE | 0.0 | 0.0 |
| 24324 | Kordia Limited | 1 | 1/1 | 0/1 | 24324 | VULNERABLE (Atlas Verified) | 0.0 | 0.0 |
| 38064 | InternetNZ (.nz tld) | 1 | 1/1 | 0/1 | 134220 | STUB: VULNERABLE | -1.0 | -1.0 |
| 38299 | REANNZ Corporate | 1 | 0/1 | 0/1 | 38299 | STUB: VOLATILE | -1.0 | -1.0 |
| 45131 | REANNZ Head Office | 1 | 0/0 | 0/0 |  | NOT ROUTED | -1.0 | -1.0 |
| 58631 | Vista Group (NZ) Limited | 1 | 0/1 | 0/1 | 45177 | STUB: VULNERABLE | -1.0 | -1.0 |
| 58666 | Vorco | 1 | 1/1 | 0/1 | 9790 | PARTIAL: VULNERABLE (Mixed) | -1.0 | 0.0 |
| 64095 | Blue Reach Services Limited | 1 | 1/1 | 0/1 | 135069 | STUB: VULNERABLE | 0.0 | 0.0 |
| 9245 | COMPASS NZ | 1 | 1/1 | 0/1 | 9245 | DISPUTED | 100.0 | 0.0 |
| 9500 | One New Zealand Group Limite | 1 | 0/0 | 0/0 |  | PARTIAL: VULNERABLE (Mixed) | 0.11 | 0.0 |
