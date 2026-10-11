    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (87459 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (125,153 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | DE | 46961    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Core-Backbone GmbH
    AS48185  | BE | 30323    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | team.blue NV
    AS29632  | DE | 30002    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Netassist International EOOD
    AS56662  | PL | 10864    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Marcin Gondek
    AS16735  | BR | 2262     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Algar Telecom
    AS1031   | US | 1202     | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | PEER 1031 LLC
    AS201054 | PL | 1167     | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Stowarzyszenie e-Poludnie
    AS35598  | RU | 902      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | INETCOM CARRIER LLC
    AS62255  | SI | 744      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | BiMajLink d.o.o.
    AS4635   | HK | 721      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | HKIX Route Servers
    AS10429  | BR | 462      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Vivo (Telefônica Brasil)
    AS24115  | SG | 387      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Equinix IX
    AS7738   | BR | 352      | NOT SIGNED (ROV LOCAL)     |   0.0%  | V.tal (fka Telemar)
    AS205794 | CN | 316      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JINZE YANG
    AS62081  | PL | 275      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Stowarzyszenie e-Poludnie

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS6461   | US | 71946    | 100.0%  | Zayo Bandwidth
    AS37721  | BF | 58312    | 100.0%  | Virtual Technologies & Solutions
    AS4837   | CN | 50577    |  99.4%  | China Unicom Backbone
    AS17639  | PH | 43147    |  97.7%  | Converge ICT Solutions Inc.
    AS34927  | CH | 34226    | 100.0%  | iFog GmbH
    AS4657   | SG | 15296    |  99.9%  | StarHub Ltd
    AS1836   | CH | 13023    |  99.9%  | green.ch AG
    AS20766  | FR | 12332    |  96.7%  | Association "Gitoyen"
    AS38001  | SG | 6112     | 100.0%  | NewMedia Express Pte. Ltd.
    AS15830  | NL | 3668     | 100.0%  | Equinix, Inc.
    AS42708  | SE | 2899     | 100.0%  | Glesys AB
    AS4755   | IN | 2547     | 100.0%  | TATA Communications (formerly VSNL)
    AS9304   | HK | 2178     | 100.0%  | HGC Global Communications Limited
    AS53062  | BR | 1557     |  96.4%  | ACESSOLINE TELECOMUNICACOES LTDA
    AS8447   | AT | 1080     |  99.3%  | A1 Telekom Austria AG

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
    AS6939   | US | 80275    | 21.66              | Hurricane Electric LLC
    AS3356   | US | 74030    | 21.50              | Lumen (Level 3)
    AS1299   | SE | 71458    | 21.36              | Arelion (fka. Telia Carrier)
    AS174    | US | 73849    | 21.32              | Cogent Communications, LLC
    AS3257   | US | 69123    | 21.27              | GTT Communications Inc.
    AS6461   | US | 71946    | 21.22              | Zayo Bandwidth
    AS2914   | US | 68933    | 21.17              | NTT America, Inc.
    AS4637   | HK | 67304    | 21.17              | Telstra International Limited
    AS6762   | IT | 66665    | 21.14              | Telecom Italia Sparkle (Seabone)
    AS6453   | US | 67808    | 21.12              | TATA Communications (America) Inc
    AS5511   | FR | 62306    | 21.07              | Orange S.A.
    AS3491   | HK | 67288    | 21.06              | PCCW Global (HK) Ltd.
    AS12956  | ES | 62395    | 20.96              | Telxius (Telefonica Global)
    AS1273   | EU | 63250    | 20.94              | Vodafone Group PLC
    AS6830   | NL | 62811    | 20.92              | Liberty Global Europe Holding B.V.
    AS3320   | DE | 67344    | 20.88              | Deutsche Telekom AG
    AS4134   | CN | 52552    | 20.84              | China Telecom Backbone
    AS9002   | GB | 48162    | 20.76              | RETN Limited
    AS701    | US | 68265    | 20.41              | Verizon Business
    AS7713   | ID | 3441     | 20.01              | PT Telkom Indonesia Tbk
    AS4837   | CN | 50577    | 19.92              | China Unicom Backbone
    AS4809   | CN | 65220    | 19.51              | China Telecom Next Generation Carri
    AS7922   | US | 26233    | 19.44              | Comcast Cable Communications, LLC
    AS34927  | CH | 34226    | 19.29              | iFog GmbH
    AS20485  | RU | 34039    | 19.27              | TransTeleCom JSC

    [+] Saved strategy to roa_strategy_weighted_v2.csv
