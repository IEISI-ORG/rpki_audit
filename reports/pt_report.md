    [*] Loading Global Audit for PT...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: PT (Portugal)
    ====================================================================================================
    Total Networks:      166
    Total Cone Gravity:  247
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    53 (31.9%) -> Protects 26.7% of Traffic
    VULNERABLE NETWORKS:        80 (48.2%) -> Exposes  20.6% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        60 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    22 (36.7%)   IPv6 verdict    23 (38.3%)
      VULNERABLE main verdict    32 (53.3%)   IPv6 verdict    32 (53.3%)

    ====================================================================================================
     THE PT CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS6424   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 108      | -      | EDGOO NETWORKS
    AS2860   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 55       | 99%    | NOS COMUNICACOES, S.A.
    AS15525  | REGRESSED                      | REGRESSED                      | 25       | 4%     | MEO - SERVICOS DE COMUNICACOES E MULTIME
    AS8657   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 15       | -      | MEO International Backbone
    AS9186   | REGRESSED                      | REGRESSED                      | 12       | 2%     | ONITELECOM - INFOCOMUNICACOES, S.A.
    AS3243   | REGRESSED                      | REGRESSED                      | 6        | 0%     | MEO
    AS12353  | VOLATILE                       | VOLATILE                       | 6        | 54%    | Vodafone Portugal - Communicacoes Pessoa
    AS1930   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 5        | 96%    | Fundacao para a Ciencia e a Tecnologia, 
    AS29003  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 4        | -      | IP TELECOM, SERVICOS DE TELECOMUNICACOES
    AS24768  | REGRESSED                      | REGRESSED                      | 3        | 1%     | AlmourolTec, Lda
    AS209874 | VULNERABLE                     | VULNERABLE                     | 2        | -      | Tech Tide Portugal Unipessoal LDA
    AS47787  | VULNERABLE                     | VULNERABLE                     | 2        | -      | EDGOO NETWORKS UNIPESSOAL LDA
    AS201782 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1        | -      | Make It Simple Consultoria Informatica L
    AS12926  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 1        | -      | AR TELECOM - Acessos e Redes de Telecomu
    AS44222  | VULNERABLE                     | VULNERABLE                     | 1        | -      | Nuno Felgueiras
    AS50293  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 1        | -      | Interfiber Networks LDA
    AS8609   | STUB: VULNERABLE               | -                              | 0        | -      | Universidade Catolica Portuguesa
    AS9118   | STUB: VULNERABLE               | -                              | 0        | -      | Novo Banco, S.A.
    AS6773   | STUB: VULNERABLE               | -                              | 0        | -      | SIBS Forward Payment Solutions, S.A.
    AS12305  | STUB: VULNERABLE               | -                              | 0        | -      | G9, S.A.

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to PT?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS2860   | 34         | ACTIVE LOCAL ROV               | NOS COMUNICACOES, S.A.
    #2   | AS15525  | 19         | REGRESSED                      | MEO - SERVICOS DE COMUNICACOES E MULTIME
    #3   | AS174    | 18         | INCONSISTENT                   | Cogent Communications, LLC
    #4   | AS12353  | 11         | VOLATILE                       | Vodafone Portugal - Communicacoes Pessoa
    #5   | AS6939   | 9          | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #6   | AS6424   | 9          | PARTIAL: VULNERABLE (Mixed)    | EDGOO NETWORKS
    #7   | AS8220   | 9          | ACTIVE LOCAL ROV               | COLT
    #8   | AS3243   | 7          | REGRESSED                      | MEO
    #9   | AS1930   | 7          | ACTIVE LOCAL ROV               | Fundacao para a Ciencia e a Tecnologia, 
    #10  | AS9186   | 7          | REGRESSED                      | ONITELECOM - INFOCOMUNICACOES, S.A.
    #11  | AS29003  | 5          | PARTIAL: VULNERABLE (Mixed)    | IP TELECOM, SERVICOS DE TELECOMUNICACOES
    #12  | AS24768  | 4          | REGRESSED                      | AlmourolTec, Lda
    #13  | AS20473  | 4          | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #14  | AS2914   | 3          | CORE: ACTIVE PROTECTOR         | NTT America, Inc.
    #15  | AS6762   | 3          | CORE: ACTIVE PROTECTOR         | Telecom Italia Sparkle (Seabone)
    #16  | AS1299   | 3          | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #17  | AS8657   | 3          | PARTIAL: VULNERABLE (Mixed)    | MEO International Backbone
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
    AS201782 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Make It Simple Consultoria Informatica L
    AS29615  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Associacao Porto Digital
