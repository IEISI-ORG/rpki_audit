    [*] Loading Data...
        - Loading ASN data from packed file... OK (124,499 records)
        - Loading Cones from final_as_rank.csv... OK (87261 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching real ASPA objects from console.rpki-client.org...
        - 3,031 ASNs have a real, published ASPA object

    ====================================================================================================
     1. REAL ASPA ADOPTION (Ground Truth, not a Model)
    ====================================================================================================
    Total audited ASNs:                     122,791
    ASNs with an inferred upstream (customers): 83,855
    ASNs with a real published ASPA object:  3,031 (2.47% of all ASNs, 3.61% of ASNs with a provider to declare)
    Average declared providers per ASPA record: 3.31 (max 225)

    ====================================================================================================
     2. MODEL vs REALITY — 'Ready-to-Sign Giants'
    ====================================================================================================
    Giants (cone > 100) with 100% ROA hygiene and 100% secure upstreams:
      Ready-to-sign giants:     88
      ...who HAVE signed ASPA:  9 (10.2%)
      ...who HAVEN'T yet:       79 (89.8%)

      Top 10 ready-but-unsigned (by cone, actionable outreach targets):
        AS24482  | cone 64,668  | SG.GS
        AS37721  | cone 50,259  | Virtual Technologies & Solutions
        AS17639  | cone 43,286  | Converge ICT Solutions Inc.
        AS48362  | cone 35,887  | Stadtwerke Feldkirch
        AS34549  | cone 34,653  | meerfarbig GmbH & Co. KG
        AS35280  | cone 34,243  | F5 Networks SARL
        AS34927  | cone 34,017  | iFog GmbH
        AS20473  | cone 20,592  | The Constant Company, LLC
        AS15830  | cone 15,000  | Equinix, Inc.
        AS50304  | cone 14,780  | Blix Solutions AS

    ====================================================================================================
     3. TOPOLOGY VALIDATION — Declared ASPA Providers vs Our Inferred Upstreams
    ====================================================================================================
    For ASNs where we have BOTH a real ASPA declaration and an inferred upstream set:
      ASNs comparable (both declared and inferred data exist): 2,581
      Exact match (Jaccard = 1.0):    835 (32.4%)
      Mean Jaccard overlap:           0.602
      Median Jaccard overlap:         0.500

      Biggest mismatches (declared vs inferred providers disagree most):
        AS264096 | RG PROVIDER LTDA ME                 | Jaccard 0.00 | declared=[263482] inferred=[6939]
        AS263331 | Netvox Telecomunicacoes LTDA        | Jaccard 0.00 | declared=[174, 2914, 3356, 6762] inferred=[52838]
        AS263321 | ILOGNET PROVEDOR                    | Jaccard 0.00 | declared=[14840, 265390, 270867] inferred=[6939]
        AS266156 | SERVICOS DE COMUNICACAO LTDA        | Jaccard 0.00 | declared=[16735, 52817, 52863, 61696, 61895, 262979] inferred=[6939]
        AS2716   | Universidade Federal do Rio Grande  | Jaccard 0.00 | declared=[1916] inferred=[4230, 16735, 28343]
        AS269265 | Cyber Link                          | Jaccard 0.00 | declared=[52872] inferred=[266020]
        AS150697 | S N FIBER                           | Jaccard 0.00 | declared=[136969] inferred=[139088]
        AS24550  | Websurfer Nepal Internet Service Pr | Jaccard 0.00 | declared=[141047] inferred=[14789]
        AS45814  | Fariya Networks Pvt. Ltd.           | Jaccard 0.00 | declared=[139879] inferred=[24499]
        AS18025  | Bhutan Telecom Ltd                  | Jaccard 0.00 | declared=[18024] inferred=[17660]

    ====================================================================================================
     4. REAL ADOPTERS BY RIR
    ====================================================================================================
      ripencc    | 1,809 adopters
      arin       |   681 adopters
      apnic      |   393 adopters
      lacnic     |   146 adopters
      afrinic    |     2 adopters

    ====================================================================================================
     TOP 15 REAL ASPA ADOPTERS BY CONE SIZE
    ====================================================================================================
    ASN      | CC | Cone     | Verdict              | Name
    ------------------------------------------------------------------------------------------
    AS174    | US | 73,560   | CORE: ACTIVE PROTECT | Cogent Communications, LLC
    AS1299   | SE | 71,086   | CORE: ACTIVE PROTECT | Arelion (fka. Telia Carrier)
    AS3257   | US | 68,432   | CORE: ACTIVE PROTECT | GTT Communications Inc.
    AS7018   | US | 67,122   | CORE: ACTIVE PROTECT | AT&T Enterprises, LLC
    AS3320   | DE | 66,965   | CORE: ACTIVE PROTECT | Deutsche Telekom AG
    AS6830   | NL | 56,800   | CORE: ACTIVE PROTECT | Liberty Global Europe Holding B.V.
    AS33891  | DE | 36,364   | PARTIAL: VULNERABLE  | Core-Backbone GmbH
    AS12779  | IT | 28,249   | PARTIAL: VULNERABLE  | IT.Gate S.p.A.
    AS34019  | FR | 27,269   | ACTIVE LOCAL ROV     | Hivane Association
    AS56662  | PL | 16,975   | PASSIVE (Clean Pipe) | Marcin Gondek
    AS212024 | FR | 13,405   | PASSIVE (Clean Pipe) | Marc Schmitt
    AS20764  | RU | 9,321    | ACTIVE LOCAL ROV     | CJSC RASCOM
    AS49673  | RU | 9,213    | PASSIVE (Clean Pipe) | Truenetwork LLC
    AS3303   | CH | 8,966    | PARTIAL: VULNERABLE  | Swisscom (Schweiz) AG
    AS204092 | FR | 3,871    | PARTIAL: VULNERABLE  | Association GRIFON

    [+] Full cross-reference saved to aspa_real_vs_model.csv
