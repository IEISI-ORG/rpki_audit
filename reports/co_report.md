    [*] Loading Global Audit for CO...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: CO (Colombia)
    ====================================================================================================
    Total Networks:      531
    Total Cone Gravity:  2,404
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    47 ( 8.9%) -> Protects 81.6% of Traffic
    VULNERABLE NETWORKS:       382 (71.9%) -> Exposes  11.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        329 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    26 ( 7.9%)   IPv6 verdict    36 (10.9%)
      VULNERABLE main verdict   300 (91.2%)   IPv6 verdict   292 (88.8%)

    ====================================================================================================
     THE CO CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS7195   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1832     | 93%    | EdgeUno
    AS18678  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 152      | 7%     | INTERNEXA S.A. E.S.P
    AS52320  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 111      | -      | V.tal (GlobeNet)
    AS262191 | REGRESSED                      | REGRESSED                      | 58       | 2%     | LIBERTY NETWORKS DE COLOMBIA S.A.S
    AS27951  | REGRESSED                      | REGRESSED                      | 53       | 0%     | Media Commerce Partners S.A
    AS3816   | REGRESSED                      | REGRESSED                      | 47       | 4%     | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC
    AS262186 | REGRESSED                      | REGRESSED                      | 32       | 0%     | TV AZTECA SUCURSAL COLOMBIA
    AS13489  | REGRESSED                      | REGRESSED                      | 25       | 0%     | EPM Telecomunicaciones S.A. E.S.P.
    AS14080  | REGRESSED                      | REGRESSED                      | 25       | 31%    | Telmex Colombia S.A.
    AS273103 | VOLATILE                       | VOLATILE                       | 19       | 68%    | TV&MÁS S.A.S
    AS19429  | REGRESSED                      | REGRESSED                      | 14       | 10%    | ETB - Colombia
    AS267708 | REGRESSED                      | REGRESSED                      | 8        | 1%     | SP SISTEMAS PALACIOS LTDA
    AS270075 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 5        | 0%     | SUPER REDES S.A.S
    AS267823 | REGRESSED                      | REGRESSED                      | 5        | 0%     | ATENEA TELECOMUNICACIONES S.A.S
    AS265688 | REGRESSED                      | REGRESSED                      | 5        | 25%    | SINERGY SOLUCIONES INTEGRALES
    AS272156 | REGRESSED                      | REGRESSED                      | 3        | 0%     | WEB MASTER COLOMBIA SAS
    AS273168 | VULNERABLE                     | VULNERABLE                     | 3        | -      | INFRAESTRUCTURA Y REDES SAS
    AS273020 | REGRESSED                      | REGRESSED                      | 2        | 13%    | IN QUALITY TELECOMUNICATIONS S.A.S. ZOMA
    AS269804 | VULNERABLE                     | VULNERABLE                     | 1        | 1%     | SEPCOM COMUNICACIONES SAS
    AS26619  | REGRESSED                      | REGRESSED                      | 1        | 1%     | GTD COLOMBIA S.A.S

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
    #13  | AS19429  | 20         | REGRESSED                      | ETB - Colombia
    #14  | AS23520  | 18         | INCONSISTENT                   | Columbus Networks USA, Inc.
    #15  | AS52320  | 15         | ACTIVE LOCAL ROV               | V.tal (GlobeNet)
    #16  | AS174    | 13         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #17  | AS18747  | 10         | PARTIAL: VULNERABLE (Mixed)    | IFX Corporation
    #18  | AS267708 | 9          | REGRESSED                      | SP SISTEMAS PALACIOS LTDA
    #19  | AS10753  | 8          | ACTIVE LOCAL ROV               | Level 3 Parent, LLC
    #20  | AS273103 | 8          | VOLATILE                       | TV&MÁS S.A.S

    ====================================================================================================
     IPv6 DIFFERENCES (CO networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS270075 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | SUPER REDES S.A.S
    AS271957 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | SOMOS NETWORKS COLOMBIA S.A.S. BIC
    AS273001 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TELECOMUNICACIONES DEL CATATUMBO S.A.S
    AS272896 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | COMSSET COMUNICACIONES SAS
    AS273131 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NETSLINK SAS
    AS271952 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | UNICABLE H.D. SAS
    AS266860 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CONEXION DIGITAL EXPRESS S.A.S.
    AS267832 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | VELONET SAS
    AS27941  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CONSULNETWORK LTDA
    AS7087   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Administración de Redes Colomsat S.A.
