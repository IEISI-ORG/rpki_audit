    [*] Loading rov_audit_v22_final.csv...
        - Loading Cones from final_as_rank.csv... OK (87912 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [!] 56 IXP phantom networks excluded (< 5% captive customers). Re-run build_topology for full fix.

    ================================================================================
     HERD IMMUNITY STATUS
    ================================================================================

    [GLOBAL CORE] (The 100 largest legitimate transit networks)
      Networks Secure:      50 / 100  (50.0%)
      Traffic Protected:   64.4% (by Cone Weight)
      Progress: |████████████████████████████████░░░░░░░░░░░░░░░░░░|

    [TRANSIT LAYER] (The 1000 largest legitimate transit networks)
      Networks Secure:     282 / 1000  (28.2%)
      Traffic Protected:   62.7% (by Cone Weight)
      Progress: |███████████████████████████████░░░░░░░░░░░░░░░░░░░|

    ================================================================================
     THE HOLDOUTS (Top Vulnerable Transit Nets)
    ================================================================================
    ------------------------------------------------------------------------------------
    Rank  | ASN      | CC |       Cone |  Excl% | Name
    ------------------------------------------------------------------------------------
    #3    | AS6461   | US |     74,006 |    46% | Zayo Bandwidth
    #5    | AS7018   | US |     72,667 |    63% | AT&T Enterprises, LLC
    #9    | AS6453   | US |     71,624 |    20% | TATA Communications (America) Inc
    #11   | AS6762   | IT |     71,093 |    25% | Telecom Italia Sparkle (Seabone)
    #21   | AS17639  | PH |     43,350 |    65% | Converge ICT Solutions Inc.
    #22   | AS20485  | RU |     35,694 |    51% | JSC TransTeleCom
    #29   | AS3216   | RU |     28,398 |    50% | PJSC Vimpelcom
    #37   | AS4657   | SG |     15,499 |    46% | StarHub Ltd
    #39   | AS12389  | RU |     13,486 |    56% | PJSC Rostelecom
    #40   | AS1836   | CH |     13,457 |    82% | green.ch AG
    #41   | AS20766  | FR |     12,463 |   100% | Association "Gitoyen"
    #46   | AS9498   | IN |      6,995 |    61% | Bharti Airtel Ltd.
    #53   | AS38001  | SG |      6,129 |    67% | NewMedia Express Pte. Ltd.
    #56   | AS6696   | BE |      5,027 |    73% | VERIXI SA
    #57   | AS8359   | RU |      4,592 |    62% | MTS PJSC
    #58   | AS2828   | US |      4,454 |   100% | Verizon (fka XO Communications)
    #61   | AS13030  | CH |      4,417 |    63% | Init7 (Switzerland) Ltd.
    #65   | AS22652  | CA |      3,443 |    68% | Videotron Ltee
    #67   | AS7713   | ID |      3,331 |    63% | PT Telkom Indonesia Tbk
    #68   | AS15830  | NL |      3,203 |    54% | Equinix, Inc.
    #72   | AS9930   | MY |      2,918 |    58% | TIME dotCom Bhd
    #74   | AS42708  | SE |      2,881 |    73% | Glesys AB
    #76   | AS4755   | IN |      2,584 |    60% | TATA Communications (formerly VSNL)
    #79   | AS401753 | VG |      2,456 |   100% | BIXCE Inc
    #81   | AS8966   | AE |      2,290 |    12% | Etisalat (E&)
    ------------------------------------------------------------------------------------

    CONCLUSION:
    NO IMMUNITY. Major transit providers are still leaking routes.
