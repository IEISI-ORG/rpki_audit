    [*] Loading Global Audit for DE...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: DE (Germany)
    ====================================================================================================
    Total Networks:      3,286
    Total Cone Gravity:  188,352
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   978 (29.8%) -> Protects 98.6% of Traffic
    VULNERABLE NETWORKS:      1575 (47.9%) -> Exposes  0.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1,795 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   676 (37.7%)   IPv6 verdict   765 (42.6%)
      VULNERABLE main verdict  1044 (58.2%)   IPv6 verdict   971 (54.1%)

    ====================================================================================================
     THE DE CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS3320   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 71101    | 94%    | Deutsche Telekom AG
    AS33891  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 46034    | -      | Core-Backbone GmbH
    AS34549  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 34612    | -      | meerfarbig GmbH & Co. KG
    AS29632  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 27985    | -      | Netassist International EOOD
    AS5405   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3343     | -      | Inter.link GmbH
    AS50629  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1403     | 92%    | LWLcom GmbH
    AS212895 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 592      | -      | Johannes Ernst
    AS13237  | REGRESSED                      | REGRESSED                      | 304      | 0%     | euNetworks GmbH
    AS8881   | REGRESSED                      | REGRESSED                      | 184      | 0%     | 1&1 Versatel GmbH
    AS49581  | REGRESSED                      | REGRESSED                      | 176      | 2%     | Ferdinand Zink trading as Tube-Hosting
    AS24961  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 174      | 1%     | WIIT AG (fka. myLoc Managed IT AG)
    AS199854 | VULNERABLE                     | VULNERABLE                     | 168      | -      | Jens Thies
    AS44066  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 114      | -      | firstcolo GmbH
    AS3209   | REGRESSED                      | REGRESSED                      | 113      | 0%     | Vodafone GmbH
    AS35708  | Unverified (Transit/Peer?)     | -                              | 103      | -      | 4b42 UG
    AS57821  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 87       | -      | Nonattached Network e.V.
    AS58212  | REGRESSED                      | REGRESSED                      | 79       | 1%     | dataforest GmbH
    AS30823  | REGRESSED                      | REGRESSED                      | 69       | 8%     | aurologic GmbH
    AS8767   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 67       | 92%    | M-net Telekommunikations GmbH
    AS9145   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 51       | 92%    | EWE TEL GmbH

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to DE?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS3320   | 504        | CORE: ACTIVE PROTECTOR         | Deutsche Telekom AG
    #2   | AS1299   | 229        | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
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
    #13  | AS2914   | 75         | CORE: ACTIVE PROTECTOR         | NTT America, Inc.
    #14  | AS3257   | 71         | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #15  | AS8767   | 60         | ACTIVE LOCAL ROV               | M-net Telekommunikations GmbH
    #16  | AS20473  | 58         | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #17  | AS50629  | 57         | ACTIVE LOCAL ROV               | LWLcom GmbH
    #18  | AS9002   | 49         | ACTIVE LOCAL ROV               | RETN Limited
    #19  | AS24961  | 47         | PASSIVE (Clean Pipe)           | WIIT AG (fka. myLoc Managed IT AG)
    #20  | AS34309  | 43         | PASSIVE (Clean Pipe)           | Link11 GmbH

    ====================================================================================================
     IPv6 DIFFERENCES (DE networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS214915 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Jan Smyrek
    AS203329 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NTT Global Data Centers EMEA GmbH
    AS48200  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | Opteamax GmbH
    AS61157  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | PlusServer GmbH
    AS12731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | IPHH Internet Port Hamburg GmbH
    AS205112 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PHILUNET GmbH
    AS8319   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NETHINKS GmbH
    AS44700  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Haendle & Korte GmbH
    AS8879   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | DTS Systeme GmbH
    AS31103  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Keyweb AG
    AS203724 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Musarubra Germany GmbH
    AS15580  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Allianz Technology SE
    AS48646  | Unverified (Transit/Peer?)     | PASSIVE (Clean Pipe)           | 0/1            | SDRmedia Verwaltungs GmbH
    AS13058  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | serve-u - Buchholz und Sünderhauf GbR
    AS12817  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | GeFoekoM e.V.
    AS59570  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Jens Zimperfeld
    AS197477 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 4/5            | Moritz Mantel trading as Nerdscave
    AS39083  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | David Froehlich
    AS39614  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Dawico Deutschland GmbH
    AS212341 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Stephan Rakowski, trading as CSN-Solutio
    AS209846 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | SWP Stadtwerke Pforzheim GmbH & Co. KG
    AS200081 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Netversor GmbH
    AS201545 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | AGRAVIS Ost GmbH & Co. KG
    AS201530 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | LVM Landwirtschaftlicher Versicherungsve
    AS209623 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | GASCADE Gastransport GmbH
    AS201222 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Frieder Mueller
    AS198818 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ISP Service eG
    AS199163 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | DATAGROUP Operations GmbH
    AS199118 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Heinlein Support GmbH
    AS210333 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Inter Krankenversicherung AG
