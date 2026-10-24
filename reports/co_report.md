    [*] Loading Global Audit for CO...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: CO (Colombia)
    ====================================================================================================
    Total Networks:      528
    Total Cone Gravity:  2,408
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    55 (10.4%) -> Protects 82.5% of Traffic
    VULNERABLE NETWORKS:       370 (70.1%) -> Exposes  10.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        320 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    33 (10.3%)   IPv6 verdict    43 (13.4%)
      VULNERABLE main verdict   284 (88.8%)   IPv6 verdict   275 (85.9%)

    ====================================================================================================
     THE CO CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS7195   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1835     | 96%    | EdgeUno
    AS18678  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 155      | 7%     | INTERNEXA S.A. E.S.P
    AS52320  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 116      | -      | V.tal (GlobeNet)
    AS262191 | REGRESSED                      | REGRESSED                      | 57       | 1%     | LIBERTY NETWORKS DE COLOMBIA S.A.S
    AS27951  | REGRESSED                      | REGRESSED                      | 50       | 0%     | Media Commerce Partners S.A
    AS3816   | REGRESSED                      | REGRESSED                      | 45       | 4%     | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC
    AS262186 | REGRESSED                      | REGRESSED                      | 31       | 0%     | TV AZTECA SUCURSAL COLOMBIA
    AS14080  | REGRESSED                      | REGRESSED                      | 26       | 36%    | Telmex Colombia S.A.
    AS13489  | REGRESSED                      | REGRESSED                      | 24       | 1%     | EPM Telecomunicaciones S.A. E.S.P.
    AS273103 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 19       | 95%    | TV&MÁS S.A.S
    AS19429  | VOLATILE                       | VOLATILE                       | 15       | 45%    | ETB - Colombia
    AS267708 | REGRESSED                      | REGRESSED                      | 7        | 0%     | SP SISTEMAS PALACIOS LTDA
    AS265688 | REGRESSED                      | REGRESSED                      | 5        | 35%    | SINERGY SOLUCIONES INTEGRALES
    AS270075 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 5        | 0%     | SUPER REDES S.A.S
    AS267823 | REGRESSED                      | REGRESSED                      | 5        | 0%     | ATENEA TELECOMUNICACIONES S.A.S
    AS269804 | VULNERABLE                     | VULNERABLE                     | 3        | 1%     | SEPCOM COMUNICACIONES SAS
    AS273168 | VULNERABLE                     | VULNERABLE                     | 2        | -      | INFRAESTRUCTURA Y REDES SAS
    AS272156 | REGRESSED                      | REGRESSED                      | 2        | 3%     | WEB MASTER COLOMBIA SAS
    AS273020 | REGRESSED                      | REGRESSED                      | 2        | 2%     | IN QUALITY TELECOMUNICATIONS S.A.S. ZOMA
    AS27845  | REGRESSED                      | REGRESSED                      | 1        | 7%     | Empresa de Recursos Tecnologicos S.A E.S

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to CO?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS18678  | 65         | PARTIAL: VULNERABLE (Mixed)    | INTERNEXA S.A. E.S.P
    #2   | AS52468  | 64         | PARTIAL: VULNERABLE (Mixed)    | UFINET PANAMA S.A.
    #3   | AS27951  | 48         | REGRESSED                      | Media Commerce Partners S.A
    #4   | AS262191 | 46         | REGRESSED                      | LIBERTY NETWORKS DE COLOMBIA S.A.S
    #5   | AS3549   | 46         | ACTIVE LOCAL ROV               | Lumen (fka. Global Crossing)
    #6   | AS3816   | 35         | REGRESSED                      | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC
    #7   | AS3356   | 33         | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #8   | AS262186 | 32         | REGRESSED                      | TV AZTECA SUCURSAL COLOMBIA
    #9   | AS262589 | 30         | PARTIAL: VULNERABLE (Mixed)    | SAMM (Internexa)
    #10  | AS13489  | 24         | REGRESSED                      | EPM Telecomunicaciones S.A. E.S.P.
    #11  | AS7195   | 23         | ACTIVE LOCAL ROV               | EdgeUno
    #12  | AS14080  | 23         | REGRESSED                      | Telmex Colombia S.A.
    #13  | AS19429  | 20         | VOLATILE                       | ETB - Colombia
    #14  | AS23520  | 18         | PARTIAL: VULNERABLE (Mixed)    | Columbus Networks USA, Inc.
    #15  | AS52320  | 15         | ACTIVE LOCAL ROV               | V.tal (GlobeNet)
    #16  | AS174    | 13         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #17  | AS18747  | 10         | PARTIAL: VULNERABLE (Mixed)    | IFX Corporation
    #18  | AS267708 | 9          | REGRESSED                      | SP SISTEMAS PALACIOS LTDA
    #19  | AS10753  | 8          | ACTIVE LOCAL ROV               | Level 3 Parent, LLC
    #20  | AS273103 | 8          | ACTIVE LOCAL ROV               | TV&MÁS S.A.S

    ====================================================================================================
     IPv6 DIFFERENCES (CO networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS270075 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | SUPER REDES S.A.S
    AS272896 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | COMSSET COMUNICACIONES SAS
    AS273131 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NETSLINK SAS
    AS273204 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | WIKI NETWORKS SAS
    AS267832 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | VELONET SAS
    AS266860 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CONEXION DIGITAL EXPRESS S.A.S.
    AS27941  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CONSULNETWORK LTDA
    AS5722   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Universidad Nacional de Colombia
    AS7087   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Administración de Redes Colomsat S.A.
    AS14187  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SENCINET LATAM COLOMBIA S.A.
