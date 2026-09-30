    [*] Loading Data...
        - Loading ASN data from packed file... OK (124,902 records)
        - Loading Cones from final_as_rank.csv... OK (87399 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 3,282 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     123,074
    ASNs with an inferred upstream (customers): 84,041
    ASNs with a real published ASPA object:  3,282 (2.67% of all ASNs, 3.91% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.30 (max 228)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     41
      ...who HAVE signed ASPA:  4 (9.8%)
      ...who HAVEN'T yet:       37 (90.2%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS48362  | cone 34,996  | Stadtwerke Feldkirch
        AS34927  | cone 34,067  | iFog GmbH
        AS20766  | cone 12,419  | Association "Gitoyen"
        AS52468  | cone 5,786   | UFINET PANAMA S.A.
        AS38255  | cone 4,183   | China Education and Research Network (CERNET)
        AS4755   | cone 2,541   | TATA Communications (formerly VSNL)
        AS401753 | cone 2,354   | BIXCE Inc
        AS53062  | cone 1,665   | ACESSOLINE TELECOMUNICACOES LTDA
        AS202365 | cone 936     | Chronos
        AS1403   | cone 499     | EBOX

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 2,793
      Exact match (Jaccard = 1.0):    936 (33.5%)
      Mean Jaccard overlap:           0.608
      Median Jaccard overlap:         0.500

      Biggest mismatches (declared vs inferred providers disagree most):
        AS215110 | Jan Hill                            | Jaccard 0.00 | declared=[219418] inferred=[47272]
        AS264096 | RG PROVIDER LTDA ME                 | Jaccard 0.00 | declared=[263482] inferred=[6939, 14840]
        AS268047 | Masterinfo Internet                 | Jaccard 0.00 | declared=[263998, 268829, 272713] inferred=[6939, 7713, 14840]
        AS2716   | Universidade Federal do Rio Grande  | Jaccard 0.00 | declared=[1916] inferred=[4230, 14840, 16735, 28343]
        AS263331 | Netvox Telecomunicacoes LTDA        | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS266156 | SERVICOS DE COMUNICACAO LTDA        | Jaccard 0.00 | declared=[16735, 52817, 52863, 61696, 61895, 262979] inferred=[6939, 14840]
        AS262352 | NOVA TELECOM LTDA                   | Jaccard 0.00 | declared=[8167, 61621, 263541, 265137] inferred=[6939, 7738]
        AS52564  | Biazi Telecom                       | Jaccard 0.00 | declared=[8167, 52935, 61621] inferred=[6939, 53062, 262907]
        AS273454 | TELVIA TELECOMUNICACOES LTDA        | Jaccard 0.00 | declared=[61625, 265080, 265147, 268746] inferred=[6939, 7713, 14840]
        AS24550  | Websurfer Nepal Internet Service Pr | Jaccard 0.00 | declared=[141047] inferred=[14789]

    ====================================================================================================
     4. REAL ADOPTERS BY RIR
    ====================================================================================================
      ripencc    | 1,897 adopters
      arin       |   720 adopters
      apnic      |   513 adopters
      lacnic     |   149 adopters
      afrinic    |     2 adopters

    ====================================================================================================
     TOP 15 REAL ASPA ADOPTERS BY CONE SIZE
    ====================================================================================================
    ASN      | Country         | Cone     | Verdict              | Name
    ----------------------------------------------------------------------------------------------------
    AS174    | United States   | 73,710   | CORE: ACTIVE PROTECT | Cogent Communications, LLC
    AS1299   | Sweden          | 71,287   | CORE: ACTIVE PROTECT | Arelion (fka. Telia Carrier)
    AS3257   | United States   | 68,849   | CORE: ACTIVE PROTECT | GTT Communications Inc.
    AS7018   | United States   | 68,610   | CORE: ACTIVE PROTECT | AT&T Enterprises, LLC
    AS3320   | Germany         | 67,206   | CORE: ACTIVE PROTECT | Deutsche Telekom AG
    AS6830   | Netherlands     | 62,532   | CORE: ACTIVE PROTECT | Liberty Global Europe Holding B.V.
    AS33891  | Germany         | 36,857   | PARTIAL: VULNERABLE  | Core-Backbone GmbH
    AS12779  | Italy           | 27,403   | VULNERABLE (Atlas Ve | IT.Gate S.p.A.
    AS34019  | France          | 25,438   | PARTIAL: VULNERABLE  | Hivane Association
    AS25091  | Switzerland     | 19,747   | PARTIAL: VULNERABLE  | IP-Max SA
    AS212024 | France          | 13,096   | PASSIVE (Clean Pipe) | Marc Schmitt
    AS56662  | Poland          | 10,948   | PASSIVE (Clean Pipe) | Marcin Gondek
    AS49673  | Russian Federat | 9,126    | PASSIVE (Clean Pipe) | Truenetwork LLC
    AS3303   | Switzerland     | 9,117    | PARTIAL: VULNERABLE  | Swisscom (Schweiz) AG
    AS20764  | Russian Federat | 6,454    | ACTIVE (Atlas Verifi | CJSC RASCOM

    [+] Full cross-reference saved to aspa_real_vs_model.csv
