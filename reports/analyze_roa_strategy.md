    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (88086 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (125,651 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | DE | 46645    | NOT SIGNED (ROV LOCAL)     |   0.0%  | Core-Backbone GmbH
    AS29632  | DE | 29955    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Netassist International EOOD
    AS48185  | BE | 29868    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | team.blue NV
    AS56662  | PL | 10929    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Marcin Gondek
    AS16735  | BR | 2315     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Algar Telecom
    AS1031   | US | 1300     | NOT SIGNED (ROV PARTIAL)   |   0.0%  | PEER 1031 LLC
    AS35598  | RU | 910      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | INETCOM CARRIER LLC
    AS4635   | HK | 809      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | HKIX Route Servers
    AS62255  | SI | 758      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | BiMajLink d.o.o.
    AS205794 | CN | 335      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JINZE YANG
    AS62081  | PL | 279      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Stowarzyszenie e-Poludnie
    AS8732   | RU | 209      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JSC Comcor
    AS11664  | AR | 205      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Techtel LMDS Comunicaciones Interactivas S.A.
    AS41051  | CH | 144      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Freetransit Project (Openfactory GmbH)
    AS52554  | BR | 107      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Rede MegasNet Telecomunicações

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS6461   | US | 74170    | 100.0%  | Zayo Bandwidth
    AS2914   | US | 72072    | 100.0%  | NTT America, Inc.
    AS17639  | PH | 43018    |  97.3%  | Converge ICT Solutions Inc.
    AS4657   | SG | 15334    |  99.9%  | StarHub Ltd
    AS1836   | CH | 13789    |  99.9%  | green.ch AG
    AS20766  | FR | 12639    |  96.7%  | Association "Gitoyen"
    AS12389  | RU | 12329    |  99.2%  | PJSC Rostelecom
    AS38001  | SG | 6373     | 100.0%  | NewMedia Express Pte. Ltd.
    AS15830  | NL | 3230     | 100.0%  | Equinix, Inc.
    AS42708  | SE | 2898     | 100.0%  | Glesys AB
    AS4755   | IN | 2658     | 100.0%  | TATA Communications (formerly VSNL)
    AS401753 | VG | 2464     | 100.0%  | BIXCE Inc
    AS14840  | BR | 2246     | 100.0%  | BR.DIGITAL 
    AS20562  | NL | 1932     | 100.0%  | Open Peering (Broadband Hosting B.V.)
    AS53062  | BR | 1565     |  97.2%  | ACESSOLINE TELECOMUNICACOES LTDA

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
    AS1299   | SE | 72867    | 21.71              | Arelion (fka. Telia Carrier)
    AS3356   | US | 76412    | 21.52              | Lumen (Level 3)
    AS174    | US | 75321    | 21.48              | Cogent Communications, LLC
    AS3257   | US | 72125    | 21.31              | GTT Communications Inc.
    AS6453   | US | 71790    | 21.31              | TATA Communications (America) Inc
    AS6939   | US | 71053    | 21.26              | Hurricane Electric LLC
    AS6461   | US | 74170    | 21.16              | Zayo Bandwidth
    AS2914   | US | 72072    | 21.14              | NTT America, Inc.
    AS6762   | IT | 71341    | 21.14              | Telecom Italia Sparkle (Seabone)
    AS3491   | HK | 71475    | 21.02              | PCCW Global (HK) Ltd.
    AS5511   | FR | 71288    | 20.94              | Orange S.A.
    AS12956  | ES | 71283    | 20.94              | Telxius (Telefonica Global)
    AS3320   | DE | 71190    | 20.93              | Deutsche Telekom AG
    AS701    | US | 72082    | 20.92              | Verizon Business
    AS9002   | GB | 48683    | 20.90              | RETN Limited
    AS4637   | HK | 5651     | 20.88              | Telstra International Limited
    AS8220   | GB | 7286     | 20.83              | COLT
    AS4755   | IN | 2658     | 20.83              | TATA Communications (formerly VSNL)
    AS9583   | IN | 560      | 20.80              | Sify Limited
    AS1273   | EU | 490      | 20.80              | Vodafone Group PLC
    AS7473   | SG | 383      | 20.79              | Singapore Telecommunications Ltd
    AS33891  | DE | 46645    | 20.78              | Core-Backbone GmbH
    AS16735  | BR | 2315     | 20.78              | Algar Telecom
    AS9498   | IN | 7867     | 20.77              | Bharti Airtel Ltd.
    AS8966   | AE | 2621     | 20.75              | Etisalat (E&)

    [+] Saved strategy to roa_strategy_weighted_v2.csv
