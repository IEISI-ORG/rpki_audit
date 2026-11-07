    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (87992 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (125,809 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | DE | 46982    | NOT SIGNED (ROV LOCAL)     |   0.0%  | Core-Backbone GmbH
    AS48185  | BE | 30170    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | team.blue NV
    AS56662  | PL | 10290    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Marcin Gondek
    AS16735  | BR | 2159     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Algar Telecom
    AS1031   | US | 1290     | NOT SIGNED (ROV PARTIAL)   |   0.0%  | PEER 1031 LLC
    AS35598  | RU | 951      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | INETCOM CARRIER LLC
    AS62255  | SI | 759      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | BiMajLink d.o.o.
    AS4635   | HK | 754      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | HKIX Route Servers
    AS205794 | CN | 363      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JINZE YANG
    AS62081  | PL | 279      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Stowarzyszenie e-Poludnie
    AS11664  | AR | 203      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Techtel LMDS Comunicaciones Interactivas S.A.
    AS41051  | CH | 145      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Freetransit Project (Openfactory GmbH)
    AS52554  | BR | 101      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Rede MegasNet Telecomunicações
    AS31242  | PL | 90       | NOT SIGNED (ROV LOCAL)     |   0.0%  | P4 Sp. z o.o.
    AS703    | US | 85       | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Verizon Business - APAC

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS6461   | US | 74018    | 100.0%  | Zayo Bandwidth
    AS1299   | SE | 72723    | 100.0%  | Arelion (fka. Telia Carrier)
    AS2914   | US | 71927    | 100.0%  | NTT America, Inc.
    AS17639  | PH | 43433    |  97.3%  | Converge ICT Solutions Inc.
    AS4657   | SG | 16147    |  99.9%  | StarHub Ltd
    AS50304  | NO | 14245    | 100.0%  | Blix Solutions AS
    AS1836   | CH | 13691    |  99.9%  | green.ch AG
    AS12389  | RU | 13429    |  99.2%  | PJSC Rostelecom
    AS20766  | FR | 12335    |  96.7%  | Association "Gitoyen"
    AS38001  | SG | 6081     | 100.0%  | NewMedia Express Pte. Ltd.
    AS15830  | NL | 3441     | 100.0%  | Equinix, Inc.
    AS42708  | SE | 2943     | 100.0%  | Glesys AB
    AS4755   | IN | 2597     | 100.0%  | TATA Communications (formerly VSNL)
    AS401753 | VG | 2485     | 100.0%  | BIXCE Inc
    AS9304   | HK | 2484     | 100.0%  | HGC Global Communications Limited

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
    AS1299   | SE | 72723    | 21.71              | Arelion (fka. Telia Carrier)
    AS3356   | US | 76241    | 21.51              | Lumen (Level 3)
    AS174    | US | 75178    | 21.47              | Cogent Communications, LLC
    AS3257   | US | 71973    | 21.31              | GTT Communications Inc.
    AS6453   | US | 71634    | 21.28              | TATA Communications (America) Inc
    AS6939   | US | 70894    | 21.25              | Hurricane Electric LLC
    AS6461   | US | 74018    | 21.15              | Zayo Bandwidth
    AS2914   | US | 71927    | 21.12              | NTT America, Inc.
    AS6762   | IT | 71186    | 21.12              | Telecom Italia Sparkle (Seabone)
    AS3491   | HK | 71320    | 20.99              | PCCW Global (HK) Ltd.
    AS5511   | FR | 71132    | 20.93              | Orange S.A.
    AS3320   | DE | 71032    | 20.92              | Deutsche Telekom AG
    AS9002   | GB | 45670    | 20.90              | RETN Limited
    AS701    | US | 71933    | 20.89              | Verizon Business
    AS12956  | ES | 71136    | 20.88              | Telxius (Telefonica Global)
    AS4637   | HK | 5625     | 20.87              | Telstra International Limited
    AS8220   | GB | 6615     | 20.83              | COLT
    AS4755   | IN | 2597     | 20.83              | TATA Communications (formerly VSNL)
    AS33891  | DE | 46982    | 20.80              | Core-Backbone GmbH
    AS9583   | IN | 554      | 20.80              | Sify Limited
    AS1273   | EU | 488      | 20.80              | Vodafone Group PLC
    AS7473   | SG | 291      | 20.79              | Singapore Telecommunications Ltd
    AS9498   | IN | 7400     | 20.77              | Bharti Airtel Ltd.
    AS7713   | ID | 3754     | 20.74              | PT Telkom Indonesia Tbk
    AS8966   | AE | 2605     | 20.74              | Etisalat (E&)

    [+] Saved strategy to roa_strategy_weighted_v2.csv
