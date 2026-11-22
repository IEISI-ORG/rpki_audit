    [*] Loading Global Audit for FR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: FR (France)
    ====================================================================================================
    Total Networks:      1,885
    Total Cone Gravity:  190,869
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   753 (39.9%) -> Protects 92.8% of Traffic
    VULNERABLE NETWORKS:       707 (37.5%) -> Exposes  0.4% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        791 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   395 (49.9%)   IPv6 verdict   427 (54.0%)
      VULNERABLE main verdict   365 (46.1%)   IPv6 verdict   340 (43.0%)

    ====================================================================================================
     THE FR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS5511   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 71205    | 93%    | Orange S.A.
    AS35280  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 52327    | -      | F5 Networks SARL
    AS34019  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 37041    | -      | Hivane Association
    AS212024 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 12766    | -      | Marc Schmitt
    AS8218   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 8974     | -      | Zayo Europe
    AS204092 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 4043     | -      | Association GRIFON
    AS50628  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 2309     | -      | Leonix Telecom SAS
    AS16276  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 580      | 0%     | OVH SAS
    AS35661  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 259      | 0%     | VIRTUA SYSTEMS SAS
    AS29075  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 218      | 91%    | IELO-LIAZO SERVICES SAS
    AS30781  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 165      | 97%    | Free Pro SAS
    AS3215   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 150      | 81%    | Orange S.A.
    AS15557  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 95       | 98%    | SFR SA
    AS35625  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 70       | 1%     | Eurofiber France SAS
    AS62000  | VOLATILE                       | VOLATILE                       | 59       | -      | SERVERD SAS
    AS20766  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 55       | -      | Association "Gitoyen"
    AS2200   | REGRESSED                      | REGRESSED                      | 39       | 2%     | Renater
    AS29169  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 37       | -      | GANDI SAS
    AS39801  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 24       | -      | France-IX L3 Services
    AS16347  | REGRESSED                      | REGRESSED                      | 23       | 0%     | ADISTA SAS

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to FR?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS174    | 317        | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
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
    #12  | AS6461   | 70         | CORE: UNPROTECTED              | Zayo Bandwidth
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
    AS202753 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | GLOBALGRID SASU
    AS211448 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | WEBCONEX SAS
    AS8304   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Ecritel SASU
    AS47600  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | RUBIX DATACENTER SAS
    AS203500 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | ABEILLE SARL
    AS205010 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | LaNetCie SAS
    AS35665  | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Netensia SARL
    AS199248 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NUMLOG S.A.S.
    AS212424 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Association des Reseaux de CentraleSupel
    AS209823 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Enki Multimedia EURL
    AS199997 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Ippon Hosting SARL
    AS209928 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ANGELINKS SAS
    AS202089 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Unimedia Services SAS
    AS201188 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | BJT Partners SAS
    AS198985 | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/2            | AQUILENET
    AS198060 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Darva (Developpement D'applications Sur 
    AS210232 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PACTOO SAS
    AS206310 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Waxx SAS
    AS205992 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HERMES INTERNATIONAL SCA
    AS206568 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ALTSYSNET.COM SAS
    AS205816 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Elkaim Elie
    AS205919 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | ON-X GROUPE SA
    AS208458 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/4            | REGION NOUVELLE-AQUITAINE
    AS204515 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Association Crans
    AS204273 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | SPIE ICS
    AS394485 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SOLUTECH.NET
    AS218715 | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/2            | Cedric LECOCQ
    AS213184 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Telyo SAS
