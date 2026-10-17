    [*] Loading rov_audit_v22_final.csv...
        - Loading Cones from final_as_rank.csv... OK (87712 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [!] 56 IXP phantom networks excluded (< 5% captive customers). Re-run build_topology for full fix.

    ================================================================================
     HERD IMMUNITY STATUS
    ================================================================================

    [GLOBAL CORE] (The 100 largest legitimate transit networks)
      Networks Secure:      58 / 100  (58.0%)
      Traffic Protected:   78.6% (by Cone Weight)
      Progress: |███████████████████████████████████████░░░░░░░░░░░|

    [TRANSIT LAYER] (The 1000 largest legitimate transit networks)
      Networks Secure:     319 / 1000  (31.9%)
      Traffic Protected:   76.3% (by Cone Weight)
      Progress: |██████████████████████████████████████░░░░░░░░░░░░|

    ================================================================================
     THE HOLDOUTS (Top Vulnerable Transit Nets)
    ================================================================================
    ------------------------------------------------------------------------------------
    Rank  | ASN      | CC |       Cone |  Excl% | Name
    ------------------------------------------------------------------------------------
    #3    | AS6461   | US |     73,779 |    46% | Zayo Bandwidth
    #4    | AS7018   | US |     72,521 |    63% | AT&T Enterprises, LLC
    #21   | AS17639  | PH |     43,464 |    65% | Converge ICT Solutions Inc.
    #29   | AS3216   | RU |     29,090 |    49% | Vimpelcom PJSC
    #37   | AS4657   | SG |     14,896 |    47% | StarHub Ltd
    #39   | AS12389  | RU |     13,839 |    57% | Rostelecom PJSC
    #40   | AS1836   | CH |     13,269 |    82% | green.ch AG
    #48   | AS9498   | IN |      7,027 |    62% | Bharti Airtel Ltd.
    #52   | AS38001  | SG |      6,332 |    67% | NewMedia Express Pte. Ltd.
    #53   | AS4637   | HK |      5,443 |    17% | Telstra International Limited
    #54   | AS6696   | BE |      5,153 |    73% | VERIXI SA
    #55   | AS8359   | RU |      4,771 |    61% | MTS PJSC
    #56   | AS13030  | CH |      4,623 |    63% | Init7 (Switzerland) Ltd.
    #57   | AS2828   | US |      4,522 |   100% | Verizon (fka XO Communications)
    #63   | AS7713   | ID |      3,650 |    63% | PT Telkom Indonesia Tbk
    #65   | AS22652  | CA |      3,557 |    68% | Videotron Ltee
    #67   | AS15830  | NL |      3,176 |    54% | Equinix, Inc.
    #68   | AS31133  | RU |      3,082 |    47% | MegaFon PJSC
    #70   | AS9930   | MY |      3,039 |    60% | TIME dotCom Bhd
    #71   | AS42708  | SE |      2,940 |    73% | Glesys AB
    #74   | AS8966   | AE |      2,609 |    10% | Etisalat (E&)
    #75   | AS4755   | IN |      2,591 |    61% | TATA Communications (formerly VSNL)
    #76   | AS401753 | VG |      2,455 |   100% | BIXCE Inc
    #78   | AS9304   | HK |      2,369 |    44% | HGC Global Communications Limited
    #86   | AS14840  | BR |      1,862 |    48% | BR.DIGITAL 
    ------------------------------------------------------------------------------------

    CONCLUSION:
    CLOSE TO IMMUNITY. The Core is mostly safe, but key giants remain.
