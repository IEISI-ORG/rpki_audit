    [*] Loading Data for ROA Strategy Report...
        - Loading Cones from final_as_rank.csv... OK (87712 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading ASN data from packed file... OK (125,397 records)

    ===============================================================================================
    1. NOT SIGNED, BY ROV COVERAGE TYPE
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | State                      | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS33891  | DE | 47014    | NOT SIGNED (ROV LOCAL)     |   0.0%  | Core-Backbone GmbH
    AS48185  | BE | 30362    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | team.blue NV
    AS29632  | DE | 29479    | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Netassist International EOOD
    AS56662  | PL | 10611    | NOT SIGNED (ROV PARTIAL)   |   0.0%  | Marcin Gondek
    AS16735  | BR | 2431     | NOT SIGNED (ROV LOCAL)     |   0.0%  | Algar Telecom
    AS1031   | US | 1159     | NOT SIGNED (ROV PARTIAL)   |   0.0%  | PEER 1031 LLC
    AS35598  | RU | 927      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | INETCOM CARRIER LLC
    AS62255  | SI | 788      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | BiMajLink d.o.o.
    AS4635   | HK | 747      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | HKIX Route Servers
    AS205794 | CN | 301      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JINZE YANG
    AS62081  | PL | 270      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Stowarzyszenie e-Poludnie
    AS8732   | RU | 208      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | JSC Comcor
    AS11664  | AR | 203      | NOT SIGNED (ROV LOCAL)     |   0.0%  | Techtel LMDS Comunicaciones Interactivas S.A.
    AS201706 | RU | 183      | NOT SIGNED (ROV PARTIAL)   |   0.0%  | SERVICEPIPE LLC
    AS41051  | CH | 111      | NOT SIGNED (ROV UPSTREAM)  |   0.0%  | Freetransit Project (Openfactory GmbH)

    ===============================================================================================
    2. SIGNED (NO ROV)
    -----------------------------------------------------------------------------------------------
    ASN      | CC | Cone     | Signed%  | Name
    -----------------------------------------------------------------------------------------------
    AS6461   | US | 73779    | 100.0%  | Zayo Bandwidth
    AS17639  | PH | 43464    |  97.5%  | Converge ICT Solutions Inc.
    AS4657   | SG | 14896    |  99.9%  | StarHub Ltd
    AS12389  | RU | 13839    |  99.2%  | Rostelecom PJSC
    AS1836   | CH | 13269    |  99.9%  | green.ch AG
    AS212024 | FR | 12971    | 100.0%  | Marc Schmitt
    AS38001  | SG | 6332     | 100.0%  | NewMedia Express Pte. Ltd.
    AS4637   | HK | 5443     | 100.0%  | Telstra International Limited
    AS15830  | NL | 3176     | 100.0%  | Equinix, Inc.
    AS31133  | RU | 3082     |  99.8%  | MegaFon PJSC
    AS9930   | MY | 3039     |  99.7%  | TIME dotCom Bhd
    AS42708  | SE | 2940     | 100.0%  | Glesys AB
    AS4755   | IN | 2591     | 100.0%  | TATA Communications (formerly VSNL)
    AS401753 | VG | 2455     | 100.0%  | BIXCE Inc
    AS9304   | HK | 2369     | 100.0%  | HGC Global Communications Limited

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
    AS1299   | SE | 72484    | 21.75              | Arelion (fka. Telia Carrier)
    AS3356   | US | 76013    | 21.55              | Lumen (Level 3)
    AS174    | US | 74930    | 21.53              | Cogent Communications, LLC
    AS3257   | US | 71749    | 21.36              | GTT Communications Inc.
    AS6939   | US | 70679    | 21.33              | Hurricane Electric LLC
    AS6453   | US | 71417    | 21.30              | TATA Communications (America) Inc
    AS2914   | US | 71704    | 21.19              | NTT America, Inc.
    AS6762   | IT | 70965    | 21.19              | Telecom Italia Sparkle (Seabone)
    AS6461   | US | 73779    | 21.16              | Zayo Bandwidth
    AS3491   | HK | 71050    | 21.07              | PCCW Global (HK) Ltd.
    AS5511   | FR | 70908    | 21.02              | Orange S.A.
    AS12956  | ES | 70905    | 20.94              | Telxius (Telefonica Global)
    AS9002   | GB | 48400    | 20.93              | RETN Limited
    AS701    | US | 71705    | 20.92              | Verizon Business
    AS3320   | DE | 70808    | 20.92              | Deutsche Telekom AG
    AS4637   | HK | 5443     | 20.89              | Telstra International Limited
    AS4755   | IN | 2591     | 20.85              | TATA Communications (formerly VSNL)
    AS8220   | GB | 6739     | 20.82              | COLT
    AS9583   | IN | 536      | 20.79              | Sify Limited
    AS22356  | BR | 86       | 20.79              | Durand do Brasil Ltda
    AS1273   | EU | 492      | 20.78              | Vodafone Group PLC
    AS7473   | SG | 300      | 20.78              | Singapore Telecommunications Ltd
    AS7713   | ID | 3650     | 20.77              | PT Telkom Indonesia Tbk
    AS16735  | BR | 2431     | 20.76              | Algar Telecom
    AS8966   | AE | 2609     | 20.72              | Etisalat (E&)

    [+] Saved strategy to roa_strategy_weighted_v2.csv
