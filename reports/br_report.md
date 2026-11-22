    [*] Loading Global Audit for BR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: BR (Brazil)
    ====================================================================================================
    Total Networks:      9,201
    Total Cone Gravity:  22,192
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   436 ( 4.7%) -> Protects 26.3% of Traffic
    VULNERABLE NETWORKS:      8151 (88.6%) -> Exposes  50.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        7,648 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   373 ( 4.9%)   IPv6 verdict   517 ( 6.8%)
      VULNERABLE main verdict  7058 (92.3%)   IPv6 verdict  6936 (90.7%)

    ====================================================================================================
     THE BR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS16735  | VOLATILE                       | VOLATILE                       | 1956     | 93%    | Algar Telecom
    AS53062  | REGRESSED                      | REGRESSED                      | 1757     | 0%     | ACESSOLINE TELECOMUNICACOES LTDA
    AS14840  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1757     | 0%     | BR.DIGITAL 
    AS4230   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 950      | 21%    | Claro (Embratel)
    AS61832  | REGRESSED                      | REGRESSED                      | 731      | 0%     | Giga+ Empresas
    AS61568  | REGRESSED                      | REGRESSED                      | 528      | 0%     | ALOO TELECOM - FSF TECNOLOGIA SA
    AS267613 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 494      | -      | ELETRONET S.A.
    AS10429  | REGRESSED                      | REGRESSED                      | 476      | 0%     | Vivo (Telefônica Brasil)
    AS28283  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 459      | 0%     | Adyl Telecom
    AS271253 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 428      | 91%    | LINK BRASIL TELECOMUNICACOES LTDA
    AS7738   | PARTIAL: VULNERABLE (Mixed)    | Unverified (Transit/Peer?)     | 337      | 0%     | V.tal (fka Telemar)
    AS264409 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 273      | -      | Huge Networks
    AS52965  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 267      | 10%    | 1Telecom
    AS22381  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 254      | 2%     | SAMM (Megatelecom)
    AS28368  | Unverified (Transit/Peer?)     | VOLATILE                       | 249      | -      | Wirelink (Sobralnet)
    AS11432  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 244      | 0%     | Telium Telecomunicações Ltda
    AS263009 | REGRESSED                      | REGRESSED                      | 244      | 0%     | FORTE TELECOM LTDA.
    AS53181  | REGRESSED                      | REGRESSED                      | 239      | 0%     | Avanca Telecom e Servicos LTDA
    AS23106  | REGRESSED                      | REGRESSED                      | 229      | 0%     | American Tower Brasil
    AS28146  | REGRESSED                      | REGRESSED                      | 222      | 0%     | MHNET TELECOM

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to BR?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS3356   | 534        | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #2   | AS16735  | 530        | VOLATILE                       | Algar Telecom
    #3   | AS14840  | 480        | PASSIVE (Clean Pipe)           | BR.DIGITAL 
    #4   | AS52468  | 450        | PARTIAL: VULNERABLE (Mixed)    | UFINET PANAMA S.A.
    #5   | AS53062  | 393        | REGRESSED                      | ACESSOLINE TELECOMUNICACOES LTDA
    #6   | AS4230   | 341        | VULNERABLE (Atlas Verified)    | Claro (Embratel)
    #7   | AS10429  | 269        | REGRESSED                      | Vivo (Telefônica Brasil)
    #8   | AS61832  | 257        | REGRESSED                      | Giga+ Empresas
    #9   | AS28283  | 215        | PARTIAL: VULNERABLE (Mixed)    | Adyl Telecom
    #10  | AS271253 | 199        | PARTIAL: VULNERABLE (Mixed)    | LINK BRASIL TELECOMUNICACOES LTDA
    #11  | AS11432  | 194        | PARTIAL: VULNERABLE (Mixed)    | Telium Telecomunicações Ltda
    #12  | AS61568  | 187        | REGRESSED                      | ALOO TELECOM - FSF TECNOLOGIA SA
    #13  | AS13786  | 173        | ACTIVE LOCAL ROV               | Seaborn (Seabras USA, LLC)
    #14  | AS53013  | 172        | VULNERABLE                     | Ufinet Brasil (WixNet do Brasil)
    #15  | AS267613 | 160        | ACTIVE LOCAL ROV               | ELETRONET S.A.
    #16  | AS23106  | 157        | REGRESSED                      | American Tower Brasil
    #17  | AS22381  | 150        | PARTIAL: VULNERABLE (Mixed)    | SAMM (Megatelecom)
    #18  | AS52965  | 147        | PARTIAL: VULNERABLE (Mixed)    | 1Telecom
    #19  | AS53181  | 144        | REGRESSED                      | Avanca Telecom e Servicos LTDA
    #20  | AS269096 | 135        | REGRESSED                      | NORTH TECNOLOGIA

    ====================================================================================================
     IPv6 DIFFERENCES (BR networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS7738   | PARTIAL: VULNERABLE (Mixed)    | Unverified (Transit/Peer?)     | 0/0            | V.tal (fka Telemar)
    AS22381  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | SAMM (Megatelecom)
    AS28368  | Unverified (Transit/Peer?)     | VOLATILE                       | 0/1            | Wirelink (Sobralnet)
    AS28220  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | Alares Internet
    AS262761 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Sinal Br Telecom Ltda
    AS262355 | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/5            | VSX Networks
    AS271493 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 44/44          | SPEED NET PEDRA
    AS53180  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | INFORTEL COMUNICACOES LTDA
    AS28189  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NOVVACORE
    AS53158  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Net Turbo Telecom
    AS265482 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NET EXPRESS BRASIL LTDA - ME
    AS61599  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | EAI TELECOMUNICACOES LTDA
    AS273421 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | MAZA Telecom
    AS52613  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | GIGA MAIS FIBRA TELECOMUNICACOES S.A.
    AS264567 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Loop Fibra
    AS263649 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | BrPhonia Provedor Ip Ltda
    AS263395 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | TINASNET SERVICOS E ACESSOS A INTERNET L
    AS272193 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 4/4            | Fly Conecta Internet LTDA
    AS52559  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | NOVATEC TELECOM LTDA
    AS53038  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | IDC19 - WDI SOLUCOES EM TEC INFORMACAO L
    AS16685  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | TIVIT TERCEIRIZAÇÃO DE PROCESSOS, SERV. 
    AS262952 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | LIFE.IN TELECOM
    AS263080 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | GTi TELECOMUNICACOES S/A
    AS28306  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Voluy Telecom Eireli
    AS267158 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | MG NET TELECOMUNICACOES LTDA ­ ME
    AS263584 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 8/9            | WanHouse Solucoes em Tecnologia LTDA - E
    AS262828 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Acesse Facil Telecomunicacoes Ltda
    AS28257  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | CONCEITOS NET SERVICOS DE COMUNICACAO E 
    AS53142  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | Friburgo Online LTDA ME
    AS273490 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | FIBRION INTERNET LTDA
