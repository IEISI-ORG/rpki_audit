    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (87459 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (125,153 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | XX | 46961    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Unknown
    AS48185  | BE | 30323    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Unknown
    AS29632  | XX | 30002    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Unknown
    AS56662  | PL | 10864    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Unknown
    AS16735  | BR | 2262     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Unknown
    AS1031   | US | 1202     | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Unknown
    AS201054 | PL | 1167     | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Unknown
    AS35598  | RU | 902      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Unknown
    AS62255  | SI | 744      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Unknown
    AS4635   | XX | 721      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Unknown
    AS10429  | BR | 462      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Unknown
    AS24115  | XX | 387      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Unknown
    AS7738   | BR | 352      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Unknown
    AS205794 | CN | 316      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Unknown
    AS62081  | PL | 275      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Unknown

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS6461   | US | 71946    | 100.0%  | Unknown
    AS37721  | BF | 58312    | 100.0%  | Unknown
    AS4837   | CN | 50577    |  99.4%  | Unknown
    AS17639  | PH | 43147    |  97.7%  | Unknown
    AS34927  | CH | 34226    | 100.0%  | Unknown
    AS4657   | SG | 15296    |  99.9%  | Unknown
    AS1836   | CH | 13023    |  99.9%  | Unknown
    AS20766  | FR | 12332    |  96.7%  | Unknown
    AS38001  | SG | 6112     | 100.0%  | Unknown
    AS15830  | NL | 3668     | 100.0%  | Unknown
    AS42708  | SE | 2899     | 100.0%  | Unknown
    AS4755   | IN | 2547     | 100.0%  | Unknown
    AS9304   | HK | 2178     | 100.0%  | Unknown
    AS64073  | NZ | 1675     | 100.0%  | Unknown
    AS53062  | BR | 1557     |  96.4%  | Unknown

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
    AS6939   | US | 80275    | 21.66              | Unknown
    AS3356   | US | 74030    | 21.50              | Unknown
    AS1299   | SE | 71458    | 21.36              | Unknown
    AS174    | US | 73849    | 21.32              | Unknown
    AS3257   | US | 69123    | 21.27              | Unknown
    AS6461   | US | 71946    | 21.22              | Unknown
    AS2914   | US | 68933    | 21.17              | Unknown
    AS4637   | HK | 67304    | 21.17              | Unknown
    AS6762   | IT | 66665    | 21.14              | Unknown
    AS6453   | US | 67808    | 21.12              | Unknown
    AS5511   | FR | 62306    | 21.07              | Unknown
    AS3491   | HK | 67288    | 21.06              | Unknown
    AS12956  | ES | 62395    | 20.96              | Unknown
    AS1273   | EU | 63250    | 20.94              | Unknown
    AS6830   | NL | 62811    | 20.92              | Unknown
    AS3320   | DE | 67344    | 20.88              | Unknown
    AS4134   | CN | 52552    | 20.84              | Unknown
    AS9002   | GB | 48162    | 20.76              | Unknown
    AS701    | US | 68265    | 20.41              | Unknown
    AS7713   | ID | 3441     | 20.01              | Unknown
    AS4837   | CN | 50577    | 19.92              | Unknown
    AS4809   | CN | 65220    | 19.51              | Unknown
    AS7922   | US | 26233    | 19.44              | Unknown
    AS34927  | CH | 34226    | 19.29              | Unknown
    AS20485  | RU | 34039    | 19.27              | Unknown

    [+] Saved strategy to roa_strategy_weighted_v2.csv
