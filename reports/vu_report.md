    [*] Loading Global Audit for VU...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: VU (Vanuatu)
    ====================================================================================================
    Total Networks:      13
    Total Cone Gravity:  3
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):     2 (15.4%) -> Protects 0.0% of Traffic
    VULNERABLE NETWORKS:         7 (53.8%) -> Exposes  100.0% of Traffic
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
    AS23959  | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | 3%     | Owl Limited
    AS9249   | STUB: VULNERABLE               | -                              | 0        | 1%     | Telecom Vanuatu Limited
    AS136949 | NOT ROUTED                     | -                              | 0        | -      | Engineering Business Services Limited
    AS136996 | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | Pacific Networks
    AS132254 | STUB: VULNERABLE               | -                              | 0        | -      | PRIMA DC LIMITED
    AS132228 | STUB: VULNERABLE               | -                              | 0        | -      | Vanuatu Government
    AS132797 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0        | -      | Vanuatu Internet Exchange (VIX)
    AS132429 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | Digicel Vanuatu LTD
    AS131166 | NOT ROUTED                     | -                              | 0        | -      | Wantok Network Limited
    AS133383 | PROVIDER UNKNOWN (In BGP)      | -                              | 0        | -      | Vanuatu Government
    AS43357  | STUB: VOLATILE                 | STUB: VOLATILE                 | 0        | 99%    | Owl Limited
    AS45935  | STUB: VULNERABLE               | -                              | 0        | -      | Wantok Network Limited

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to VU?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS45495  | 4          | VULNERABLE                     | Interchange Ltd.
    #2   | AS17819  | 1          | VULNERABLE                     | Equinix Asia Pacific
    #3   | AS4785   | 1          | PASSIVE (Clean Pipe)           | xTom
    #4   | AS38442  | 1          | REGRESSED                      | Vodafone Fiji Limited
    #5   | AS7492   | 1          | STUB: PASSIVE (Clean Pipe)     | Nexon Global Backbone
    #6   | AS153346 | 1          | STUB: VULNERABLE               | HawkNet Labs Pty Ltd
    #7   | AS136557 | 1          | PARTIAL: VULNERABLE (Mixed)    | Host Universal Pty Ltd
    #8   | AS6939   | 1          | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #9   | AS133383 | 1          | PROVIDER UNKNOWN (In BGP)      | Vanuatu Government
    #10  | AS45355  | 1          | ACTIVE LOCAL ROV               | Digicel Fiji Limited
    #11  | AS142616 | 1          | STUB: VULNERABLE               | Misaka Network, Inc.
    #12  | AS3214   | 1          | ACTIVE LOCAL ROV               | xTom GmbH
    #13  | AS8888   | 1          | INCONSISTENT                   | xTom Pty Ltd
    #14  | AS23961  | 1          | PARTIAL: VULNERABLE (Mixed)    | Misaka Network, Inc.
    #15  | AS57695  | 1          | VULNERABLE                     | Misaka Network, Inc.

    ====================================================================================================
     IPv6 DIFFERENCES (VU networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS132797 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | Vanuatu Internet Exchange (VIX)
