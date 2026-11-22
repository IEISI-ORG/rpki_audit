        - Loading Cones from final_as_rank.csv... OK (88077 ASNs)
        - Loading Graph from data/downstream_graph.json... OK

    ====================================================================================================
     NEW ZEALAND ROUTING SECURITY — PROJECT REPORT (2026-11-22)
    ====================================================================================================
    Audit file:        rov_audit_v22_final.csv (written 2026-11-22)
    NZ networks:       698
    APNIC excluded:    2026-08-05 to 2026-08-18 (APNIC Labs test window lifted non-filtering NZ/AU networks); a daily reading is dropped
                       when its rolling window overlaps these dates.

    ====================================================================================================
     1. VERDICTS
    ====================================================================================================
    PARTIAL        12 networks ( 1.7%) |  3.0% of NZ cone gravity
    SECURE         80 networks (11.5%) | 90.5% of NZ cone gravity
    UNKNOWN       273 networks (39.1%) |  1.4% of NZ cone gravity
    VULNERABLE    333 networks (47.7%) |  5.2% of NZ cone gravity

    By verdict label:
      STUB: VULNERABLE                      318
      NOT ROUTED                            272
      STUB: PASSIVE (Clean Pipe)             64
      PARTIAL: VULNERABLE (Mixed)            12
      PASSIVE (Clean Pipe)                    7
      STUB: UNRELIABLE                        5
      VULNERABLE (Atlas Verified)             4
      STUB: VOLATILE                          4
      VULNERABLE                              3
      REGRESSED                               3
      ACTIVE (Atlas Verified)                 2
      Unverified (Transit/Peer?)              1
      VOLATILE                                1
      STUB: FORTUITOUS ROV                    1
      STUB: ACTIVE LOCAL ROV                  1

    ====================================================================================================
     2. NZ TOP 20 NETWORKS BY CUSTOMER CONE
    ====================================================================================================
    ASN       | Name                       | Verdict                     |  Cone | APNIC% |      n | Atlas v4                 | Atlas v6
    --------------------------------------------------------------------------------------------------------------------------------------------
    AS64073   | Vetta Group                | PASSIVE (Clean Pipe)        |  1857 |      0 |    147 | INCONCLUSIVE (stale)     | INCONCLUSIVE (stale)
    AS9790    | Two Degrees Networks Limit | ACTIVE (Atlas Verified)     |   122 |     96 | 22,519 | SECURE (Verified Activ   | INCONCLUSIVE (stale)
    AS55850   | Mercury NZ Limited         | VOLATILE                    |    62 |     92 |  8,840 | VULNERABLE (stale)       | VULNERABLE (stale)
    AS135069  | Feenix Communications Limi | PASSIVE (Clean Pipe)        |    56 |      0 |    217 | VULNERABLE (stale)       | VULNERABLE (stale)
    AS45177   | Devoli                     | REGRESSED                   |    47 |      0 |  7,834 | VULNERABLE (stale)       | INCONCLUSIVE (stale)
    AS4648    | Spark New Zealand          | PASSIVE (Clean Pipe)        |    47 |      0 |    111 | INCONCLUSIVE             | -
    AS4768    | One New Zealand Group Limi | Unverified (Transit/Peer?)  |    33 |      0 |    203 | INCONCLUSIVE (Bypassed (stale) | -
    AS38022   | REANNZ National Research a | PARTIAL: VULNERABLE (Mixed) |    32 |     80 |    132 | INCONCLUSIVE (stale)     | INCONCLUSIVE (stale)
    AS23838   | Solarix Networks Limited   | VULNERABLE (Atlas Verified) |    22 |      0 |    100 | VULNERABLE               | -
    AS18400   | Xtreme Networks Limited    | VULNERABLE                  |    16 |      0 |    102 | -                        | -
    AS24324   | Kordia Limited             | VULNERABLE (Atlas Verified) |    14 |      1 |    144 | VULNERABLE               | VULNERABLE (stale)
    AS4049    | CELLO GROUP LIMITED        | VULNERABLE (Atlas Verified) |    12 |      0 |    137 | VULNERABLE               | VULNERABLE (stale)
    AS56030   | Voyager Internet Ltd.      | PARTIAL: VULNERABLE (Mixed) |    11 |      0 |    659 | VULNERABLE (stale)       | VULNERABLE (stale)
    AS23655   | 2degrees Networks Limited  | ACTIVE (Atlas Verified)     |     8 |     95 |    482 | SECURE (Verified Activ   | SECURE (Verified Activ (stale)
    AS4771    | Spark New Zealand Trading  | VULNERABLE (Atlas Verified) |     8 |      0 | 29,556 | VULNERABLE               | -
    AS17705   | InSPire Net Ltd            | PASSIVE (Clean Pipe)        |     6 |     94 |    492 | INCONCLUSIVE (stale)     | INCONCLUSIVE (stale)
    AS138398  | Prodigi Technology Service | PARTIAL: VULNERABLE (Mixed) |     6 |      0 |    105 | -                        | -
    AS24183   | DTS LTD                    | PASSIVE (Clean Pipe)        |     4 |     98 |    122 | -                        | -
    AS151336  | Verge                      | PARTIAL: VULNERABLE (Mixed) |     4 |      0 |    107 | INCONCLUSIVE (stale)     | -
    AS9500    | One New Zealand Group Limi | PARTIAL: VULNERABLE (Mixed) |     4 |      0 | 18,123 | INCONCLUSIVE             | VULNERABLE (stale)

    APNIC% and n: most recent daily reading with n >= 100 samples, test window excluded.

    ====================================================================================================
     2b. RIPE ATLAS DETAIL (per-probe outcomes for NZ networks with an Atlas result)
    ====================================================================================================
    AS64073   IPv4 Vetta Group                  INCONCLUSIVE (2026-10-11) msm: 221357766 221357767 221357769 221357770
                  4 x INCONCLUSIVE (Off-Path)
                  probe 55515: no resolvable hop before the destination AS (probe's own AS not on the path)
    AS64073   IPv6 Vetta Group                  INCONCLUSIVE (2026-10-11) msm: 221363917 221363918 221363919 221363920
                  5 x INCONCLUSIVE (Off-Path)
    AS9790    IPv4 Two Degrees Networks Limited SECURE (Verified Active) (2026-11-19) msm: 240718736 240718737 240718738 240718739
                  2 x INCONCLUSIVE (Off-Path); 1 x SECURE (Target Filtered)
                  probe 1017031: no resolvable hop before the destination AS (probe's own AS not on the path)
    AS9790    IPv6 Two Degrees Networks Limited INCONCLUSIVE (2026-10-11) msm: 221361422 221361423 221361424 221361425
                  3 x INCONCLUSIVE (Off-Path); 2 x SECURE (Pre-Target Filtered)
                  probe 28226: invalid dropped at sibling AS23655 (SECURE (Pre-Target Filtered))
                  probe 1014480: invalid dropped at sibling AS23655 (SECURE (Pre-Target Filtered))
    AS55850   IPv4 Mercury NZ Limited           VULNERABLE (2026-10-11) msm: 221355646 221355648 221355649 221355651
                  2 x INCONCLUSIVE (Off-Path); 2 x VULNERABLE
    AS55850   IPv6 Mercury NZ Limited           VULNERABLE (2026-10-11) msm: 221362344 221362345 221362346 221362347
                  1 x INCONCLUSIVE (Off-Path); 3 x VULNERABLE
    AS135069  IPv4 Feenix Communications Limite VULNERABLE (2026-10-11) msm: 221358195 221358196 221358197 221358198
                  2 x INCONCLUSIVE (Off-Path); 1 x VULNERABLE
    AS135069  IPv6 Feenix Communications Limite VULNERABLE (2026-10-11) msm: 221364341 221364342 221364343 221364344
                  1 x INCONCLUSIVE (Off-Path); 1 x VULNERABLE
    AS45177   IPv4 Devoli                       VULNERABLE (2026-10-11) msm: 221355101 221355102 221355103 221355104
                  4 x INCONCLUSIVE (Off-Path); 1 x VULNERABLE
    AS45177   IPv6 Devoli                       INCONCLUSIVE (2026-10-11) msm: 221362002 221362003 221362004 221362005
                  2 x INCONCLUSIVE (Off-Path); 1 x SECURE (Pre-Target Filtered)
    AS4648    IPv4 Spark New Zealand            INCONCLUSIVE (2026-11-20) msm: 241359878 241359879 241359880 241359881
                  no probe returned results (measurements ran, see msm IDs)
    AS38022   IPv4 REANNZ National Research and INCONCLUSIVE (2026-10-11) msm: 221357489 221357490 221357491 221357492
                  1 x INCONCLUSIVE (Off-Path); 1 x SECURE (Pre-Target Filtered)
                  probe 61253: invalid dropped at sibling AS38299 (SECURE (Pre-Target Filtered))
    AS38022   IPv6 REANNZ National Research and INCONCLUSIVE (2026-10-11) msm: 221363379 221363381 221363383 221363385
                  1 x SECURE (Pre-Target Filtered)
                  probe 61253: invalid dropped at sibling AS38299 (SECURE (Pre-Target Filtered))
    AS23838   IPv4 Solarix Networks Limited     VULNERABLE (2026-11-21) msm: 241931040 241931041 241931043 241931044
                  1 x VULNERABLE
    AS24324   IPv4 Kordia Limited               VULNERABLE (2026-11-20) msm: 241377679 241377680 241377681 241377682
                  2 x VULNERABLE
    AS24324   IPv6 Kordia Limited               VULNERABLE (2026-10-11) msm: 221364652 221364653 221364654 221364655
                  1 x VULNERABLE
    AS4049    IPv4 CELLO GROUP LIMITED          VULNERABLE (2026-11-19) msm: 240711018 240711019 240711021 240711023
                  1 x INCONCLUSIVE (Off-Path); 1 x VULNERABLE
                  probe 21714: no resolvable hop before the destination AS (probe's own AS not on the path)
    AS4049    IPv6 CELLO GROUP LIMITED          VULNERABLE (2026-10-11) msm: 221364902 221364903 221364904 221364905
                  2 x VULNERABLE
    AS56030   IPv4 Voyager Internet Ltd.        VULNERABLE (2026-10-11) msm: 221360263 221360264 221360265 221360266
                  5 x VULNERABLE
    AS56030   IPv6 Voyager Internet Ltd.        VULNERABLE (2026-10-11) msm: 221365775 221365779 221365782 221365785
                  5 x VULNERABLE
    AS23655   IPv4 2degrees Networks Limited    SECURE (Verified Active) (2026-11-21) msm: 241930653 241930654 241930655 241930656
                  4 x INCONCLUSIVE (Off-Path); 1 x SECURE (Target Filtered)
                  probe 1008416: routed via sibling AS9790, counted off-path
                  probe 28226: routed via sibling AS9790, counted off-path
                  probe 1014480: routed via sibling AS9790, counted off-path
                  probe 50866: routed via sibling AS9790, counted off-path
    AS23655   IPv6 2degrees Networks Limited    SECURE (Verified Active) (2026-10-11) msm: 221365326 221365327 221365328 221365329
                  2 x SECURE (Target Filtered)
    AS4771    IPv4 Spark New Zealand Trading Lt VULNERABLE (2026-11-20) msm: 241361033 241361034 241361035 241361036
                  2 x INCONCLUSIVE (Off-Path); 2 x VULNERABLE
                  probe 53909: no resolvable hop before the destination AS (probe's own AS not on the path)
                  probe 62811: no resolvable hop before the destination AS (probe's own AS not on the path)
    AS17705   IPv4 InSPire Net Ltd              INCONCLUSIVE (2026-10-20) msm: 225373909 225373911 225373913 225373914
                  no probe returned results (measurements ran, see msm IDs)
    AS17705   IPv6 InSPire Net Ltd              INCONCLUSIVE (2026-10-11) msm: 221366187 221366188 221366189 221366190
                  no probe returned results (measurements ran, see msm IDs)
    AS151336  IPv4 Verge                        INCONCLUSIVE (2026-10-11) msm: 221360707 221360708 221360710 221360711
                  1 x INCONCLUSIVE (Off-Path)
    AS9500    IPv4 One New Zealand Group Limite INCONCLUSIVE (2026-11-19) msm: 240717663 240717664 240717665 240717667
                  5 x INCONCLUSIVE (Off-Path)
                  probe 27273: no resolvable hop before the destination AS (probe's own AS not on the path)
                  probe 2547: no resolvable hop before the destination AS (probe's own AS not on the path)
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

    AS9790    Two Degrees Networks Limited   started NOT FILTERING; now FILTERING (96%, n=22,519, 2026-11-15)
                                            2026-08-25: NOT FILTERING -> FILTERING
                                            Atlas v4: SECURE (Verified Active) (2026-11-19)
    AS45177   Devoli                         started FILTERING; now NOT FILTERING (0%, n=7,834, 2026-11-15)
                                            2026-07-06: FILTERING -> MIXED
                                            2026-07-15: MIXED -> FILTERING
                                            2026-07-22: FILTERING -> MIXED
                                            2026-07-28: MIXED -> NOT FILTERING
                                            Atlas v4: VULNERABLE (2026-10-11)
    AS55850   Mercury NZ Limited             started FILTERING; now MIXED (92%, n=8,840, 2026-11-15)
                                            2026-09-02: FILTERING -> MIXED
                                            2026-09-05: MIXED -> NOT FILTERING
                                            2026-10-22: NOT FILTERING -> FILTERING
                                            2026-10-30: FILTERING -> MIXED
                                            Atlas v4: VULNERABLE (2026-10-11)
    AS4771    Spark New Zealand Trading Ltd. started NOT FILTERING; now NOT FILTERING (0%, n=29,556, 2026-11-15)
                                            Atlas v4: VULNERABLE (2026-11-20)
    AS4648    Spark New Zealand              started NOT FILTERING; now NOT FILTERING (0%, n=111, 2026-11-15)
                                            Atlas v4: INCONCLUSIVE (2026-11-20)
    AS9500    One New Zealand Group Limited  started NOT FILTERING; now NOT FILTERING (0%, n=18,123, 2026-11-15)
                                            Atlas v4: INCONCLUSIVE (2026-11-19)
    AS4768    One New Zealand Group Limited  started NOT FILTERING; now NOT FILTERING (0%, n=203, 2026-11-15)
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
      probe inside network (IPv4 / IPv6): 33 / 20 of 698
      testable via a direct customer:     11
      not testable over IPv4:             654

    APNIC Labs:
      any APNIC score:                    43 of 698
      reading with n>=100 in last 30 days: 36 of 698
      APNIC samples come from ad impressions, so networks with few end users
      (research, enterprise, wholesale transit) get few or no readings.
      Largest networks with no APNIC score: AS38022 REANNZ National Rese, AS23838 Solarix Networks Lim, AS18400 Xtreme Networks Limi, AS138398 Prodigi Technology S, AS24183 DTS LTD, AS151336 Verge, AS58666 Vorco, AS17492 Vector Communication, AS135889 Softsource Ltd, AS9303 The Digital Lab 2007

    ====================================================================================================
     5. METHOD LIMITS
    ====================================================================================================
    Siblings: the topology treats each AS separately. CAIDA AS-to-organisation data puts
    315 NZ ASes in 74 multi-AS organisations, including:
      VETTA TRADING LIMITED                    AS64073, AS132918
      Two Degrees Mobile Limited               AS4610, AS9503, AS9790, AS9889, AS17474, AS17656 (+27 more)
      Mercury NZ Limited                       AS9876, AS55850, AS55926, AS132333, AS132375, AS132687 (+2 more)
      Feenix Communications Limited            AS132809, AS135069
      Spark Ventures                           AS2569, AS2570, AS4648, AS4771, AS4834, AS9325 (+12 more)
      Devoli LTD                               AS9727, AS45177, AS56171, AS58443, AS132048, AS132391 (+3 more)
      One New Zealand Group Limited            AS4763, AS4768, AS4830, AS7657, AS7714, AS9345 (+14 more)
      Research and Education Advanced Network  AS38018, AS38022, AS38299, AS38300, AS38492, AS38711 (+11 more)

    Inferred topology: of 90 AS adjacencies on NZ Atlas valid-path traceroutes,
    14 (16%) match an inferred provider-customer link. The rest are peering, IXP
    or links the valley-free inference missed; customer cones are built only from inferred links.

    IPv6: forensic tests can now run over IPv6 (batch_verify_smart_v4.py --af 6);
    networks without an IPv6 Atlas result above are IPv4-tested only.

    Customer routes: the isbgpsafeyet beacon is reached via peers and transit. No test here
    shows whether a network applies ROV to routes learned from its own customers.

    [*] Per-network verdicts: reports/nz_verdicts.csv (698 rows)
