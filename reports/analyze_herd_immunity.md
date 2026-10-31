    [*] Loading rov_audit_v22_final.csv...
        - Loading Cones from final_as_rank.csv... OK (88086 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [!] 56 IXP phantom networks excluded (< 5% captive customers). Re-run build_topology for full fix.

    ================================================================================
     HERD IMMUNITY STATUS
    ================================================================================

    [GLOBAL CORE] (The 100 largest legitimate transit networks)
      Networks Secure:      56 / 100  (56.0%)
      Traffic Protected:   71.1% (by Cone Weight)
      Progress: |███████████████████████████████████░░░░░░░░░░░░░░░|

    [TRANSIT LAYER] (The 1000 largest legitimate transit networks)
      Networks Secure:     300 / 1000  (30.0%)
      Traffic Protected:   69.1% (by Cone Weight)
      Progress: |██████████████████████████████████░░░░░░░░░░░░░░░░|

    ================================================================================
     THE HOLDOUTS (Top Vulnerable Transit Nets)
    ================================================================================
    ------------------------------------------------------------------------------------
    Rank  | ASN      | CC |       Cone |  Excl% | Name
    ------------------------------------------------------------------------------------
    #3    | AS6461   | US |     74,170 |    46% | Zayo Bandwidth
    #4    | AS7018   | US |     72,893 |    63% | AT&T Enterprises, LLC
    #8    | AS2914   | US |     72,072 |    27% | NTT America, Inc.
    #21   | AS17639  | PH |     43,018 |    64% | Converge ICT Solutions Inc.
    #23   | AS20485  | RU |     34,696 |    50% | JSC TransTeleCom
    #30   | AS3216   | RU |     25,820 |    50% | PJSC Vimpelcom
    #37   | AS4657   | SG |     15,334 |    45% | StarHub Ltd
    #39   | AS1836   | CH |     13,789 |    82% | green.ch AG
    #41   | AS20766  | FR |     12,639 |   100% | Association "Gitoyen"
    #42   | AS12389  | RU |     12,329 |    57% | PJSC Rostelecom
    #46   | AS9498   | IN |      7,867 |    61% | Bharti Airtel Ltd.
    #50   | AS38001  | SG |      6,373 |    67% | NewMedia Express Pte. Ltd.
    #56   | AS6696   | BE |      5,029 |    73% | VERIXI SA
    #57   | AS2828   | US |      4,826 |   100% | Verizon (fka XO Communications)
    #60   | AS13030  | CH |      4,445 |    63% | Init7 (Switzerland) Ltd.
    #62   | AS8359   | RU |      4,312 |    62% | MTS PJSC
    #66   | AS22652  | CA |      3,504 |    68% | Videotron Ltee
    #67   | AS15830  | NL |      3,230 |    54% | Equinix, Inc.
    #71   | AS7713   | ID |      3,011 |    63% | PT Telkom Indonesia Tbk
    #72   | AS42708  | SE |      2,898 |    73% | Glesys AB
    #75   | AS4755   | IN |      2,658 |    60% | TATA Communications (formerly VSNL)
    #76   | AS8966   | AE |      2,621 |    12% | Etisalat (E&)
    #78   | AS401753 | VG |      2,464 |   100% | BIXCE Inc
    #80   | AS14840  | BR |      2,246 |    48% | BR.DIGITAL 
    #85   | AS20562  | NL |      1,932 |    18% | Open Peering (Broadband Hosting B.V.)
    ------------------------------------------------------------------------------------

    CONCLUSION:
    NO IMMUNITY. Major transit providers are still leaking routes.
