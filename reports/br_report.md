    [*] Loading Global Audit for BR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: BR (Brazil)
    ====================================================================================================
    Total Networks:      9,195
    Total Cone Gravity:  22,622
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   357 ( 3.9%) -> Protects 15.1% of Traffic
    VULNERABLE NETWORKS:      8339 (90.7%) -> Exposes  74.4% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        7,632 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   304 ( 4.0%)   IPv6 verdict   463 ( 6.1%)
      VULNERABLE main verdict  7220 (94.6%)   IPv6 verdict  7076 (92.7%)

    ====================================================================================================
     THE BR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS14840  | REGRESSED                      | REGRESSED                      | 2010     | 0%     | BR.DIGITAL 
    AS16735  | VOLATILE                       | VOLATILE                       | 1949     | 93%    | Algar Telecom
    AS53062  | REGRESSED                      | REGRESSED                      | 1820     | 0%     | ACESSOLINE TELECOMUNICACOES LTDA
    AS4230   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 914      | 29%    | Claro (Embratel)
    AS61832  | REGRESSED                      | REGRESSED                      | 781      | 0%     | Giga+ Empresas
    AS267613 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 505      | -      | ELETRONET S.A.
    AS28283  | REGRESSED                      | REGRESSED                      | 474      | 0%     | Adyl Telecom
    AS61568  | REGRESSED                      | REGRESSED                      | 465      | 2%     | ALOO TELECOM - FSF TECNOLOGIA SA
    AS10429  | REGRESSED                      | REGRESSED                      | 451      | 0%     | Vivo (Telefônica Brasil)
    AS271253 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 433      | 90%    | LINK BRASIL TELECOMUNICACOES LTDA
    AS22381  | REGRESSED                      | REGRESSED                      | 363      | 2%     | SAMM (Megatelecom)
    AS7738   | REGRESSED                      | REGRESSED                      | 330      | 0%     | V.tal (fka Telemar)
    AS264409 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 296      | -      | Huge Networks
    AS28368  | Unverified (Transit/Peer?)     | VOLATILE                       | 272      | -      | Wirelink (Sobralnet)
    AS52965  | REGRESSED                      | REGRESSED                      | 265      | 9%     | 1Telecom
    AS53181  | REGRESSED                      | REGRESSED                      | 249      | 0%     | Avanca Telecom e Servicos LTDA
    AS263009 | REGRESSED                      | REGRESSED                      | 242      | 0%     | FORTE TELECOM LTDA.
    AS11432  | REGRESSED                      | REGRESSED                      | 242      | 0%     | Telium Telecomunicações Ltda
    AS23106  | REGRESSED                      | REGRESSED                      | 220      | 0%     | American Tower Brasil
    AS28146  | REGRESSED                      | REGRESSED                      | 213      | 0%     | MHNET TELECOM

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
    #6   | AS4230   | 341        | VULNERABLE (Atlas Verified)    | Claro (Embratel)
    #7   | AS10429  | 269        | REGRESSED                      | Vivo (Telefônica Brasil)
    #8   | AS61832  | 257        | REGRESSED                      | Giga+ Empresas
    #9   | AS28283  | 215        | REGRESSED                      | Adyl Telecom
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
    AS28368  | Unverified (Transit/Peer?)     | VOLATILE                       | 0/1            | Wirelink (Sobralnet)
    AS53158  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Net Turbo Telecom
    AS265482 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | NET EXPRESS BRASIL LTDA - ME
    AS28663  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | FLYS INTERATIVA LTDA
    AS273421 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | MAZA Telecom
    AS28605  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | Defferrari Informatica Ltda.
    AS28352  | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | NETSPEED LTDA
    AS53038  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | IDC19 - WDI SOLUCOES EM TEC INFORMACAO L
    AS16685  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | TIVIT TERCEIRIZAÇÃO DE PROCESSOS, SERV. 
    AS263080 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | GTi TELECOMUNICACOES S/A
    AS264013 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | CONNECTA TELECOM INTERNET LTDA - EPP
    AS266103 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | AGILITY TELECOM
    AS272713 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | CDN Star Ltda
    AS273461 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Atjp Corp
    AS28257  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | CONCEITOS NET SERVICOS DE COMUNICACAO E 
    AS28219  | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/3            | Net Rosas Telecomunicações Ltda.
    AS262609 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | CL9 Tecnologias Ltda.
    AS61624  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | ISPSHIELD (InfNOC Tecnologia)
    AS262708 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Bit Fibra
    AS263471 | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Intervel Informatica Ltda
    AS267321 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | NTISP TELECOM
    AS267460 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | ALLNET TELECOMUNICAÇÕES EIRELE ME
    AS268047 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | Masterinfo Internet
    AS53162  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Go! Telecom
    AS52877  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | TUPIX INTERNET EXCHANGE
    AS269244 | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | DEAN MURILO GONCALVES OLIVEIRA - ME
    AS269039 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | CONNECTIONS TELECOM LTDA
    AS52778  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | VILANET INFORMÁTICA
    AS272786 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | X99 INTERNET
    AS11271  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SENCINET LATAM BRASIL LTDA
