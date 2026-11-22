    [*] Loading rov_audit_v22_final.csv...
        - Loading Cones from final_as_rank.csv... OK (88077 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [!] 52 IXP phantom networks excluded (< 5% captive customers). Re-run build_topology for full fix.

    ================================================================================
     HERD IMMUNITY STATUS
    ================================================================================

    [GLOBAL CORE] (The 100 largest legitimate transit networks)
      Networks Secure:      60 / 100  (60.0%)
      Traffic Protected:   77.2% (by Cone Weight)
      Progress: |██████████████████████████████████████░░░░░░░░░░░░|

    [TRANSIT LAYER] (The 1000 largest legitimate transit networks)
      Networks Secure:     348 / 1000  (34.8%)
      Traffic Protected:   75.2% (by Cone Weight)
      Progress: |█████████████████████████████████████░░░░░░░░░░░░░|

    ================================================================================
     THE HOLDOUTS (Top Vulnerable Transit Nets)
    ================================================================================
    ------------------------------------------------------------------------------------
    Rank  | ASN      | CC |       Cone |  Excl% | Name
    ------------------------------------------------------------------------------------
    #3    | AS6461   | US |     74,093 |    46% | Zayo Bandwidth
    #4    | AS7018   | US |     73,047 |    63% | AT&T Enterprises, LLC
    #22   | AS17639  | PH |     42,701 |    65% | Converge ICT Solutions Inc.
    #23   | AS204457 | TR |     40,974 |    82% | Atlantis Telekomunikasyon Bilisim Hizmet
    #25   | AS20485  | RU |     35,195 |    51% | JSC TransTeleCom
    #32   | AS3216   | RU |     25,692 |    51% | PJSC Vimpelcom
    #40   | AS1836   | CH |     13,302 |    82% | green.ch AG
    #42   | AS12389  | RU |     12,304 |    57% | PJSC Rostelecom
    #48   | AS9498   | IN |      7,510 |    62% | Bharti Airtel Ltd.
    #49   | AS8966   | AE |      7,006 |    10% | Etisalat (E&)
    #53   | AS38001  | SG |      6,033 |    67% | NewMedia Express Pte. Ltd.
    #57   | AS6696   | BE |      5,257 |    73% | VERIXI SA
    #59   | AS13030  | CH |      4,951 |    64% | Init7 (Switzerland) Ltd.
    #62   | AS8359   | RU |      3,627 |    64% | MTS PJSC
    #64   | AS7713   | ID |      3,479 |    64% | PT Telkom Indonesia Tbk
    #65   | AS22652  | CA |      3,445 |    68% | Videotron Ltee
    #66   | AS15830  | NL |      3,352 |    54% | Equinix, Inc.
    #70   | AS42708  | SE |      2,959 |    71% | Glesys AB
    #72   | AS401753 | VG |      2,710 |   100% | BIXCE Inc
    #73   | AS4755   | IN |      2,592 |    61% | TATA Communications (formerly VSNL)
    #81   | AS9930   | MY |      1,852 |    59% | TIME dotCom Bhd
    #84   | AS53062  | BR |      1,757 |    62% | ACESSOLINE TELECOMUNICACOES LTDA
    #91   | AS201054 | PL |      1,241 |    35% | Stowarzyszenie e-Poludnie
    #92   | AS4766   | KR |      1,230 |    76% | Korea Telecom
    #93   | AS46887  | US |      1,183 |    66% | Zayo (fka. Crown Castle)
    ------------------------------------------------------------------------------------

    CONCLUSION:
    CLOSE TO IMMUNITY. The Core is mostly safe, but key giants remain.
