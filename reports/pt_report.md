    [*] Loading Global Audit for PT...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: PT (Portugal)
    ====================================================================================================
    Total Networks:      167
    Total Cone Gravity:  245
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    65 (38.9%) -> Protects 31.4% of Traffic
    VULNERABLE NETWORKS:        69 (41.3%) -> Exposes  17.6% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        61 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    31 (50.8%)   IPv6 verdict    31 (50.8%)
      VULNERABLE main verdict    25 (41.0%)   IPv6 verdict    26 (42.6%)

    ====================================================================================================
     THE PT CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS6424   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 109      | -      | EDGOO NETWORKS
    AS2860   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 55       | 99%    | NOS COMUNICACOES, S.A.
    AS15525  | REGRESSED                      | REGRESSED                      | 25       | 1%     | MEO - SERVICOS DE COMUNICACOES E MULTIME
    AS9186   | REGRESSED                      | REGRESSED                      | 12       | 4%     | ONITELECOM - INFOCOMUNICACOES, S.A.
    AS8657   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 11       | -      | MEO International Backbone
    AS12353  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 8        | 99%    | Vodafone Portugal - Communicacoes Pessoa
    AS3243   | REGRESSED                      | REGRESSED                      | 6        | 0%     | MEO
    AS1930   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 4        | 99%    | Fundacao para a Ciencia e a Tecnologia, 
    AS29003  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 4        | -      | IP TELECOM, SERVICOS DE TELECOMUNICACOES
    AS24768  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3        | 51%    | AlmourolTec, Lda
    AS209874 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2        | -      | Tech Tide Portugal Unipessoal LDA
    AS47787  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 2        | -      | EDGOO NETWORKS UNIPESSOAL LDA
    AS50293  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1        | -      | Interfiber Networks LDA
    AS12926  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 1        | 3%     | AR TELECOM - Acessos e Redes de Telecomu
    AS201782 | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1        | -      | Make It Simple Consultoria Informatica L
    AS44222  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1        | -      | Nuno Felgueiras
    AS200454 | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | Tomas Oliveira Valente Leite de Castro
    AS200706 | STUB: VULNERABLE               | -                              | 0        | -      | AXIANSEU - DIGITAL SOLUTIONS, S.A.
    AS201238 | STUB: VULNERABLE               | STUB: VULNERABLE               | 0        | -      | Antonio Carlos Correia da Silva
    AS201170 | STUB: VULNERABLE               | -                              | 0        | -      | ANA - Aeroportos de Portugal, SA

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to PT?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS2860   | 34         | ACTIVE LOCAL ROV               | NOS COMUNICACOES, S.A.
    #2   | AS15525  | 19         | REGRESSED                      | MEO - SERVICOS DE COMUNICACOES E MULTIME
    #3   | AS174    | 18         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #4   | AS12353  | 11         | ACTIVE LOCAL ROV               | Vodafone Portugal - Communicacoes Pessoa
    #5   | AS6939   | 9          | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #6   | AS6424   | 9          | PARTIAL: VULNERABLE (Mixed)    | EDGOO NETWORKS
    #7   | AS8220   | 9          | ACTIVE LOCAL ROV               | COLT
    #8   | AS9186   | 7          | REGRESSED                      | ONITELECOM - INFOCOMUNICACOES, S.A.
    #9   | AS1930   | 7          | ACTIVE LOCAL ROV               | Fundacao para a Ciencia e a Tecnologia, 
    #10  | AS3243   | 7          | REGRESSED                      | MEO
    #11  | AS29003  | 5          | PASSIVE (Clean Pipe)           | IP TELECOM, SERVICOS DE TELECOMUNICACOES
    #12  | AS24768  | 4          | ACTIVE LOCAL ROV               | AlmourolTec, Lda
    #13  | AS20473  | 4          | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #14  | AS2914   | 3          | CORE: ACTIVE PROTECTOR         | NTT America, Inc.
    #15  | AS6762   | 3          | CORE: UNPROTECTED              | Telecom Italia Sparkle (Seabone)
    #16  | AS1299   | 3          | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #17  | AS8657   | 3          | PARTIAL: VULNERABLE (Mixed)    | MEO International Backbone
    #18  | AS8426   | 3          | ACTIVE LOCAL ROV               | Claranet Limited
    #19  | AS6453   | 2          | CORE: UNPROTECTED              | TATA Communications (America) Inc
    #20  | AS3257   | 2          | CORE: ACTIVE PROTECTOR         | GTT Communications Inc.

    ====================================================================================================
     IPv6 DIFFERENCES (PT networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS209874 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 3/3            | Tech Tide Portugal Unipessoal LDA
