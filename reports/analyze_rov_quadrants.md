    [*] Loading Data...
        - Loading Cones from final_as_rank.csv... OK (87261 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (124,499 records)
    [!] 69 IXP phantom networks excluded (< 5% captive customers).
    [*] Classifying Quadrants (this takes a moment)...
        - Processing 200/1145...    - Processing 400/1145...    - Processing 600/1145...    - Processing 800/1145...    - Processing 1000/1145...
    ==============================================================================================================
     ROV STRATEGIC QUADRANT REPORT
    ==============================================================================================================

    === Q1: SECURE PROVIDER, SIGNED CUSTOMERS ===
       Provider filters RPKI-invalid routes and customers have signed ROAs (>60% cone average).
       Both layers of defense are active.
    --------------------------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | % Sign | Name
    --------------------------------------------------------------------------------------------------------------
    AS4809   | CN | 64883    |  60.9% | China Telecom Next Generation Carrier Network
    AS34927  | CH | 34017    |  61.1% | iFog GmbH
    AS8218   | FR | 9085     |  69.4% | Zayo Europe
    AS208972 | TR | 8210     |  65.6% | GIBIRNet Iletisim
    AS58057  | CH | 4502     |  63.6% | Securebit AG

    === Q2: SIGNED CUSTOMERS, UNSECURED PROVIDER ===
       Customers have signed ROAs (>60% cone average), but the provider does not filter invalid routes.
       Customer-side signing has no effect without upstream filtering.
    --------------------------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | % Sign | Name
    --------------------------------------------------------------------------------------------------------------
    AS4837   | CN | 48116    |  60.3% | China Unicom Backbone
    AS9002   | GB | 46326    |  60.6% | RETN Limited
    AS33891  | DE | 36364    |  63.9% | Core-Backbone GmbH
    AS20485  | RU | 34017    |  62.3% | TransTeleCom JSC
    AS15830  | NL | 15000    |  60.5% | Equinix, Inc.

    === Q3: SECURE PROVIDER, UNSIGNED CUSTOMERS ===
       Provider filters invalid routes, but customers (<60% cone average) have not signed ROAs.
       Filtering has few signed routes to act on.
    --------------------------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | % Sign | Name
    --------------------------------------------------------------------------------------------------------------
    AS6939   | US | 80006    |  53.5% | Hurricane Electric LLC
    AS3356   | US | 73731    |  55.5% | Lumen (Level 3)
    AS174    | US | 73560    |  56.9% | Cogent Communications, LLC
    AS6461   | US | 71623    |  57.4% | Zayo Bandwidth
    AS1299   | SE | 71086    |  57.3% | Arelion (fka. Telia Carrier)

    === Q4: UNSECURED PROVIDER, UNSIGNED CUSTOMERS ===
       Provider does not filter invalid routes and customers have not signed ROAs.
       Neither defense layer is active.
    --------------------------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | % Sign | Name
    --------------------------------------------------------------------------------------------------------------
    AS4134   | CN | 50788    |  60.0% | China Telecom Backbone
    AS3216   | RU | 26727    |  58.2% | Vimpelcom PJSC
    AS12389  | RU | 12968    |  54.7% | Rostelecom PJSC
    AS22652  | CA | 3634     |  53.9% | Videotron Ltee
    AS52025  | GB | 1785     |  57.9% | ParadoxNetworks Limited

    [+] Full quadrant data saved to rov_quadrants_full.csv
