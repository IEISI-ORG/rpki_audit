    [*] Loading Global Audit for CL...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: CL (Chile)
    ====================================================================================================
    Total Networks:      405
    Total Cone Gravity:  291
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    51 (12.6%) -> Protects 16.8% of Traffic
    VULNERABLE NETWORKS:       270 (66.7%) -> Exposes  71.1% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        125 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    19 (15.2%)   IPv6 verdict    31 (24.8%)
      VULNERABLE main verdict   102 (81.6%)   IPv6 verdict    92 (73.6%)

    ====================================================================================================
     THE CL CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS263702 | REGRESSED                      | REGRESSED                      | 64       | 0%     | GRUPO ZGH SPA
    AS14259  | INCONSISTENT                   | INCONSISTENT                   | 59       | 0%     | Gtd Internet S.A.
    AS7004   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 29       | 95%    | TELEFÓNICA CHILE S.A.
    AS16629  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 19       | 98%    | CTC. CORP S.A. (TELEFONICA EMPRESAS)
    AS6471   | Unverified (Transit/Peer?)     | -                              | 18       | 7%     | ENTEL CHILE S.A.
    AS61503  | REGRESSED                      | REGRESSED                      | 18       | 0%     | SERVICIOS DE TELECOMUNICACIONES INTERCAB
    AS6429   | REGRESSED                      | REGRESSED                      | 15       | 3%     | Telmex Chile Internet S.A.
    AS263237 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 12       | -      | PowerHost Telecom SPA
    AS266771 | REGRESSED                      | REGRESSED                      | 9        | 6%     | MAKRONET CONSULTING TECNOLOGIA E INFORMA
    AS14117  | REGRESSED                      | REGRESSED                      | 8        | 0%     | Telefonica del Sur S.A.
    AS265757 | REGRESSED                      | REGRESSED                      | 6        | 0%     | Intersur Limitada
    AS11340  | REGRESSED                      | -                              | 6        | 1%     | Red Universitaria Nacional
    AS264827 | REGRESSED                      | REGRESSED                      | 5        | 0%     | WIRCOM S.P.A.
    AS64139  | REGRESSED                      | REGRESSED                      | 5        | 0%     | GRUPO METROWAN TELECOM SPA
    AS10778  | REGRESSED                      | -                              | 4        | -      | MCL Internet
    AS266830 | REGRESSED                      | REGRESSED                      | 3        | 0%     | AIRPOINT TELECOMUNICACIONES LIMITADA
    AS262237 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 3        | -      | Orbyta S.A.
    AS27901  | REGRESSED                      | REGRESSED                      | 3        | 0%     | Pacifico Cable SPA.
    AS27986  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 2        | -      | ENTEL CHILE S.A.
    AS271869 | REGRESSED                      | REGRESSED                      | 1        | 0%     | SERVICIOS ZONALES DE INTERNET LIMITADA

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to CL?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS14259  | 54         | INCONSISTENT                   | Gtd Internet S.A.
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
    #16  | AS266771 | 12         | REGRESSED                      | MAKRONET CONSULTING TECNOLOGIA E INFORMA
    #17  | AS262589 | 11         | PARTIAL: VULNERABLE (Mixed)    | SAMM (Internexa)
    #18  | AS266830 | 11         | REGRESSED                      | AIRPOINT TELECOMUNICACIONES LIMITADA
    #19  | AS52468  | 10         | PARTIAL: VULNERABLE (Mixed)    | UFINET PANAMA S.A.
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
    AS264806 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TNA Solutions SpA
    AS264780 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HomeNet LTDA
    AS263784 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | BYNARYA SPA
    AS265743 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | COMERCIAL WASHINGTON ERNESTO OYARCE SAZO
    AS27978  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Telmex Servicios Empresariales S.A.
    AS23140  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Universidad de Chile
    AS20191  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Pontificia Universidad Catolica de Chile
    AS61506  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Insacom y Cia. Limitada
    AS61526  | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | PIT CHILE SP
    AS52489  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TELEFÓNICA CHILE S.A.
