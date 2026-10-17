    [*] Loading Global Audit for GU...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: GU (Guam)
    ====================================================================================================
    Total Networks:      10
    Total Cone Gravity:  6
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):     0 ( 0.0%) -> Protects 0.0% of Traffic
    VULNERABLE NETWORKS:         7 (70.0%) -> Exposes  100.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        6 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict     0 ( 0.0%)   IPv6 verdict     1 (16.7%)
      VULNERABLE main verdict     6 (100.0%)   IPv6 verdict     5 (83.3%)

    ====================================================================================================
     THE GU CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS3605   | REGRESSED                      | REGRESSED                      | 6        | 0%     | Guam Cablevision, LLC.
    AS152735 | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | Guam Exchange
    AS395400 | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | UNIVERSITY OF GUAM
    AS23676  | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | Mariana Islands Internet Exchange
    AS17456  | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | Pacific Data Systems
    AS9246   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0        | 0%     | Teleguam Holdings, LLC
    AS9548   | NOT ROUTED                     | -                              | 0        | -      | InternetPCI
    AS56200  | STUB: VULNERABLE               | -                              | 0        | -      | Guam Community College
    AS55863  | NOT ROUTED                     | -                              | 0        | -      | Choice Phone LLC
    AS133071 | NOT ROUTED                     | -                              | 0        | -      | DoCoMo Pacific

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to GU?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS7131   | 4          | REGRESSED                      | PTI Pacifica Inc.
    #2   | AS3356   | 2          | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #3   | AS2914   | 1          | CORE: ACTIVE PROTECTOR         | NTT America, Inc.
    #4   | AS17456  | 1          | STUB: VULNERABLE               | Pacific Data Systems
    #5   | AS3605   | 1          | REGRESSED                      | Guam Cablevision, LLC.
    #6   | AS395400 | 1          | STUB: VULNERABLE               | UNIVERSITY OF GUAM
    #7   | AS140627 | 1          | ACTIVE LOCAL ROV               | OneQode
    #8   | AS4637   | 1          | REGRESSED                      | Telstra International Limited
    #9   | AS174    | 1          | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC

    ====================================================================================================
     IPv6 DIFFERENCES (GU networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS9246   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Teleguam Holdings, LLC
