    [*] Loading rov_audit_v22_final.csv...
        - Loading Cones from final_as_rank.csv... OK (87449 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [!] 90 IXP phantom networks excluded (< 5% captive customers). Re-run build_topology for full fix.

    ================================================================================
     HERD IMMUNITY STATUS
    ================================================================================

    [GLOBAL CORE] (The 100 largest legitimate transit networks)
      Networks Secure:      32 / 100  (32.0%)
      Traffic Protected:   68.4% (by Cone Weight)
      Progress: |██████████████████████████████████░░░░░░░░░░░░░░░░|

    [TRANSIT LAYER] (The 1000 largest legitimate transit networks)
      Networks Secure:     170 / 1000  (17.0%)
      Traffic Protected:   66.3% (by Cone Weight)
      Progress: |█████████████████████████████████░░░░░░░░░░░░░░░░░|

    ================================================================================
     THE HOLDOUTS (Top Vulnerable Transit Nets)
    ================================================================================
    ------------------------------------------------------------------------------------
    Rank  | ASN      | CC |       Cone |  Excl% | Name
    ------------------------------------------------------------------------------------
    #4    | AS6461   | US |     72,157 |    40% | Zayo Bandwidth
    #7    | AS2914   | US |     68,901 |    17% | NTT America, Inc.
    #20   | AS4134   | CN |     51,855 |    81% | China Telecom Backbone
    #22   | AS4837   | CN |     46,767 |    59% | China Unicom Backbone
    #23   | AS20485  | RU |     34,809 |    19% | TransTeleCom JSC
    #24   | AS34927  | CH |     33,526 |    14% | iFog GmbH
    #27   | AS3216   | RU |     25,830 |    31% | Vimpelcom PJSC
    #29   | AS15830  | NL |     15,640 |    38% | Equinix, Inc.
    #32   | AS9498   | IN |      9,481 |    56% | Bharti Airtel Ltd.
    #38   | AS52468  | PA |      5,951 |    53% | UFINET PANAMA S.A.
    #40   | AS9304   | HK |      5,297 |    25% | HGC Global Communications Limited
    #41   | AS8359   | RU |      5,088 |    50% | MTS PJSC
    #47   | AS22652  | CA |      3,668 |    20% | Videotron Ltee
    #49   | AS31133  | RU |      3,378 |    40% | MegaFon PJSC
    #50   | AS7713   | ID |      3,292 |    22% | PT Telkom Indonesia Tbk
    #53   | AS9808   | CN |      2,502 |    73% | China Mobile Backbone
    #54   | AS4755   | IN |      2,235 |    61% | TATA Communications (formerly VSNL)
    #56   | AS42708  | SE |      2,198 |    23% | Glesys AB
    #60   | AS64073  | NZ |      1,685 |    15% | Vetta Group
    #61   | AS53062  | BR |      1,636 |    61% | ACESSOLINE TELECOMUNICACOES LTDA
    #63   | AS9929   | CN |      1,434 |    67% | China Unicom Industrial Internet Backbon
    #64   | AS8447   | AT |      1,356 |    56% | A1 Telekom Austria AG
    #65   | AS58717  | BD |      1,250 |    81% | Summit Communications Ltd
    #81   | AS3223   | GB |        758 |    20% | Voxility LLP
    #83   | AS61832  | BR |        713 |    27% | Giga+ Empresas
    ------------------------------------------------------------------------------------

    CONCLUSION:
    NO IMMUNITY. Major transit providers are still leaking routes.
