# Globalping vs RIPE Atlas

Generated 2026-11-28 by `globalping_verify.py --compare`. Globalping is in shadow mode: its results are **not used in verdicts**. This report decides whether they may be (`plan/globalping_plan.md` section 7).

**Result: NOT YET** (verdicts as `_classify_probe` gives them). With the beacon origin ruled out as a drop point on both sides: NOT YET.

22 Globalping results; 22 have an Atlas result no more than 7 days apart; 18 are conclusive on both sides; 8 agree.

## Pass criteria

| Criterion | Threshold | As classified | | Origin ruled out | |
|---|---|---|---|---|---|
| Sample | >= 60 ASes, >= 25 Atlas-SECURE and >= 25 Atlas-VULNERABLE | 18 ASes: 13 Atlas-SECURE, 5 Atlas-VULNERABLE | NOT YET | 18 ASes: 13 Atlas-SECURE, 5 Atlas-VULNERABLE | NOT YET |
| Overall agreement | >= 95% | 44.4% (8/18) | NOT YET | 66.7% (12/18) | NOT YET |
| Globalping SECURE confirmed by Atlas | >= 90% | 100.0% (3/3) | PASS | 100.0% (7/7) | PASS |
| Globalping VULNERABLE confirmed by Atlas | >= 95% | 33.3% (5/15) | NOT YET | 45.5% (5/11) | NOT YET |
| Repeatability | >= 20 targets re-run 24 h later, >= 95% same | n/a (0/0) | NOT YET | n/a (0/0) | NOT YET |

"Origin ruled out": `_classify_probe` names the first AS of the valid path that the invalid trace did not reach as the drop point. When that AS is Cloudflare (AS13335, the origin of both beacons) and the invalid trace ended inside the target, the probe is read as SECURE (Upstream Filtered), which counts against the target. The second pair of columns reads those probes as SECURE (Target Filtered), on the Atlas side too. Which reading is right is an open decision (TODO.md).

## Globalping against Atlas, AS level

| Globalping \ Atlas | SECURE | VULNERABLE | INCONCLUSIVE |
|---|---|---|---|
| SECURE | 3 | 0 | 0 |
| VULNERABLE | 10 | 5 | 0 |
| INCONCLUSIVE | 2 | 2 | 0 |

## By probe type

Each Globalping probe against the Atlas verdict for the AS. A probe is conclusive when it reads VULNERABLE, SECURE (Target Filtered) or SECURE (Upstream Filtered).

| Network | Probe is | probes | no data | off-path | conclusive | agree with Atlas |
|---|---|---|---|---|---|---|
| datacenter | customer | 9 | 0 | 6 | 3 | 66.7% (2/3) |
| datacenter | in-target | 3 | 0 | 0 | 3 | 0.0% (0/3) |
| eyeball | customer | 18 | 0 | 10 | 7 | 85.7% (6/7) |
| eyeball | in-target | 20 | 1 | 2 | 16 | 25.0% (4/16) |

## Disagreements

10 as classified; 6 with the origin ruled out (6517, 9299, 9790, 11351, 11426, 12912). Each one needs reading at trace level: Globalping fault, Atlas fault, or a real difference. Globalping measurements: `https://api.globalping.io/v1/measurements/<id>`; Atlas: `https://atlas.ripe.net/measurements/<id>/`.

Atlas side: 22 of the 25 SECURE (Target Filtered) probe readings in the Atlas-SECURE results compared here were stored with an empty invalid path. An empty path can mean the invalid traceroute had not arrived when the result was fetched; the classifier then names the first AS of the valid path as the boundary. Check the trace on atlas.ripe.net before counting such a disagreement against Globalping.

- **AS2027 MilkyWan** (4.4 days apart)
  - Atlas: SECURE (Verified Active) (2026-11-23; origin ruled out: SECURE (Verified Active)); trace_valid 242802869, trace_invalid 242802870; probe verdicts {'SECURE (Target Filtered)': 3, 'INCONCLUSIVE (Off-Path)': 2}; Target Filtered probes stored with an empty invalid path: 3 of 3
  - Globalping: VULNERABLE (2026-11-28; origin ruled out: SECURE (Verified Active)); mtr_valid 2XdKqZ88WkYFeutjN00021aHa, mtr_invalid 2UM9tutiJbCFXtlXE00021aHb
    - probe 0 (Lyon, FR AS2027, eyeball, in-target): SECURE (Upstream Filtered) (drop point named as AS13335); valid path [2027, 13335], invalid path [2027]
