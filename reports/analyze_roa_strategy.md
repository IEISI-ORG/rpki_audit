    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (87261 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (124,499 records)

    ===============================================================================================
    1. SECURE PROVIDERS, UNSIGNED ROUTES
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS48185  | BE | 30588    |   0.0%  | team.blue NV
    AS29632  | DE | 30481    |   0.0%  | Netassist International EOOD
    AS56662  | PL | 16975    |   0.0%  | Marcin Gondek
    AS16735  | BR | 1979     |   0.0%  | Algar Telecom
    AS201054 | PL | 1348     |   0.0%  | Stowarzyszenie e-Poludnie
    AS1031   | US | 1274     |   0.0%  | PEER 1031 LLC
    AS46887  | US | 1182     |   0.3%  | Zayo (fka. Crown Castle)
    AS3549   | US | 454      |   1.0%  | Lumen (fka. Global Crossing)
    AS10429  | BR | 435      |   0.0%  | Vivo (Telefônica Brasil)
    AS209    | US | 394      |   1.3%  | Lumen (ex. Qwest)
    AS2764   | AU | 344      |   0.8%  | AAPT Limited
    AS62081  | PL | 279      |   0.0%  | Stowarzyszenie e-Poludnie
    AS263009 | BR | 232      |   0.0%  | FORTE TELECOM LTDA.
    AS28368  | BR | 208      |   0.0%  | Wirelink (Sobralnet)
    AS11664  | AR | 197      |   0.0%  | Techtel LMDS Comunicaciones Interactivas S.A.

    ===============================================================================================
    2. FULLY SIGNED, VULNERABLE VERDICT
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS37721  | BF | 50259    | 100.0%  | Virtual Technologies & Solutions
    AS4837   | CN | 48116    |  99.4%  | China Unicom Backbone
    AS17639  | PH | 43286    |  97.5%  | Converge ICT Solutions Inc.
    AS48362  | AT | 35887    | 100.0%  | Stadtwerke Feldkirch
    AS15830  | NL | 15000    | 100.0%  | Equinix, Inc.
    AS1836   | CH | 13001    |  99.9%  | green.ch AG
    AS38001  | SG | 7856     | 100.0%  | NewMedia Express Pte. Ltd.
    AS4755   | IN | 2482     | 100.0%  | TATA Communications (formerly VSNL)
    AS9304   | HK | 2406     | 100.0%  | HGC Global Communications Limited
    AS42708  | SE | 2169     | 100.0%  | Glesys AB
    AS53062  | BR | 1733     |  96.4%  | GGNET TELECOMUNICACOES LTDA
    AS64073  | NZ | 1689     | 100.0%  | Vetta Group
    AS58717  | BD | 1293     | 100.0%  | Summit Communications Ltd
    AS14789  | US | 1197     | 100.0%  | Cloudflare, Inc.
    AS59919  | IT | 1057     | 100.0%  | Brainbox S.r.l.

    ===============================================================================================
    3. WEIGHTED OUTREACH TARGETS
       Metric = (Provider Cone Size) * (Count of Unsigned Customers)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Unsigned | Impact Score   | Name
    -----------------------------------------------------------------------------------------------
    AS6939   | US | 80006    | 31566    | 2,525,469,396  | Hurricane Electric LLC
    AS3356   | US | 73731    | 28159    | 2,076,191,229  | Lumen (Level 3)
    AS174    | US | 73560    | 24750    | 1,820,610,000  | Cogent Communications, LLC
    AS1299   | SE | 71086    | 25366    | 1,803,167,476  | Arelion (fka. Telia Carrier)
    AS6461   | US | 71623    | 23079    | 1,652,987,217  | Zayo Bandwidth
    AS3257   | US | 68432    | 24021    | 1,643,805,072  | GTT Communications Inc.
    AS2914   | US | 68563    | 21786    | 1,493,713,518  | NTT America, Inc.
    AS4637   | HK | 66936    | 22262    | 1,490,129,232  | Telstra International Limited
    AS6762   | IT | 64955    | 22137    | 1,437,908,835  | Telecom Italia Sparkle (Seabone)
    AS6453   | US | 67382    | 21301    | 1,435,303,982  | TATA Communications (America) Inc
    AS3491   | HK | 66961    | 20627    | 1,381,204,547  | PCCW Global (HK) Ltd.
    AS3320   | DE | 66965    | 18789    | 1,258,205,385  | Deutsche Telekom AG
    AS5511   | FR | 56686    | 20587    | 1,166,994,682  | Orange S.A.
    AS12956  | ES | 59644    | 19257    | 1,148,564,508  | Telxius (Telefonica Global)
    AS1273   | EU | 56947    | 19486    | 1,109,669,242  | Vodafone Group PLC
    AS6830   | NL | 56800    | 19011    | 1,079,824,800  | Liberty Global Europe Holding B.V.
    AS4134   | CN | 50788    | 17882    | 908,191,016    | China Telecom Backbone
    AS701    | US | 66715    | 12317    | 821,728,655    | Verizon Business
    AS9002   | GB | 46326    | 16676    | 772,532,376    | RETN Limited
    AS4837   | CN | 48116    | 11942    | 574,601,272    | China Unicom Backbone
    AS4809   | CN | 64883    | 8025     | 520,686,075    | China Telecom Next Generation Carri
    AS7018   | US | 67122    | 4239     | 284,530,158    | AT&T Enterprises, LLC
    AS33891  | DE | 36364    | 6665     | 242,366,060    | Core-Backbone GmbH
    AS20485  | RU | 34017    | 6692     | 227,641,764    | TransTeleCom JSC
    AS34927  | CH | 34017    | 6412     | 218,117,004    | iFog GmbH

    [+] Saved strategy to roa_strategy_weighted_v2.csv
