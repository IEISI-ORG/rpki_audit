    [*] Loading Global Audit for MA...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: MA (Morocco)
    ====================================================================================================
    Total Networks:      33
    Total Cone Gravity:  35
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    21 (63.6%) -> Protects 94.3% of Traffic
    VULNERABLE NETWORKS:         8 (24.2%) -> Exposes  0.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        18 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    14 (77.8%)   IPv6 verdict    17 (94.4%)
      VULNERABLE main verdict     4 (22.2%)   IPv6 verdict     1 ( 5.6%)

    ====================================================================================================
     THE MA CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS36925  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 13       | 99%    | Orange Maroc
    AS36884  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 10       | 97%    | Wana Corporate
    AS6713   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 8        | 99%    | Maroc Telecom
    AS328867 | PARTIAL: VULNERABLE (Mixed)    | -                              | 2        | -      | Corebach Backbone SARL
    AS36956  | PASSIVE (Clean Pipe)           | -                              | 2        | -      | Office National des Postes et Telecommun
    AS201129 | STUB: VULNERABLE               | -                              | 0        | -      | Linceris International Cloud Solutions -
    AS329280 | STUB: VULNERABLE               | -                              | 0        | -      | Centre Royal de Télédétection Spatiale
    AS329442 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | L'Agence Nationale de Réglementation des
    AS329461 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0        | -      | Maroc Datacenter MDC
    AS329691 | STUB: PASSIVE (Clean Pipe)     | -                              | 0        | -      | AFRIQUIA S.M.D.C.
    AS329628 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | AL BARID BANK
    AS329612 | STUB: VULNERABLE               | -                              | 0        | -      | MTDS
    AS329605 | STUB: VULNERABLE               | -                              | 0        | -      | ATTIJARIWAFABANK
    AS328280 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | L'Agence Nationale de Réglementation des
    AS328272 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0        | -      | CIE NATIONALE ROYAL AIR MAROC
    AS328268 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | INSTITUT NATIONAL DES POSTES ET TELECOMM
    AS327989 | STUB: PASSIVE (Clean Pipe)     | -                              | 0        | -      | Genious Communications
    AS327917 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | Direction Generale de la Securite des Sy
    AS328066 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0        | -      | MEDAFRICA SYSTEMS
    AS328055 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | NPONE

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to MA?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS36925  | 13         | ACTIVE LOCAL ROV               | Orange Maroc
    #2   | AS6713   | 7          | ACTIVE LOCAL ROV               | Maroc Telecom
    #3   | AS36884  | 7          | ACTIVE LOCAL ROV               | Wana Corporate
    #4   | AS174    | 4          | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #5   | AS5511   | 3          | CORE: ACTIVE PROTECTOR         | Orange S.A.
    #6   | AS12956  | 2          | CORE: ACTIVE PROTECTOR         | Telxius (Telefonica Global)
    #7   | AS6762   | 2          | CORE: ACTIVE PROTECTOR         | Telecom Italia Sparkle (Seabone)
    #8   | AS36956  | 2          | PASSIVE (Clean Pipe)           | Office National des Postes et Telecommun
    #9   | AS6453   | 1          | CORE: ACTIVE PROTECTOR         | TATA Communications (America) Inc
    #10  | AS3257   | 1          | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.
    #11  | AS2914   | 1          | INCONSISTENT                   | NTT America, Inc.
    #12  | AS1299   | 1          | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #13  | AS13335  | 1          | ACTIVE LOCAL ROV (Hardcoded)   | Cloudflare, Inc.
    #14  | AS6939   | 1          | ACTIVE LOCAL ROV               | Hurricane Electric LLC

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
