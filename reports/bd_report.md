    [*] Loading Global Audit for BD...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: BD (Bangladesh)
    ====================================================================================================
    Total Networks:      2,031
    Total Cone Gravity:  3,458
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    13 ( 0.6%) -> Protects 0.0% of Traffic
    VULNERABLE NETWORKS:      1545 (76.1%) -> Exposes  89.6% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        537 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict     1 ( 0.2%)   IPv6 verdict     5 ( 0.9%)
      VULNERABLE main verdict   529 (98.5%)   IPv6 verdict   529 (98.5%)

    ====================================================================================================
     THE BD CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS58717  | REGRESSED                      | REGRESSED                      | 1027     | 0%     | Summit Communications Ltd
    AS10075  | REGRESSED                      | REGRESSED                      | 407      | 0%     | Fiber@Home Global Limited
    AS139009 | REGRESSED                      | REGRESSED                      | 356      | 0%     | Windstream Communication Limited
    AS58682  | REGRESSED                      | REGRESSED                      | 264      | 0%     | Level3 Carrier Ltd.
    AS150178 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 200      | -      | EXABYTE LTD
    AS58715  | REGRESSED                      | REGRESSED                      | 158      | 0%     | EARTH TELECOMMUNICATION (Pvt) LTD.
    AS17494  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 91       | 0%     | Bangladesh Telegraph & Telephone Board
    AS139901 | REGRESSED                      | REGRESSED                      | 86       | -      | Apple Communication Ltd.
    AS150748 | REGRESSED                      | REGRESSED                      | 61       | 0%     | Gmax
    AS137491 | REGRESSED                      | REGRESSED                      | 61       | 0%     | Peerex Networks Ltd
    AS58656  | REGRESSED                      | REGRESSED                      | 55       | 0%     | bdHUB Limited
    AS149765 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 52       | 0%     | Coronet Corporation Limited
    AS149994 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 52       | 3%     | Rego Communications Ltd
    AS23688  | REGRESSED                      | REGRESSED                      | 44       | 0%     | Link3 Technologies Ltd.
    AS58945  | REGRESSED                      | REGRESSED                      | 38       | 0%     | Virgo Communication Ltd
    AS24323  | VULNERABLE                     | VULNERABLE                     | 34       | 13%    | aamra networks limited
    AS63961  | REGRESSED                      | REGRESSED                      | 32       | 0%     | Bangladesh Research and Education Networ
    AS141731 | REGRESSED                      | REGRESSED                      | 31       | 0%     | Max Hub Limited
    AS9230   | VULNERABLE                     | VULNERABLE                     | 26       | 0%     | Bangladesh Online Ltd.
    AS38203  | REGRESSED                      | REGRESSED                      | 24       | 2%     | ADN Telecom Ltd.

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to BD?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS58717  | 450        | REGRESSED                      | Summit Communications Ltd
    #2   | AS139009 | 172        | REGRESSED                      | Windstream Communication Limited
    #3   | AS10075  | 161        | REGRESSED                      | Fiber@Home Global Limited
    #4   | AS58682  | 153        | REGRESSED                      | Level3 Carrier Ltd.
    #5   | AS150178 | 121        | PARTIAL: VULNERABLE (Mixed)    | EXABYTE LTD
    #6   | AS58715  | 81         | REGRESSED                      | EARTH TELECOMMUNICATION (Pvt) LTD.
    #7   | AS139901 | 72         | REGRESSED                      | Apple Communication Ltd.
    #8   | AS137491 | 65         | REGRESSED                      | Peerex Networks Ltd
    #9   | AS149994 | 59         | PARTIAL: VULNERABLE (Mixed)    | Rego Communications Ltd
    #10  | AS17494  | 52         | VULNERABLE (Atlas Verified)    | Bangladesh Telegraph & Telephone Board
    #11  | AS58656  | 49         | REGRESSED                      | bdHUB Limited
    #12  | AS150748 | 44         | REGRESSED                      | Gmax
    #13  | AS141731 | 42         | REGRESSED                      | Max Hub Limited
    #14  | AS58945  | 41         | REGRESSED                      | Virgo Communication Ltd
    #15  | AS140684 | 38         | STUB: VULNERABLE               | Bangladesh Internet Exchange Trust
    #16  | AS23688  | 38         | REGRESSED                      | Link3 Technologies Ltd.
    #17  | AS24323  | 35         | VULNERABLE                     | aamra networks limited
    #18  | AS63961  | 33         | REGRESSED                      | Bangladesh Research and Education Networ
    #19  | AS132602 | 32         | PARTIAL: VULNERABLE (Mixed)    | Bangladesh Submarine Cable Company Limit
    #20  | AS149765 | 30         | PARTIAL: VULNERABLE (Mixed)    | Coronet Corporation Limited

    ====================================================================================================
     IPv6 DIFFERENCES (BD networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS149994 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 3/3            | Rego Communications Ltd
    AS132602 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | Bangladesh Submarine Cable Company Limit
    AS132267 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | NovoCom Limited
    AS139931 | Unverified (Transit/Peer?)     | PASSIVE (Clean Pipe)           | 0/1            | Bangladesh Submarine Cable Company Limit
    AS64092  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | IT Consultants PLC
    AS132817 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | DZCRD Networks Ltd
