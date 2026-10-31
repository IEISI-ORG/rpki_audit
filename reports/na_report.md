    [*] Loading Global Audit for NA...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: NA (Namibia)
    ====================================================================================================
    Total Networks:      20
    Total Cone Gravity:  4
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):     1 ( 5.0%) -> Protects 0.0% of Traffic
    VULNERABLE NETWORKS:        16 (80.0%) -> Exposes  0.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        2 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict     0 ( 0.0%)   IPv6 verdict     1 (50.0%)
      VULNERABLE main verdict     1 (50.0%)   IPv6 verdict     1 (50.0%)

    ====================================================================================================
     THE NA CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS20459  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 4        | -      | Telecom Namibia
    AS329400 | STUB: VULNERABLE               | -                              | 0        | -      | Loc Eight Mobile (Pty) Ltd
    AS329395 | STUB: VULNERABLE               | -                              | 0        | -      | Rocketnet Internet Namibia
    AS329067 | STUB: VULNERABLE               | -                              | 0        | -      | Click Cloud Hosting Services CC
    AS329115 | NOT ROUTED                     | -                              | 0        | -      | Africa Online (Africa) (Pty) Ltd
    AS329665 | STUB: PASSIVE (Clean Pipe)     | -                              | 0        | -      | NamPower
    AS329698 | STUB: VULNERABLE               | -                              | 0        | -      | Unknown
    AS329626 | REGRESSED                      | -                              | 0        | -      | Oryx Fibre Infrastructure (Pty) Ltd
    AS329802 | STUB: VULNERABLE               | -                              | 0        | -      | Unknown
    AS328506 | STUB: VULNERABLE               | -                              | 0        | -      | Radio Electronic (Proprietary) Limited
    AS327842 | NOT ROUTED                     | -                              | 0        | -      | Trustco Group Holdings
    AS327694 | STUB: VULNERABLE               | -                              | 0        | -      | NamPower
    AS22735  | STUB: VULNERABLE               | -                              | 0        | -      | Government of the Republic of Namibia
    AS37201  | STUB: VULNERABLE               | -                              | 0        | -      | Bank Windhoek
    AS36877  | STUB: VULNERABLE               | -                              | 0        | -      | Africa Online (Africa) (Pty) Ltd
    AS37026  | STUB: VULNERABLE               | -                              | 0        | -      | Salt Essential Information Technology
    AS37009  | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | 0%     | MTC - Mobile Telecommunications, Ltd.
    AS36999  | STUB: VULNERABLE               | -                              | 0        | 2%     | Telecom Namibia
    AS36996  | STUB: VULNERABLE               | -                              | 0        | 1%     | Telecom Namibia
    AS37513  | STUB: VULNERABLE               | -                              | 0        | 0%     | Namibia University of Science and Techno

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to NA?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS33763  | 5          | PARTIAL: VULNERABLE (Mixed)    | Paratus Telecommunications Limited
    #2   | AS37009  | 4          | STUB: VULNERABLE               | MTC - Mobile Telecommunications, Ltd.
    #3   | AS20459  | 4          | PARTIAL: VULNERABLE (Mixed)    | Telecom Namibia
    #4   | AS174    | 2          | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #5   | AS37468  | 2          | VOLATILE                       | Angola Cables
    #6   | AS3741   | 1          | REGRESSED                      | Dimension Data
    #7   | AS37662  | 1          | PARTIAL: VULNERABLE (Mixed)    | West Indian Ocean Cable Company (WIOCC)
    #8   | AS329395 | 1          | STUB: VULNERABLE               | Rocketnet Internet Namibia
    #9   | AS30896  | 1          | STUB: VULNERABLE               | Afsat Communications Ltd
    #10  | AS30844  | 1          | PASSIVE (Clean Pipe)           | Liquid Intelligent Technologies 
    #11  | AS37100  | 1          | ACTIVE LOCAL ROV               | SEACOM Limited

    ====================================================================================================
     IPv6 DIFFERENCES (NA networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS20459  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Telecom Namibia
