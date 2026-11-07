    [*] Loading Global Audit for FR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: FR (France)
    ====================================================================================================
    Total Networks:      1,879
    Total Cone Gravity:  173,519
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   687 (36.6%) -> Protects 83.6% of Traffic
    VULNERABLE NETWORKS:       757 (40.3%) -> Exposes  7.6% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        784 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   354 (45.2%)   IPv6 verdict   389 (49.6%)
      VULNERABLE main verdict   390 (49.7%)   IPv6 verdict   363 (46.3%)

    ====================================================================================================
     THE FR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS5511   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 71132    | 91%    | Orange S.A.
    AS35280  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 32285    | -      | F5 Networks SARL
    AS34019  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 27347    | -      | Hivane Association
    AS212024 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 13228    | -      | Marc Schmitt
    AS20766  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 12335    | -      | Association "Gitoyen"
    AS8218   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 6576     | 94%    | Zayo Europe
    AS204092 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 4043     | -      | Association GRIFON
    AS29075  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 2821     | 99%    | IELO-LIAZO SERVICES SAS
    AS50628  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 1776     | -      | Leonix Telecom SAS
    AS16276  | REGRESSED                      | REGRESSED                      | 574      | 2%     | OVH SAS
    AS35661  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 275      | 0%     | VIRTUA SYSTEMS SAS
    AS30781  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 166      | 100%   | Free Pro SAS
    AS3215   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 145      | 99%    | Orange S.A.
    AS15557  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 94       | 98%    | SFR SA
    AS29169  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 89       | -      | GANDI SAS
    AS35625  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 67       | 2%     | Eurofiber France SAS
    AS62000  | INCONSISTENT                   | INCONSISTENT                   | 48       | 26%    | SERVERD SAS
    AS2200   | REGRESSED                      | REGRESSED                      | 39       | 3%     | Renater
    AS16347  | REGRESSED                      | REGRESSED                      | 24       | 0%     | ADISTA SAS
    AS39801  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 23       | -      | France-IX L3 Services

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
    #8   | AS1299   | 87         | INCONSISTENT                   | Arelion (fka. Telia Carrier)
    #9   | AS6939   | 76         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #10  | AS5511   | 74         | CORE: ACTIVE PROTECTOR         | Orange S.A.
    #11  | AS15557  | 74         | ACTIVE LOCAL ROV               | SFR SA
    #12  | AS6461   | 70         | REGRESSED                      | Zayo Bandwidth
    #13  | AS3257   | 66         | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #14  | AS35625  | 57         | PASSIVE (Clean Pipe)           | Eurofiber France SAS
    #15  | AS39801  | 52         | PASSIVE (Clean Pipe)           | France-IX L3 Services
    #16  | AS6762   | 40         | CORE: ACTIVE PROTECTOR         | Telecom Italia Sparkle (Seabone)
    #17  | AS2914   | 29         | INCONSISTENT                   | NTT America, Inc.
    #18  | AS20473  | 25         | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #19  | AS39180  | 24         | PARTIAL: VULNERABLE (Mixed)    | LASOTEL SAS
    #20  | AS62000  | 23         | INCONSISTENT                   | SERVERD SAS

    ====================================================================================================
     IPv6 DIFFERENCES (FR networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS212024 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Marc Schmitt
    AS202753 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | GLOBALGRID SASU
    AS8304   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Ecritel SASU
    AS47600  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | RUBIX DATACENTER SAS
    AS211448 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | WEBCONEX SAS
    AS33930  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Cloud Temple SAS
    AS31564  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Hexaglobe SAS
    AS199248 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NUMLOG S.A.S.
    AS203500 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | ABEILLE SARL
    AS212424 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Association des Reseaux de CentraleSupel
    AS201188 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | BJT Partners SAS
    AS201085 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ANTEMETA SAS
    AS198060 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Darva (Developpement D'applications Sur 
    AS199396 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Association Sames Wireless
    AS199997 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Ippon Hosting SARL
    AS206568 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ALTSYSNET.COM SAS
    AS206310 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Waxx SAS
    AS205919 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | ON-X GROUPE SA
    AS205816 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Elkaim Elie
    AS205992 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HERMES INTERNATIONAL SCA
    AS204515 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Association Crans
    AS205010 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | LaNetCie SAS
    AS396950 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | COLLECTIVITE DE SAINT BARTHELEMY
    AS215035 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CONNECT-IX SAS
    AS210232 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PACTOO SAS
    AS209928 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ANGELINKS SAS
    AS213184 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Telyo SAS
    AS34197  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Three Fourteen SASU
    AS30919  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Expertise France SAS
    AS61205  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Infomil S.A.S.
