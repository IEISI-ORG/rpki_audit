    [*] Loading rov_audit_v22_final.csv...
        - Loading Cones from final_as_rank.csv... OK (87399 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [!] 85 IXP phantom networks excluded (< 5% captive customers). Re-run build_topology for full fix.

    ================================================================================
     HERD IMMUNITY STATUS
    ================================================================================

    [GLOBAL CORE] (The 100 largest legitimate transit networks)
      Networks Secure:      34 / 100  (34.0%)
      Traffic Protected:   70.4% (by Cone Weight)
      Progress: |███████████████████████████████████░░░░░░░░░░░░░░░|

    [TRANSIT LAYER] (The 1000 largest legitimate transit networks)
      Networks Secure:     178 / 1000  (17.8%)
      Traffic Protected:   68.3% (by Cone Weight)
      Progress: |██████████████████████████████████░░░░░░░░░░░░░░░░|

    ================================================================================
     THE HOLDOUTS (Top Vulnerable Transit Nets)
    ================================================================================
    ------------------------------------------------------------------------------------
    Rank  | ASN      | CC |       Cone |  Excl% | Name
    ------------------------------------------------------------------------------------
    #4    | AS6461   | US |     71,747 |    41% | Zayo Bandwidth
    #7    | AS2914   | US |     68,809 |    17% | NTT America, Inc.
    #20   | AS4134   | CN |     52,098 |    80% | China Telecom Backbone
    #21   | AS4837   | CN |     49,153 |    59% | China Unicom Backbone
    #25   | AS20485  | RU |     33,889 |    19% | TransTeleCom JSC
    #27   | AS3216   | RU |     25,276 |    32% | Vimpelcom PJSC
    #29   | AS15830  | NL |     15,804 |    37% | Equinix, Inc.
    #35   | AS9498   | IN |      7,428 |    60% | Bharti Airtel Ltd.
    #38   | AS52468  | PA |      5,786 |    46% | UFINET PANAMA S.A.
    #39   | AS8359   | RU |      5,144 |    50% | MTS PJSC
    #45   | AS22652  | CA |      3,735 |    18% | Videotron Ltee
    #48   | AS31133  | RU |      3,431 |    41% | MegaFon PJSC
    #49   | AS7713   | ID |      2,865 |    18% | PT Telkom Indonesia Tbk
    #51   | AS9808   | CN |      2,701 |    73% | China Mobile Backbone
    #52   | AS4755   | IN |      2,541 |    61% | TATA Communications (formerly VSNL)
    #53   | AS42708  | SE |      2,358 |    22% | Glesys AB
    #54   | AS9304   | HK |      2,338 |    31% | HGC Global Communications Limited
    #58   | AS64073  | NZ |      1,683 |    15% | Vetta Group
    #60   | AS53062  | BR |      1,665 |    50% | ACESSOLINE TELECOMUNICACOES LTDA
    #61   | AS9929   | CN |      1,580 |    67% | China Unicom Industrial Internet Backbon
    #66   | AS58717  | BD |      1,253 |    80% | Summit Communications Ltd
    #70   | AS8447   | AT |      1,180 |    57% | A1 Telekom Austria AG
    #81   | AS3223   | GB |        747 |    20% | Voxility LLP
    #82   | AS12741  | PL |        720 |    70% | Netia SA
    #86   | AS61832  | BR |        673 |    19% | Giga+ Empresas
    ------------------------------------------------------------------------------------

    CONCLUSION:
    NO IMMUNITY. Major transit providers are still leaking routes.
