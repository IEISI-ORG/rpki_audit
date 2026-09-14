    [*] Loading rov_audit_v22_final.csv...
        - Loading Cones from final_as_rank.csv... OK (87261 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [!] 86 IXP phantom networks excluded (< 5% captive customers). Re-run build_topology for full fix.

    ================================================================================
     HERD IMMUNITY STATUS
    ================================================================================

    [GLOBAL CORE] (The 100 largest legitimate transit networks)
      Networks Secure:      51 / 100  (51.0%)
      Traffic Protected:   80.5% (by Cone Weight)
      Progress: |████████████████████████████████████████░░░░░░░░░░|

    [TRANSIT LAYER] (The 1000 largest legitimate transit networks)
      Networks Secure:     228 / 1000  (22.8%)
      Traffic Protected:   78.1% (by Cone Weight)
      Progress: |███████████████████████████████████████░░░░░░░░░░░|

    ================================================================================
     THE HOLDOUTS (Top Vulnerable Transit Nets)
    ================================================================================
    ------------------------------------------------------------------------------------
    Rank  | ASN      | CC |       Cone |  Excl% | Name
    ------------------------------------------------------------------------------------
    #20   | AS4134   | CN |     50,788 |    82% | China Telecom Backbone
    #21   | AS4837   | CN |     48,116 |    61% | China Unicom Backbone
    #25   | AS20485  | RU |     34,017 |    19% | TransTeleCom JSC
    #26   | AS3216   | RU |     26,727 |    32% | Vimpelcom PJSC
    #29   | AS15830  | NL |     15,000 |    37% | Equinix, Inc.
    #35   | AS9498   | IN |      6,974 |    61% | Bharti Airtel Ltd.
    #44   | AS22652  | CA |      3,634 |    19% | Videotron Ltee
    #47   | AS7713   | ID |      3,221 |    22% | PT Telkom Indonesia Tbk
    #49   | AS9808   | CN |      2,761 |    73% | China Mobile Backbone
    #51   | AS4755   | IN |      2,482 |    61% | TATA Communications (formerly VSNL)
    #52   | AS9304   | HK |      2,406 |    30% | HGC Global Communications Limited
    #54   | AS42708  | SE |      2,169 |    24% | Glesys AB
    #58   | AS53062  | BR |      1,733 |    62% | GGNET TELECOMUNICACOES LTDA
    #59   | AS64073  | NZ |      1,689 |    14% | Vetta Group
    #60   | AS9929   | CN |      1,603 |    67% | China Unicom Industrial Internet Backbon
    #62   | AS58717  | BD |      1,293 |    80% | Summit Communications Ltd
    #65   | AS14789  | US |      1,197 |    23% | Cloudflare, Inc.
    #78   | AS3223   | GB |        744 |    20% | Voxility LLP
    #80   | AS61832  | BR |        738 |    25% | Giga+ Empresas
    #83   | AS12741  | PL |        720 |    71% | Netia SA
    #87   | AS4800   | ID |        630 |    53% | PT Aplikanusa Lintasarta
    #89   | AS18229  | IN |        584 |    78% | CtrlS
    #93   | AS20804  | PL |        550 |    54% | Exatel S.A.
    #94   | AS61568  | BR |        545 |    53% | ALOO TELECOM - FSF TECNOLOGIA SA
    #101  | AS3786   | KR |        495 |    73% | LG DACOM Corporation
    ------------------------------------------------------------------------------------

    CONCLUSION:
    CLOSE TO IMMUNITY. The Core is mostly safe, but key giants remain.
