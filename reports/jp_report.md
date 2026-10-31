    [*] Loading Global Audit for JP...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: JP (Japan)
    ====================================================================================================
    Total Networks:      982
    Total Cone Gravity:  1,801
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   200 (20.4%) -> Protects 62.2% of Traffic
    VULNERABLE NETWORKS:       533 (54.3%) -> Exposes  34.9% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        433 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   109 (25.2%)   IPv6 verdict   124 (28.6%)
      VULNERABLE main verdict   311 (71.8%)   IPv6 verdict   299 (69.1%)

    ====================================================================================================
     THE JP CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS2497   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 467      | 94%    | Internet Initiative Japan Inc.
    AS17676  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 431      | 96%    | SoftBank Corp.
    AS2516   | REGRESSED                      | REGRESSED                      | 263      | 0%     | KDDI Corporation
    AS2907   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 114      | 8%     | Science Information Network
    AS4713   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 99       | 90%    | NTT Communications Corporation (OCN)
    AS2519   | REGRESSED                      | REGRESSED                      | 88       | 0%     | ARTERIA Networks Corporation
    AS10010  | REGRESSED                      | REGRESSED                      | 39       | 0%     | TOKAI Communications Corporation
    AS2518   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 37       | 90%    | BIGLOBE Inc.
    AS59105  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 27       | -      | Home NOC Operators Group
    AS150369 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 17       | -      | TelHi Corporation
    AS9824   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 15       | 91%    | JCOM Co., Ltd.
    AS7670   | REGRESSED                      | REGRESSED                      | 15       | 0%     | Enecom,Inc.
    AS2500   | REGRESSED                      | REGRESSED                      | 14       | -      | WIDE Project
    AS7529   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 13       | -      | GMO NetIRD, Inc.
    AS59103  | REGRESSED                      | REGRESSED                      | 12       | -      | SoftEther Corporation
    AS9354   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 11       | 90%    | Community Network Center Inc.
    AS7679   | REGRESSED                      | REGRESSED                      | 10       | 0%     | QTnet,Inc.
    AS38074  | VULNERABLE                     | VULNERABLE                     | 9        | -      | SDCC Japan-West Area
    AS17511  | REGRESSED                      | REGRESSED                      | 8        | 0%     | OPTAGE Inc.
    AS214675 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 7        | -      | Hidenori Matsuo

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to JP?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS2497   | 164        | ACTIVE LOCAL ROV               | Internet Initiative Japan Inc.
    #2   | AS17676  | 143        | ACTIVE LOCAL ROV               | SoftBank Corp.
    #3   | AS2516   | 113        | REGRESSED                      | KDDI Corporation
    #4   | AS2907   | 95         | VULNERABLE (Atlas Verified)    | Science Information Network
    #5   | AS2914   | 82         | INCONSISTENT                   | NTT America, Inc.
    #6   | AS4713   | 82         | ACTIVE LOCAL ROV               | NTT Communications Corporation (OCN)
    #7   | AS2519   | 71         | REGRESSED                      | ARTERIA Networks Corporation
    #8   | AS6939   | 35         | ACTIVE LOCAL ROV               | Hurricane Electric LLC
    #9   | AS4637   | 35         | VOLATILE                       | Telstra International Limited
    #10  | AS2518   | 34         | ACTIVE LOCAL ROV               | BIGLOBE Inc.
    #11  | AS10010  | 32         | REGRESSED                      | TOKAI Communications Corporation
    #12  | AS3356   | 20         | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #13  | AS9607   | 19         | ACTIVE LOCAL ROV               | BroadBand Tower, Inc.
    #14  | AS9824   | 19         | ACTIVE LOCAL ROV               | JCOM Co., Ltd.
    #15  | AS7670   | 19         | REGRESSED                      | Enecom,Inc.
    #16  | AS59105  | 18         | ACTIVE LOCAL ROV               | Home NOC Operators Group
    #17  | AS2500   | 17         | REGRESSED                      | WIDE Project
    #18  | AS7529   | 17         | PARTIAL: VULNERABLE (Mixed)    | GMO NetIRD, Inc.
    #19  | AS174    | 16         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #20  | AS8220   | 16         | ACTIVE LOCAL ROV               | COLT

    ====================================================================================================
     IPv6 DIFFERENCES (JP networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS58791  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 3/3            | GMO Internet, Inc.
    AS2515   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Japan Network Information Center
    AS139076 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | EnjoyVC Japan Corporation
    AS138968 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | rainbow network limited
    AS151374 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | IX-layers, Inc.
    AS153929 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Allied Business Inc.
    AS18135  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | BTV CO.,LTD.
    AS4680   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Mitsubishi Electric Information Network 
    AS7674   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NTT DOCOMO BUSINESS, Inc
    AS7665   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Okayama Prefectural Government
    AS17937  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NIKKEI ADVANCED SYSTEMS INC.
    AS63793  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Japan OPS Better Co., Ltd.
    AS63794  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ILKS Inc.
    AS59098  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Mamireimu Net Work's
    AS45689  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Convivial Net
    AS37922  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Diversitymedia Co.,Ltd.
    AS37918  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NTT, Inc.
