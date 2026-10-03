    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (87449 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (125,032 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | DE | 32143    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Core-Backbone GmbH
    AS48185  | BE | 31047    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | team.blue NV
    AS29632  | DE | 29789    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Netassist International EOOD
    AS56662  | PL | 10840    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Marcin Gondek
    AS16735  | BR | 1888     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Algar Telecom
    AS1031   | US | 1198     | NOT SIGNED (ROV PARTIAL)   |   0.0%  | PEER 1031 LLC
    AS201054 | PL | 1155     | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Stowarzyszenie e-Poludnie
    AS35598  | RU | 912      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | INETCOM CARRIER LLC
    AS4635   | HK | 812      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | HKIX Route Servers
    AS62255  | SI | 737      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | BiMajLink d.o.o.
    AS50263  | PL | 554      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | A-Systems Sp. z o.o.
    AS10429  | BR | 476      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Vivo (Telefônica Brasil)
    AS24115  | SG | 424      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Equinix IX
    AS7738   | BR | 303      | NOT SIGNED (ROV LOCAL)     |   0.0%  | V.tal (fka Telemar)
    AS62081  | PL | 275      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Stowarzyszenie e-Poludnie

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS6461   | US | 72157    | 100.0%  | Zayo Bandwidth
    AS2914   | US | 68901    | 100.0%  | NTT America, Inc.
    AS37721  | BF | 58323    | 100.0%  | Virtual Technologies & Solutions
    AS4837   | CN | 46767    |  99.2%  | China Unicom Backbone
    AS17639  | PH | 41743    |  97.5%  | Converge ICT Solutions Inc.
    AS34927  | CH | 33526    | 100.0%  | iFog GmbH
    AS15830  | NL | 15640    | 100.0%  | Equinix, Inc.
    AS1836   | CH | 12842    |  99.9%  | green.ch AG
    AS20766  | FR | 12333    |  96.7%  | Association "Gitoyen"
    AS38001  | SG | 6689     | 100.0%  | NewMedia Express Pte. Ltd.
    AS52468  | PA | 5951     | 100.0%  | UFINET PANAMA S.A.
    AS9304   | HK | 5297     | 100.0%  | HGC Global Communications Limited
    AS31133  | RU | 3378     |  99.8%  | MegaFon PJSC
    AS4755   | IN | 2235     | 100.0%  | TATA Communications (formerly VSNL)
    AS42708  | SE | 2198     | 100.0%  | Glesys AB

    ===============================================================================================
    3. WEIGHTED OUTREACH TARGETS
       Metric = log(Signing Opportunity,2)
       Signing Opportunity = sum over downstream customers of (100 - signed_pct) —
       partial credit, not a binary unsigned/signed cutoff: a 0%-signed customer
       contributes 100, a 95%-signed customer contributes only 5. Shown as log10
       to read as an ordinal scale rather than a raw magnitude.
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Opportunity        | Name
    -----------------------------------------------------------------------------------------------
    AS6939   | US | 80174    | 21.67              | Hurricane Electric LLC
    AS3356   | US | 73936    | 21.52              | Lumen (Level 3)
    AS1299   | SE | 71317    | 21.38              | Arelion (fka. Telia Carrier)
    AS174    | US | 73729    | 21.33              | Cogent Communications, LLC
    AS3257   | US | 68984    | 21.30              | GTT Communications Inc.
    AS6461   | US | 72157    | 21.24              | Zayo Bandwidth
    AS4637   | HK | 67289    | 21.20              | Telstra International Limited
    AS2914   | US | 68901    | 21.19              | NTT America, Inc.
    AS6762   | IT | 66265    | 21.17              | Telecom Italia Sparkle (Seabone)
    AS6453   | US | 67661    | 21.13              | TATA Communications (America) Inc
    AS3491   | HK | 67287    | 21.08              | PCCW Global (HK) Ltd.
    AS5511   | FR | 61919    | 21.08              | Orange S.A.
    AS6830   | NL | 62226    | 21.00              | Liberty Global Europe Holding B.V.
    AS12956  | ES | 62352    | 20.99              | Telxius (Telefonica Global)
    AS1273   | EU | 53887    | 20.94              | Vodafone Group PLC
    AS3320   | DE | 67133    | 20.93              | Deutsche Telekom AG
    AS4134   | CN | 51855    | 20.87              | China Telecom Backbone
    AS9002   | GB | 46998    | 20.77              | RETN Limited
    AS701    | US | 68285    | 20.43              | Verizon Business
    AS4837   | CN | 46767    | 20.17              | China Unicom Backbone
    AS7713   | ID | 3292     | 20.02              | PT Telkom Indonesia Tbk
    AS4809   | CN | 65543    | 19.61              | China Telecom Next Generation Carri
    AS7922   | US | 27506    | 19.46              | Comcast Cable Communications, LLC
    AS20485  | RU | 34809    | 19.36              | TransTeleCom JSC
    AS34927  | CH | 33526    | 19.32              | iFog GmbH

    [+] Saved strategy to roa_strategy_weighted_v2.csv
