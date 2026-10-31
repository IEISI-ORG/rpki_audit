    [*] Loading Global Audit for FR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: FR (France)
    ====================================================================================================
    Total Networks:      1,894
    Total Cone Gravity:  171,741
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   733 (38.7%) -> Protects 84.6% of Traffic
    VULNERABLE NETWORKS:       721 (38.1%) -> Exposes  7.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        786 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   383 (48.7%)   IPv6 verdict   417 (53.1%)
      VULNERABLE main verdict   372 (47.3%)   IPv6 verdict   347 (44.1%)

    ====================================================================================================
     THE FR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS5511   | CORE: ACTIVE PROTECTOR         | CORE: ACTIVE PROTECTOR         | 71288    | -      | Orange S.A.
    AS35280  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 32070    | -      | F5 Networks SARL
    AS34019  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 25713    | -      | Hivane Association
    AS212024 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 13002    | -      | Marc Schmitt
    AS20766  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 12639    | -      | Association "Gitoyen"
    AS8218   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 6206     | -      | Zayo Europe
    AS204092 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3983     | -      | Association GRIFON
    AS29075  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3082     | 97%    | IELO-LIAZO SERVICES SAS
    AS50628  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1741     | -      | Leonix Telecom SAS
    AS16276  | REGRESSED                      | REGRESSED                      | 581      | 2%     | OVH SAS
    AS35661  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 282      | -      | VIRTUA SYSTEMS SAS
    AS30781  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 168      | 95%    | Free Pro SAS
    AS3215   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 147      | 99%    | Orange S.A.
    AS29169  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 102      | -      | GANDI SAS
    AS15557  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 94       | 99%    | SFR SA
    AS35625  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 68       | 1%     | Eurofiber France SAS
    AS62000  | VOLATILE                       | VOLATILE                       | 48       | -      | SERVERD SAS
    AS2200   | REGRESSED                      | REGRESSED                      | 39       | 2%     | Renater
    AS197959 | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 22       | -      | VIRTUA SYSTEMS SAS
    AS39801  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 22       | -      | France-IX L3 Services

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
    #9   | AS6939   | 77         | ACTIVE LOCAL ROV               | Hurricane Electric LLC
    #10  | AS5511   | 74         | CORE: ACTIVE PROTECTOR         | Orange S.A.
    #11  | AS15557  | 74         | ACTIVE LOCAL ROV               | SFR SA
    #12  | AS6461   | 70         | REGRESSED                      | Zayo Bandwidth
    #13  | AS3257   | 66         | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #14  | AS35625  | 57         | PASSIVE (Clean Pipe)           | Eurofiber France SAS
    #15  | AS39801  | 52         | PASSIVE (Clean Pipe)           | France-IX L3 Services
    #16  | AS6762   | 40         | CORE: ACTIVE PROTECTOR         | Telecom Italia Sparkle (Seabone)
    #17  | AS2914   | 29         | INCONSISTENT                   | NTT America, Inc.
    #18  | AS20473  | 27         | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #19  | AS39180  | 24         | PARTIAL: VULNERABLE (Mixed)    | LASOTEL SAS
    #20  | AS62000  | 23         | VOLATILE                       | SERVERD SAS

    ====================================================================================================
     IPv6 DIFFERENCES (FR networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS212024 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Marc Schmitt
    AS39180  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | LASOTEL SAS
    AS202753 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | GLOBALGRID SASU
    AS211448 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | WEBCONEX SAS
    AS8304   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Ecritel SASU
    AS47600  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | RUBIX DATACENTER SAS
    AS197922 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Techcrea Solutions SAS
    AS212424 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/2            | Association des Reseaux de CentraleSupel
    AS199248 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NUMLOG S.A.S.
    AS43858  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | WEBAXYS SAS
    AS199396 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Association Sames Wireless
    AS208458 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/4            | REGION NOUVELLE-AQUITAINE
    AS199997 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Ippon Hosting SARL
    AS198060 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Darva (Developpement D'applications Sur 
    AS204273 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | SPIE ICS
    AS206568 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ALTSYSNET.COM SAS
    AS205992 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HERMES INTERNATIONAL SCA
    AS205919 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | ON-X GROUPE SA
    AS206310 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Waxx SAS
    AS205010 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | LaNetCie SAS
    AS201188 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | BJT Partners SAS
    AS202089 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Unimedia Services SAS
    AS215035 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CONNECT-IX SAS
    AS216222 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Julien Bellier
    AS210232 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PACTOO SAS
    AS209928 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | XEFI LYON SAS
    AS213184 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Telyo SAS
    AS34197  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Three Fourteen SASU
    AS30919  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Expertise France SAS
    AS61205  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Infomil S.A.S.
