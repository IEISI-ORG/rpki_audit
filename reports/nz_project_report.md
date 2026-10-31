        - Loading Cones from final_as_rank.csv... OK (88086 ASNs)
        - Loading Graph from data/downstream_graph.json... OK

    ====================================================================================================
     NEW ZEALAND ROUTING SECURITY — PROJECT REPORT (2026-11-01)
    ====================================================================================================
    Audit file:        rov_audit_v22_final.csv (written 2026-11-01)
    NZ networks:       699
    APNIC excluded:    2026-08-05 to 2026-08-18 (APNIC Labs test window lifted non-filtering NZ/AU networks); a daily reading is dropped
                       when its rolling window overlaps these dates.

    ====================================================================================================
     1. VERDICTS
    ====================================================================================================
    PARTIAL        14 networks ( 2.0%) | 84.5% of NZ cone gravity
    SECURE         85 networks (12.2%) |  8.6% of NZ cone gravity
    UNKNOWN       270 networks (38.6%) |  0.0% of NZ cone gravity
    VULNERABLE    330 networks (47.2%) |  6.9% of NZ cone gravity

    By verdict label:
      STUB: VULNERABLE                      316
      NOT ROUTED                            270
      STUB: PASSIVE (Clean Pipe)             67
      PARTIAL: VULNERABLE (Mixed)            14
      STUB: VOLATILE                          7
      PASSIVE (Clean Pipe)                    5
      VULNERABLE (Atlas Verified)             4
      STUB: UNRELIABLE                        4
      VULNERABLE                              4
      ACTIVE (Atlas Verified)                 2
      STUB: ACTIVE LOCAL ROV                  2
      REGRESSED                               2
      VOLATILE                                1
      STUB: FORTUITOUS ROV                    1

    ====================================================================================================
     2. NZ TOP 20 NETWORKS BY CUSTOMER CONE
    ====================================================================================================
    ASN       | Name                       | Verdict                     |  Cone | APNIC% |      n | Atlas v4                 | Atlas v6
    --------------------------------------------------------------------------------------------------------------------------------------------
    AS64073   | Vetta Group                | PARTIAL: VULNERABLE (Mixed) |  1696 |      0 |    161 | INCONCLUSIVE (stale)     | INCONCLUSIVE (stale)
    AS9790    | Two Degrees Networks Limit | ACTIVE (Atlas Verified)     |   112 |     99 | 20,773 | SECURE (Verified Activ   | INCONCLUSIVE (stale)
    AS135069  | Feenix Communications Limi | PARTIAL: VULNERABLE (Mixed) |    55 |      0 |    270 | VULNERABLE (stale)       | VULNERABLE (stale)
    AS45177   | Devoli                     | REGRESSED                   |    55 |      0 |  5,776 | VULNERABLE (stale)       | INCONCLUSIVE (stale)
    AS55850   | Mercury NZ Limited         | VOLATILE                    |    51 |     97 |  8,154 | VULNERABLE (stale)       | VULNERABLE (stale)
    AS4648    | Spark New Zealand          | PARTIAL: VULNERABLE (Mixed) |    48 |      3 |    101 | INCONCLUSIVE             | -
    AS38022   | REANNZ National Research a | PARTIAL: VULNERABLE (Mixed) |    32 |     80 |    132 | INCONCLUSIVE (stale)     | INCONCLUSIVE (stale)
    AS4768    | One New Zealand Group Limi | VULNERABLE                  |    31 |      1 |    156 | INCONCLUSIVE (Bypassed (stale) | -
    AS23838   | Solarix Networks Limited   | VULNERABLE (Atlas Verified) |    22 |      0 |    100 | VULNERABLE               | -
    AS18400   | Xtreme Networks Limited    | VULNERABLE                  |    16 |      0 |    102 | -                        | -
    AS24324   | Kordia Limited             | VULNERABLE (Atlas Verified) |    14 |      0 |    281 | VULNERABLE               | VULNERABLE (stale)
    AS4049    | CELLO GROUP LIMITED        | PARTIAL: VULNERABLE (Mixed) |    13 |      0 |    254 | INCONCLUSIVE             | VULNERABLE (stale)
    AS23655   | 2degrees Networks Limited  | ACTIVE (Atlas Verified)     |    12 |     98 |    388 | SECURE (Verified Activ   | SECURE (Verified Activ (stale)
    AS56030   | Voyager Internet Ltd.      | PARTIAL: VULNERABLE (Mixed) |    11 |      0 |    522 | VULNERABLE (stale)       | VULNERABLE (stale)
    AS4771    | Spark New Zealand Trading  | VULNERABLE (Atlas Verified) |     6 |      0 | 26,766 | VULNERABLE               | -
    AS17705   | InSPire Net Ltd            | PASSIVE (Clean Pipe)        |     6 |     99 |    586 | INCONCLUSIVE (stale)     | INCONCLUSIVE (stale)
    AS151336  | Verge                      | PARTIAL: VULNERABLE (Mixed) |     6 |      0 |    107 | INCONCLUSIVE (stale)     | -
    AS138398  | Prodigi Technology Service | PARTIAL: VULNERABLE (Mixed) |     5 |      0 |    105 | -                        | -
    AS9500    | One New Zealand Group Limi | VULNERABLE (Atlas Verified) |     4 |      0 | 15,222 | VULNERABLE               | VULNERABLE (stale)
    AS24183   | DTS LTD                    | PASSIVE (Clean Pipe)        |     4 |     98 |    122 | -                        | -

    APNIC% and n: most recent daily reading with n >= 100 samples, test window excluded.

    ====================================================================================================
     2b. RIPE ATLAS DETAIL (per-probe outcomes for NZ networks with an Atlas result)
    ====================================================================================================
    AS64073   IPv4 Vetta Group                  INCONCLUSIVE (2026-10-11) msm: 221357766 221357767 221357769 221357770
                  4 x INCONCLUSIVE (Off-Path)
                  probe 55515: no resolvable hop before the destination AS (probe's own AS not on the path)
    AS64073   IPv6 Vetta Group                  INCONCLUSIVE (2026-10-11) msm: 221363917 221363918 221363919 221363920
                  5 x INCONCLUSIVE (Off-Path)
    AS9790    IPv4 Two Degrees Networks Limited SECURE (Verified Active) (2026-10-26) msm: 227808125 227808126 227808127 227808128
                  2 x INCONCLUSIVE (Off-Path); 3 x SECURE (Target Filtered)
                  probe 1017031: no resolvable hop before the destination AS (probe's own AS not on the path)
    AS9790    IPv6 Two Degrees Networks Limited INCONCLUSIVE (2026-10-11) msm: 221361422 221361423 221361424 221361425
                  3 x INCONCLUSIVE (Off-Path); 2 x SECURE (Pre-Target Filtered)
                  probe 28226: invalid dropped at sibling AS23655 (SECURE (Pre-Target Filtered))
                  probe 1014480: invalid dropped at sibling AS23655 (SECURE (Pre-Target Filtered))
    AS135069  IPv4 Feenix Communications Limite VULNERABLE (2026-10-11) msm: 221358195 221358196 221358197 221358198
                  2 x INCONCLUSIVE (Off-Path); 1 x VULNERABLE
    AS135069  IPv6 Feenix Communications Limite VULNERABLE (2026-10-11) msm: 221364341 221364342 221364343 221364344
                  1 x INCONCLUSIVE (Off-Path); 1 x VULNERABLE
    AS45177   IPv4 Devoli                       VULNERABLE (2026-10-11) msm: 221355101 221355102 221355103 221355104
                  4 x INCONCLUSIVE (Off-Path); 1 x VULNERABLE
    AS45177   IPv6 Devoli                       INCONCLUSIVE (2026-10-11) msm: 221362002 221362003 221362004 221362005
                  2 x INCONCLUSIVE (Off-Path); 1 x SECURE (Pre-Target Filtered)
    AS55850   IPv4 Mercury NZ Limited           VULNERABLE (2026-10-11) msm: 221355646 221355648 221355649 221355651
                  2 x INCONCLUSIVE (Off-Path); 2 x VULNERABLE
    AS55850   IPv6 Mercury NZ Limited           VULNERABLE (2026-10-11) msm: 221362344 221362345 221362346 221362347
                  1 x INCONCLUSIVE (Off-Path); 3 x VULNERABLE
    AS4648    IPv4 Spark New Zealand            INCONCLUSIVE (2026-10-26) msm: 227803712 227803713 227803714 227803715
                  4 x INCONCLUSIVE (Off-Path)
                  probe 11172: routed via sibling AS4771, counted off-path
                  probe 25103: routed via sibling AS4771, counted off-path
                  probe 50937: no resolvable hop before the destination AS (probe's own AS not on the path)
    AS38022   IPv4 REANNZ National Research and INCONCLUSIVE (2026-10-11) msm: 221357489 221357490 221357491 221357492
                  1 x INCONCLUSIVE (Off-Path); 1 x SECURE (Pre-Target Filtered)
                  probe 61253: invalid dropped at sibling AS38299 (SECURE (Pre-Target Filtered))
    AS38022   IPv6 REANNZ National Research and INCONCLUSIVE (2026-10-11) msm: 221363379 221363381 221363383 221363385
                  1 x SECURE (Pre-Target Filtered)
                  probe 61253: invalid dropped at sibling AS38299 (SECURE (Pre-Target Filtered))
    AS23838   IPv4 Solarix Networks Limited     VULNERABLE (2026-10-29) msm: 229299652 229299653 229299654 229299655
                  1 x VULNERABLE
    AS24324   IPv4 Kordia Limited               VULNERABLE (2026-10-26) msm: 227842743 227842751 227842754 227842758
                  2 x VULNERABLE
    AS24324   IPv6 Kordia Limited               VULNERABLE (2026-10-11) msm: 221364652 221364653 221364654 221364655
                  1 x VULNERABLE
    AS4049    IPv4 CELLO GROUP LIMITED          INCONCLUSIVE (2026-10-26) msm: 227803252 227803254 227803255 227803257
                  2 x INCONCLUSIVE (Off-Path)
                  probe 21714: no resolvable hop before the destination AS (probe's own AS not on the path)
                  probe 1011526: no resolvable hop before the destination AS (probe's own AS not on the path)
    AS4049    IPv6 CELLO GROUP LIMITED          VULNERABLE (2026-10-11) msm: 221364902 221364903 221364904 221364905
                  2 x VULNERABLE
    AS23655   IPv4 2degrees Networks Limited    SECURE (Verified Active) (2026-10-29) msm: 229298507 229298508 229298509 229298510
                  4 x INCONCLUSIVE (Off-Path); 1 x SECURE (Target Filtered)
                  probe 1008416: routed via sibling AS9790, counted off-path
                  probe 28226: routed via sibling AS9790, counted off-path
                  probe 51455: routed via sibling AS9790, counted off-path
    AS23655   IPv6 2degrees Networks Limited    SECURE (Verified Active) (2026-10-11) msm: 221365326 221365327 221365328 221365329
                  2 x SECURE (Target Filtered)
    AS56030   IPv4 Voyager Internet Ltd.        VULNERABLE (2026-10-11) msm: 221360263 221360264 221360265 221360266
                  5 x VULNERABLE
    AS56030   IPv6 Voyager Internet Ltd.        VULNERABLE (2026-10-11) msm: 221365775 221365779 221365782 221365785
                  5 x VULNERABLE
    AS4771    IPv4 Spark New Zealand Trading Lt VULNERABLE (2026-10-26) msm: 227804928 227804929 227804930 227804931
                  2 x INCONCLUSIVE (Off-Path); 2 x VULNERABLE
                  probe 53909: no resolvable hop before the destination AS (probe's own AS not on the path)
                  probe 62811: no resolvable hop before the destination AS (probe's own AS not on the path)
    AS17705   IPv4 InSPire Net Ltd              INCONCLUSIVE (2026-10-20) msm: 225373909 225373911 225373913 225373914
                  no probe returned results (measurements ran, see msm IDs)
    AS17705   IPv6 InSPire Net Ltd              INCONCLUSIVE (2026-10-11) msm: 221366187 221366188 221366189 221366190
                  no probe returned results (measurements ran, see msm IDs)
    AS151336  IPv4 Verge                        INCONCLUSIVE (2026-10-11) msm: 221360707 221360708 221360710 221360711
                  1 x INCONCLUSIVE (Off-Path)
    AS9500    IPv4 One New Zealand Group Limite VULNERABLE (2026-10-26) msm: 227807874 227807875 227807876 227807877
                  4 x INCONCLUSIVE (Off-Path); 1 x VULNERABLE
                  probe 27273: no resolvable hop before the destination AS (probe's own AS not on the path)
                  probe 25812: no resolvable hop before the destination AS (probe's own AS not on the path)
                  probe 52955: no resolvable hop before the destination AS (probe's own AS not on the path)
                  probe 21757: no resolvable hop before the destination AS (probe's own AS not on the path)
    AS9500    IPv6 One New Zealand Group Limite VULNERABLE (2026-10-11) msm: 221362879 221362880 221362881 221362882
                  1 x INCONCLUSIVE (Probe Down); 1 x VULNERABLE
    AS45267   IPv4 Lightwire LTD                VULNERABLE (2026-10-11) msm: 221360932 221360933 221360934 221360935
                  1 x VULNERABLE
    AS45267   IPv6 Lightwire LTD                INCONCLUSIVE (2026-10-11) msm: 221366377 221366378 221366379 221366380
                  no probe returned results (measurements ran, see msm IDs)

    ====================================================================================================
     3. ROV TIMELINE, LAST 365 DAYS (APNIC, test window masked)
    ====================================================================================================
    States: FILTERING >= 95%, NOT FILTERING < 60%, else MIXED; a change needs 3 consecutive readings.

    AS9790    Two Degrees Networks Limited   started NOT FILTERING; now FILTERING (99%, n=20,773, 2026-10-24)
                                            2026-08-25: NOT FILTERING -> FILTERING
                                            Atlas v4: SECURE (Verified Active) (2026-10-26)
    AS45177   Devoli                         started FILTERING; now NOT FILTERING (0%, n=5,776, 2026-10-24)
                                            2026-07-06: FILTERING -> MIXED
                                            2026-07-15: MIXED -> FILTERING
                                            2026-07-22: FILTERING -> MIXED
                                            2026-07-28: MIXED -> NOT FILTERING
                                            Atlas v4: VULNERABLE (2026-10-11)
    AS55850   Mercury NZ Limited             started FILTERING; now FILTERING (97%, n=8,154, 2026-10-24)
                                            2026-09-02: FILTERING -> MIXED
                                            2026-09-05: MIXED -> NOT FILTERING
                                            2026-10-22: NOT FILTERING -> FILTERING
                                            Atlas v4: VULNERABLE (2026-10-11)
    AS4771    Spark New Zealand Trading Ltd. started NOT FILTERING; now NOT FILTERING (0%, n=26,766, 2026-10-24)
                                            Atlas v4: VULNERABLE (2026-10-26)
    AS4648    Spark New Zealand              started NOT FILTERING; now NOT FILTERING (3%, n=101, 2026-10-23)
                                            Atlas v4: INCONCLUSIVE (2026-10-26)
    AS9500    One New Zealand Group Limited  started NOT FILTERING; now NOT FILTERING (0%, n=15,222, 2026-10-24)
                                            Atlas v4: VULNERABLE (2026-10-26)
    AS4768    One New Zealand Group Limited  started NOT FILTERING; now NOT FILTERING (1%, n=156, 2026-10-24)
                                            Atlas v4: INCONCLUSIVE (Bypassed) (2026-04-22)
    AS38022   REANNZ National Research and E started MIXED; now MIXED (80%, n=132, 2026-07-29 — OLD READING)
                                            Atlas v4: INCONCLUSIVE (2026-10-11)

    Change dates are the first day the new state held. Readings whose window overlaps the
    test window are masked, so a change during 5-24 Aug (7-day window) shows as the first
    unmasked day; confirm such dates with Atlas.

    APNIC measures what users of the network see: filtering inherited from an upstream
    counts the same as local ROV. The Atlas verdicts above test the network itself.

    ====================================================================================================
     4. MEASUREMENT COVERAGE
    ====================================================================================================
    RIPE Atlas (from reports/nz_probe_gap.csv):
      probe inside network (IPv4 / IPv6): 30 / 19 of 699
      testable via a direct customer:     10
      not testable over IPv4:             659

    APNIC Labs:
      any APNIC score:                    45 of 699
      reading with n>=100 in last 30 days: 37 of 699
      APNIC samples come from ad impressions, so networks with few end users
      (research, enterprise, wholesale transit) get few or no readings.
      Largest networks with no APNIC score: AS38022 REANNZ National Rese, AS23838 Solarix Networks Lim, AS18400 Xtreme Networks Limi, AS151336 Verge, AS138398 Prodigi Technology S, AS24183 DTS LTD, AS58666 Vorco, AS55785 ISP Limited, AS17492 Vector Communication, AS18119 ACSData

    ====================================================================================================
     5. METHOD LIMITS
    ====================================================================================================
    Siblings: the topology treats each AS separately. CAIDA AS-to-organisation data puts
    315 NZ ASes in 74 multi-AS organisations, including:
      VETTA TRADING LIMITED                    AS64073, AS132918
      Two Degrees Mobile Limited               AS4610, AS9503, AS9790, AS9889, AS17474, AS17656 (+27 more)
      Feenix Communications Limited            AS132809, AS135069
      Devoli LTD                               AS9727, AS45177, AS56171, AS58443, AS132048, AS132391 (+3 more)
      Spark Ventures                           AS2569, AS2570, AS4648, AS4771, AS4834, AS9325 (+12 more)
      Mercury NZ Limited                       AS9876, AS55850, AS55926, AS132333, AS132375, AS132687 (+2 more)
      One New Zealand Group Limited            AS4763, AS4768, AS4830, AS7657, AS7714, AS9345 (+14 more)
      Research and Education Advanced Network  AS38018, AS38022, AS38299, AS38300, AS38492, AS38711 (+11 more)

    Inferred topology: of 96 AS adjacencies on NZ Atlas valid-path traceroutes,
    14 (15%) match an inferred provider-customer link. The rest are peering, IXP
    or links the valley-free inference missed; customer cones are built only from inferred links.

    IPv6: forensic tests can now run over IPv6 (batch_verify_smart_v4.py --af 6);
    networks without an IPv6 Atlas result above are IPv4-tested only.

    Customer routes: the isbgpsafeyet beacon is reached via peers and transit. No test here
    shows whether a network applies ROV to routes learned from its own customers.

    [*] Per-network verdicts: reports/nz_verdicts.csv (699 rows)
