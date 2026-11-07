    [*] Loading Data...
        - Loading ASN data from packed file... OK (125,809 records)
        - Loading Cones from final_as_rank.csv... OK (87992 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 4,020 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     123,436
    ASNs with an inferred upstream (customers): 87,606
    ASNs with a real published ASPA object:  4,020 (3.26% of all ASNs, 4.59% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.30 (max 239)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     39
      ...who HAVE signed ASPA:  7 (17.9%)
      ...who HAVEN'T yet:       32 (82.1%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS9002   | cone 45,670  | RETN Limited
        AS31500  | cone 5,408   | Global Network Management Inc
        AS38255  | cone 4,183   | China Education and Research Network (CERNET)
        AS4755   | cone 2,597   | TATA Communications (formerly VSNL)
        AS14840  | cone 2,011   | BR.DIGITAL 
        AS64073  | cone 1,671   | Vetta Group
        AS57304  | cone 1,547   | RETN Russia
        AS59919  | cone 1,039   | Brainbox S.r.l.
        AS13786  | cone 980     | Seaborn (Seabras USA, LLC)
        AS31543  | cone 862     | myNet GmbH

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 3,598
      Exact match (Jaccard = 1.0):    1,715 (47.7%)
      Mean Jaccard overlap:           0.737
      Median Jaccard overlap:         0.800

      Biggest mismatches (declared vs inferred providers disagree most):
        AS269288 | DW SOLUTIONS SERVICOS DE TELECOMUNI | Jaccard 0.00 | declared=[52873, 61618] inferred=[52872]
        AS263331 | Netvox Telecomunicacoes LTDA        | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS150697 | S N FIBER                           | Jaccard 0.00 | declared=[136969] inferred=[139088, 139820]
        AS23930  | VITRO INC.                          | Jaccard 0.00 | declared=[1299, 3491, 4635, 4637, 4779, 6648, 7707, 9299, 15169, 15412, 17639, 18187, 18392, 23942, 24095, 24115, 55821, 59360, 135607] inferred=[7629]
        AS154383 | ZORNTECH WEB SOLUTIONS              | Jaccard 0.00 | declared=[17644, 23470, 55492, 63969, 138640, 139921] inferred=[207208]
        AS56052  | Zero Point Internet eXchange        | Jaccard 0.00 | declared=[174, 1299, 3356, 8529, 17557, 23764] inferred=[23750]
        AS141733 | Legion Telecom Pty Ltd              | Jaccard 0.00 | declared=[2764] inferred=[141457]
        AS140995 | The 1 Web Solution                  | Jaccard 0.00 | declared=[58689] inferred=[137491]
        AS18025  | Bhutan Telecom Ltd                  | Jaccard 0.00 | declared=[18024] inferred=[17660]
        AS136809 | FAST ZONE IT                        | Jaccard 0.00 | declared=[17644, 150142] inferred=[62610, 63199, 401322]

    ====================================================================================================
     4. REAL ADOPTERS BY RIR
    ====================================================================================================
      ripencc    | 2,138 adopters
      arin       |   829 adopters
      apnic      |   697 adopters
      lacnic     |   351 adopters
      afrinic    |     2 adopters

    ====================================================================================================
     TOP 15 REAL ASPA ADOPTERS BY CONE SIZE
    ====================================================================================================
    ASN      | Country         | Cone     | Verdict              | Name
    ----------------------------------------------------------------------------------------------------
    AS174    | United States   | 75,178   | CORE: ACTIVE PROTECT | Cogent Communications, LLC
    AS7018   | United States   | 72,750   | REGRESSED            | AT&T Enterprises, LLC
    AS1299   | Sweden          | 72,723   | INCONSISTENT         | Arelion (fka. Telia Carrier)
    AS3257   | United States   | 71,973   | CORE: ACTIVE PROTECT | GTT Communications Inc.
    AS6762   | Italy           | 71,186   | CORE: ACTIVE PROTECT | Telecom Italia Sparkle (Seabone)
    AS3320   | Germany         | 71,032   | CORE: ACTIVE PROTECT | Deutsche Telekom AG
    AS6830   | Netherlands     | 70,949   | CORE: ACTIVE PROTECT | Liberty Global Europe Holding B.V.
    AS33891  | Germany         | 46,982   | ACTIVE LOCAL ROV     | Core-Backbone GmbH
    AS12779  | Italy           | 27,764   | ACTIVE LOCAL ROV     | IT.Gate S.p.A.
    AS34019  | France          | 27,347   | ACTIVE LOCAL ROV     | Hivane Association
    AS25091  | Switzerland     | 17,636   | PARTIAL: VULNERABLE  | IP-Max SA
    AS212024 | France          | 13,228   | PARTIAL: VULNERABLE  | Marc Schmitt
    AS56662  | Poland          | 10,290   | PARTIAL: VULNERABLE  | Marcin Gondek
    AS49673  | Russian Federat | 9,713    | PARTIAL: VULNERABLE  | Truenetwork LLC
    AS3303   | Switzerland     | 7,196    | ACTIVE LOCAL ROV     | Swisscom (Schweiz) AG

    [+] Full cross-reference saved to aspa_real_vs_model.csv
