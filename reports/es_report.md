    [*] Loading Global Audit for ES...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ES (Spain)
    ====================================================================================================
    Total Networks:      1,172
    Total Cone Gravity:  72,321
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   243 (20.7%) -> Protects 98.7% of Traffic
    VULNERABLE NETWORKS:       695 (59.3%) -> Exposes  1.1% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        281 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    62 (22.1%)   IPv6 verdict    84 (29.9%)
      VULNERABLE main verdict   202 (71.9%)   IPv6 verdict   189 (67.3%)

    ====================================================================================================
     THE ES CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS12956  | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 70905    | -      | Telxius (Telefonica Global)
    AS29119  | REGRESSED                      | REGRESSED                      | 332      | 0%     | AIRE NETWORKS DEL MEDITERRANEO SL UNIPER
    AS60171  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 211      | 100%   | AFR-IX TELECOM S.A.
    AS12357  | REGRESSED                      | REGRESSED                      | 96       | 0%     | VODAFONE ESPANA S.A.U.
    AS12479  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 81       | 99%    | Orange Espagne SA
    AS3352   | ACTIVE (Atlas Verified)        | ACTIVE (Atlas Verified)        | 77       | 99%    | TELEFONICA DE ESPANA S.A.U.
    AS8903   | REGRESSED                      | REGRESSED                      | 76       | 0%     | LYNTIA NETWORKS S.A.
    AS12541  | VULNERABLE                     | Unverified (Transit/Peer?)     | 66       | -      | LYNTIA NETWORKS S.A.
    AS35699  | REGRESSED                      | REGRESSED                      | 55       | 0%     | Adamo Telecom Iberia S.A.
    AS49600  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 33       | -      | NEAR IP, S.L.
    AS3262   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 31       | 83%    | SAREnet, S.A.
    AS15704  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 27       | 99%    | XTRA TELECOM S.A.
    AS766    | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 23       | 5%     | Entidad Publica Empresarial Red.es
    AS34696  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 23       | -      | MISMELINK NETWORKS, SL
    AS8637   | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 22       | -      | SpainWISP, S.L.
    AS13287  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 17       | -      | FALBOX S.L. trading as NIXVAL
    AS34471  | REGRESSED                      | REGRESSED                      | 17       | 0%     | Free Technologies Excom S.L.
    AS49353  | VULNERABLE                     | VULNERABLE                     | 15       | -      | Valor Information Technologies, S.L.
    AS201942 | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 12       | -      | Soltia Consulting SL
    AS210321 | REGRESSED                      | REGRESSED                      | 11       | 0%     | Operadors Quilometre Zero S.L.

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to ES?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS29119  | 187        | REGRESSED                      | AIRE NETWORKS DEL MEDITERRANEO SL UNIPER
    #2   | AS174    | 153        | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #3   | AS12357  | 90         | REGRESSED                      | VODAFONE ESPANA S.A.U.
    #4   | AS3352   | 87         | ACTIVE (Atlas Verified)        | TELEFONICA DE ESPANA S.A.U.
    #5   | AS8220   | 80         | ACTIVE LOCAL ROV               | COLT
    #6   | AS12479  | 79         | ACTIVE LOCAL ROV               | Orange Espagne SA
    #7   | AS8903   | 64         | REGRESSED                      | LYNTIA NETWORKS S.A.
    #8   | AS12541  | 53         | VULNERABLE                     | LYNTIA NETWORKS S.A.
    #9   | AS35699  | 51         | REGRESSED                      | Adamo Telecom Iberia S.A.
    #10  | AS3356   | 43         | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #11  | AS3257   | 40         | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #12  | AS6939   | 34         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #13  | AS1299   | 31         | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #14  | AS49600  | 31         | VULNERABLE (Atlas Verified)    | NEAR IP, S.L.
    #15  | AS15704  | 30         | ACTIVE LOCAL ROV               | XTRA TELECOM S.A.
    #16  | AS3262   | 30         | ACTIVE LOCAL ROV               | SAREnet, S.A.
    #17  | AS8637   | 21         | PASSIVE (Clean Pipe)           | SpainWISP, S.L.
    #18  | AS766    | 19         | VULNERABLE (Atlas Verified)    | Entidad Publica Empresarial Red.es
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
    AS13287  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | FALBOX S.L. trading as NIXVAL
    AS201942 | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | Soltia Consulting SL
    AS43833  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | OPEN CABLE TELECOMUNICACIONES, S.L.
    AS59432  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | GINERNET S.L.
    AS202766 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | LYNTIA NETWORKS S.A.
    AS215691 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | AP INTERACTIVE SOLUTIONS SL
    AS49835  | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 2/2            | Fundacio Privada per a la Xarxa Lliure, 
    AS43160  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | TEMPLUS SPAIN SL
    AS210123 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | NUBBITEL TELECOM,S.L.
    AS12540  | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | IdecNet S.A.
    AS197518 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Rackmarkt SL
    AS200165 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Asac Comunicaciones S.L.
    AS199581 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Data Rush IT Services, S.L.
    AS206702 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | 7P SERVICIOS INTEGRADOS SLU
    AS206886 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CYBERMAN INFORMATICA Y COMUNICACIONES, S
    AS207714 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Fundacion Tecnalia Research and Innovati
    AS202207 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | ASPA CLOUD SL
    AS214043 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Christian Barba trading as Cloudfira
    AS215424 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | ASOCIACION ESPANIX
    AS209478 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Leyre Rivera Martin
    AS212059 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TESTIGOS CRISTIANOS DE JEHOVA
    AS212190 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PISTA CERO, S.L.
    AS30937  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Walhalla Data Center Services SL
    AS60551  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | D.P.S. Giro-consulting S.L.
    AS48348  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Cloud Builders SA
    AS48846  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Inetum Espana, S.A.
