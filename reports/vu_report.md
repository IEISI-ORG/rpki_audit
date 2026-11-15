    [*] Loading Global Audit for VU...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: VU (Vanuatu)
    ====================================================================================================
    Total Networks:      14
    Total Cone Gravity:  3
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):     2 (14.3%) -> Protects 0.0% of Traffic
    VULNERABLE NETWORKS:         7 (50.0%) -> Exposes  100.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        5 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict     2 (40.0%)   IPv6 verdict     3 (60.0%)
      VULNERABLE main verdict     2 (40.0%)   IPv6 verdict     2 (40.0%)

    ====================================================================================================
     THE VU CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS45495  | VULNERABLE                     | -                              | 3        | -      | Interchange Ltd.
    AS9249   | STUB: VULNERABLE               | -                              | 0        | -      | Telecom Vanuatu Limited
    AS23959  | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | 0%     | Owl Limited
    AS43357  | STUB: VOLATILE                 | STUB: VOLATILE                 | 0        | 97%    | Owl Limited
    AS45935  | STUB: VULNERABLE               | -                              | 0        | -      | Wantok Network Limited
    AS131166 | NOT ROUTED                     | -                              | 0        | -      | Wantok Network Limited
    AS132228 | STUB: VULNERABLE               | -                              | 0        | -      | Vanuatu Government
    AS132254 | STUB: VULNERABLE               | -                              | 0        | -      | PRIMA DC LIMITED
    AS132429 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | Digicel Vanuatu LTD
    AS132797 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0        | -      | Vanuatu Internet Exchange (VIX)
    AS133383 | PROVIDER UNKNOWN (In BGP)      | -                              | 0        | -      | Vanuatu Government
    AS136949 | NOT ROUTED                     | -                              | 0        | -      | Engineering Business Services Limited
    AS136996 | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | Pacific Networks
    AS155052 | NOT ROUTED                     | -                              | 0        | -      | Telecom Vanuatu Limited

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to VU?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS45495  | 4          | VULNERABLE                     | Interchange Ltd.
    #2   | AS17819  | 1          | VULNERABLE                     | Equinix Asia Pacific
    #3   | AS38442  | 1          | REGRESSED                      | Vodafone Fiji Limited
    #4   | AS7492   | 1          | STUB: PASSIVE (Clean Pipe)     | Nexon Global Backbone
    #5   | AS4785   | 1          | PASSIVE (Clean Pipe)           | xTom
    #6   | AS142616 | 1          | STUB: VULNERABLE               | Misaka Network, Inc.
    #7   | AS3214   | 1          | ACTIVE LOCAL ROV               | xTom GmbH
    #8   | AS8888   | 1          | VOLATILE                       | xTom Pty Ltd
    #9   | AS23961  | 1          | VULNERABLE                     | Misaka Network, Inc.
    #10  | AS57695  | 1          | VULNERABLE                     | Misaka Network, Inc.
    #11  | AS45355  | 1          | ACTIVE LOCAL ROV               | Digicel Fiji Limited
    #12  | AS6939   | 1          | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #13  | AS133383 | 1          | PROVIDER UNKNOWN (In BGP)      | Vanuatu Government
    #14  | AS153346 | 1          | STUB: VULNERABLE               | HawkNet Labs Pty Ltd
    #15  | AS136557 | 1          | PARTIAL: VULNERABLE (Mixed)    | Host Universal Pty Ltd

    ====================================================================================================
     IPv6 DIFFERENCES (VU networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS132797 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | Vanuatu Internet Exchange (VIX)
