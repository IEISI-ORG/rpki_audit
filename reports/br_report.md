    [*] Loading Global Audit for BR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: BR (Brazil)
    ====================================================================================================
    Total Networks:      9,192
    Total Cone Gravity:  23,425
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   354 ( 3.9%) -> Protects 20.1% of Traffic
    VULNERABLE NETWORKS:      8354 (90.9%) -> Exposes  71.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        7,645 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   297 ( 3.9%)   IPv6 verdict   436 ( 5.7%)
      VULNERABLE main verdict  7241 (94.7%)   IPv6 verdict  7114 (93.1%)

    ====================================================================================================
     THE BR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS16735  | VOLATILE                       | VOLATILE                       | 2315     | 79%    | Algar Telecom
    AS14840  | REGRESSED                      | REGRESSED                      | 2246     | 1%     | BR.DIGITAL 
    AS53062  | REGRESSED                      | REGRESSED                      | 1565     | 0%     | ACESSOLINE TELECOMUNICACOES LTDA
    AS4230   | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 984      | 18%    | Claro (Embratel)
    AS61832  | REGRESSED                      | REGRESSED                      | 811      | 0%     | Giga+ Empresas
    AS61568  | REGRESSED                      | REGRESSED                      | 540      | 3%     | ALOO TELECOM - FSF TECNOLOGIA SA
    AS267613 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 534      | -      | ELETRONET S.A.
    AS10429  | REGRESSED                      | REGRESSED                      | 486      | 0%     | Vivo (Telefônica Brasil)
    AS271253 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 468      | 94%    | LINK BRASIL TELECOMUNICACOES LTDA
    AS28283  | REGRESSED                      | REGRESSED                      | 467      | 0%     | Adyl Telecom
    AS7738   | REGRESSED                      | REGRESSED                      | 333      | 0%     | V.tal (fka Telemar)
    AS264409 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 315      | -      | Huge Networks
    AS52965  | REGRESSED                      | REGRESSED                      | 286      | 6%     | 1Telecom
    AS22381  | REGRESSED                      | REGRESSED                      | 270      | 1%     | SAMM (Megatelecom)
    AS11432  | REGRESSED                      | REGRESSED                      | 246      | 0%     | Telium Telecomunicações Ltda
    AS53181  | REGRESSED                      | REGRESSED                      | 246      | 0%     | Avanca Telecom e Servicos LTDA
    AS263009 | REGRESSED                      | REGRESSED                      | 245      | 0%     | FORTE TELECOM LTDA.
    AS23106  | REGRESSED                      | REGRESSED                      | 242      | 0%     | American Tower Brasil
    AS53087  | REGRESSED                      | REGRESSED                      | 231      | 1%     | TELY Ltda.
    AS28368  | REGRESSED                      | REGRESSED                      | 226      | 0%     | Wirelink (Sobralnet)

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to BR?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS3356   | 534        | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #2   | AS16735  | 530        | VOLATILE                       | Algar Telecom
    #3   | AS14840  | 480        | REGRESSED                      | BR.DIGITAL 
    #4   | AS52468  | 450        | PASSIVE (Clean Pipe)           | UFINET PANAMA S.A.
    #5   | AS53062  | 393        | REGRESSED                      | ACESSOLINE TELECOMUNICACOES LTDA
    #6   | AS4230   | 341        | PASSIVE (Clean Pipe)           | Claro (Embratel)
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
    AS262355 | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/5            | VSX Networks
    AS53158  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Net Turbo Telecom
    AS28189  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NOVVACORE
    AS61599  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | EAI TELECOMUNICACOES LTDA
    AS28666  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | HostLocation Ltda
    AS28663  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | FLYS INTERATIVA LTDA
    AS273421 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | MAZA Telecom
    AS265436 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | SkyNet Telecomunicações
    AS16685  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | TIVIT TERCEIRIZAÇÃO DE PROCESSOS, SERV. 
    AS272713 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | CDN Star Ltda
    AS267056 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | EVEREST RIDGE DO BRASIL LTDA
    AS263457 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | Alpinet Informática Ltda
    AS28352  | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | NETSPEED LTDA
    AS267638 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Wind Telecomunicação do Brasil Ltda - ME
    AS28257  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | CONCEITOS NET SERVICOS DE COMUNICACAO E 
    AS53162  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Go! Telecom
    AS273461 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Atjp Corp
    AS272451 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | UltraIP Telecom
    AS262708 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Bit Fibra
    AS262609 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | CL9 Tecnologias Ltda.
    AS270711 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Cloud Telecom LTDA
    AS268047 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Masterinfo Internet
    AS267321 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NTISP TELECOM
    AS265188 | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | Grupo WCM net
    AS267460 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | ALLNET TELECOMUNICAÇÕES EIRELE ME
    AS263471 | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Intervel Informatica Ltda
    AS269039 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | CONNECTIONS TELECOM LTDA
    AS272786 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | X99 INTERNET
    AS61624  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | ISPSHIELD (InfNOC Tecnologia)
    AS268321 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Pontual Telecom
