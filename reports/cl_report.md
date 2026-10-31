    [*] Loading Global Audit for CL...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: CL (Chile)
    ====================================================================================================
    Total Networks:      403
    Total Cone Gravity:  300
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    49 (12.2%) -> Protects 16.3% of Traffic
    VULNERABLE NETWORKS:       271 (67.2%) -> Exposes  67.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        128 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    19 (14.8%)   IPv6 verdict    32 (25.0%)
      VULNERABLE main verdict   104 (81.2%)   IPv6 verdict    93 (72.7%)

    ====================================================================================================
     THE CL CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS263702 | REGRESSED                      | REGRESSED                      | 66       | 0%     | GRUPO ZGH SPA
    AS14259  | REGRESSED                      | REGRESSED                      | 61       | 1%     | Gtd Internet S.A.
    AS7004   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 29       | 98%    | TELEFÓNICA CHILE S.A.
    AS16629  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 19       | 98%    | CTC. CORP S.A. (TELEFONICA EMPRESAS)
    AS6471   | Unverified (Transit/Peer?)     | -                              | 18       | -      | ENTEL CHILE S.A.
    AS61503  | REGRESSED                      | REGRESSED                      | 18       | 0%     | SERVICIOS DE TELECOMUNICACIONES INTERCAB
    AS6429   | REGRESSED                      | REGRESSED                      | 18       | 1%     | Telmex Chile Internet S.A.
    AS263237 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 13       | -      | PowerHost Telecom SPA
    AS266771 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 10       | 73%    | MAKRONET CONSULTING TECNOLOGIA E INFORMA
    AS14117  | REGRESSED                      | REGRESSED                      | 8        | 0%     | Telefonica del Sur S.A.
    AS265757 | REGRESSED                      | REGRESSED                      | 7        | 0%     | Intersur Limitada
    AS11340  | REGRESSED                      | -                              | 6        | 2%     | Red Universitaria Nacional
    AS264827 | REGRESSED                      | REGRESSED                      | 5        | -      | WIRCOM S.P.A.
    AS64139  | REGRESSED                      | REGRESSED                      | 4        | 0%     | GRUPO METROWAN TELECOM SPA
    AS10778  | PARTIAL: VULNERABLE (Mixed)    | -                              | 4        | -      | MCL Internet
    AS266830 | REGRESSED                      | REGRESSED                      | 3        | 0%     | AIRPOINT TELECOMUNICACIONES LIMITADA
    AS27901  | REGRESSED                      | REGRESSED                      | 3        | 0%     | Pacifico Cable SPA.
    AS262237 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 3        | -      | Orbyta S.A.
    AS27986  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 2        | -      | ENTEL CHILE S.A.
    AS27659  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1        | -      | Ingeniería e Informática Asociada Ltda (

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to CL?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS14259  | 54         | REGRESSED                      | Gtd Internet S.A.
    #2   | AS263702 | 46         | REGRESSED                      | GRUPO ZGH SPA
    #3   | AS7004   | 33         | ACTIVE LOCAL ROV               | TELEFÓNICA CHILE S.A.
    #4   | AS3549   | 26         | ACTIVE LOCAL ROV               | Lumen (fka. Global Crossing)
    #5   | AS6429   | 22         | REGRESSED                      | Telmex Chile Internet S.A.
    #6   | AS174    | 21         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #7   | AS3356   | 21         | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #8   | AS6471   | 20         | Unverified (Transit/Peer?)     | ENTEL CHILE S.A.
    #9   | AS263237 | 18         | PARTIAL: VULNERABLE (Mixed)    | PowerHost Telecom SPA
    #10  | AS7049   | 18         | REGRESSED                      | Silica Networks Argentina S.A.
    #11  | AS16629  | 17         | ACTIVE LOCAL ROV               | CTC. CORP S.A. (TELEFONICA EMPRESAS)
    #12  | AS7195   | 14         | ACTIVE LOCAL ROV               | EdgeUno
    #13  | AS61503  | 14         | REGRESSED                      | SERVICIOS DE TELECOMUNICACIONES INTERCAB
    #14  | AS12956  | 12         | CORE: ACTIVE PROTECTOR         | Telxius (Telefonica Global)
    #15  | AS18747  | 12         | PARTIAL: VULNERABLE (Mixed)    | IFX Corporation
    #16  | AS266771 | 12         | PARTIAL: VULNERABLE (Mixed)    | MAKRONET CONSULTING TECNOLOGIA E INFORMA
    #17  | AS262589 | 11         | PARTIAL: VULNERABLE (Mixed)    | SAMM (Internexa)
    #18  | AS266830 | 11         | REGRESSED                      | AIRPOINT TELECOMUNICACIONES LIMITADA
    #19  | AS52468  | 10         | PASSIVE (Clean Pipe)           | UFINET PANAMA S.A.
    #20  | AS14117  | 9          | REGRESSED                      | Telefonica del Sur S.A.

    ====================================================================================================
     IPv6 DIFFERENCES (CL networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS27986  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | ENTEL CHILE S.A.
    AS267848 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Mainstreet Ltda
    AS270024 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ICONEX SPA
    AS270008 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SOCIEDAD COMERCIAL Y DE SERVICIOS DE INT
    AS263784 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | BYNARYA SPA
    AS265703 | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/3            | AUSTRO INTERNET S.A.
    AS265743 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | COMERCIAL WASHINGTON ERNESTO OYARCE SAZO
    AS264814 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | BITRED GROUP SPA
    AS23140  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Universidad de Chile
    AS22047  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | VTR BANDA ANCHA S.A.
    AS20191  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Pontificia Universidad Catolica de Chile
    AS27978  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Telmex Servicios Empresariales S.A.
    AS61506  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Insacom y Cia. Limitada
    AS61526  | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | PIT CHILE SP
    AS52489  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TELEFÓNICA CHILE S.A.
