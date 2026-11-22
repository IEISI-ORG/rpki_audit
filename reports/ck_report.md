    [*] Loading Global Audit for CK...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: CK (Cook Islands)
    ====================================================================================================
    Total Networks:      2
    Total Cone Gravity:  0
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):     0 ( 0.0%) -> Protects 0.0% of Traffic
    VULNERABLE NETWORKS:         1 (50.0%) -> Exposes  0.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict     0 ( 0.0%)   IPv6 verdict     1 (100.0%)
      VULNERABLE main verdict     0 ( 0.0%)   IPv6 verdict     0 ( 0.0%)

    ====================================================================================================
     THE CK CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS152093 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0        | -      | VakaNet Limited
    AS10131  | STUB: VULNERABLE               | -                              | 0        | 1%     | Telecom Cook Islands

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to CK?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS9507   | 1          | PARTIAL: VULNERABLE (Mixed)    | NextHop Pty Ltd
    #2   | AS45177  | 1          | REGRESSED                      | Devoli
    #3   | AS12684  | 1          | REGRESSED                      | SES ASTRA S.A.
    #4   | AS174    | 1          | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC

    ====================================================================================================
     IPv6 DIFFERENCES (CK networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS152093 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | VakaNet Limited
