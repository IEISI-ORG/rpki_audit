    [*] Loading Data...
        - Loading ASN data from packed file... OK (126,094 records)
        - Loading Cones from final_as_rank.csv... OK (88077 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 4,260 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     123,678
    ASNs with an inferred upstream (customers): 87,720
    ASNs with a real published ASPA object:  4,260 (3.44% of all ASNs, 4.86% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.31 (max 246)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     135
      ...who HAVE signed ASPA:  15 (11.1%)
      ...who HAVEN'T yet:       120 (88.9%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS6939   | cone 70,880  | Hurricane Electric LLC
        AS35280  | cone 52,327  | F5 Networks SARL
        AS9002   | cone 44,905  | RETN Limited
        AS17639  | cone 42,701  | Converge ICT Solutions Inc.
        AS48362  | cone 34,983  | Stadtwerke Feldkirch
        AS34549  | cone 34,612  | meerfarbig GmbH & Co. KG
        AS34927  | cone 33,680  | iFog GmbH
        AS6204   | cone 23,701  | ZET Communications S.R.L.
        AS50304  | cone 14,065  | Blix Solutions AS
        AS1836   | cone 13,302  | green.ch AG

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 3,818
      Exact match (Jaccard = 1.0):    1,822 (47.7%)
      Mean Jaccard overlap:           0.737
      Median Jaccard overlap:         0.800

      Biggest mismatches (declared vs inferred providers disagree most):
        AS269288 | DW SOLUTIONS SERVICOS DE TELECOMUNI | Jaccard 0.00 | declared=[52873, 61618] inferred=[52872]
        AS263331 | Netvox Telecomunicacoes LTDA        | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS150697 | S N FIBER                           | Jaccard 0.00 | declared=[136969] inferred=[139088, 139820]
        AS154383 | ZORNTECH WEB SOLUTIONS              | Jaccard 0.00 | declared=[17644, 23470, 55492, 63969, 138640, 139921] inferred=[207208]
        AS18025  | Bhutan Telecom Ltd                  | Jaccard 0.00 | declared=[18024] inferred=[17660]
        AS136809 | FAST ZONE IT                        | Jaccard 0.00 | declared=[17644, 150142] inferred=[62610, 63199, 401322]
        AS153947 | FAST ZONE IT                        | Jaccard 0.00 | declared=[17644, 150142] inferred=[51765]
        AS23930  | VITRO INC.                          | Jaccard 0.00 | declared=[1299, 3491, 4635, 4637, 4779, 6648, 7707, 9299, 15169, 15412, 17639, 18187, 18392, 23942, 24095, 24115, 55821, 59360, 135607] inferred=[7629]
        AS141733 | Legion Telecom Pty Ltd              | Jaccard 0.00 | declared=[2764] inferred=[141457]
        AS140995 | The 1 Web Solution                  | Jaccard 0.00 | declared=[58689] inferred=[137491]

    ====================================================================================================
     4. REAL ADOPTERS BY RIR
    ====================================================================================================
      ripencc    | 2,229 adopters
      arin       |   868 adopters
      apnic      |   792 adopters
      lacnic     |   367 adopters
      afrinic    |     2 adopters

    ====================================================================================================
     TOP 15 REAL ASPA ADOPTERS BY CONE SIZE
    ====================================================================================================
    ASN      | Country         | Cone     | Verdict              | Name
    ----------------------------------------------------------------------------------------------------
    AS174    | United States   | 75,247   | CORE: ACTIVE PROTECT | Cogent Communications, LLC
    AS7018   | United States   | 73,047   | REGRESSED            | AT&T Enterprises, LLC
    AS1299   | Sweden          | 72,810   | CORE: ACTIVE PROTECT | Arelion (fka. Telia Carrier)
    AS3257   | United States   | 72,153   | CORE: ACTIVE PROTECT | GTT Communications Inc.
    AS6762   | Italy           | 71,146   | CORE: ACTIVE PROTECT | Telecom Italia Sparkle (Seabone)
    AS3320   | Germany         | 71,101   | CORE: ACTIVE PROTECT | Deutsche Telekom AG
    AS6830   | Netherlands     | 71,019   | CORE: ACTIVE PROTECT | Liberty Global Europe Holding B.V.
    AS33891  | Germany         | 46,034   | ACTIVE LOCAL ROV     | Core-Backbone GmbH
    AS34019  | France          | 37,041   | ACTIVE LOCAL ROV     | Hivane Association
    AS12779  | Italy           | 27,092   | ACTIVE LOCAL ROV     | IT.Gate S.p.A.
    AS25091  | Switzerland     | 16,442   | PASSIVE (Clean Pipe) | IP-Max SA
    AS212024 | France          | 12,766   | PARTIAL: VULNERABLE  | Marc Schmitt
    AS56662  | Poland          | 11,963   | PARTIAL: VULNERABLE  | Marcin Gondek
    AS3303   | Switzerland     | 9,203    | ACTIVE LOCAL ROV     | Swisscom (Schweiz) AG
    AS49673  | Russian Federat | 9,148    | PARTIAL: VULNERABLE  | Truenetwork LLC

    [+] Full cross-reference saved to aspa_real_vs_model.csv
