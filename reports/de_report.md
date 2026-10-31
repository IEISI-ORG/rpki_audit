    [*] Loading Global Audit for DE...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: DE (Germany)
    ====================================================================================================
    Total Networks:      3,285
    Total Cone Gravity:  190,704
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   932 (28.4%) -> Protects 80.6% of Traffic
    VULNERABLE NETWORKS:      1592 (48.5%) -> Exposes  0.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1,778 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   633 (35.6%)   IPv6 verdict   720 (40.5%)
      VULNERABLE main verdict  1060 (59.6%)   IPv6 verdict   989 (55.6%)

    ====================================================================================================
     THE DE CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS3320   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 71190    | 96%    | Deutsche Telekom AG
    AS33891  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 46645    | -      | Core-Backbone GmbH
    AS34549  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 34261    | -      | meerfarbig GmbH & Co. KG
    AS29632  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 29955    | -      | Netassist International EOOD
    AS5405   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3559     | -      | Inter.link GmbH
    AS50629  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1215     | 93%    | LWLcom GmbH
    AS212895 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 579      | -      | Johannes Ernst
    AS13237  | REGRESSED                      | REGRESSED                      | 302      | 0%     | euNetworks GmbH
    AS8881   | REGRESSED                      | REGRESSED                      | 213      | 0%     | 1&1 Versatel GmbH
    AS24961  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 179      | 2%     | WIIT AG (fka. myLoc Managed IT AG)
    AS199854 | VULNERABLE                     | VULNERABLE                     | 152      | -      | Jens Thies
    AS49581  | REGRESSED                      | REGRESSED                      | 146      | 2%     | Ferdinand Zink trading as Tube-Hosting
    AS44066  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 141      | -      | firstcolo GmbH
    AS3209   | REGRESSED                      | REGRESSED                      | 124      | 0%     | Vodafone GmbH
    AS35708  | Unverified (Transit/Peer?)     | -                              | 90       | -      | 4b42 UG
    AS57821  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 88       | -      | Nonattached Network e.V.
    AS58212  | REGRESSED                      | REGRESSED                      | 77       | 0%     | dataforest GmbH
    AS8767   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 71       | 94%    | M-net Telekommunikations GmbH
    AS30823  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 68       | -      | aurologic GmbH
    AS9145   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 54       | 95%    | EWE TEL GmbH

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to DE?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS3320   | 504        | CORE: ACTIVE PROTECTOR         | Deutsche Telekom AG
    #2   | AS6939   | 229        | ACTIVE LOCAL ROV               | Hurricane Electric LLC
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
    #13  | AS2914   | 75         | INCONSISTENT                   | NTT America, Inc.
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
    AS51396  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 4/5            | Pfcloud UG (haftungsbeschrankt)
    AS61407  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | NewTelco GmbH
    AS61157  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | PlusServer GmbH
    AS12731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | IPHH Internet Port Hamburg GmbH
    AS205112 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PHILUNET GmbH
    AS8319   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NETHINKS GmbH
    AS31103  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Keyweb AG
    AS44700  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Haendle & Korte GmbH
    AS8879   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | DTS Systeme GmbH
    AS203724 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Musarubra Germany GmbH
    AS15580  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Allianz Technology SE
    AS48646  | Unverified (Transit/Peer?)     | PASSIVE (Clean Pipe)           | 0/1            | SDRmedia Verwaltungs GmbH
    AS212341 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Stephan Rakowski, trading as CSN-Solutio
    AS59570  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Jens Zimperfeld
    AS39614  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Dawico Deutschland GmbH
    AS15372  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | IBH connect GmbH
    AS12817  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | GeFoekoM e.V.
    AS39083  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | David Froehlich
    AS13058  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | serve-u - Buchholz und Sünderhauf GbR
    AS199163 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | DATAGROUP Operations GmbH
    AS208444 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Bringe Informationstechnik GmbH
    AS208025 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | RSG Group GmbH
    AS207999 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | regiocom SE
    AS200599 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | eins energie in sachsen GmbH & Co. KG
    AS208058 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | InnoGames GmbH
    AS200081 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Netversor GmbH
    AS209216 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Trusted-Service.net GmbH trading as Trus
    AS209185 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Tim Niemeyer
    AS197148 | PROVIDER UNKNOWN (In BGP)      | STUB: VULNERABLE               | 1/1            | Pepe Rosam
    AS198818 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | ISP Service eG
