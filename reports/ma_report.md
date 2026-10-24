    [*] Loading Global Audit for MA...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: MA (Morocco)
    ====================================================================================================
    Total Networks:      33
    Total Cone Gravity:  34
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    15 (45.5%) -> Protects 70.6% of Traffic
    VULNERABLE NETWORKS:        14 (42.4%) -> Exposes  5.9% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        18 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict     8 (44.4%)   IPv6 verdict    11 (61.1%)
      VULNERABLE main verdict     9 (50.0%)   IPv6 verdict     6 (33.3%)

    ====================================================================================================
     THE MA CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS36925  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 12       | 99%    | Orange Maroc
    AS36884  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 10       | 98%    | Wana Corporate
    AS6713   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 8        | 91%    | Maroc Telecom
    AS36956  | VULNERABLE                     | -                              | 2        | -      | Office National des Postes et Telecommun
    AS328867 | PASSIVE (Clean Pipe)           | -                              | 2        | -      | Corebach Backbone SARL
    AS201129 | STUB: VULNERABLE               | -                              | 0        | -      | Linceris International Cloud Solutions -
    AS329280 | STUB: VULNERABLE               | -                              | 0        | -      | Centre Royal de Télédétection Spatiale
    AS329461 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0        | -      | Maroc Datacenter MDC
    AS329442 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | L'Agence Nationale de Réglementation des
    AS328960 | STUB: PASSIVE (Clean Pipe)     | -                              | 0        | -      | Ministry of Foreign Affairs African Coop
    AS329628 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | AL BARID BANK
    AS329612 | STUB: VULNERABLE               | -                              | 0        | -      | MTDS
    AS329605 | STUB: VULNERABLE               | -                              | 0        | -      | ATTIJARIWAFABANK
    AS329691 | STUB: PASSIVE (Clean Pipe)     | -                              | 0        | -      | AFRIQUIA S.M.D.C.
    AS328280 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | L'Agence Nationale de Réglementation des
    AS328268 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | INSTITUT NATIONAL DES POSTES ET TELECOMM
    AS328272 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0        | -      | CIE NATIONALE ROYAL AIR MAROC
    AS327917 | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | Direction Generale de la Securite des Sy
    AS328066 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0        | -      | MEDAFRICA SYSTEMS
    AS328055 | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | NPONE

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to MA?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS36925  | 13         | ACTIVE LOCAL ROV               | Orange Maroc
    #2   | AS6713   | 7          | PARTIAL: VULNERABLE (Mixed)    | Maroc Telecom
    #3   | AS36884  | 7          | ACTIVE LOCAL ROV               | Wana Corporate
    #4   | AS174    | 4          | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #5   | AS5511   | 3          | CORE: ACTIVE PROTECTOR         | Orange S.A.
    #6   | AS12956  | 2          | CORE: ACTIVE PROTECTOR         | Telxius (Telefonica Global)
    #7   | AS6762   | 2          | CORE: UNPROTECTED              | Telecom Italia Sparkle (Seabone)
    #8   | AS36956  | 2          | VULNERABLE                     | Office National des Postes et Telecommun
    #9   | AS6453   | 1          | CORE: UNPROTECTED              | TATA Communications (America) Inc
    #10  | AS3257   | 1          | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #11  | AS2914   | 1          | CORE: ACTIVE PROTECTOR         | NTT America, Inc.
    #12  | AS1299   | 1          | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #13  | AS13335  | 1          | ACTIVE LOCAL ROV (Hardcoded)   | Cloudflare, Inc.
    #14  | AS6939   | 1          | ACTIVE (Atlas Verified)        | Hurricane Electric LLC

    ====================================================================================================
     IPv6 DIFFERENCES (MA networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS329461 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Maroc Datacenter MDC
    AS328272 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CIE NATIONALE ROYAL AIR MAROC
    AS328066 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MEDAFRICA SYSTEMS
