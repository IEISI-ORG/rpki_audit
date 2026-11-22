    [*] Loading Global Audit for JP...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: JP (Japan)
    ====================================================================================================
    Total Networks:      979
    Total Cone Gravity:  1,798
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   229 (23.4%) -> Protects 63.4% of Traffic
    VULNERABLE NETWORKS:       503 (51.4%) -> Exposes  34.1% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        432 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   127 (29.4%)   IPv6 verdict   144 (33.3%)
      VULNERABLE main verdict   291 (67.4%)   IPv6 verdict   277 (64.1%)

    ====================================================================================================
     THE JP CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS2497   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 466      | 93%    | Internet Initiative Japan Inc.
    AS17676  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 430      | 95%    | SoftBank Corp.
    AS2516   | REGRESSED                      | REGRESSED                      | 264      | 0%     | KDDI Corporation
    AS2907   | INCONSISTENT                   | INCONSISTENT                   | 115      | 13%    | Science Information Network
    AS4713   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 96       | 85%    | NTT Communications Corporation (OCN)
    AS2519   | REGRESSED                      | REGRESSED                      | 85       | 0%     | ARTERIA Networks Corporation
    AS10010  | REGRESSED                      | REGRESSED                      | 38       | 4%     | TOKAI Communications Corporation
    AS2518   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 36       | 85%    | BIGLOBE Inc.
    AS59105  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 26       | -      | Home NOC Operators Group
    AS150369 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 18       | -      | TelHi Corporation
    AS9824   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 15       | 87%    | JCOM Co., Ltd.
    AS7670   | REGRESSED                      | REGRESSED                      | 14       | 0%     | Enecom,Inc.
    AS7529   | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 14       | -      | GMO NetIRD, Inc.
    AS2500   | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 13       | -      | WIDE Project
    AS7679   | REGRESSED                      | REGRESSED                      | 12       | 0%     | QTnet,Inc.
    AS9354   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 11       | 86%    | Community Network Center Inc.
    AS59103  | REGRESSED                      | REGRESSED                      | 11       | -      | SoftEther Corporation
    AS214675 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 10       | -      | Hidenori Matsuo
    AS38074  | VULNERABLE                     | VULNERABLE                     | 10       | -      | SDCC Japan-West Area
    AS17511  | REGRESSED                      | REGRESSED                      | 8        | 0%     | OPTAGE Inc.

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to JP?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS2497   | 164        | ACTIVE LOCAL ROV               | Internet Initiative Japan Inc.
    #2   | AS17676  | 143        | ACTIVE LOCAL ROV               | SoftBank Corp.
    #3   | AS2516   | 113        | REGRESSED                      | KDDI Corporation
    #4   | AS2907   | 95         | INCONSISTENT                   | Science Information Network
    #5   | AS2914   | 82         | CORE: ACTIVE PROTECTOR         | NTT America, Inc.
    #6   | AS4713   | 82         | ACTIVE LOCAL ROV               | NTT Communications Corporation (OCN)
    #7   | AS2519   | 71         | REGRESSED                      | ARTERIA Networks Corporation
    #8   | AS4637   | 35         | VOLATILE                       | Telstra International Limited
    #9   | AS6939   | 34         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #10  | AS2518   | 34         | ACTIVE LOCAL ROV               | BIGLOBE Inc.
    #11  | AS10010  | 32         | REGRESSED                      | TOKAI Communications Corporation
    #12  | AS3356   | 20         | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #13  | AS9607   | 19         | ACTIVE LOCAL ROV               | BroadBand Tower, Inc.
    #14  | AS9824   | 19         | ACTIVE LOCAL ROV               | JCOM Co., Ltd.
    #15  | AS7670   | 19         | REGRESSED                      | Enecom,Inc.
    #16  | AS2500   | 17         | PASSIVE (Clean Pipe)           | WIDE Project
    #17  | AS59105  | 17         | ACTIVE LOCAL ROV               | Home NOC Operators Group
    #18  | AS7529   | 17         | PASSIVE (Clean Pipe)           | GMO NetIRD, Inc.
    #19  | AS174    | 16         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #20  | AS8220   | 16         | ACTIVE LOCAL ROV               | COLT

    ====================================================================================================
     IPv6 DIFFERENCES (JP networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS138968 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | rainbow network limited
    AS2515   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Japan Network Information Center
    AS139076 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | EnjoyVC Japan Corporation
    AS151374 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | IX-layers, Inc.
    AS153929 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Allied Business Inc.
    AS37918  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NTT, Inc.
    AS37922  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Diversitymedia Co.,Ltd.
    AS4680   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Mitsubishi Electric Information Network 
    AS7674   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NTT DOCOMO BUSINESS, Inc
    AS7665   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Okayama Prefectural Government
    AS18135  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | BTV CO.,LTD.
    AS18097  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | D.C.N. Corporation
    AS17937  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NIKKEI ADVANCED SYSTEMS INC.
    AS63793  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Japan OPS Better Co., Ltd.
    AS63794  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ILKS Inc.
    AS59098  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Mamireimu Net Work's
    AS45689  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Convivial Net
