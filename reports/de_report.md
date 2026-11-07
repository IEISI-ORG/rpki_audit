    [*] Loading Global Audit for DE...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: DE (Germany)
    ====================================================================================================
    Total Networks:      3,286
    Total Cone Gravity:  189,691
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   876 (26.7%) -> Protects 64.8% of Traffic
    VULNERABLE NETWORKS:      1644 (50.0%) -> Exposes  15.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1,790 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   585 (32.7%)   IPv6 verdict   663 (37.0%)
      VULNERABLE main verdict  1107 (61.8%)   IPv6 verdict  1037 (57.9%)

    ====================================================================================================
     THE DE CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS3320   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 71032    | 95%    | Deutsche Telekom AG
    AS33891  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 46982    | -      | Core-Backbone GmbH
    AS34549  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 35255    | -      | meerfarbig GmbH & Co. KG
    AS29632  | VULNERABLE                     | VULNERABLE                     | 28453    | -      | Netassist International EOOD
    AS5405   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 2620     | -      | Inter.link GmbH
    AS50629  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1479     | 95%    | LWLcom GmbH
    AS212895 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 578      | -      | Johannes Ernst
    AS13237  | REGRESSED                      | REGRESSED                      | 302      | 0%     | euNetworks GmbH
    AS8881   | REGRESSED                      | REGRESSED                      | 213      | 0%     | 1&1 Versatel GmbH
    AS24961  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 170      | 2%     | WIIT AG (fka. myLoc Managed IT AG)
    AS199854 | VULNERABLE                     | VULNERABLE                     | 163      | -      | Jens Thies
    AS49581  | REGRESSED                      | REGRESSED                      | 152      | 0%     | Ferdinand Zink trading as Tube-Hosting
    AS44066  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 134      | -      | firstcolo GmbH
    AS3209   | REGRESSED                      | REGRESSED                      | 125      | 0%     | Vodafone GmbH
    AS35708  | Unverified (Transit/Peer?)     | -                              | 94       | -      | 4b42 UG
    AS57821  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 80       | -      | Nonattached Network e.V.
    AS58212  | REGRESSED                      | REGRESSED                      | 77       | 1%     | dataforest GmbH
    AS8767   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 70       | 95%    | M-net Telekommunikations GmbH
    AS30823  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 69       | 9%     | aurologic GmbH
    AS9145   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 54       | 95%    | EWE TEL GmbH

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to DE?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS3320   | 504        | CORE: ACTIVE PROTECTOR         | Deutsche Telekom AG
    #2   | AS1299   | 229        | INCONSISTENT                   | Arelion (fka. Telia Carrier)
    #3   | AS6939   | 226        | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #4   | AS8220   | 212        | ACTIVE LOCAL ROV               | COLT
    #5   | AS3356   | 193        | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #6   | AS174    | 183        | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #7   | AS8881   | 160        | REGRESSED                      | 1&1 Versatel GmbH
    #8   | AS33891  | 156        | ACTIVE LOCAL ROV               | Core-Backbone GmbH
    #9   | AS5405   | 112        | ACTIVE LOCAL ROV               | Inter.link GmbH
    #10  | AS13237  | 96         | REGRESSED                      | euNetworks GmbH
    #11  | AS3209   | 93         | REGRESSED                      | Vodafone GmbH
    #12  | AS34927  | 81         | PARTIAL: VULNERABLE (Mixed)    | iFog GmbH
    #13  | AS2914   | 75         | INCONSISTENT                   | NTT America, Inc.
    #14  | AS3257   | 71         | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #15  | AS8767   | 60         | ACTIVE LOCAL ROV               | M-net Telekommunikations GmbH
    #16  | AS20473  | 58         | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #17  | AS50629  | 57         | ACTIVE LOCAL ROV               | LWLcom GmbH
    #18  | AS9002   | 49         | ACTIVE LOCAL ROV               | RETN Limited
    #19  | AS24961  | 47         | PARTIAL: VULNERABLE (Mixed)    | WIIT AG (fka. myLoc Managed IT AG)
    #20  | AS34309  | 43         | PARTIAL: VULNERABLE (Mixed)    | Link11 GmbH

    ====================================================================================================
     IPv6 DIFFERENCES (DE networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS51396  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 4/5            | Pfcloud UG (haftungsbeschrankt)
    AS12731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | IPHH Internet Port Hamburg GmbH
    AS205112 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PHILUNET GmbH
    AS41692  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/2            | OpenCarrier eG
    AS8319   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NETHINKS GmbH
    AS31103  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Keyweb AG
    AS8879   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | DTS Systeme GmbH
    AS203724 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Musarubra Germany GmbH
    AS59570  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Jens Zimperfeld
    AS15580  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Allianz Technology SE
    AS15372  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | IBH connect GmbH
    AS12817  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | GeFoekoM e.V.
    AS13058  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | serve-u - Buchholz und Sünderhauf GbR
    AS202046 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | FairNetz GmbH
    AS5605   | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | NetUSE AG
    AS39614  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Dawico Deutschland GmbH
    AS201222 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Frieder Mueller
    AS200599 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | eins energie in sachsen GmbH & Co. KG
    AS198333 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | DATAGROUP SE
    AS199118 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Heinlein Support GmbH
    AS199163 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | DATAGROUP Operations GmbH
    AS206356 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/4            | Freifunk Essen e.V.
    AS207160 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Factory Campus Verwaltungs-GmbH
    AS208444 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Bringe Informationstechnik GmbH
    AS209216 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Trusted-Service.net GmbH trading as Trus
    AS209185 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Tim Niemeyer
    AS208968 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Avacon Connect GmbH
    AS207498 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Expert Mark GmbH
    AS207535 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SONEXTIS GmbH
    AS207999 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | regiocom SE