- **AS6517 LAKENETWORKS** (6.4 days apart)
  - Atlas: SECURE (Verified Active) (2026-11-21; origin ruled out: SECURE (Verified Active)); trace_valid 241879475, trace_invalid 241879476; probe verdicts {'SECURE (Target Filtered)': 1, 'INCONCLUSIVE (Off-Path)': 2}; Target Filtered probes stored with an empty invalid path: 1 of 1
  - Globalping: VULNERABLE (2026-11-28; origin ruled out: VULNERABLE); mtr_valid 21mffLhWJs5bJMrNO00021aHb, mtr_invalid 2Yyhv7MHFjbR2KHz400021aHb
    - probe 0 (Milan, IT AS6517, datacenter, in-target): VULNERABLE; valid path [6517, 13335], invalid path [6517, 13335]
    - probe 1 (Monza, IT AS6517, datacenter, in-target): VULNERABLE; valid path [6517, 13335], invalid path [6517, 13335]
    - probe 2 (Como, IT AS6517, datacenter, in-target): VULNERABLE; valid path [6517, 13335], invalid path [6517, 13335]
- **AS6799 Ote SA (Hellenic Telecommunications Orga** (3.3 days apart)
  - Atlas: SECURE (Verified Active) (2026-11-24; origin ruled out: SECURE (Verified Active)); trace_valid 243558127, trace_invalid 243558128; probe verdicts {'SECURE (Target Filtered)': 2, 'VULNERABLE (Bypass Route)': 1, 'INCONCLUSIVE (Off-Path)': 1}; Target Filtered probes stored with an empty invalid path: 2 of 2
  - Globalping: VULNERABLE (2026-11-28; origin ruled out: SECURE (Verified Active)); mtr_valid 20Vjl34j8Ojs3Sw5y00021aHa, mtr_invalid 2G8rX12FsD5HchufF00021aHa
    - probe 0 (Gerakini, GR AS29247, eyeball, customer): INCONCLUSIVE (Off-Path); valid path [13335], invalid path []
    - probe 1 (Rhodes, GR AS6799, eyeball, in-target): SECURE (Upstream Filtered) (drop point named as AS13335); valid path [6799, 13335], invalid path [6799]
- **AS6866 Cyprus Telecommunications Authority** (2.4 days apart)
  - Atlas: SECURE (Verified Active) (2026-11-25; origin ruled out: SECURE (Verified Active)); trace_valid 244222077, trace_invalid 244222080; probe verdicts {'INCONCLUSIVE (Off-Path)': 3, 'SECURE (Pre-Target Filtered)': 1, 'SECURE (Target Filtered)': 1}; Target Filtered probes stored with an empty invalid path: 1 of 1
  - Globalping: VULNERABLE (2026-11-28; origin ruled out: SECURE (Verified Active)); mtr_valid 2G1r99c9s6FeWkNEd00021aHa, mtr_invalid 25RLZrfJ43FSUjs5F00021aHa
    - probe 0 (Brussels, BE AS57169, datacenter, customer): INCONCLUSIVE (Off-Path); valid path [57169, 9009, 13335], invalid path [57169, 9009, 13335]
    - probe 1 (Dronten, NL AS202448, datacenter, customer): INCONCLUSIVE (Off-Path); valid path [202448, 50673, 13335], invalid path [202448, 50673, 13335]
    - probe 2 (Larnaca, CY AS216151, datacenter, customer): SECURE (Upstream Filtered) (drop point named as AS13335); valid path [216151, 6866, 13335], invalid path [216151, 6866]
- **AS9299 PLDT (Philippine Long Distance Telephone** (1.4 days apart)
  - Atlas: SECURE (Verified Active) (2026-11-26; origin ruled out: SECURE (Verified Active)); trace_valid 244787479, trace_invalid 244787480; probe verdicts {'SECURE (Target Filtered)': 1, 'INCONCLUSIVE (Off-Path)': 3}; Target Filtered probes stored with an empty invalid path: 1 of 1
  - Globalping: VULNERABLE (2026-11-28; origin ruled out: VULNERABLE); mtr_valid 2gc5zkNTC6eqzUn5400021aHZ, mtr_invalid 2LNhsMvPdl0BAt4Nf00021aHZ
    - probe 0 (Quezon City, PH AS9299, eyeball, in-target): VULNERABLE; valid path [9299, 13335], invalid path [9299, 13335]
    - probe 1 (Taguig, PH AS9299, eyeball, in-target): INCONCLUSIVE (Probe Down); valid path [], invalid path []; no data: invalid result failed
    - probe 2 (Cebu City, PH AS10139, eyeball, customer): INCONCLUSIVE (Off-Path); valid path [13335], invalid path [13335]
- **AS9790 Two Degrees Networks Limited** (0.4 days apart)
  - Atlas: SECURE (Verified Active) (2026-11-27; origin ruled out: SECURE (Verified Active)); trace_valid 245316015, trace_invalid 245316017; probe verdicts {'SECURE (Target Filtered)': 2, 'INCONCLUSIVE (Off-Path)': 2, 'INCONCLUSIVE (Probe Down)': 1}; Target Filtered probes stored with an empty invalid path: 2 of 2
  - Globalping: VULNERABLE (2026-11-28; origin ruled out: VULNERABLE (Partial Deployment)); mtr_valid 2XhJYJh48VnAfBPGI00021aHX, mtr_invalid 27B5fk8pIkVLOun0K00021aHY
    - probe 0 (Paraparaumu, NZ AS58666, eyeball, customer): INCONCLUSIVE (Off-Path); valid path [13335], invalid path [13335]
    - probe 1 (Christchurch, NZ AS140220, eyeball, customer): SECURE (Upstream Filtered); valid path [9790, 2906, 13335], invalid path [9790, 4826]
    - probe 2 (Clive, NZ AS9790, eyeball, in-target): SECURE (Upstream Filtered) (drop point named as AS13335); valid path [9790, 13335], invalid path [9790]
- **AS11351 Charter Communications Inc** (1.3 days apart)
  - Atlas: SECURE (Verified Active) (2026-11-26; origin ruled out: SECURE (Verified Active)); trace_valid 244801134, trace_invalid 244801135; probe verdicts {'INCONCLUSIVE (Off-Path)': 1, 'SECURE (Target Filtered)': 3}; Target Filtered probes stored with an empty invalid path: 3 of 3
  - Globalping: VULNERABLE (2026-11-28; origin ruled out: VULNERABLE); mtr_valid 2xJ2Ppb2pERMP0FVo00021aHY, mtr_invalid 2cakdIeX7HJZAjRTO00021aHY
    - probe 0 (Fayetteville, US AS11351, eyeball, in-target): SECURE (Upstream Filtered); valid path [11351, 7843, 13335], invalid path [11351]
    - probe 1 (Buffalo, US AS11351, eyeball, in-target): SECURE (Upstream Filtered); valid path [11351, 7843, 13335], invalid path [11351]
    - probe 2 (Rochester, US AS11351, eyeball, in-target): SECURE (Upstream Filtered); valid path [11351, 7843, 13335], invalid path [11351]
- **AS11426 Charter Communications Inc** (1.3 days apart)
  - Atlas: SECURE (Verified Active) (2026-11-26; origin ruled out: SECURE (Verified Active)); trace_valid 244803032, trace_invalid 244803033; probe verdicts {'SECURE (Target Filtered)': 4, 'INCONCLUSIVE (Off-Path)': 1}; Target Filtered probes stored with an empty invalid path: 4 of 4
  - Globalping: VULNERABLE (2026-11-28; origin ruled out: VULNERABLE); mtr_valid 2ihK154HjkTMW1sKu00021aHY, mtr_invalid 298cEoqDLT2kCKnW400021aHY
    - probe 0 (Sumter, US AS11426, eyeball, in-target): SECURE (Upstream Filtered); valid path [11426, 7843, 13335], invalid path [11426]
    - probe 1 (Albemarle, US AS11426, eyeball, in-target): SECURE (Upstream Filtered); valid path [11426, 7843, 13335], invalid path [11426]
    - probe 2 (Fayetteville, US AS11426, eyeball, in-target): SECURE (Upstream Filtered); valid path [11426, 7843, 13335], invalid path [11426]
- **AS11845 Vox Telecom Ltd** (1.3 days apart)
  - Atlas: SECURE (Verified Active) (2026-11-26; origin ruled out: SECURE (Verified Active)); trace_valid 244805760, trace_invalid 244805761; probe verdicts {'SECURE (Target Filtered)': 2}; Target Filtered probes stored with an empty invalid path: 2 of 2
  - Globalping: VULNERABLE (2026-11-28; origin ruled out: SECURE (Verified Active)); mtr_valid 20wvBvSMBZMTOhM2f00021aHY, mtr_invalid 2QLiTUVyRyy1tYQWc00021aHY
    - probe 0 (Cape Town, ZA AS11845, eyeball, in-target): SECURE (Upstream Filtered) (drop point named as AS13335); valid path [11845, 13335], invalid path [11845]
- **AS12912 T-Mobile Polska S.A.** (0.3 days apart)
  - Atlas: SECURE (Verified Active) (2026-11-27; origin ruled out: SECURE (Verified Active)); trace_valid 245333349, trace_invalid 245333350; probe verdicts {'INCONCLUSIVE (Off-Path)': 4, 'SECURE (Target Filtered)': 1}; Target Filtered probes stored with an empty invalid path: 0 of 1
  - Globalping: VULNERABLE (2026-11-28; origin ruled out: VULNERABLE); mtr_valid 2Np1UzYAiTeqmjL2y00021aHX, mtr_invalid 2T0cLAiC49kvGbJZQ00021aHX
    - probe 0 (Bytom, PL AS12912, eyeball, in-target): INCONCLUSIVE (Off-Path); valid path [13335], invalid path [13335]
    - probe 1 (Piotrkow Trybunalski, PL AS12912, eyeball, in-target): VULNERABLE; valid path [12912, 13335], invalid path [12912, 13335]

## Hop ASNs: Globalping's against the local mapping

357 public hops carried a Globalping ASN; 2 differed from the local mapping (PeeringDB IX LAN holder, else iptoasn).

| local | Globalping | on an IX LAN | hops |
|---|---|---|---|
| 29580 | 8717 | no | 1 |
| 13335 | 513 | yes | 1 |
