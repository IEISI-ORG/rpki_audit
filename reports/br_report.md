    [*] Loading Global Audit for BR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: BR (Brazil)
    ====================================================================================================
    Total Networks:      9,180
    Total Cone Gravity:  22,937
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   396 ( 4.3%) -> Protects 17.1% of Traffic
    VULNERABLE NETWORKS:      8300 (90.4%) -> Exposes  73.7% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        7,614 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   325 ( 4.3%)   IPv6 verdict   488 ( 6.4%)
      VULNERABLE main verdict  7192 (94.5%)   IPv6 verdict  7044 (92.5%)

    ====================================================================================================
     THE BR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS16735  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 2431     | 67%    | Algar Telecom
    AS14840  | REGRESSED                      | REGRESSED                      | 1862     | 0%     | BR.DIGITAL 
    AS53062  | REGRESSED                      | REGRESSED                      | 1659     | 0%     | ACESSOLINE TELECOMUNICACOES LTDA
    AS4230   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 983      | 22%    | Claro (Embratel)
    AS61832  | REGRESSED                      | REGRESSED                      | 691      | 0%     | Giga+ Empresas
    AS61568  | REGRESSED                      | REGRESSED                      | 542      | 2%     | ALOO TELECOM - FSF TECNOLOGIA SA
    AS10429  | REGRESSED                      | REGRESSED                      | 532      | 0%     | Vivo (Telefônica Brasil)
    AS267613 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 523      | 1%     | ELETRONET S.A.
    AS271253 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 505      | 95%    | LINK BRASIL TELECOMUNICACOES LTDA
    AS28283  | REGRESSED                      | REGRESSED                      | 420      | 0%     | Adyl Telecom
    AS7738   | REGRESSED                      | REGRESSED                      | 328      | 0%     | V.tal (fka Telemar)
    AS264409 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 312      | -      | Huge Networks
    AS22381  | REGRESSED                      | REGRESSED                      | 285      | 4%     | SAMM (Megatelecom)
    AS52965  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 283      | 14%    | 1Telecom
    AS263009 | REGRESSED                      | REGRESSED                      | 245      | 11%    | FORTE TELECOM LTDA.
    AS23106  | REGRESSED                      | REGRESSED                      | 243      | 0%     | American Tower Brasil
    AS11432  | REGRESSED                      | REGRESSED                      | 242      | 0%     | Telium Telecomunicações Ltda
    AS53087  | REGRESSED                      | REGRESSED                      | 234      | 1%     | TELY Ltda.
    AS53181  | REGRESSED                      | REGRESSED                      | 231      | 0%     | Avanca Telecom e Servicos LTDA
    AS28368  | REGRESSED                      | REGRESSED                      | 225      | 0%     | Wirelink (Sobralnet)

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to BR?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS3356   | 534        | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #2   | AS16735  | 530        | ACTIVE LOCAL ROV               | Algar Telecom
    #3   | AS14840  | 480        | REGRESSED                      | BR.DIGITAL 
    #4   | AS52468  | 450        | PASSIVE (Clean Pipe)           | UFINET PANAMA S.A.
    #5   | AS53062  | 393        | REGRESSED                      | ACESSOLINE TELECOMUNICACOES LTDA
    #6   | AS4230   | 341        | VULNERABLE (Atlas Verified)    | Claro (Embratel)
    #7   | AS10429  | 269        | REGRESSED                      | Vivo (Telefônica Brasil)
    #8   | AS61832  | 257        | REGRESSED                      | Giga+ Empresas
    #9   | AS28283  | 216        | REGRESSED                      | Adyl Telecom
    #10  | AS271253 | 199        | ACTIVE LOCAL ROV               | LINK BRASIL TELECOMUNICACOES LTDA
    #11  | AS11432  | 194        | REGRESSED                      | Telium Telecomunicações Ltda
    #12  | AS61568  | 187        | REGRESSED                      | ALOO TELECOM - FSF TECNOLOGIA SA
    #13  | AS13786  | 173        | ACTIVE LOCAL ROV               | Seaborn (Seabras USA, LLC)
    #14  | AS53013  | 172        | VULNERABLE                     | Ufinet Brasil (WixNet do Brasil)
    #15  | AS267613 | 160        | PARTIAL: VULNERABLE (Mixed)    | ELETRONET S.A.
    #16  | AS23106  | 157        | REGRESSED                      | American Tower Brasil
    #17  | AS22381  | 150        | REGRESSED                      | SAMM (Megatelecom)
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
    AS28189  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NOVVACORE
    AS53158  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Net Turbo Telecom
    AS264556 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Liberty Fibra
    AS61599  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | EAI TELECOMUNICACOES LTDA
    AS264170 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Winet Brasil
    AS28663  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | FLYS INTERATIVA LTDA
    AS273421 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | MAZA Telecom
    AS265436 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | SkyNet Telecomunicações
    AS52630  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | MOTTANET  TI  - SERVICOS  DE TECNOLOGIA 
    AS28306  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Voluy Telecom Eireli
    AS28352  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | NETSPEED LTDA
    AS16685  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | TIVIT TERCEIRIZAÇÃO DE PROCESSOS, SERV. 
    AS263457 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | Alpinet Informática Ltda
    AS53038  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | IDC19 - WDI SOLUCOES EM TEC INFORMACAO L
    AS267056 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | EVEREST RIDGE DO BRASIL LTDA
    AS273490 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | FIBRION INTERNET LTDA
    AS273461 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Atjp Corp
    AS28257  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | CONCEITOS NET SERVICOS DE COMUNICACAO E 
    AS272451 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | UltraIP Telecom
    AS267638 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Wind Telecomunicação do Brasil Ltda - ME
    AS263471 | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Intervel Informatica Ltda
    AS265188 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Grupo WCM net
    AS267460 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | ALLNET TELECOMUNICAÇÕES EIRELE ME
    AS262609 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | CL9 Tecnologias Ltda.
    AS268047 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Masterinfo Internet
    AS53162  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Go! Telecom
    AS269039 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | CONNECTIONS TELECOM LTDA
    AS61624  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | ISPSHIELD (InfNOC Tecnologia)
    AS266399 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | NUDOZE TELECOMUNICACOES EIRELI
    AS272786 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | X99 INTERNET
