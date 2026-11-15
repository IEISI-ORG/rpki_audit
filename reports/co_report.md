    [*] Loading Global Audit for CO...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: CO (Colombia)
    ====================================================================================================
    Total Networks:      533
    Total Cone Gravity:  2,389
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    44 ( 8.3%) -> Protects 81.2% of Traffic
    VULNERABLE NETWORKS:       380 (71.3%) -> Exposes  11.7% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        326 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    24 ( 7.4%)   IPv6 verdict    33 (10.1%)
      VULNERABLE main verdict   297 (91.1%)   IPv6 verdict   290 (89.0%)

    ====================================================================================================
     THE CO CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS7195   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1826     | 87%    | EdgeUno
    AS18678  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 142      | 8%     | INTERNEXA S.A. E.S.P
    AS52320  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 114      | -      | V.tal (GlobeNet)
    AS262191 | REGRESSED                      | REGRESSED                      | 56       | 1%     | LIBERTY NETWORKS DE COLOMBIA S.A.S
    AS27951  | REGRESSED                      | REGRESSED                      | 54       | 1%     | Media Commerce Partners S.A
    AS3816   | REGRESSED                      | REGRESSED                      | 46       | 4%     | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC
    AS262186 | REGRESSED                      | REGRESSED                      | 31       | 2%     | TV AZTECA SUCURSAL COLOMBIA
    AS14080  | REGRESSED                      | REGRESSED                      | 25       | 31%    | Telmex Colombia S.A.
    AS13489  | REGRESSED                      | REGRESSED                      | 25       | 0%     | EPM Telecomunicaciones S.A. E.S.P.
    AS273103 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 20       | 97%    | TV&MÁS S.A.S
    AS19429  | REGRESSED                      | REGRESSED                      | 13       | 4%     | ETB - Colombia
    AS267708 | REGRESSED                      | REGRESSED                      | 8        | 0%     | SP SISTEMAS PALACIOS LTDA
    AS267823 | REGRESSED                      | REGRESSED                      | 5        | 0%     | ATENEA TELECOMUNICACIONES S.A.S
    AS265688 | REGRESSED                      | REGRESSED                      | 5        | 17%    | SINERGY SOLUCIONES INTEGRALES
    AS270075 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 5        | 1%     | SUPER REDES S.A.S
    AS272156 | REGRESSED                      | REGRESSED                      | 3        | 1%     | WEB MASTER COLOMBIA SAS
    AS273168 | VULNERABLE                     | VULNERABLE                     | 3        | -      | INFRAESTRUCTURA Y REDES SAS
    AS273020 | REGRESSED                      | REGRESSED                      | 2        | 1%     | IN QUALITY TELECOMUNICATIONS S.A.S. ZOMA
    AS269804 | VULNERABLE                     | VULNERABLE                     | 1        | 0%     | SEPCOM COMUNICACIONES SAS
    AS272851 | REGRESSED                      | REGRESSED                      | 1        | 4%     | GIGA FIBRA SAS

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
    #14  | AS23520  | 18         | PARTIAL: VULNERABLE (Mixed)    | Columbus Networks USA, Inc.
    #15  | AS52320  | 15         | ACTIVE LOCAL ROV               | V.tal (GlobeNet)
    #16  | AS174    | 13         | INCONSISTENT                   | Cogent Communications, LLC
    #17  | AS18747  | 10         | PARTIAL: VULNERABLE (Mixed)    | IFX Corporation
    #18  | AS267708 | 9          | REGRESSED                      | SP SISTEMAS PALACIOS LTDA
    #19  | AS10753  | 8          | PARTIAL: VULNERABLE (Mixed)    | Level 3 Parent, LLC
    #20  | AS273103 | 8          | PARTIAL: VULNERABLE (Mixed)    | TV&MÁS S.A.S

    ====================================================================================================
     IPv6 DIFFERENCES (CO networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS270075 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | SUPER REDES S.A.S
    AS271957 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | SOMOS NETWORKS COLOMBIA S.A.S. BIC
    AS7087   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Administración de Redes Colomsat S.A.
    AS27941  | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CONSULNETWORK LTDA
    AS266860 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CONEXION DIGITAL EXPRESS S.A.S.
    AS267832 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | VELONET SAS
    AS271952 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | UNICABLE H.D. SAS
    AS272896 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | COMSSET COMUNICACIONES SAS
    AS273212 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SISTEMAS, TELECOMUNICACIONES Y BIOMEDICO
