    [*] Loading Global Audit for FR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: FR (France)
    ====================================================================================================
    Total Networks:      1,893
    Total Cone Gravity:  168,331
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   707 (37.3%) -> Protects 83.1% of Traffic
    VULNERABLE NETWORKS:       746 (39.4%) -> Exposes  15.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        784 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   361 (46.0%)   IPv6 verdict   394 (50.3%)
      VULNERABLE main verdict   390 (49.7%)   IPv6 verdict   363 (46.3%)

    ====================================================================================================
     THE FR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS5511   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 71045    | 94%    | Orange S.A.
    AS35280  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 30427    | -      | F5 Networks SARL
    AS34019  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 24131    | -      | Hivane Association
    AS212024 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 13403    | -      | Marc Schmitt
    AS20766  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 12463    | -      | Association "Gitoyen"
    AS8218   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 6245     | -      | Zayo Europe
    AS204092 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3919     | -      | Association GRIFON
    AS29075  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3043     | 98%    | IELO-LIAZO SERVICES SAS
    AS50628  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 1668     | -      | Leonix Telecom SAS
    AS16276  | REGRESSED                      | REGRESSED                      | 567      | 1%     | OVH SAS
    AS35661  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 280      | -      | VIRTUA SYSTEMS SAS
    AS30781  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 168      | 100%   | Free Pro SAS
    AS3215   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 145      | 99%    | Orange S.A.
    AS15557  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 94       | 99%    | SFR SA
    AS29169  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 91       | -      | GANDI SAS
    AS35625  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 71       | 1%     | Eurofiber France SAS
    AS62000  | REGRESSED                      | REGRESSED                      | 52       | 1%     | SERVERD SAS
    AS2200   | REGRESSED                      | REGRESSED                      | 39       | 3%     | Renater
    AS39801  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 23       | -      | France-IX L3 Services
    AS8309   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 21       | -      | SIPARTECH SAS

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to FR?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS174    | 318        | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #2   | AS30781  | 138        | ACTIVE LOCAL ROV               | Free Pro SAS
    #3   | AS3215   | 124        | ACTIVE LOCAL ROV               | Orange S.A.
    #4   | AS3356   | 116        | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #5   | AS8218   | 114        | ACTIVE LOCAL ROV               | Zayo Europe
    #6   | AS8220   | 96         | ACTIVE LOCAL ROV               | COLT
    #7   | AS29075  | 92         | ACTIVE LOCAL ROV               | IELO-LIAZO SERVICES SAS
    #8   | AS1299   | 87         | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #9   | AS6939   | 77         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #10  | AS5511   | 74         | CORE: ACTIVE PROTECTOR         | Orange S.A.
    #11  | AS15557  | 74         | ACTIVE LOCAL ROV               | SFR SA
    #12  | AS6461   | 70         | REGRESSED                      | Zayo Bandwidth
    #13  | AS3257   | 66         | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #14  | AS35625  | 57         | PASSIVE (Clean Pipe)           | Eurofiber France SAS
    #15  | AS39801  | 52         | PASSIVE (Clean Pipe)           | France-IX L3 Services
    #16  | AS6762   | 40         | CORE: UNPROTECTED              | Telecom Italia Sparkle (Seabone)
    #17  | AS2914   | 29         | CORE: ACTIVE PROTECTOR         | NTT America, Inc.
    #18  | AS20473  | 27         | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #19  | AS39180  | 24         | PARTIAL: VULNERABLE (Mixed)    | LASOTEL SAS
    #20  | AS62000  | 23         | REGRESSED                      | SERVERD SAS

    ====================================================================================================
     IPv6 DIFFERENCES (FR networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS212024 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | Marc Schmitt
    AS39180  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | LASOTEL SAS
    AS202753 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | GLOBALGRID SASU
    AS8304   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Ecritel SASU
    AS47600  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | RUBIX DATACENTER SAS
    AS31564  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Hexaglobe SAS
    AS199248 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NUMLOG S.A.S.
    AS219331 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Thomas BOUZIN
    AS199660 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | LTI NETWORKS SASU
    AS212424 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/2            | Association des Reseaux de CentraleSupel
    AS197816 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Etix Everywhere Ouest SAS
    AS197922 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Techcrea Solutions SAS
    AS201188 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | BJT Partners SAS
    AS199396 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Association Sames Wireless
    AS198060 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Darva (Developpement D'applications Sur 
    AS200245 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Syndicat Mixte Manche Numerique
    AS199997 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Ippon Hosting SARL
    AS206310 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Waxx SAS
    AS205992 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HERMES INTERNATIONAL SCA
    AS205919 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | ON-X GROUPE SA
    AS204273 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | SPIE ICS
    AS205010 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | LaNetCie SAS
    AS215035 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CONNECT-IX SAS
    AS209823 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Enki Multimedia EURL
    AS213184 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Telyo SAS
    AS34197  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Three Fourteen SASU
    AS30919  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Expertise France SAS
    AS12670  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Completel SAS
    AS61205  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Infomil S.A.S.
    AS41935  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Dassault Systemes SE
