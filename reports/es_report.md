    [*] Loading Global Audit for ES...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ES (Spain)
    ====================================================================================================
    Total Networks:      1,169
    Total Cone Gravity:  72,851
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   251 (21.5%) -> Protects 98.8% of Traffic
    VULNERABLE NETWORKS:       692 (59.2%) -> Exposes  1.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        284 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    65 (22.9%)   IPv6 verdict    83 (29.2%)
      VULNERABLE main verdict   205 (72.2%)   IPv6 verdict   192 (67.6%)

    ====================================================================================================
     THE ES CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS12956  | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 71429    | -      | Telxius (Telefonica Global)
    AS29119  | REGRESSED                      | REGRESSED                      | 338      | 0%     | AIRE NETWORKS DEL MEDITERRANEO SL UNIPER
    AS60171  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 212      | 97%    | AFR-IX TELECOM S.A.
    AS12357  | REGRESSED                      | REGRESSED                      | 98       | 0%     | VODAFONE ESPANA S.A.U.
    AS12479  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 80       | 99%    | Orange Espagne SA
    AS8903   | REGRESSED                      | REGRESSED                      | 77       | 0%     | LYNTIA NETWORKS S.A.
    AS3352   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 76       | 99%    | TELEFONICA DE ESPANA S.A.U.
    AS12541  | VULNERABLE                     | Unverified (Transit/Peer?)     | 66       | -      | LYNTIA NETWORKS S.A.
    AS35699  | REGRESSED                      | REGRESSED                      | 52       | 0%     | Adamo Telecom Iberia S.A.
    AS49600  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 35       | -      | NEAR IP, S.L.
    AS34696  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 33       | 0%     | MISMELINK NETWORKS, SL
    AS3262   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 30       | 97%    | SAREnet, S.A.
    AS15704  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 26       | 99%    | XTRA TELECOM S.A.
    AS766    | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 23       | 15%    | Entidad Publica Empresarial Red.es
    AS8637   | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 21       | -      | SpainWISP, S.L.
    AS13287  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 20       | -      | FALBOX S.L. trading as NIXVAL
    AS34471  | REGRESSED                      | REGRESSED                      | 16       | 0%     | Free Technologies Excom S.L.
    AS49353  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 15       | -      | Valor Information Technologies, S.L.
    AS201942 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 12       | -      | Soltia Consulting SL
    AS210321 | REGRESSED                      | REGRESSED                      | 11       | 5%     | Operadors Quilometre Zero S.L.

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to ES?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS29119  | 187        | REGRESSED                      | AIRE NETWORKS DEL MEDITERRANEO SL UNIPER
    #2   | AS174    | 153        | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #3   | AS12357  | 90         | REGRESSED                      | VODAFONE ESPANA S.A.U.
    #4   | AS3352   | 87         | ACTIVE LOCAL ROV               | TELEFONICA DE ESPANA S.A.U.
    #5   | AS8220   | 80         | ACTIVE LOCAL ROV               | COLT
    #6   | AS12479  | 79         | ACTIVE LOCAL ROV               | Orange Espagne SA
    #7   | AS8903   | 64         | REGRESSED                      | LYNTIA NETWORKS S.A.
    #8   | AS12541  | 53         | VULNERABLE                     | LYNTIA NETWORKS S.A.
    #9   | AS35699  | 49         | REGRESSED                      | Adamo Telecom Iberia S.A.
    #10  | AS3356   | 43         | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #11  | AS3257   | 40         | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #12  | AS6939   | 34         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #13  | AS1299   | 31         | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #14  | AS49600  | 31         | PASSIVE (Clean Pipe)           | NEAR IP, S.L.
    #15  | AS15704  | 30         | ACTIVE LOCAL ROV               | XTRA TELECOM S.A.
    #16  | AS3262   | 30         | ACTIVE LOCAL ROV               | SAREnet, S.A.
    #17  | AS8637   | 21         | PASSIVE (Clean Pipe)           | SpainWISP, S.L.
    #18  | AS766    | 19         | PASSIVE (Clean Pipe)           | Entidad Publica Empresarial Red.es
    #19  | AS6453   | 18         | CORE: ACTIVE PROTECTOR         | TATA Communications (America) Inc
    #20  | AS12956  | 18         | CORE: ACTIVE PROTECTOR         | Telxius (Telefonica Global)

    ====================================================================================================
     IPv6 DIFFERENCES (ES networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS12541  | VULNERABLE                     | Unverified (Transit/Peer?)     | 0/0            | LYNTIA NETWORKS S.A.
    AS13287  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | FALBOX S.L. trading as NIXVAL
    AS49353  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Valor Information Technologies, S.L.
    AS201942 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Soltia Consulting SL
    AS59432  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | GINERNET S.L.
    AS43160  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | TEMPLUS SPAIN SL
    AS49835  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | Fundacio Privada per a la Xarxa Lliure, 
    AS200165 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Asac Comunicaciones S.L.
    AS199581 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Data Rush IT Services, S.L.
    AS209478 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Leyre Rivera Martin
    AS197518 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Rackmarkt SL
    AS197927 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | THEIPBOX, SL
    AS206702 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | 7P SERVICIOS INTEGRADOS SLU
    AS207714 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Fundacion Tecnalia Research and Innovati
    AS202207 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/4            | ASPA CLOUD SL
    AS212059 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TESTIGOS CRISTIANOS DE JEHOVA
    AS212190 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PISTA CERO, S.L.
    AS214043 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Christian Barba trading as Cloudfira
    AS30937  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Walhalla Data Center Services SL
    AS60551  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | D.P.S. Giro-consulting S.L.
    AS48348  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Cloud Builders SA
    AS48846  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Inetum Espana, S.A.
