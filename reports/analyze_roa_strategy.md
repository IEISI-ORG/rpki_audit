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
       Metric = (Provider Cone Size) * (Signing Opportunity)
       Signing Opportunity = sum over downstream customers of (100 - signed_pct) —
       partial credit, not a binary unsigned/signed cutoff: a 0%-signed customer
       contributes 100, a 95%-signed customer contributes only 5.
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Opportunity | Impact Score   | Name
    -----------------------------------------------------------------------------------------------
    AS6939   | US | 80006    | 3,354,041.0 | 268,343,404,246 | Hurricane Electric LLC
    AS3356   | US | 73731    | 3,015,225.3 | 222,315,576,594 | Lumen (Level 3)
    AS174    | US | 73560    | 2,661,902.4 | 195,809,540,544 | Cogent Communications, LLC
    AS1299   | SE | 71086    | 2,724,965.1 | 193,706,869,099 | Arelion (fka. Telia Carrier)
    AS6461   | US | 71623    | 2,484,454.5 | 177,944,084,653 | Zayo Bandwidth
    AS3257   | US | 68432    | 2,578,560.0 | 176,456,017,920 | GTT Communications Inc.
    AS2914   | US | 68563    | 2,343,632.1 | 160,686,447,672 | NTT America, Inc.
    AS4637   | HK | 66936    | 2,390,075.9 | 159,982,120,442 | Telstra International Limited
    AS6762   | IT | 64955    | 2,376,018.0 | 154,334,249,190 | Telecom Italia Sparkle (Seabone)
    AS6453   | US | 67382    | 2,288,846.0 | 154,227,021,172 | TATA Communications (America) Inc
    AS3491   | HK | 66961    | 2,218,065.5 | 148,523,883,946 | PCCW Global (HK) Ltd.
    AS3320   | DE | 66965    | 2,023,446.6 | 135,500,101,569 | Deutsche Telekom AG
    AS5511   | FR | 56686    | 2,210,253.6 | 125,290,435,570 | Orange S.A.
    AS12956  | ES | 59644    | 2,073,049.4 | 123,644,958,414 | Telxius (Telefonica Global)
    AS1273   | EU | 56947    | 2,095,196.0 | 119,315,126,612 | Vodafone Group PLC
    AS6830   | NL | 56800    | 2,046,711.7 | 116,253,224,560 | Liberty Global Europe Holding B.V.
    AS4134   | CN | 50788    | 1,925,941.9 | 97,814,737,217 | China Telecom Backbone
    AS701    | US | 66715    | 1,323,349.6 | 88,287,268,564 | Verizon Business
    AS9002   | GB | 46326    | 1,799,561.0 | 83,366,462,886 | RETN Limited
    AS4837   | CN | 48116    | 1,289,169.9 | 62,029,698,908 | China Unicom Backbone
    AS4809   | CN | 64883    | 870,372.7   | 56,472,391,894 | China Telecom Next Generation Carri
    AS7018   | US | 67122    | 455,950.8   | 30,604,329,598 | AT&T Enterprises, LLC
    AS33891  | DE | 36364    | 724,283.1   | 26,337,830,648 | Core-Backbone GmbH
    AS20485  | RU | 34017    | 725,288.7   | 24,672,145,708 | TransTeleCom JSC
    AS34927  | CH | 34017    | 693,867.5   | 23,603,290,747 | iFog GmbH

    [+] Saved strategy to roa_strategy_weighted_v2.csv
