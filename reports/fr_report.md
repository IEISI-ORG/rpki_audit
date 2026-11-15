    [*] Loading Global Audit for FR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: FR (France)
    ====================================================================================================
    Total Networks:      1,882
    Total Cone Gravity:  171,830
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   564 (30.0%) -> Protects 91.4% of Traffic
    VULNERABLE NETWORKS:       877 (46.6%) -> Exposes  0.1% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        794 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   319 (40.2%)   IPv6 verdict   362 (45.6%)
      VULNERABLE main verdict   425 (53.5%)   IPv6 verdict   393 (49.5%)

    ====================================================================================================
     THE FR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS5511   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 71044    | 100%   | Orange S.A.
    AS34019  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 38150    | -      | Hivane Association
    AS35280  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 32814    | -      | F5 Networks SARL
    AS212024 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 13520    | -      | Marc Schmitt
    AS8218   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 8224     | -      | Zayo Europe
    AS204092 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 4135     | -      | Association GRIFON
    AS50628  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1744     | -      | Leonix Telecom SAS
    AS16276  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 574      | 1%     | OVH SAS
    AS35661  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 272      | 0%     | VIRTUA SYSTEMS SAS
    AS29075  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 220      | 99%    | IELO-LIAZO SERVICES SAS
    AS30781  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 167      | 92%    | Free Pro SAS
    AS3215   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 144      | 99%    | Orange S.A.
    AS15557  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 94       | 98%    | SFR SA
    AS35625  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 72       | 0%     | Eurofiber France SAS
    AS62000  | VOLATILE                       | VOLATILE                       | 52       | -      | SERVERD SAS
    AS20766  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 48       | -      | Association "Gitoyen"
    AS29169  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 41       | -      | GANDI SAS
    AS2200   | REGRESSED                      | REGRESSED                      | 40       | 1%     | Renater
    AS16347  | REGRESSED                      | REGRESSED                      | 23       | 0%     | ADISTA SAS
    AS8309   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 21       | -      | SIPARTECH SAS

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to FR?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS174    | 317        | INCONSISTENT                   | Cogent Communications, LLC
    #2   | AS30781  | 137        | ACTIVE LOCAL ROV               | Free Pro SAS
    #3   | AS3215   | 124        | ACTIVE LOCAL ROV               | Orange S.A.
    #4   | AS3356   | 116        | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #5   | AS8218   | 114        | ACTIVE LOCAL ROV               | Zayo Europe
    #6   | AS8220   | 96         | ACTIVE LOCAL ROV               | COLT
    #7   | AS29075  | 92         | ACTIVE LOCAL ROV               | IELO-LIAZO SERVICES SAS
    #8   | AS1299   | 87         | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #9   | AS6939   | 76         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #10  | AS5511   | 74         | CORE: ACTIVE PROTECTOR         | Orange S.A.
    #11  | AS15557  | 74         | ACTIVE LOCAL ROV               | SFR SA
    #12  | AS6461   | 70         | REGRESSED                      | Zayo Bandwidth
    #13  | AS3257   | 66         | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #14  | AS35625  | 57         | PASSIVE (Clean Pipe)           | Eurofiber France SAS
    #15  | AS39801  | 52         | PASSIVE (Clean Pipe)           | France-IX L3 Services
    #16  | AS6762   | 40         | CORE: ACTIVE PROTECTOR         | Telecom Italia Sparkle (Seabone)
    #17  | AS2914   | 29         | CORE: ACTIVE PROTECTOR         | NTT America, Inc.
    #18  | AS20473  | 25         | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #19  | AS39180  | 24         | PARTIAL: VULNERABLE (Mixed)    | LASOTEL SAS
    #20  | AS62000  | 23         | VOLATILE                       | SERVERD SAS

    ====================================================================================================
     IPv6 DIFFERENCES (FR networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS212024 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Marc Schmitt
    AS39180  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | LASOTEL SAS
    AS59877  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | VA TELECOM SAS
    AS202753 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | GLOBALGRID SASU
    AS211448 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | WEBCONEX SAS
    AS60456  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Revtelecom Group SAS
    AS21409  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Ikoula Net SAS
    AS47600  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/2            | RUBIX DATACENTER SAS
    AS199248 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NUMLOG S.A.S.
    AS31564  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Hexaglobe SAS
    AS25358  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Novso SARL
    AS35665  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Netensia SARL
    AS212424 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Association des Reseaux de CentraleSupel
    AS219331 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | Thomas BOUZIN
    AS57902  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Metro Optic SAS
    AS57119  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NAITWAYS SAS
    AS29322  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | STREAMWIDE SA
    AS34197  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Three Fourteen SASU
    AS39509  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NGANALYTICS SAS
    AS41935  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Dassault Systemes SE
    AS44994  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | IPEVA SARL
    AS47314  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | VINCI SA
    AS49463  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | BASSAC SA
    AS51306  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Tellam Holding, SARL
    AS57103  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Nomotech SAS
    AS59721  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SAFECLOUDBOX SAS
    AS61026  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HASGARD s.a.r.l.
    AS61205  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Infomil S.A.S.
    AS197883 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Serinya Telecom SAS
    AS198060 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Darva (Developpement D'applications Sur 
