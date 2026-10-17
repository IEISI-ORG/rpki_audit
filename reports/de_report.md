    [*] Loading Global Audit for DE...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: DE (Germany)
    ====================================================================================================
    Total Networks:      3,276
    Total Cone Gravity:  190,351
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   988 (30.2%) -> Protects 98.7% of Traffic
    VULNERABLE NETWORKS:      1523 (46.5%) -> Exposes  0.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1,753 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   686 (39.1%)   IPv6 verdict   768 (43.8%)
      VULNERABLE main verdict   994 (56.7%)   IPv6 verdict   931 (53.1%)

    ====================================================================================================
     THE DE CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS3320   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 70808    | 98%    | Deutsche Telekom AG
    AS33891  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 47014    | -      | Core-Backbone GmbH
    AS34549  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 34730    | -      | meerfarbig GmbH & Co. KG
    AS29632  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 29479    | -      | Netassist International EOOD
    AS5405   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3490     | -      | Inter.link GmbH
    AS50629  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1073     | 97%    | LWLcom GmbH
    AS212895 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 480      | -      | Johannes Ernst
    AS13237  | REGRESSED                      | REGRESSED                      | 304      | 0%     | euNetworks GmbH
    AS8881   | REGRESSED                      | REGRESSED                      | 215      | 0%     | 1&1 Versatel GmbH
    AS24961  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 189      | 1%     | WIIT AG (fka. myLoc Managed IT AG)
    AS49581  | REGRESSED                      | REGRESSED                      | 145      | 0%     | Ferdinand Zink trading as Tube-Hosting
    AS199854 | VULNERABLE                     | VULNERABLE                     | 138      | -      | Jens Thies
    AS44066  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 128      | -      | firstcolo GmbH
    AS3209   | REGRESSED                      | REGRESSED                      | 126      | 0%     | Vodafone GmbH
    AS57821  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 85       | -      | Nonattached Network e.V.
    AS35708  | Unverified (Transit/Peer?)     | -                              | 84       | -      | 4b42 UG
    AS34309  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 70       | -      | Link11 GmbH
    AS8767   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 70       | 97%    | M-net Telekommunikations GmbH
    AS30823  | REGRESSED                      | REGRESSED                      | 69       | -      | aurologic GmbH
    AS58212  | REGRESSED                      | REGRESSED                      | 68       | 1%     | dataforest GmbH

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to DE?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS3320   | 504        | CORE: ACTIVE PROTECTOR         | Deutsche Telekom AG
    #2   | AS1299   | 230        | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #3   | AS6939   | 229        | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #4   | AS8220   | 212        | ACTIVE LOCAL ROV               | COLT
    #5   | AS3356   | 193        | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #6   | AS174    | 184        | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #7   | AS8881   | 160        | REGRESSED                      | 1&1 Versatel GmbH
    #8   | AS33891  | 156        | ACTIVE LOCAL ROV               | Core-Backbone GmbH
    #9   | AS5405   | 112        | ACTIVE LOCAL ROV               | Inter.link GmbH
    #10  | AS13237  | 96         | REGRESSED                      | euNetworks GmbH
    #11  | AS3209   | 93         | REGRESSED                      | Vodafone GmbH
    #12  | AS34927  | 83         | PARTIAL: VULNERABLE (Mixed)    | iFog GmbH
    #13  | AS2914   | 76         | CORE: ACTIVE PROTECTOR         | NTT America, Inc.
    #14  | AS3257   | 71         | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #15  | AS8767   | 60         | ACTIVE LOCAL ROV               | M-net Telekommunikations GmbH
    #16  | AS20473  | 59         | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #17  | AS50629  | 57         | ACTIVE LOCAL ROV               | LWLcom GmbH
    #18  | AS9002   | 50         | ACTIVE LOCAL ROV               | RETN Limited
    #19  | AS24961  | 47         | PASSIVE (Clean Pipe)           | WIIT AG (fka. myLoc Managed IT AG)
    #20  | AS34309  | 43         | PASSIVE (Clean Pipe)           | Link11 GmbH

    ====================================================================================================
     IPv6 DIFFERENCES (DE networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS24637  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | WEBDISCOUNT GmbH & Co. KG
    AS203329 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NTT Global Data Centers EMEA GmbH
    AS61407  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | NewTelco GmbH
    AS61157  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | PlusServer GmbH
    AS12731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | IPHH Internet Port Hamburg GmbH
    AS205112 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PHILUNET GmbH
    AS48200  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Opteamax GmbH
    AS16205  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | DSI GmbH Daten Service Informationssyste
    AS8319   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NETHINKS GmbH
    AS31103  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Keyweb AG
    AS203724 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Musarubra Germany GmbH
    AS44700  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Haendle & Korte GmbH
    AS8879   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | DTS Systeme GmbH
    AS48173  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Orange Business Digital Germany GmbH
    AS25081  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Heidelberg IT Management GmbH & Co.KG
    AS13058  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | serve-u - Buchholz und Sünderhauf GbR
    AS59570  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Jens Zimperfeld
    AS12817  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | GeFoekoM e.V.
    AS15580  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Allianz Technology SE
    AS48646  | Unverified (Transit/Peer?)     | PASSIVE (Clean Pipe)           | 0/1            | SDRmedia Verwaltungs GmbH
    AS39083  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | David Froehlich
    AS39614  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Dawico Deutschland GmbH
    AS197148 | PROVIDER UNKNOWN (In BGP)      | STUB: VULNERABLE               | 1/1            | Pepe Rosam
    AS201222 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Frieder Mueller
    AS199163 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | DATAGROUP Operations GmbH
    AS199118 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Heinlein Support GmbH
    AS198818 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | ISP Service eG
    AS198333 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | DATAGROUP SE
    AS200081 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Netversor GmbH
    AS199753 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | UD Media GmbH
