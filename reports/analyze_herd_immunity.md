    [*] Loading rov_audit_v22_final.csv...
        - Loading Cones from final_as_rank.csv... OK (87904 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [!] 52 IXP phantom networks excluded (< 5% captive customers). Re-run build_topology for full fix.

    ================================================================================
     HERD IMMUNITY STATUS
    ================================================================================

    [GLOBAL CORE] (The 100 largest legitimate transit networks)
      Networks Secure:      53 / 100  (53.0%)
      Traffic Protected:   72.5% (by Cone Weight)
      Progress: |████████████████████████████████████░░░░░░░░░░░░░░|

    [TRANSIT LAYER] (The 1000 largest legitimate transit networks)
      Networks Secure:     270 / 1000  (27.0%)
      Traffic Protected:   70.4% (by Cone Weight)
      Progress: |███████████████████████████████████░░░░░░░░░░░░░░░|

    ================================================================================
     THE HOLDOUTS (Top Vulnerable Transit Nets)
    ================================================================================
    ------------------------------------------------------------------------------------
    Rank  | ASN      | CC |       Cone |  Excl% | Name
    ------------------------------------------------------------------------------------
    #2    | AS174    | US |     75,065 |    50% | Cogent Communications, LLC
    #3    | AS6461   | US |     73,917 |    46% | Zayo Bandwidth
    #4    | AS7018   | US |     72,662 |    63% | AT&T Enterprises, LLC
    #21   | AS17639  | PH |     42,697 |    65% | Converge ICT Solutions Inc.
    #23   | AS20485  | RU |     35,820 |    50% | JSC TransTeleCom
    #31   | AS3216   | RU |     26,148 |    50% | PJSC Vimpelcom
    #37   | AS4657   | SG |     15,955 |    48% | StarHub Ltd
    #38   | AS1836   | CH |     14,269 |    82% | green.ch AG
    #41   | AS12389  | RU |     12,793 |    57% | PJSC Rostelecom
    #47   | AS9498   | IN |      7,755 |    62% | Bharti Airtel Ltd.
    #51   | AS38001  | SG |      6,118 |    67% | NewMedia Express Pte. Ltd.
    #55   | AS6696   | BE |      5,320 |    73% | VERIXI SA
    #56   | AS13030  | CH |      4,985 |    66% | Init7 (Switzerland) Ltd.
    #60   | AS15830  | NL |      3,623 |    54% | Equinix, Inc.
    #61   | AS22652  | CA |      3,565 |    68% | Videotron Ltee
    #62   | AS8359   | RU |      3,316 |    64% | MTS PJSC
    #63   | AS7713   | ID |      3,284 |    64% | PT Telkom Indonesia Tbk
    #65   | AS42708  | SE |      2,926 |    71% | Glesys AB
    #69   | AS8966   | AE |      2,710 |    10% | Etisalat (E&)
    #70   | AS4755   | IN |      2,629 |    61% | TATA Communications (formerly VSNL)
    #71   | AS401753 | VG |      2,601 |   100% | BIXCE Inc
    #72   | AS9304   | HK |      2,457 |    42% | HGC Global Communications Limited
    #77   | AS14840  | BR |      2,010 |    49% | BR.DIGITAL 
    #81   | AS53062  | BR |      1,820 |    62% | ACESSOLINE TELECOMUNICACOES LTDA
    #82   | AS64073  | NZ |      1,807 |    79% | Vetta Group
    ------------------------------------------------------------------------------------

    CONCLUSION:
    NO IMMUNITY. Major transit providers are still leaking routes.
