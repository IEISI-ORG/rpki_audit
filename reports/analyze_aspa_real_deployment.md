    [*] Loading Data...
        - Loading ASN data from packed file... OK (125,524 records)
        - Loading Cones from final_as_rank.csv... OK (87912 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 3,703 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     123,487
    ASNs with an inferred upstream (customers): 87,546
    ASNs with a real published ASPA object:  3,703 (3.00% of all ASNs, 4.23% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.32 (max 232)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     74
      ...who HAVE signed ASPA:  6 (8.1%)
      ...who HAVEN'T yet:       68 (91.9%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS6939   | cone 70,809  | Hurricane Electric LLC
        AS17639  | cone 43,350  | Converge ICT Solutions Inc.
        AS48362  | cone 35,078  | Stadtwerke Feldkirch
        AS50304  | cone 13,808  | Blix Solutions AS
        AS1836   | cone 13,457  | green.ch AG
        AS20766  | cone 12,463  | Association "Gitoyen"
        AS56655  | cone 12,436  | Gigahost AS
        AS13030  | cone 4,417   | Init7 (Switzerland) Ltd.
        AS38255  | cone 4,183   | China Education and Research Network (CERNET)
        AS24961  | cone 2,524   | WIIT AG (fka. myLoc Managed IT AG)

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 3,310
      Exact match (Jaccard = 1.0):    1,556 (47.0%)
      Mean Jaccard overlap:           0.731
      Median Jaccard overlap:         0.750

      Biggest mismatches (declared vs inferred providers disagree most):
        AS263331 | Netvox Telecomunicacoes LTDA        | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS262895 | Norte Line Telecomunicacoes Ltda.   | Jaccard 0.00 | declared=[11344, 52907] inferred=[21574, 52928]
        AS150697 | S N FIBER                           | Jaccard 0.00 | declared=[136969] inferred=[139088, 139820]
        AS154383 | ZORNTECH WEB SOLUTIONS              | Jaccard 0.00 | declared=[17644, 23470, 55492, 63969, 138640, 139921] inferred=[207208]
        AS139922 | DISH MEDIA NETWORK PUBLIC LIMITED   | Jaccard 0.00 | declared=[132799] inferred=[38565]
        AS141733 | Legion Telecom Pty Ltd              | Jaccard 0.00 | declared=[2764] inferred=[141457]
        AS138678 | Grandbo Technology Development Corp | Jaccard 0.00 | declared=[0] inferred=[45904]
        AS18025  | Bhutan Telecom Ltd                  | Jaccard 0.00 | declared=[18024] inferred=[17660]
        AS136809 | FAST ZONE IT                        | Jaccard 0.00 | declared=[17644, 147181, 150142] inferred=[62610, 63199, 401322]
        AS133298 | Netflow broadband Pvt Ltd.          | Jaccard 0.00 | declared=[150593] inferred=[18229]

    ====================================================================================================
     4. REAL ADOPTERS BY RIR
    ====================================================================================================
      ripencc    | 2,029 adopters
      arin       |   784 adopters
      apnic      |   625 adopters
      lacnic     |   261 adopters
      afrinic    |     2 adopters

    ====================================================================================================
     TOP 15 REAL ASPA ADOPTERS BY CONE SIZE
    ====================================================================================================
    ASN      | Country         | Cone     | Verdict              | Name
    ----------------------------------------------------------------------------------------------------
    AS174    | United States   | 75,151   | CORE: ACTIVE PROTECT | Cogent Communications, LLC
    AS1299   | Sweden          | 72,705   | CORE: ACTIVE PROTECT | Arelion (fka. Telia Carrier)
    AS7018   | United States   | 72,667   | REGRESSED            | AT&T Enterprises, LLC
    AS3257   | United States   | 71,885   | CORE: ACTIVE PROTECT | GTT Communications Inc.
    AS6762   | Italy           | 71,093   | CORE: UNPROTECTED    | Telecom Italia Sparkle (Seabone)
    AS3320   | Germany         | 70,940   | CORE: ACTIVE PROTECT | Deutsche Telekom AG
    AS6830   | Netherlands     | 70,862   | CORE: ACTIVE PROTECT | Liberty Global Europe Holding B.V.
    AS33891  | Germany         | 47,131   | ACTIVE LOCAL ROV     | Core-Backbone GmbH
    AS12779  | Italy           | 26,828   | ACTIVE LOCAL ROV     | IT.Gate S.p.A.
    AS34019  | France          | 24,131   | ACTIVE LOCAL ROV     | Hivane Association
    AS25091  | Switzerland     | 19,553   | PARTIAL: VULNERABLE  | IP-Max SA
    AS212024 | France          | 13,403   | VULNERABLE           | Marc Schmitt
    AS56662  | Poland          | 10,719   | PARTIAL: VULNERABLE  | Marcin Gondek
    AS49673  | Russian Federat | 9,463    | PARTIAL: VULNERABLE  | Truenetwork LLC
    AS3303   | Switzerland     | 6,836    | ACTIVE LOCAL ROV     | Swisscom (Schweiz) AG

    [+] Full cross-reference saved to aspa_real_vs_model.csv
