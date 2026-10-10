    [*] Loading Data...
        - Loading ASN data from packed file... OK (125,153 records)
        - Loading Cones from final_as_rank.csv... OK (87459 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 3,421 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     88,254
    ASNs with an inferred upstream (customers): 83,999
    ASNs with a real published ASPA object:  3,421 (3.88% of all ASNs, 4.07% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.29 (max 230)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     61
      ...who HAVE signed ASPA:  6 (9.8%)
      ...who HAVEN'T yet:       55 (90.2%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS48362  | cone 35,675  | Unknown
        AS34927  | cone 34,226  | Unknown
        AS20473  | cone 21,916  | Unknown
        AS20766  | cone 12,332  | Unknown
        AS52468  | cone 5,868   | Unknown
        AS38255  | cone 4,183   | Unknown
        AS15830  | cone 3,668   | Unknown
        AS7713   | cone 3,441   | Unknown
        AS4755   | cone 2,547   | Unknown
        AS401753 | cone 2,410   | Unknown

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 2,916
      Exact match (Jaccard = 1.0):    986 (33.8%)
      Mean Jaccard overlap:           0.611
      Median Jaccard overlap:         0.500

      Biggest mismatches (declared vs inferred providers disagree most):
        AS269981 | Unknown                             | Jaccard 0.00 | declared=[7195] inferred=[263702]
        AS262352 | Unknown                             | Jaccard 0.00 | declared=[8167, 61621, 263541, 265137] inferred=[6939]
        AS264096 | Unknown                             | Jaccard 0.00 | declared=[263482] inferred=[6939]
        AS263321 | Unknown                             | Jaccard 0.00 | declared=[14840, 265390, 270867] inferred=[6939]
        AS2716   | Unknown                             | Jaccard 0.00 | declared=[1916] inferred=[4230, 16735, 28343]
        AS268047 | Unknown                             | Jaccard 0.00 | declared=[263998, 268829, 272713] inferred=[6939, 7713]
        AS262895 | Unknown                             | Jaccard 0.00 | declared=[11344, 52907] inferred=[21574, 52928]
        AS273454 | Unknown                             | Jaccard 0.00 | declared=[61625, 265080, 265147, 268746] inferred=[6939, 7713]
        AS263331 | Unknown                             | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS59678  | Unknown                             | Jaccard 0.00 | declared=[6939, 34927, 54218, 55081] inferred=[200242]

    ====================================================================================================
     4. REAL ADOPTERS BY RIR
    ====================================================================================================
      ripencc    | 1,709 adopters
      arin       |   661 adopters
      apnic      |   519 adopters
      lacnic     |   166 adopters
      afrinic    |     2 adopters

    ====================================================================================================
     TOP 15 REAL ASPA ADOPTERS BY CONE SIZE
    ====================================================================================================
    ASN      | Country         | Cone     | Verdict              | Name
    ----------------------------------------------------------------------------------------------------
    AS174    | United States   | 73,849   | CORE: ACTIVE PROTECT | Unknown
    AS1299   | Sweden          | 71,458   | CORE: ACTIVE PROTECT | Unknown
    AS3257   | United States   | 69,123   | CORE: ACTIVE PROTECT | Unknown
    AS7018   | United States   | 68,769   | CORE: ACTIVE PROTECT | Unknown
    AS3320   | Germany         | 67,344   | CORE: ACTIVE PROTECT | Unknown
    AS6830   | Netherlands     | 62,811   | CORE: ACTIVE PROTECT | Unknown
    AS33891  | XX              | 46,961   | PARTIAL: VULNERABLE  | Unknown
    AS12779  | Italy           | 27,909   | VULNERABLE (Atlas Ve | Unknown
    AS34019  | France          | 25,044   | PARTIAL: VULNERABLE  | Unknown
    AS25091  | Switzerland     | 20,059   | PARTIAL: VULNERABLE  | Unknown
    AS212024 | France          | 13,154   | PASSIVE (Clean Pipe) | Unknown
    AS56662  | Poland          | 10,864   | PASSIVE (Clean Pipe) | Unknown
    AS49673  | Russian Federat | 9,423    | PASSIVE (Clean Pipe) | Unknown
    AS20764  | Russian Federat | 8,599    | PASSIVE (Clean Pipe) | Unknown
    AS3303   | Switzerland     | 6,551    | PARTIAL: VULNERABLE  | Unknown

    [+] Full cross-reference saved to aspa_real_vs_model.csv
