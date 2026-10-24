    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (87912 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (125,524 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | DE | 47131    | NOT SIGNED (ROV LOCAL)     |   0.0%  | Core-Backbone GmbH
    AS48185  | BE | 29289    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | team.blue NV
    AS56662  | PL | 10719    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Marcin Gondek
    AS16735  | BR | 2529     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Algar Telecom
    AS1031   | US | 1266     | NOT SIGNED (ROV PARTIAL)   |   0.0%  | PEER 1031 LLC
    AS35598  | RU | 921      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | INETCOM CARRIER LLC
    AS4635   | HK | 817      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | HKIX Route Servers
    AS62255  | SI | 742      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | BiMajLink d.o.o.
    AS205794 | CN | 304      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JINZE YANG
    AS62081  | PL | 276      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Stowarzyszenie e-Poludnie
    AS8732   | RU | 211      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JSC Comcor
    AS11664  | AR | 204      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Techtel LMDS Comunicaciones Interactivas S.A.
    AS41051  | CH | 124      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Freetransit Project (Openfactory GmbH)
    AS52554  | BR | 104      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Rede MegasNet Telecomunicações
    AS31242  | PL | 90       | NOT SIGNED (ROV LOCAL)     |   0.0%  | P4 Sp. z o.o.

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS6461   | US | 74006    | 100.0%  | Zayo Bandwidth
    AS6453   | US | 71624    | 100.0%  | TATA Communications (America) Inc
    AS6762   | IT | 71093    | 100.0%  | Telecom Italia Sparkle (Seabone)
    AS17639  | PH | 43350    |  97.5%  | Converge ICT Solutions Inc.
    AS4657   | SG | 15499    |  99.9%  | StarHub Ltd
    AS12389  | RU | 13486    |  99.2%  | PJSC Rostelecom
    AS1836   | CH | 13457    |  99.9%  | green.ch AG
    AS212024 | FR | 13403    | 100.0%  | Marc Schmitt
    AS20766  | FR | 12463    |  96.7%  | Association "Gitoyen"
    AS38001  | SG | 6129     | 100.0%  | NewMedia Express Pte. Ltd.
    AS15830  | NL | 3203     | 100.0%  | Equinix, Inc.
    AS9930   | MY | 2918     |  99.7%  | TIME dotCom Bhd
    AS42708  | SE | 2881     | 100.0%  | Glesys AB
    AS4755   | IN | 2584     | 100.0%  | TATA Communications (formerly VSNL)
    AS401753 | VG | 2456     | 100.0%  | BIXCE Inc

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
    AS1299   | SE | 72705    | 21.75              | Arelion (fka. Telia Carrier)
    AS3356   | US | 76266    | 21.56              | Lumen (Level 3)
    AS174    | US | 75151    | 21.48              | Cogent Communications, LLC
    AS3257   | US | 71885    | 21.36              | GTT Communications Inc.
    AS6939   | US | 70809    | 21.31              | Hurricane Electric LLC
    AS6453   | US | 71624    | 21.30              | TATA Communications (America) Inc
    AS6762   | IT | 71093    | 21.19              | Telecom Italia Sparkle (Seabone)
    AS6461   | US | 74006    | 21.15              | Zayo Bandwidth
    AS2914   | US | 71914    | 21.14              | NTT America, Inc.
    AS3491   | HK | 71205    | 21.06              | PCCW Global (HK) Ltd.
    AS5511   | FR | 71045    | 21.01              | Orange S.A.
    AS12956  | ES | 71039    | 20.95              | Telxius (Telefonica Global)
    AS9002   | GB | 48512    | 20.91              | RETN Limited
    AS701    | US | 71846    | 20.89              | Verizon Business
    AS4637   | HK | 5611     | 20.87              | Telstra International Limited
    AS3320   | DE | 70940    | 20.83              | Deutsche Telekom AG
    AS8220   | GB | 6840     | 20.80              | COLT
    AS7473   | SG | 376      | 20.76              | Singapore Telecommunications Ltd
    AS22356  | BR | 86       | 20.76              | Durand do Brasil Ltda
    AS1273   | EU | 500      | 20.75              | Vodafone Group PLC
    AS7713   | ID | 3331     | 20.74              | PT Telkom Indonesia Tbk
    AS8966   | AE | 2290     | 20.70              | Etisalat (E&)
    AS16735  | BR | 2529     | 20.60              | Algar Telecom
    AS23764  | HK | 1013     | 20.52              | China Telecom Global
    AS12389  | RU | 13486    | 20.42              | PJSC Rostelecom

    [+] Saved strategy to roa_strategy_weighted_v2.csv
