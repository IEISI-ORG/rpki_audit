    [*] Loading Global Audit for DE...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: DE (Germany)
    ====================================================================================================
    Total Networks:      3,285
    Total Cone Gravity:  189,467
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   901 (27.4%) -> Protects 98.4% of Traffic
    VULNERABLE NETWORKS:      1644 (50.0%) -> Exposes  0.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1,796 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   623 (34.7%)   IPv6 verdict   702 (39.1%)
      VULNERABLE main verdict  1091 (60.7%)   IPv6 verdict  1024 (57.0%)

    ====================================================================================================
     THE DE CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS3320   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 70941    | 94%    | Deutsche Telekom AG
    AS33891  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 46803    | -      | Core-Backbone GmbH
    AS34549  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 35236    | -      | meerfarbig GmbH & Co. KG
    AS29632  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 28352    | -      | Netassist International EOOD
    AS5405   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 2837     | -      | Inter.link GmbH
    AS50629  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1434     | 94%    | LWLcom GmbH
    AS212895 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 566      | -      | Johannes Ernst
    AS13237  | REGRESSED                      | REGRESSED                      | 302      | 0%     | euNetworks GmbH
    AS8881   | REGRESSED                      | REGRESSED                      | 211      | 0%     | 1&1 Versatel GmbH
    AS199854 | VULNERABLE                     | VULNERABLE                     | 168      | -      | Jens Thies
    AS24961  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 165      | 2%     | WIIT AG (fka. myLoc Managed IT AG)
    AS49581  | REGRESSED                      | REGRESSED                      | 162      | 3%     | Ferdinand Zink trading as Tube-Hosting
    AS44066  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 130      | -      | firstcolo GmbH
    AS3209   | REGRESSED                      | REGRESSED                      | 111      | 0%     | Vodafone GmbH
    AS35708  | Unverified (Transit/Peer?)     | -                              | 93       | -      | 4b42 UG
    AS57821  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 92       | -      | Nonattached Network e.V.
    AS58212  | REGRESSED                      | REGRESSED                      | 77       | 0%     | dataforest GmbH
    AS30823  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 74       | 22%    | aurologic GmbH
    AS8767   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 70       | 94%    | M-net Telekommunikations GmbH
    AS9145   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 54       | 92%    | EWE TEL GmbH

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
    #6   | AS174    | 183        | INCONSISTENT                   | Cogent Communications, LLC
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
    #19  | AS24961  | 47         | PARTIAL: VULNERABLE (Mixed)    | WIIT AG (fka. myLoc Managed IT AG)
    #20  | AS34309  | 43         | PARTIAL: VULNERABLE (Mixed)    | Link11 GmbH

    ====================================================================================================
     IPv6 DIFFERENCES (DE networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS216078 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 5/6            | Liam Kremer
    AS203329 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NTT Global Data Centers EMEA GmbH
    AS43623  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | Hessischer Rundfunk
    AS61157  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | PlusServer GmbH
    AS12731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | IPHH Internet Port Hamburg GmbH
    AS48200  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | Opteamax GmbH
    AS205112 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PHILUNET GmbH
    AS8319   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NETHINKS GmbH
    AS31103  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Keyweb AG
    AS8879   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | DTS Systeme GmbH
    AS209824 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Georg Kroeber
    AS44700  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Haendle & Korte GmbH
    AS61218  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | 4b42 UG
    AS203724 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Musarubra Germany GmbH
    AS25081  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Heidelberg IT Management GmbH & Co.KG
    AS212341 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Stephan Rakowski, trading as CSN-Solutio
    AS213527 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Lorenz Knak trading as IT-adjutor GmbH
    AS39083  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | David Froehlich
    AS39614  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Dawico Deutschland GmbH
    AS15580  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Allianz Technology SE
    AS59570  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Jens Zimperfeld
    AS13058  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | serve-u - Buchholz und Sünderhauf GbR
    AS12817  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | GeFoekoM e.V.
    AS48646  | Unverified (Transit/Peer?)     | PASSIVE (Clean Pipe)           | 0/1            | SDRmedia Verwaltungs GmbH
    AS12460  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | mandala IT GmbH
    AS12655  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Sellwerk Verwaltungs GmbH
    AS12748  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | IAV GmbH Ingenieurgesellschaft Auto und 
    AS16218  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Ingo Assion trading as "IACD Systemhaus 
    AS20830  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | The Cloud Networks Germany GmbH
    AS21083  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Proact Deutschland GmbH
