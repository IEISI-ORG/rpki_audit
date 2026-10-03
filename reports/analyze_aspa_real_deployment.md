    [*] Loading Data...
        - Loading ASN data from packed file... OK (125,032 records)
        - Loading Cones from final_as_rank.csv... OK (87449 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 3,282 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     123,155
    ASNs with an inferred upstream (customers): 83,984
    ASNs with a real published ASPA object:  3,282 (2.66% of all ASNs, 3.91% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.30 (max 228)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     46
      ...who HAVE signed ASPA:  4 (8.7%)
      ...who HAVEN'T yet:       42 (91.3%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS48362  | cone 35,486  | Stadtwerke Feldkirch
        AS34927  | cone 33,526  | iFog GmbH
        AS20766  | cone 12,333  | Association "Gitoyen"
        AS52468  | cone 5,951   | UFINET PANAMA S.A.
        AS38255  | cone 4,183   | China Education and Research Network (CERNET)
        AS401753 | cone 2,443   | BIXCE Inc
        AS4755   | cone 2,235   | TATA Communications (formerly VSNL)
        AS202365 | cone 928     | Chronos
        AS1403   | cone 502     | EBOX
        AS50607  | cone 395     | Stowarzyszenie e-Poludnie

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 2,792
      Exact match (Jaccard = 1.0):    940 (33.7%)
      Mean Jaccard overlap:           0.608
      Median Jaccard overlap:         0.500

      Biggest mismatches (declared vs inferred providers disagree most):
        AS215110 | Jan Hill                            | Jaccard 0.00 | declared=[219418] inferred=[47272]
        AS264096 | RG PROVIDER LTDA ME                 | Jaccard 0.00 | declared=[263482] inferred=[6939]
        AS268047 | Masterinfo Internet                 | Jaccard 0.00 | declared=[263998, 268829, 272713] inferred=[6939, 7713]
        AS2716   | Universidade Federal do Rio Grande  | Jaccard 0.00 | declared=[1916] inferred=[4230, 16735, 28343]
        AS263331 | Netvox Telecomunicacoes LTDA        | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS263321 | ILOGNET PROVEDOR                    | Jaccard 0.00 | declared=[14840, 265390, 270867] inferred=[6939]
        AS266156 | SERVICOS DE COMUNICACAO LTDA        | Jaccard 0.00 | declared=[16735, 52817, 52863, 61696, 61895, 262979] inferred=[6939]
        AS262352 | NOVA TELECOM LTDA                   | Jaccard 0.00 | declared=[8167, 61621, 263541, 265137] inferred=[6939]
        AS52564  | Biazi Telecom                       | Jaccard 0.00 | declared=[8167, 52935, 61621] inferred=[6939, 52573, 262907]
        AS273454 | TELVIA TELECOMUNICACOES LTDA        | Jaccard 0.00 | declared=[61625, 265080, 265147, 268746] inferred=[6939, 7713]

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
    AS174    | United States   | 73,729   | CORE: ACTIVE PROTECT | Cogent Communications, LLC
    AS1299   | Sweden          | 71,317   | CORE: ACTIVE PROTECT | Arelion (fka. Telia Carrier)
    AS3257   | United States   | 68,984   | CORE: ACTIVE PROTECT | GTT Communications Inc.
    AS7018   | United States   | 68,761   | CORE: ACTIVE PROTECT | AT&T Enterprises, LLC
    AS3320   | Germany         | 67,133   | CORE: ACTIVE PROTECT | Deutsche Telekom AG
    AS6830   | Netherlands     | 62,226   | CORE: ACTIVE PROTECT | Liberty Global Europe Holding B.V.
    AS33891  | Germany         | 32,143   | PARTIAL: VULNERABLE  | Core-Backbone GmbH
    AS12779  | Italy           | 27,999   | VULNERABLE (Atlas Ve | IT.Gate S.p.A.
    AS34019  | France          | 24,934   | PARTIAL: VULNERABLE  | Hivane Association
    AS25091  | Switzerland     | 19,289   | PARTIAL: VULNERABLE  | IP-Max SA
    AS212024 | France          | 12,523   | PASSIVE (Clean Pipe) | Marc Schmitt
    AS56662  | Poland          | 10,840   | PASSIVE (Clean Pipe) | Marcin Gondek
    AS49673  | Russian Federat | 9,076    | PASSIVE (Clean Pipe) | Truenetwork LLC
    AS3303   | Switzerland     | 8,596    | PARTIAL: VULNERABLE  | Swisscom (Schweiz) AG
    AS20764  | Russian Federat | 5,733    | ACTIVE (Atlas Verifi | CJSC RASCOM

    [+] Full cross-reference saved to aspa_real_vs_model.csv
