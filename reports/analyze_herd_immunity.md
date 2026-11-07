    [*] Loading rov_audit_v22_final.csv...
        - Loading Cones from final_as_rank.csv... OK (87992 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [!] 49 IXP phantom networks excluded (< 5% captive customers). Re-run build_topology for full fix.

    ================================================================================
     HERD IMMUNITY STATUS
    ================================================================================

    [GLOBAL CORE] (The 100 largest legitimate transit networks)
      Networks Secure:      51 / 100  (51.0%)
      Traffic Protected:   63.7% (by Cone Weight)
      Progress: |███████████████████████████████░░░░░░░░░░░░░░░░░░░|

    [TRANSIT LAYER] (The 1000 largest legitimate transit networks)
      Networks Secure:     261 / 1000  (26.1%)
      Traffic Protected:   61.7% (by Cone Weight)
      Progress: |██████████████████████████████░░░░░░░░░░░░░░░░░░░░|

    ================================================================================
     THE HOLDOUTS (Top Vulnerable Transit Nets)
    ================================================================================
    ------------------------------------------------------------------------------------
    Rank  | ASN      | CC |       Cone |  Excl% | Name
    ------------------------------------------------------------------------------------
    #3    | AS6461   | US |     74,018 |    46% | Zayo Bandwidth
    #4    | AS7018   | US |     72,750 |    63% | AT&T Enterprises, LLC
    #5    | AS1299   | SE |     72,723 |    28% | Arelion (fka. Telia Carrier)
    #8    | AS2914   | US |     71,927 |    27% | NTT America, Inc.
    #21   | AS17639  | PH |     43,433 |    65% | Converge ICT Solutions Inc.
    #22   | AS20485  | RU |     35,449 |    49% | JSC TransTeleCom
    #28   | AS29632  | DE |     28,453 |    38% | Netassist International EOOD
    #31   | AS3216   | RU |     26,131 |    50% | PJSC Vimpelcom
    #37   | AS4657   | SG |     16,147 |    46% | StarHub Ltd
    #38   | AS50304  | NO |     14,245 |    87% | Blix Solutions AS
    #39   | AS1836   | CH |     13,691 |    82% | green.ch AG
    #40   | AS12389  | RU |     13,429 |    57% | PJSC Rostelecom
    #42   | AS20766  | FR |     12,335 |   100% | Association "Gitoyen"
    #47   | AS9498   | IN |      7,400 |    61% | Bharti Airtel Ltd.
    #53   | AS38001  | SG |      6,081 |    67% | NewMedia Express Pte. Ltd.
    #57   | AS2828   | US |      5,138 |   100% | Verizon (fka XO Communications)
    #60   | AS13030  | CH |      5,130 |    64% | Init7 (Switzerland) Ltd.
    #61   | AS6696   | BE |      4,965 |    73% | VERIXI SA
    #64   | AS7713   | ID |      3,754 |    64% | PT Telkom Indonesia Tbk
    #65   | AS15830  | NL |      3,441 |    54% | Equinix, Inc.
    #66   | AS22652  | CA |      3,401 |    70% | Videotron Ltee
    #67   | AS8359   | RU |      3,273 |    63% | MTS PJSC
    #72   | AS42708  | SE |      2,943 |    73% | Glesys AB
    #76   | AS8966   | AE |      2,605 |    10% | Etisalat (E&)
    #77   | AS4755   | IN |      2,597 |    61% | TATA Communications (formerly VSNL)
    ------------------------------------------------------------------------------------

    CONCLUSION:
    NO IMMUNITY. Major transit providers are still leaking routes.
