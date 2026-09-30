    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (87399 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (124,902 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | DE | 36857    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Core-Backbone GmbH
    AS48185  | BE | 30946    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | team.blue NV
    AS29632  | DE | 29759    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Netassist International EOOD
    AS56662  | PL | 10948    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Marcin Gondek
    AS16735  | BR | 1901     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Algar Telecom
    AS1031   | US | 1298     | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | PEER 1031 LLC
    AS201054 | PL | 1150     | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Stowarzyszenie e-Poludnie
    AS35598  | RU | 913      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | INETCOM CARRIER LLC
    AS62255  | SI | 837      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | BiMajLink d.o.o.
    AS4635   | HK | 836      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | HKIX Route Servers
    AS50263  | PL | 539      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | A-Systems Sp. z o.o.
    AS10429  | BR | 477      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Vivo (Telefônica Brasil)
    AS24115  | SG | 434      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Equinix IX
    AS7738   | BR | 306      | NOT SIGNED (ROV LOCAL)     |   0.0%  | V.tal (fka Telemar)
    AS62081  | PL | 275      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Stowarzyszenie e-Poludnie

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS6461   | US | 71747    | 100.0%  | Zayo Bandwidth
    AS2914   | US | 68809    | 100.0%  | NTT America, Inc.
    AS37721  | BF | 58336    | 100.0%  | Virtual Technologies & Solutions
    AS4837   | CN | 49153    |  99.2%  | China Unicom Backbone
    AS17639  | PH | 42697    |  97.5%  | Converge ICT Solutions Inc.
    AS15830  | NL | 15804    | 100.0%  | Equinix, Inc.
    AS1836   | CH | 12665    |  99.9%  | green.ch AG
    AS20766  | FR | 12419    |  96.7%  | Association "Gitoyen"
    AS38001  | SG | 7831     | 100.0%  | NewMedia Express Pte. Ltd.
    AS52468  | PA | 5786     | 100.0%  | UFINET PANAMA S.A.
    AS31133  | RU | 3431     |  99.8%  | MegaFon PJSC
    AS4755   | IN | 2541     | 100.0%  | TATA Communications (formerly VSNL)
    AS42708  | SE | 2358     | 100.0%  | Glesys AB
    AS9304   | HK | 2338     |  97.7%  | HGC Global Communications Limited
    AS64073  | NZ | 1683     | 100.0%  | Vetta Group

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
    AS6939   | US | 80125    | 21.67              | Hurricane Electric LLC
    AS3356   | US | 73867    | 21.54              | Lumen (Level 3)
    AS174    | US | 73710    | 21.38              | Cogent Communications, LLC
    AS1299   | SE | 71287    | 21.38              | Arelion (fka. Telia Carrier)
    AS6461   | US | 71747    | 21.37              | Zayo Bandwidth
    AS3257   | US | 68849    | 21.30              | GTT Communications Inc.
    AS6762   | IT | 66337    | 21.25              | Telecom Italia Sparkle (Seabone)
    AS4637   | HK | 67179    | 21.20              | Telstra International Limited
    AS2914   | US | 68809    | 21.16              | NTT America, Inc.
    AS6453   | US | 67572    | 21.13              | TATA Communications (America) Inc
    AS5511   | FR | 61995    | 21.08              | Orange S.A.
    AS3491   | HK | 67181    | 21.07              | PCCW Global (HK) Ltd.
    AS1273   | EU | 63121    | 21.00              | Vodafone Group PLC
    AS6830   | NL | 62532    | 21.00              | Liberty Global Europe Holding B.V.
    AS12956  | ES | 62220    | 20.99              | Telxius (Telefonica Global)
    AS3320   | DE | 67206    | 20.94              | Deutsche Telekom AG
    AS4134   | CN | 52098    | 20.87              | China Telecom Backbone
    AS701    | US | 68113    | 20.83              | Verizon Business
    AS9002   | GB | 46994    | 20.78              | RETN Limited
    AS14840  | BR | 1978     | 20.45              | BR.DIGITAL 
    AS4837   | CN | 49153    | 20.35              | China Unicom Backbone
    AS7713   | ID | 2865     | 19.90              | PT Telkom Indonesia Tbk
    AS4809   | CN | 65073    | 19.59              | China Telecom Next Generation Carri
    AS33891  | DE | 36857    | 19.59              | Core-Backbone GmbH
    AS7922   | US | 25889    | 19.40              | Comcast Cable Communications, LLC

    [+] Saved strategy to roa_strategy_weighted_v2.csv
