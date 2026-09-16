    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (87261 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (124,499 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | DE | 36364    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Core-Backbone GmbH
    AS48185  | BE | 30588    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | team.blue NV
    AS29632  | DE | 30481    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Netassist International EOOD
    AS56662  | PL | 16975    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Marcin Gondek
    AS16735  | BR | 1979     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Algar Telecom
    AS201054 | PL | 1348     | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Stowarzyszenie e-Poludnie
    AS1031   | BR | 1274     | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | PEER 1031 LLC
    AS35598  | RU | 893      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | INETCOM CARRIER LLC
    AS4635   | HK | 768      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | HKIX Route Servers
    AS62255  | SI | 690      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | BiMajLink d.o.o.
    AS50263  | PL | 559      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | A-Systems Sp. z o.o.
    AS10429  | BR | 435      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Vivo (Telefônica Brasil)
    AS24115  | SG | 406      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Equinix IX
    AS62081  | PL | 279      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Stowarzyszenie e-Poludnie
    AS263009 | BR | 232      | NOT SIGNED (ROV LOCAL)     |   0.0%  | FORTE TELECOM LTDA.

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS37721  | BF | 50259    | 100.0%  | Virtual Technologies & Solutions
    AS4837   | CN | 48116    |  99.4%  | China Unicom Backbone
    AS17639  | PH | 43286    |  97.5%  | Converge ICT Solutions Inc.
    AS48362  | AT | 35887    | 100.0%  | Stadtwerke Feldkirch
    AS34927  | CH | 34017    | 100.0%  | iFog GmbH
    AS15830  | NL | 15000    | 100.0%  | Equinix, Inc.
    AS1836   | CH | 13001    |  99.9%  | green.ch AG
    AS38001  | SG | 7856     | 100.0%  | NewMedia Express Pte. Ltd.
    AS4755   | IN | 2482     | 100.0%  | TATA Communications (formerly VSNL)
    AS9304   | HK | 2406     | 100.0%  | HGC Global Communications Limited
    AS42708  | SE | 2169     | 100.0%  | Glesys AB
    AS53062  | BR | 1733     |  96.4%  | GGNET TELECOMUNICACOES LTDA
    AS64073  | NZ | 1689     | 100.0%  | Vetta Group
    AS58717  | BD | 1293     | 100.0%  | Summit Communications Ltd
    AS59919  | IT | 1057     | 100.0%  | Brainbox S.r.l.

    ===============================================================================================
    3. WEIGHTED OUTREACH TARGETS
       Metric = log10(Signing Opportunity)
       Signing Opportunity = sum over downstream customers of (100 - signed_pct) —
       partial credit, not a binary unsigned/signed cutoff: a 0%-signed customer
       contributes 100, a 95%-signed customer contributes only 5. Shown as log10
       to read as an ordinal scale rather than a raw magnitude.
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | log10(Opportunity) | Name
    -----------------------------------------------------------------------------------------------
    AS6939   | US | 80006    | 6.53               | Hurricane Electric LLC
    AS3356   | US | 73731    | 6.48               | Lumen (Level 3)
    AS1299   | SE | 71086    | 6.44               | Arelion (fka. Telia Carrier)
    AS174    | US | 73560    | 6.43               | Cogent Communications, LLC
    AS3257   | US | 68432    | 6.41               | GTT Communications Inc.
    AS6461   | US | 71623    | 6.40               | Zayo Bandwidth
    AS4637   | HK | 66936    | 6.38               | Telstra International Limited
    AS6762   | IT | 64955    | 6.38               | Telecom Italia Sparkle (Seabone)
    AS2914   | US | 68563    | 6.37               | NTT America, Inc.
    AS6453   | US | 67382    | 6.36               | TATA Communications (America) Inc
    AS3491   | HK | 66961    | 6.35               | PCCW Global (HK) Ltd.
    AS5511   | FR | 56686    | 6.34               | Orange S.A.
    AS12956  | ES | 59644    | 6.32               | Telxius (Telefonica Global)
    AS1273   | EU | 56947    | 6.32               | Vodafone Group PLC
    AS3320   | DE | 66965    | 6.31               | Deutsche Telekom AG
    AS6830   | NL | 56800    | 6.31               | Liberty Global Europe Holding B.V.
    AS4134   | CN | 50788    | 6.28               | China Telecom Backbone
    AS9002   | GB | 46326    | 6.26               | RETN Limited
    AS701    | US | 66715    | 6.12               | Verizon Business
    AS4837   | CN | 48116    | 6.11               | China Unicom Backbone
    AS7713   | ID | 3221     | 5.99               | PT Telkom Indonesia Tbk
    AS4809   | CN | 64883    | 5.94               | China Telecom Next Generation Carri
    AS33891  | DE | 36364    | 5.86               | Core-Backbone GmbH
    AS20485  | RU | 34017    | 5.86               | TransTeleCom JSC
    AS34927  | CH | 34017    | 5.84               | iFog GmbH

    [+] Saved strategy to roa_strategy_weighted_v2.csv
