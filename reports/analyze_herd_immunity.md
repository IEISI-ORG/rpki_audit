    [*] Loading rov_audit_v22_final.csv...
        - Loading Cones from final_as_rank.csv... OK (87459 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [!] 92 IXP phantom networks excluded (< 5% captive customers). Re-run build_topology for full fix.

    ================================================================================
     HERD IMMUNITY STATUS
    ================================================================================

    [GLOBAL CORE] (The 100 largest legitimate transit networks)
      Networks Secure:      35 / 100  (35.0%)
      Traffic Protected:   73.8% (by Cone Weight)
      Progress: |████████████████████████████████████░░░░░░░░░░░░░░|

    [TRANSIT LAYER] (The 1000 largest legitimate transit networks)
      Networks Secure:     184 / 1000  (18.4%)
      Traffic Protected:   71.5% (by Cone Weight)
      Progress: |███████████████████████████████████░░░░░░░░░░░░░░░|

    ================================================================================
     THE HOLDOUTS (Top Vulnerable Transit Nets)
    ================================================================================
    ------------------------------------------------------------------------------------
    Rank  | ASN      | CC |       Cone |  Excl% | Name
    ------------------------------------------------------------------------------------
    #4    | AS6461   | US |     71,946 |    41% | Zayo Bandwidth
    #20   | AS4134   | CN |     52,552 |    81% | China Telecom Backbone
    #21   | AS4837   | CN |     50,577 |    57% | China Unicom Backbone
    #23   | AS34927  | CH |     34,226 |    11% | iFog GmbH
    #24   | AS20485  | RU |     34,039 |    20% | TransTeleCom JSC
    #25   | AS3216   | RU |     30,350 |    29% | Vimpelcom PJSC
    #28   | AS4657   | SG |     15,296 |     8% | StarHub Ltd
    #33   | AS9498   | IN |      7,421 |    60% | Bharti Airtel Ltd.
    #38   | AS8359   | RU |      5,054 |    50% | MTS PJSC
    #44   | AS15830  | NL |      3,668 |    54% | Equinix, Inc.
    #45   | AS22652  | CA |      3,658 |    20% | Videotron Ltee
    #46   | AS7713   | ID |      3,441 |    23% | PT Telkom Indonesia Tbk
    #50   | AS42708  | SE |      2,899 |    17% | Glesys AB
    #51   | AS9808   | CN |      2,840 |    69% | China Mobile Backbone
    #52   | AS4755   | IN |      2,547 |    60% | TATA Communications (formerly VSNL)
    #56   | AS9304   | HK |      2,178 |    32% | HGC Global Communications Limited
    #60   | AS53062  | BR |      1,557 |    60% | ACESSOLINE TELECOMUNICACOES LTDA
    #61   | AS9929   | CN |      1,508 |    67% | China Unicom Industrial Internet Backbon
    #70   | AS8447   | AT |      1,080 |    59% | A1 Telekom Austria AG
    #72   | AS58717  | BD |      1,014 |    80% | Summit Communications Ltd
    #77   | AS4230   | BR |        880 |    37% | Claro (Embratel)
    #79   | AS12741  | PL |        763 |    71% | Netia SA
    #81   | AS3223   | GB |        738 |    21% | Voxility LLP
    #83   | AS61832  | BR |        703 |    26% | Giga+ Empresas
    #85   | AS4800   | ID |        691 |    52% | PT Aplikanusa Lintasarta
    ------------------------------------------------------------------------------------

    CONCLUSION:
    CLOSE TO IMMUNITY. The Core is mostly safe, but key giants remain.
