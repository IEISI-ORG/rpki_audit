    [*] Loading Global Audit for DE...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: DE (Germany)
    ====================================================================================================
    Total Networks:      3,274
    Total Cone Gravity:  193,512
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   955 (29.2%) -> Protects 65.6% of Traffic
    VULNERABLE NETWORKS:      1558 (47.6%) -> Exposes  0.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1,763 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   658 (37.3%)   IPv6 verdict   751 (42.6%)
      VULNERABLE main verdict  1024 (58.1%)   IPv6 verdict   952 (54.0%)

    ====================================================================================================
     THE DE CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS3320   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 70940    | 97%    | Deutsche Telekom AG
    AS33891  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 47131    | -      | Core-Backbone GmbH
    AS34549  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 35181    | -      | meerfarbig GmbH & Co. KG
    AS29632  | Unverified (Transit/Peer?)     | PASSIVE (Clean Pipe)           | 28862    | -      | Netassist International EOOD
    AS5405   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3406     | -      | Inter.link GmbH
    AS24961  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 2524     | 1%     | WIIT AG (fka. myLoc Managed IT AG)
    AS50629  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1833     | 96%    | LWLcom GmbH
    AS212895 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 511      | -      | Johannes Ernst
    AS13237  | REGRESSED                      | REGRESSED                      | 287      | 0%     | euNetworks GmbH
    AS8881   | REGRESSED                      | REGRESSED                      | 213      | 0%     | 1&1 Versatel GmbH
    AS199854 | VULNERABLE                     | VULNERABLE                     | 163      | -      | Jens Thies
    AS49581  | REGRESSED                      | REGRESSED                      | 141      | 1%     | Ferdinand Zink trading as Tube-Hosting
    AS44066  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 128      | -      | firstcolo GmbH
    AS3209   | REGRESSED                      | REGRESSED                      | 127      | 0%     | Vodafone GmbH
    AS57821  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 89       | -      | Nonattached Network e.V.
    AS35708  | Unverified (Transit/Peer?)     | -                              | 82       | -      | 4b42 UG
    AS8767   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 70       | 97%    | M-net Telekommunikations GmbH
    AS58212  | REGRESSED                      | REGRESSED                      | 70       | 0%     | dataforest GmbH
    AS34309  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 69       | -      | Link11 GmbH
    AS30823  | REGRESSED                      | REGRESSED                      | 68       | -      | aurologic GmbH

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to DE?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS3320   | 504        | CORE: ACTIVE PROTECTOR         | Deutsche Telekom AG
    #2   | AS6939   | 229        | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #3   | AS1299   | 229        | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #4   | AS8220   | 212        | ACTIVE LOCAL ROV               | COLT
    #5   | AS3356   | 193        | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #6   | AS174    | 184        | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #7   | AS8881   | 160        | REGRESSED                      | 1&1 Versatel GmbH
    #8   | AS33891  | 156        | ACTIVE LOCAL ROV               | Core-Backbone GmbH
    #9   | AS5405   | 112        | ACTIVE LOCAL ROV               | Inter.link GmbH
    #10  | AS13237  | 96         | REGRESSED                      | euNetworks GmbH
    #11  | AS3209   | 93         | REGRESSED                      | Vodafone GmbH
    #12  | AS34927  | 83         | PARTIAL: VULNERABLE (Mixed)    | iFog GmbH
    #13  | AS2914   | 75         | CORE: ACTIVE PROTECTOR         | NTT America, Inc.
    #14  | AS3257   | 71         | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #15  | AS8767   | 60         | ACTIVE LOCAL ROV               | M-net Telekommunikations GmbH
    #16  | AS20473  | 59         | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #17  | AS50629  | 57         | ACTIVE LOCAL ROV               | LWLcom GmbH
    #18  | AS9002   | 50         | ACTIVE (Atlas Verified)        | RETN Limited
    #19  | AS24961  | 47         | PASSIVE (Clean Pipe)           | WIIT AG (fka. myLoc Managed IT AG)
    #20  | AS34309  | 43         | PARTIAL: VULNERABLE (Mixed)    | Link11 GmbH

    ====================================================================================================
     IPv6 DIFFERENCES (DE networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS29632  | Unverified (Transit/Peer?)     | PASSIVE (Clean Pipe)           | 0/1            | Netassist International EOOD
    AS24637  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | WEBDISCOUNT GmbH & Co. KG
    AS51396  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 5/6            | Pfcloud UG (haftungsbeschrankt)
    AS203329 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NTT Global Data Centers EMEA GmbH
    AS61407  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | NewTelco GmbH
    AS61157  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | PlusServer GmbH
    AS12731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | IPHH Internet Port Hamburg GmbH
    AS205112 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PHILUNET GmbH
    AS48200  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Opteamax GmbH
    AS16205  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | DSI GmbH Daten Service Informationssyste
    AS8319   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NETHINKS GmbH
    AS203724 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Musarubra Germany GmbH
    AS31103  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Keyweb AG
    AS44700  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Haendle & Korte GmbH
    AS25081  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Heidelberg IT Management GmbH & Co.KG
    AS20677  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | imos Gesellschaft fuer Internet-Marketin
    AS8879   | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | DTS Systeme GmbH
    AS59570  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Jens Zimperfeld
    AS12817  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | GeFoekoM e.V.
    AS48646  | Unverified (Transit/Peer?)     | PASSIVE (Clean Pipe)           | 0/1            | SDRmedia Verwaltungs GmbH
    AS15372  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | IBH connect GmbH
    AS13058  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | serve-u - Buchholz und Sünderhauf GbR
    AS15580  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Allianz Technology SE
    AS212341 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Stephan Rakowski, trading as CSN-Solutio
    AS39083  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | David Froehlich
    AS39614  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Dawico Deutschland GmbH
    AS201222 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Frieder Mueller
    AS197148 | PROVIDER UNKNOWN (In BGP)      | STUB: VULNERABLE               | 1/1            | Pepe Rosam
    AS199753 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | UD Media GmbH
    AS199118 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Heinlein Support GmbH
