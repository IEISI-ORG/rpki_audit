    [*] Loading Data...
        - Loading ASN data from packed file... OK (125,153 records)
        - Loading Cones from final_as_rank.csv... OK (87459 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 3,421 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     123,297
    ASNs with an inferred upstream (customers): 83,999
    ASNs with a real published ASPA object:  3,421 (2.77% of all ASNs, 4.07% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.29 (max 230)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     61
      ...who HAVE signed ASPA:  6 (9.8%)
      ...who HAVEN'T yet:       55 (90.2%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS48362  | cone 35,675  | Stadtwerke Feldkirch
        AS34927  | cone 34,226  | iFog GmbH
        AS20473  | cone 21,916  | The Constant Company, LLC
        AS20766  | cone 12,332  | Association "Gitoyen"
        AS52468  | cone 5,868   | UFINET PANAMA S.A.
        AS38255  | cone 4,183   | China Education and Research Network (CERNET)
        AS15830  | cone 3,668   | Equinix, Inc.
        AS7713   | cone 3,441   | PT Telkom Indonesia Tbk
        AS4755   | cone 2,547   | TATA Communications (formerly VSNL)
        AS401753 | cone 2,410   | BIXCE Inc

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 2,916
      Exact match (Jaccard = 1.0):    986 (33.8%)
      Mean Jaccard overlap:           0.611
      Median Jaccard overlap:         0.500

      Biggest mismatches (declared vs inferred providers disagree most):
        AS269981 | COMPUNETWORK S.A.C.                 | Jaccard 0.00 | declared=[7195] inferred=[263702]
        AS262352 | NOVA TELECOM LTDA                   | Jaccard 0.00 | declared=[8167, 61621, 263541, 265137] inferred=[6939]
        AS264096 | RG PROVIDER LTDA ME                 | Jaccard 0.00 | declared=[263482] inferred=[6939]
        AS263321 | ILOGNET PROVEDOR                    | Jaccard 0.00 | declared=[14840, 265390, 270867] inferred=[6939]
        AS2716   | Universidade Federal do Rio Grande  | Jaccard 0.00 | declared=[1916] inferred=[4230, 16735, 28343]
        AS268047 | Masterinfo Internet                 | Jaccard 0.00 | declared=[263998, 268829, 272713] inferred=[6939, 7713]
        AS262895 | Norte Line Telecomunicacoes Ltda.   | Jaccard 0.00 | declared=[11344, 52907] inferred=[21574, 52928]
        AS273454 | TELVIA TELECOMUNICACOES LTDA        | Jaccard 0.00 | declared=[61625, 265080, 265147, 268746] inferred=[6939, 7713]
        AS263331 | Netvox Telecomunicacoes LTDA        | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS59678  | SYSTEM36 LLC                        | Jaccard 0.00 | declared=[6939, 34927, 54218, 55081] inferred=[200242]

    ====================================================================================================
     4. REAL ADOPTERS BY RIR
    ====================================================================================================
      ripencc    | 1,940 adopters
      arin       |   749 adopters
      apnic      |   559 adopters
      lacnic     |   169 adopters
      afrinic    |     2 adopters

    ====================================================================================================
     TOP 15 REAL ASPA ADOPTERS BY CONE SIZE
    ====================================================================================================
    ASN      | Country         | Cone     | Verdict              | Name
    ----------------------------------------------------------------------------------------------------
    AS174    | United States   | 73,849   | CORE: ACTIVE PROTECT | Cogent Communications, LLC
    AS1299   | Sweden          | 71,458   | CORE: ACTIVE PROTECT | Arelion (fka. Telia Carrier)
    AS3257   | United States   | 69,123   | CORE: ACTIVE PROTECT | GTT Communications Inc.
    AS7018   | United States   | 68,769   | CORE: ACTIVE PROTECT | AT&T Enterprises, LLC
    AS3320   | Germany         | 67,344   | CORE: ACTIVE PROTECT | Deutsche Telekom AG
    AS6830   | Netherlands     | 62,811   | CORE: ACTIVE PROTECT | Liberty Global Europe Holding B.V.
    AS33891  | Germany         | 46,961   | PARTIAL: VULNERABLE  | Core-Backbone GmbH
    AS12779  | Italy           | 27,909   | VULNERABLE (Atlas Ve | IT.Gate S.p.A.
    AS34019  | France          | 25,044   | PARTIAL: VULNERABLE  | Hivane Association
    AS25091  | Switzerland     | 20,059   | PARTIAL: VULNERABLE  | IP-Max SA
    AS212024 | France          | 13,154   | PASSIVE (Clean Pipe) | Marc Schmitt
    AS56662  | Poland          | 10,864   | PASSIVE (Clean Pipe) | Marcin Gondek
    AS49673  | Russian Federat | 9,423    | PASSIVE (Clean Pipe) | Truenetwork LLC
    AS20764  | Russian Federat | 8,599    | ACTIVE LOCAL ROV     | CJSC RASCOM
    AS3303   | Switzerland     | 6,551    | PARTIAL: VULNERABLE  | Swisscom (Schweiz) AG

    [+] Full cross-reference saved to aspa_real_vs_model.csv
