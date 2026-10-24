    [*] Loading Global Audit for SB...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: SB (Solomon Islands)
    ====================================================================================================
    Total Networks:      11
    Total Cone Gravity:  4
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):     0 ( 0.0%) -> Protects 0.0% of Traffic
    VULNERABLE NETWORKS:         9 (81.8%) -> Exposes  50.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        3 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict     0 ( 0.0%)   IPv6 verdict     1 (33.3%)
      VULNERABLE main verdict     2 (66.7%)   IPv6 verdict     2 (66.7%)

    ====================================================================================================
     THE SB CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS139609 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 2        | -      | Solomon Islands Submarine Cable Company
    AS45891  | VULNERABLE                     | -                              | 2        | 1%     | Solomon Telekom Co Ltd
    AS139277 | STUB: VULNERABLE               | -                              | 0        | -      | Solomon Islands Government ICT Support D
    AS142279 | STUB: VULNERABLE               | -                              | 0        | -      | Solitech Ltd
    AS150403 | STUB: VULNERABLE               | -                              | 0        | -      | Solomon Islands National Provident Fund 
    AS150349 | STUB: VULNERABLE               | -                              | 0        | -      | Pacific Vaizeds Enterprise Ltd
    AS24013  | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | SB Professional Services
    AS132260 | NOT ROUTED                     | -                              | 0        | -      | SATSOL LIMITED
    AS132468 | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | 1%     | SATSOL LIMITED
    AS132462 | STUB: VULNERABLE               | -                              | 0        | -      | Bemobile Solomon Islands Ltd
    AS134525 | STUB: VULNERABLE               | -                              | 0        | -      | Solomon Telekom Co Ltd

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to SB?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS139609 | 4          | PARTIAL: VULNERABLE (Mixed)    | Solomon Islands Submarine Cable Company
    #2   | AS45891  | 2          | VULNERABLE                     | Solomon Telekom Co Ltd
    #3   | AS4637   | 1          | VOLATILE                       | Telstra International Limited
    #4   | AS17559  | 1          | PASSIVE (Clean Pipe)           | Spectrums Core Network
    #5   | AS135409 | 1          | PARTIAL: VULNERABLE (Mixed)    | Kacific Broadband Satellites Pte Ltd
    #6   | AS132468 | 1          | STUB: VULNERABLE               | SATSOL LIMITED
    #7   | AS7594   | 1          | PASSIVE (Clean Pipe)           | On Q

    ====================================================================================================
     IPv6 DIFFERENCES (SB networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS139609 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Solomon Islands Submarine Cable Company
