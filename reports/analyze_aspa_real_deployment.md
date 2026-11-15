    [*] Loading Data...
        - Loading ASN data from packed file... OK (125,950 records)
        - Loading Cones from final_as_rank.csv... OK (87904 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 4,098 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     123,535
    ASNs with an inferred upstream (customers): 87,549
    ASNs with a real published ASPA object:  4,098 (3.32% of all ASNs, 4.68% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.31 (max 240)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     77
      ...who HAVE signed ASPA:  9 (11.7%)
      ...who HAVEN'T yet:       68 (88.3%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS6939   | cone 70,802  | Hurricane Electric LLC
        AS9002   | cone 44,969  | RETN Limited
        AS34549  | cone 35,236  | meerfarbig GmbH & Co. KG
        AS48362  | cone 34,757  | Stadtwerke Feldkirch
        AS35280  | cone 32,814  | F5 Networks SARL
        AS50304  | cone 14,215  | Blix Solutions AS
        AS56655  | cone 12,997  | Gigahost AS
        AS12389  | cone 12,793  | PJSC Rostelecom
        AS8220   | cone 6,902   | COLT
        AS31500  | cone 5,388   | Global Network Management Inc

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 3,663
      Exact match (Jaccard = 1.0):    1,739 (47.5%)
      Mean Jaccard overlap:           0.735
      Median Jaccard overlap:         0.800

      Biggest mismatches (declared vs inferred providers disagree most):
        AS269288 | DW SOLUTIONS SERVICOS DE TELECOMUNI | Jaccard 0.00 | declared=[52873, 61618] inferred=[52872]
        AS263331 | Netvox Telecomunicacoes LTDA        | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS150697 | S N FIBER                           | Jaccard 0.00 | declared=[136969] inferred=[139088, 139820]
        AS154383 | ZORNTECH WEB SOLUTIONS              | Jaccard 0.00 | declared=[17644, 23470, 55492, 63969, 138640, 139921] inferred=[207208]
        AS141733 | Legion Telecom Pty Ltd              | Jaccard 0.00 | declared=[2764] inferred=[141457]
        AS140995 | The 1 Web Solution                  | Jaccard 0.00 | declared=[58689] inferred=[137491]
        AS18025  | Bhutan Telecom Ltd                  | Jaccard 0.00 | declared=[18024] inferred=[17660]
        AS136809 | FAST ZONE IT                        | Jaccard 0.00 | declared=[17644, 150142] inferred=[62610, 63199, 401322]
        AS23930  | VITRO INC.                          | Jaccard 0.00 | declared=[1299, 3491, 4635, 4637, 4779, 6648, 7707, 9299, 15169, 15412, 17639, 18187, 18392, 23942, 24095, 24115, 55821, 59360, 135607] inferred=[7629]
        AS56052  | Zero Point Internet eXchange        | Jaccard 0.00 | declared=[174, 1299, 3356, 8529, 17557, 23764] inferred=[23750]

    ====================================================================================================
     4. REAL ADOPTERS BY RIR
    ====================================================================================================
      ripencc    | 2,172 adopters
      arin       |   844 adopters
      apnic      |   720 adopters
      lacnic     |   358 adopters
      afrinic    |     2 adopters

    ====================================================================================================
     TOP 15 REAL ASPA ADOPTERS BY CONE SIZE
    ====================================================================================================
    ASN      | Country         | Cone     | Verdict              | Name
    ----------------------------------------------------------------------------------------------------
    AS174    | United States   | 75,065   | INCONSISTENT         | Cogent Communications, LLC
    AS7018   | United States   | 72,662   | REGRESSED            | AT&T Enterprises, LLC
    AS1299   | Sweden          | 72,631   | CORE: ACTIVE PROTECT | Arelion (fka. Telia Carrier)
    AS3257   | United States   | 71,895   | CORE: ACTIVE PROTECT | GTT Communications Inc.
    AS6762   | Italy           | 71,090   | CORE: ACTIVE PROTECT | Telecom Italia Sparkle (Seabone)
    AS3320   | Germany         | 70,941   | CORE: ACTIVE PROTECT | Deutsche Telekom AG
    AS6830   | Netherlands     | 70,859   | CORE: ACTIVE PROTECT | Liberty Global Europe Holding B.V.
    AS33891  | Germany         | 46,803   | ACTIVE LOCAL ROV     | Core-Backbone GmbH
    AS34019  | France          | 38,150   | ACTIVE LOCAL ROV     | Hivane Association
    AS12779  | Italy           | 27,342   | ACTIVE LOCAL ROV     | IT.Gate S.p.A.
    AS25091  | Switzerland     | 17,473   | PASSIVE (Clean Pipe) | IP-Max SA
    AS212024 | France          | 13,520   | PARTIAL: VULNERABLE  | Marc Schmitt
    AS56662  | Poland          | 12,316   | PARTIAL: VULNERABLE  | Marcin Gondek
    AS49673  | Russian Federat | 9,669    | PARTIAL: VULNERABLE  | Truenetwork LLC
    AS3303   | Switzerland     | 9,521    | ACTIVE LOCAL ROV     | Swisscom (Schweiz) AG

    [+] Full cross-reference saved to aspa_real_vs_model.csv
