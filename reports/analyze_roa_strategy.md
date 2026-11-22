    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (88077 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (126,094 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | DE | 46034    | NOT SIGNED (ROV LOCAL)     |   0.0%  | Core-Backbone GmbH
    AS48185  | BE | 29277    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | team.blue NV
    AS29632  | DE | 27985    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Netassist International EOOD
    AS56662  | PL | 11963    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Marcin Gondek
    AS16735  | BR | 1956     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Algar Telecom
    AS1031   | US | 1379     | NOT SIGNED (ROV PARTIAL)   |   0.0%  | PEER 1031 LLC
    AS35598  | RU | 1000     | NOT SIGNED (ROV PARTIAL)   |   0.0%  | INETCOM CARRIER LLC
    AS4635   | HK | 750      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | HKIX Route Servers
    AS62255  | SI | 698      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | BiMajLink d.o.o.
    AS205794 | CN | 359      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JINZE YANG
    AS7738   | BR | 337      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | V.tal (fka Telemar)
    AS62081  | PL | 277      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Stowarzyszenie e-Poludnie
    AS11664  | AR | 203      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Techtel LMDS Comunicaciones Interactivas S.A.
    AS41051  | CH | 163      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Freetransit Project (Openfactory GmbH)
    AS52554  | BR | 99       | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Rede MegasNet Telecomunicações

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS6461   | US | 74093    | 100.0%  | Zayo Bandwidth
    AS17639  | PH | 42701    |  97.3%  | Converge ICT Solutions Inc.
    AS204457 | TR | 40974    | 100.0%  | Atlantis Telekomunikasyon Bilisim Hizmetleri 
    AS1836   | CH | 13302    |  99.9%  | green.ch AG
    AS12389  | RU | 12304    |  99.1%  | PJSC Rostelecom
    AS38001  | SG | 6033     | 100.0%  | NewMedia Express Pte. Ltd.
    AS15830  | NL | 3352     | 100.0%  | Equinix, Inc.
    AS42708  | SE | 2959     | 100.0%  | Glesys AB
    AS401753 | VG | 2710     | 100.0%  | BIXCE Inc
    AS4755   | IN | 2592     | 100.0%  | TATA Communications (formerly VSNL)
    AS9930   | MY | 1852     |  99.7%  | TIME dotCom Bhd
    AS53062  | BR | 1757     |  97.2%  | ACESSOLINE TELECOMUNICACOES LTDA
    AS29504  | CZ | 1283     | 100.0%  | Freenet Liberec, z.s.
    AS58717  | BD | 1154     | 100.0%  | Summit Communications Ltd
    AS59919  | IT | 1042     | 100.0%  | Brainbox S.r.l.

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
    AS1299   | SE | 72810    | 21.70              | Arelion (fka. Telia Carrier)
    AS3356   | US | 76341    | 21.51              | Lumen (Level 3)
    AS174    | US | 75247    | 21.47              | Cogent Communications, LLC
    AS6453   | US | 71716    | 21.31              | TATA Communications (America) Inc
    AS3257   | US | 72153    | 21.29              | GTT Communications Inc.
    AS6939   | US | 70880    | 21.21              | Hurricane Electric LLC
    AS2914   | US | 72251    | 21.17              | NTT America, Inc.
    AS6461   | US | 74093    | 21.12              | Zayo Bandwidth
    AS6762   | IT | 71146    | 21.10              | Telecom Italia Sparkle (Seabone)
    AS9002   | GB | 44905    | 20.96              | RETN Limited
    AS3491   | HK | 71394    | 20.95              | PCCW Global (HK) Ltd.
    AS5511   | FR | 71205    | 20.95              | Orange S.A.
    AS12956  | ES | 71429    | 20.87              | Telxius (Telefonica Global)
    AS4637   | HK | 5503     | 20.82              | Telstra International Limited
    AS7713   | ID | 3479     | 20.82              | PT Telkom Indonesia Tbk
    AS8966   | AE | 7006     | 20.69              | Etisalat (E&)
    AS16735  | BR | 1956     | 20.69              | Algar Telecom
    AS23764  | HK | 1529     | 20.64              | China Telecom Global
    AS3320   | DE | 71101    | 20.31              | Deutsche Telekom AG
    AS701    | US | 72227    | 20.10              | Verizon Business
    AS37468  | AO | 934      | 20.00              | Angola Cables
    AS5405   | DE | 3343     | 19.96              | Inter.link GmbH
    AS31133  | RU | 2885     | 19.94              | PJSC MegaFon
    AS12389  | RU | 12304    | 19.91              | PJSC Rostelecom
    AS22356  | BR | 83       | 19.88              | Durand do Brasil Ltda

    [+] Saved strategy to roa_strategy_weighted_v2.csv
