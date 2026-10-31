    [*] Loading Global Audit for PT...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: PT (Portugal)
    ====================================================================================================
    Total Networks:      167
    Total Cone Gravity:  251
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    63 (37.7%) -> Protects 34.7% of Traffic
    VULNERABLE NETWORKS:        71 (42.5%) -> Exposes  17.1% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        61 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    32 (52.5%)   IPv6 verdict    32 (52.5%)
      VULNERABLE main verdict    24 (39.3%)   IPv6 verdict    25 (41.0%)

    ====================================================================================================
     THE PT CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS6424   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 111      | -      | EDGOO NETWORKS
    AS2860   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 55       | 99%    | NOS COMUNICACOES, S.A.
    AS15525  | REGRESSED                      | REGRESSED                      | 25       | 3%     | MEO - SERVICOS DE COMUNICACOES E MULTIME
    AS8657   | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 15       | -      | MEO International Backbone
    AS9186   | REGRESSED                      | REGRESSED                      | 12       | 6%     | ONITELECOM - INFOCOMUNICACOES, S.A.
    AS12353  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 6        | 99%    | Vodafone Portugal - Communicacoes Pessoa
    AS3243   | REGRESSED                      | REGRESSED                      | 6        | 0%     | MEO
    AS29003  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 4        | -      | IP TELECOM, SERVICOS DE TELECOMUNICACOES
    AS209874 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 4        | -      | Tech Tide Portugal Unipessoal LDA
    AS1930   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 4        | 98%    | Fundacao para a Ciencia e a Tecnologia, 
    AS24768  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 3        | 0%     | AlmourolTec, Lda
    AS47787  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 2        | -      | EDGOO NETWORKS UNIPESSOAL LDA
    AS50293  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1        | -      | Interfiber Networks LDA
    AS201782 | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1        | -      | Make It Simple Consultoria Informatica L
    AS12926  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 1        | 2%     | AR TELECOM - Acessos e Redes de Telecomu
    AS44222  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1        | -      | Nuno Felgueiras
    AS199155 | STUB: FORTUITOUS ROV           | STUB: FORTUITOUS ROV           | 0        | 99%    | Direcao Geral de Estatisticas da Educaca
    AS199667 | NOT ROUTED                     | -                              | 0        | -      | 4Spiro - Sociedade de Consultoria, LDA
    AS208277 | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | CiberConceito Informatica e Servicos Uni
    AS208457 | STUB: PASSIVE (Clean Pipe)     | STUB: PASSIVE (Clean Pipe)     | 0        | -      | CLOUD Telecom Lda

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to PT?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS2860   | 34         | ACTIVE LOCAL ROV               | NOS COMUNICACOES, S.A.
    #2   | AS15525  | 19         | REGRESSED                      | MEO - SERVICOS DE COMUNICACOES E MULTIME
    #3   | AS174    | 18         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #4   | AS12353  | 11         | ACTIVE LOCAL ROV               | Vodafone Portugal - Communicacoes Pessoa
    #5   | AS6939   | 9          | ACTIVE LOCAL ROV               | Hurricane Electric LLC
    #6   | AS6424   | 9          | PARTIAL: VULNERABLE (Mixed)    | EDGOO NETWORKS
    #7   | AS8220   | 9          | ACTIVE LOCAL ROV               | COLT
    #8   | AS1930   | 7          | ACTIVE LOCAL ROV               | Fundacao para a Ciencia e a Tecnologia, 
    #9   | AS9186   | 7          | REGRESSED                      | ONITELECOM - INFOCOMUNICACOES, S.A.
    #10  | AS3243   | 7          | REGRESSED                      | MEO
    #11  | AS29003  | 5          | PASSIVE (Clean Pipe)           | IP TELECOM, SERVICOS DE TELECOMUNICACOES
    #12  | AS24768  | 4          | PARTIAL: VULNERABLE (Mixed)    | AlmourolTec, Lda
    #13  | AS20473  | 4          | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #14  | AS2914   | 3          | INCONSISTENT                   | NTT America, Inc.
    #15  | AS6762   | 3          | CORE: ACTIVE PROTECTOR         | Telecom Italia Sparkle (Seabone)
    #16  | AS1299   | 3          | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #17  | AS8657   | 3          | PASSIVE (Clean Pipe)           | MEO International Backbone
    #18  | AS8426   | 3          | ACTIVE LOCAL ROV               | Claranet Limited
    #19  | AS6453   | 2          | CORE: ACTIVE PROTECTOR         | TATA Communications (America) Inc
    #20  | AS3257   | 2          | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.

    ====================================================================================================
     IPv6 DIFFERENCES (PT networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS209874 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 3/3            | Tech Tide Portugal Unipessoal LDA
