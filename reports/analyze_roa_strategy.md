    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (87904 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (125,950 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | DE | 46803    | NOT SIGNED (ROV LOCAL)     |   0.0%  | Core-Backbone GmbH
    AS48185  | BE | 29778    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | team.blue NV
    AS29632  | DE | 28352    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Netassist International EOOD
    AS56662  | PL | 12316    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Marcin Gondek
    AS16735  | BR | 1949     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Algar Telecom
    AS1031   | US | 1341     | NOT SIGNED (ROV PARTIAL)   |   0.0%  | PEER 1031 LLC
    AS35598  | RU | 1021     | NOT SIGNED (ROV PARTIAL)   |   0.0%  | INETCOM CARRIER LLC
    AS4635   | HK | 744      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | HKIX Route Servers
    AS62255  | SI | 740      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | BiMajLink d.o.o.
    AS62081  | PL | 275      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Stowarzyszenie e-Poludnie
    AS8732   | RU | 230      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JSC Comcor
    AS11664  | AR | 202      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Techtel LMDS Comunicaciones Interactivas S.A.
    AS205794 | CN | 133      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JINZE YANG
    AS41051  | CH | 123      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Freetransit Project (Openfactory GmbH)
    AS52554  | BR | 104      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Rede MegasNet Telecomunicações

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS174    | US | 75065    | 100.0%  | Cogent Communications, LLC
    AS6461   | US | 73917    | 100.0%  | Zayo Bandwidth
    AS17639  | PH | 42697    |  97.1%  | Converge ICT Solutions Inc.
    AS4657   | SG | 15955    |  99.9%  | StarHub Ltd
    AS1836   | CH | 14269    | 100.0%  | green.ch AG
    AS12389  | RU | 12793    |  99.2%  | PJSC Rostelecom
    AS38001  | SG | 6118     | 100.0%  | NewMedia Express Pte. Ltd.
    AS13030  | CH | 4985     |  95.6%  | Init7 (Switzerland) Ltd.
    AS15830  | NL | 3623     | 100.0%  | Equinix, Inc.
    AS7713   | ID | 3284     | 100.0%  | PT Telkom Indonesia Tbk
    AS42708  | SE | 2926     | 100.0%  | Glesys AB
    AS4755   | IN | 2629     | 100.0%  | TATA Communications (formerly VSNL)
    AS401753 | VG | 2601     | 100.0%  | BIXCE Inc
    AS9304   | HK | 2457     | 100.0%  | HGC Global Communications Limited
    AS14840  | BR | 2010     | 100.0%  | BR.DIGITAL 

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
    AS1299   | SE | 72631    | 21.69              | Arelion (fka. Telia Carrier)
    AS3356   | US | 76152    | 21.50              | Lumen (Level 3)
    AS174    | US | 75065    | 21.46              | Cogent Communications, LLC
    AS3257   | US | 71895    | 21.30              | GTT Communications Inc.
    AS6453   | US | 71557    | 21.28              | TATA Communications (America) Inc
    AS6939   | US | 70802    | 21.22              | Hurricane Electric LLC
    AS6461   | US | 73917    | 21.13              | Zayo Bandwidth
    AS6762   | IT | 71090    | 21.11              | Telecom Italia Sparkle (Seabone)
    AS2914   | US | 71827    | 21.09              | NTT America, Inc.
    AS3491   | HK | 71168    | 20.97              | PCCW Global (HK) Ltd.
    AS5511   | FR | 71044    | 20.91              | Orange S.A.
    AS12956  | ES | 71046    | 20.87              | Telxius (Telefonica Global)
    AS3320   | DE | 70941    | 20.87              | Deutsche Telekom AG
    AS9002   | GB | 44969    | 20.87              | RETN Limited
    AS4637   | HK | 5550     | 20.82              | Telstra International Limited
    AS8220   | GB | 6902     | 20.77              | COLT
    AS4755   | IN | 2629     | 20.77              | TATA Communications (formerly VSNL)
    AS9583   | IN | 538      | 20.74              | Sify Limited
    AS1273   | EU | 489      | 20.74              | Vodafone Group PLC
    AS7473   | SG | 349      | 20.73              | Singapore Telecommunications Ltd
    AS16735  | BR | 1949     | 20.72              | Algar Telecom
    AS7713   | ID | 3284     | 20.68              | PT Telkom Indonesia Tbk
    AS8966   | AE | 2710     | 20.68              | Etisalat (E&)
    AS23764  | HK | 1542     | 20.64              | China Telecom Global
    AS701    | US | 71844    | 20.24              | Verizon Business

    [+] Saved strategy to roa_strategy_weighted_v2.csv
