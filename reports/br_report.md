    [*] Loading Global Audit for BR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: BR (Brazil)
    ====================================================================================================
    Total Networks:      9,180
    Total Cone Gravity:  23,243
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   361 ( 3.9%) -> Protects 16.6% of Traffic
    VULNERABLE NETWORKS:      8344 (90.9%) -> Exposes  74.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        7,632 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   298 ( 3.9%)   IPv6 verdict   441 ( 5.8%)
      VULNERABLE main verdict  7233 (94.8%)   IPv6 verdict  7101 (93.0%)

    ====================================================================================================
     THE BR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS16735  | VOLATILE                       | VOLATILE                       | 2529     | 58%    | Algar Telecom
    AS14840  | REGRESSED                      | REGRESSED                      | 1974     | 1%     | BR.DIGITAL 
    AS53062  | REGRESSED                      | REGRESSED                      | 1588     | 0%     | ACESSOLINE TELECOMUNICACOES LTDA
    AS4230   | REGRESSED                      | REGRESSED                      | 1007     | 16%    | Claro (Embratel)
    AS61832  | REGRESSED                      | REGRESSED                      | 760      | 0%     | Giga+ Empresas
    AS61568  | REGRESSED                      | REGRESSED                      | 544      | 4%     | ALOO TELECOM - FSF TECNOLOGIA SA
    AS267613 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 526      | -      | ELETRONET S.A.
    AS271253 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 500      | 92%    | LINK BRASIL TELECOMUNICACOES LTDA
    AS10429  | REGRESSED                      | REGRESSED                      | 474      | 0%     | Vivo (Telefônica Brasil)
    AS28283  | REGRESSED                      | REGRESSED                      | 436      | 0%     | Adyl Telecom
    AS7738   | REGRESSED                      | REGRESSED                      | 328      | 0%     | V.tal (fka Telemar)
    AS264409 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 305      | -      | Huge Networks
    AS52965  | REGRESSED                      | REGRESSED                      | 289      | 7%     | 1Telecom
    AS22381  | REGRESSED                      | REGRESSED                      | 282      | 1%     | SAMM (Megatelecom)
    AS11432  | REGRESSED                      | REGRESSED                      | 248      | 1%     | Telium Telecomunicações Ltda
    AS28368  | REGRESSED                      | REGRESSED                      | 246      | 1%     | Wirelink (Sobralnet)
    AS263009 | REGRESSED                      | REGRESSED                      | 246      | 0%     | FORTE TELECOM LTDA.
    AS23106  | REGRESSED                      | REGRESSED                      | 245      | 0%     | American Tower Brasil
    AS53181  | REGRESSED                      | REGRESSED                      | 243      | 0%     | Avanca Telecom e Servicos LTDA
    AS53087  | REGRESSED                      | REGRESSED                      | 236      | 2%     | TELY Ltda.

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to BR?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS3356   | 534        | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #2   | AS16735  | 530        | VOLATILE                       | Algar Telecom
    #3   | AS14840  | 480        | REGRESSED                      | BR.DIGITAL 
    #4   | AS52468  | 450        | PARTIAL: VULNERABLE (Mixed)    | UFINET PANAMA S.A.
    #5   | AS53062  | 393        | REGRESSED                      | ACESSOLINE TELECOMUNICACOES LTDA
    #6   | AS4230   | 341        | REGRESSED                      | Claro (Embratel)
    #7   | AS10429  | 269        | REGRESSED                      | Vivo (Telefônica Brasil)
    #8   | AS61832  | 257        | REGRESSED                      | Giga+ Empresas
    #9   | AS28283  | 216        | REGRESSED                      | Adyl Telecom
    #10  | AS271253 | 199        | PARTIAL: VULNERABLE (Mixed)    | LINK BRASIL TELECOMUNICACOES LTDA
    #11  | AS11432  | 194        | REGRESSED                      | Telium Telecomunicações Ltda
    #12  | AS61568  | 187        | REGRESSED                      | ALOO TELECOM - FSF TECNOLOGIA SA
    #13  | AS13786  | 173        | ACTIVE LOCAL ROV               | Seaborn (Seabras USA, LLC)
    #14  | AS53013  | 172        | REGRESSED                      | Ufinet Brasil (WixNet do Brasil)
    #15  | AS267613 | 160        | ACTIVE LOCAL ROV               | ELETRONET S.A.
    #16  | AS23106  | 157        | REGRESSED                      | American Tower Brasil
    #17  | AS22381  | 150        | REGRESSED                      | SAMM (Megatelecom)
    #18  | AS52965  | 147        | REGRESSED                      | 1Telecom
    #19  | AS53181  | 144        | REGRESSED                      | Avanca Telecom e Servicos LTDA
    #20  | AS269096 | 135        | REGRESSED                      | NORTH TECNOLOGIA

    ====================================================================================================
     IPv6 DIFFERENCES (BR networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS28189  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NOVVACORE
    AS53158  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Net Turbo Telecom
    AS52630  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | MOTTANET  TI  - SERVICOS  DE TECNOLOGIA 
    AS265436 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | SkyNet Telecomunicações
    AS273421 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | MAZA Telecom
    AS53038  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | IDC19 - WDI SOLUCOES EM TEC INFORMACAO L
    AS16685  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | TIVIT TERCEIRIZAÇÃO DE PROCESSOS, SERV. 
    AS272451 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | UltraIP Telecom
    AS273461 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Atjp Corp
    AS273490 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | FIBRION INTERNET LTDA
    AS265198 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | BLUE3 TECNOLOGIA EIRELI
    AS53162  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Go! Telecom
    AS267638 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Wind Telecomunicação do Brasil Ltda - ME
    AS264013 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | CONNECTA TELECOM INTERNET LTDA - EPP
    AS28257  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | CONCEITOS NET SERVICOS DE COMUNICACAO E 
    AS262708 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Bit Fibra
    AS61624  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | ISPSHIELD (InfNOC Tecnologia)
    AS262609 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | CL9 Tecnologias Ltda.
    AS263471 | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Intervel Informatica Ltda
    AS265188 | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | Grupo WCM net
    AS268047 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Masterinfo Internet
    AS270711 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Cloud Telecom LTDA
    AS269039 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | CONNECTIONS TELECOM LTDA
    AS267460 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | ALLNET TELECOMUNICAÇÕES EIRELE ME
    AS267450 | UNRELIABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | oliveira & sousa comunicações Ltda
    AS267321 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NTISP TELECOM
    AS272275 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | 5HM TELECOMUNICAÇÃO LTDA ME
    AS272187 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CCOP NET  COMERCIO E SOLUCOES DE EQUIP D
    AS272480 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MGA NET Provedor de Internet LTDA
    AS271314 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | JECTIX TELECOM
