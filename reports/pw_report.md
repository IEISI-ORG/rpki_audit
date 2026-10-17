    [*] Loading Global Audit for PW...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: PW (Palau)
    ====================================================================================================
    Total Networks:      4
    Total Cone Gravity:  0
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):     1 (25.0%) -> Protects 0.0% of Traffic
    VULNERABLE NETWORKS:         3 (75.0%) -> Exposes  0.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        2 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict     1 (50.0%)   IPv6 verdict     2 (100.0%)
      VULNERABLE main verdict     1 (50.0%)   IPv6 verdict     0 ( 0.0%)

    ====================================================================================================
     THE PW CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS214652 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | ANQI CHEN
    AS17893  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0        | 0%     | Palau National Communications Corp.
    AS58932  | STUB: VULNERABLE               | -                              | 0        | 0%     | Palau Mobile Communications Inc.
    AS133897 | STUB: VULNERABLE               | -                              | 0        | -      | Palau Equipment Co. Inc.

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to PW?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS3605   | 2          | REGRESSED                      | Guam Cablevision, LLC.
    #2   | AS20473  | 1          | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #3   | AS140627 | 1          | ACTIVE LOCAL ROV               | OneQode
    #4   | AS174    | 1          | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #5   | AS24545  | 1          | STUB: VULNERABLE               | 8/F.,Sino Favour Centre ,1 OnYip Street 

    ====================================================================================================
     IPv6 DIFFERENCES (PW networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS17893  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Palau National Communications Corp.
