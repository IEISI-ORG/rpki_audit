    [*] Loading Data...
        - Loading ASN data from packed file... OK (125,397 records)
        - Loading Cones from final_as_rank.csv... OK (87712 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 3,537 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     123,387
    ASNs with an inferred upstream (customers): 87,401
    ASNs with a real published ASPA object:  3,537 (2.87% of all ASNs, 4.05% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.31 (max 232)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     113
      ...who HAVE signed ASPA:  10 (8.8%)
      ...who HAVEN'T yet:       103 (91.2%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS6939   | cone 70,679  | Hurricane Electric LLC
        AS9002   | cone 48,400  | RETN Limited
        AS48362  | cone 35,641  | Stadtwerke Feldkirch
        AS34549  | cone 34,730  | meerfarbig GmbH & Co. KG
        AS34927  | cone 34,393  | iFog GmbH
        AS35280  | cone 32,991  | F5 Networks SARL
        AS50304  | cone 14,224  | Blix Solutions AS
        AS12389  | cone 13,839  | Rostelecom PJSC
        AS1836   | cone 13,269  | green.ch AG
        AS56655  | cone 12,906  | Gigahost AS

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 3,144
      Exact match (Jaccard = 1.0):    1,474 (46.9%)
      Mean Jaccard overlap:           0.730
      Median Jaccard overlap:         0.750

      Biggest mismatches (declared vs inferred providers disagree most):
        AS263331 | Netvox Telecomunicacoes LTDA        | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS262895 | Norte Line Telecomunicacoes Ltda.   | Jaccard 0.00 | declared=[11344, 52907] inferred=[21574, 52928]
        AS150697 | S N FIBER                           | Jaccard 0.00 | declared=[136969] inferred=[139088, 139820]
        AS154383 | ZORNTECH WEB SOLUTIONS              | Jaccard 0.00 | declared=[17644, 23470, 55492, 63969, 138640, 139921] inferred=[207208]
        AS18025  | Bhutan Telecom Ltd                  | Jaccard 0.00 | declared=[18024] inferred=[17660]
        AS153947 | FAST ZONE IT                        | Jaccard 0.00 | declared=[17644, 147181, 150142] inferred=[51765]
        AS56052  | Zero Point Internet eXchange        | Jaccard 0.00 | declared=[174, 1299, 3356, 8529, 17557, 23764] inferred=[23750]
        AS141733 | Legion Telecom Pty Ltd              | Jaccard 0.00 | declared=[2764] inferred=[141457]
        AS139922 | DISH MEDIA NETWORK PUBLIC LIMITED   | Jaccard 0.00 | declared=[132799] inferred=[38565]
        AS133298 | Netflow broadband Pvt Ltd.          | Jaccard 0.00 | declared=[150593] inferred=[18229]

    ====================================================================================================
     4. REAL ADOPTERS BY RIR
    ====================================================================================================
      ripencc    | 1,988 adopters
      arin       |   768 adopters
      apnic      |   593 adopters
      lacnic     |   184 adopters
      afrinic    |     2 adopters

    ====================================================================================================
     TOP 15 REAL ASPA ADOPTERS BY CONE SIZE
    ====================================================================================================
    ASN      | Country         | Cone     | Verdict              | Name
    ----------------------------------------------------------------------------------------------------
    AS174    | United States   | 74,930   | CORE: ACTIVE PROTECT | Cogent Communications, LLC
    AS7018   | United States   | 72,521   | REGRESSED            | AT&T Enterprises, LLC
    AS1299   | Sweden          | 72,484   | CORE: ACTIVE PROTECT | Arelion (fka. Telia Carrier)
    AS3257   | United States   | 71,749   | CORE: ACTIVE PROTECT | GTT Communications Inc.
    AS3320   | Germany         | 70,808   | CORE: ACTIVE PROTECT | Deutsche Telekom AG
    AS6830   | Netherlands     | 70,729   | CORE: ACTIVE PROTECT | Liberty Global Europe Holding B.V.
    AS33891  | Germany         | 47,014   | ACTIVE LOCAL ROV     | Core-Backbone GmbH
    AS12779  | Italy           | 28,152   | ACTIVE LOCAL ROV     | IT.Gate S.p.A.
    AS34019  | France          | 25,150   | ACTIVE LOCAL ROV     | Hivane Association
    AS25091  | Switzerland     | 19,347   | PASSIVE (Clean Pipe) | IP-Max SA
    AS212024 | France          | 12,971   | VULNERABLE           | Marc Schmitt
    AS56662  | Poland          | 10,611   | PARTIAL: VULNERABLE  | Marcin Gondek
    AS49673  | Russian Federat | 9,425    | PARTIAL: VULNERABLE  | Truenetwork LLC
    AS3303   | Switzerland     | 7,185    | ACTIVE (Atlas Verifi | Swisscom (Schweiz) AG
    AS20764  | Russian Federat | 7,039    | ACTIVE LOCAL ROV     | CJSC RASCOM

    [+] Full cross-reference saved to aspa_real_vs_model.csv
