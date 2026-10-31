    [*] Loading Data...
        - Loading ASN data from packed file... OK (125,651 records)
        - Loading Cones from final_as_rank.csv... OK (88086 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 3,904 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     123,570
    ASNs with an inferred upstream (customers): 87,672
    ASNs with a real published ASPA object:  3,904 (3.16% of all ASNs, 4.45% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.31 (max 231)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     91
      ...who HAVE signed ASPA:  10 (11.0%)
      ...who HAVEN'T yet:       81 (89.0%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS6939   | cone 71,053  | Hurricane Electric LLC
        AS9002   | cone 48,683  | RETN Limited
        AS17639  | cone 43,018  | Converge ICT Solutions Inc.
        AS48362  | cone 35,190  | Stadtwerke Feldkirch
        AS50304  | cone 13,891  | Blix Solutions AS
        AS1836   | cone 13,789  | green.ch AG
        AS56655  | cone 12,891  | Gigahost AS
        AS20766  | cone 12,639  | Association "Gitoyen"
        AS12389  | cone 12,329  | PJSC Rostelecom
        AS8220   | cone 7,286   | COLT

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 3,501
      Exact match (Jaccard = 1.0):    1,675 (47.8%)
      Mean Jaccard overlap:           0.737
      Median Jaccard overlap:         0.800

      Biggest mismatches (declared vs inferred providers disagree most):
        AS263331 | Netvox Telecomunicacoes LTDA        | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS262895 | Norte Line Telecomunicacoes Ltda.   | Jaccard 0.00 | declared=[11344, 52907] inferred=[21574, 52928]
        AS150697 | S N FIBER                           | Jaccard 0.00 | declared=[136969] inferred=[139088, 139820]
        AS154383 | ZORNTECH WEB SOLUTIONS              | Jaccard 0.00 | declared=[17644, 23470, 55492, 63969, 138640, 139921] inferred=[207208]
        AS141733 | Legion Telecom Pty Ltd              | Jaccard 0.00 | declared=[2764] inferred=[141457]
        AS138678 | Grandbo Technology Development Corp | Jaccard 0.00 | declared=[0] inferred=[45904]
        AS18025  | Bhutan Telecom Ltd                  | Jaccard 0.00 | declared=[18024] inferred=[17660]
        AS136809 | FAST ZONE IT                        | Jaccard 0.00 | declared=[17644, 150142] inferred=[62610, 63199, 401322]
        AS23930  | VITRO INC.                          | Jaccard 0.00 | declared=[1299, 3491, 4635, 4637, 4779, 6648, 7707, 9299, 15169, 15412, 17639, 18187, 18392, 23942, 24095, 24115, 55821, 59360, 135607] inferred=[7629]
        AS139922 | DISH MEDIA NETWORK PUBLIC LIMITED   | Jaccard 0.00 | declared=[132799] inferred=[38565]

    ====================================================================================================
     4. REAL ADOPTERS BY RIR
    ====================================================================================================
      ripencc    | 2,093 adopters
      arin       |   811 adopters
      apnic      |   666 adopters
      lacnic     |   330 adopters
      afrinic    |     2 adopters

    ====================================================================================================
     TOP 15 REAL ASPA ADOPTERS BY CONE SIZE
    ====================================================================================================
    ASN      | Country         | Cone     | Verdict              | Name
    ----------------------------------------------------------------------------------------------------
    AS174    | United States   | 75,321   | CORE: ACTIVE PROTECT | Cogent Communications, LLC
    AS7018   | United States   | 72,893   | REGRESSED            | AT&T Enterprises, LLC
    AS1299   | Sweden          | 72,867   | CORE: ACTIVE PROTECT | Arelion (fka. Telia Carrier)
    AS3257   | United States   | 72,125   | CORE: ACTIVE PROTECT | GTT Communications Inc.
    AS6762   | Italy           | 71,341   | CORE: ACTIVE PROTECT | Telecom Italia Sparkle (Seabone)
    AS3320   | Germany         | 71,190   | CORE: ACTIVE PROTECT | Deutsche Telekom AG
    AS6830   | Netherlands     | 71,107   | CORE: ACTIVE PROTECT | Liberty Global Europe Holding B.V.
    AS33891  | Germany         | 46,645   | ACTIVE LOCAL ROV     | Core-Backbone GmbH
    AS12779  | Italy           | 27,394   | ACTIVE LOCAL ROV     | IT.Gate S.p.A.
    AS34019  | France          | 25,713   | ACTIVE LOCAL ROV     | Hivane Association
    AS25091  | Switzerland     | 19,267   | PARTIAL: VULNERABLE  | IP-Max SA
    AS212024 | France          | 13,002   | PARTIAL: VULNERABLE  | Marc Schmitt
    AS56662  | Poland          | 10,929   | PARTIAL: VULNERABLE  | Marcin Gondek
    AS49673  | Russian Federat | 9,674    | PARTIAL: VULNERABLE  | Truenetwork LLC
    AS3303   | Switzerland     | 7,139    | ACTIVE LOCAL ROV     | Swisscom (Schweiz) AG

    [+] Full cross-reference saved to aspa_real_vs_model.csv
