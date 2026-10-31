    [*] Loading Global Audit for ID...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ID (Indonesia)
    ====================================================================================================
    Total Networks:      4,082
    Total Cone Gravity:  10,301
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   129 ( 3.2%) -> Protects 9.3% of Traffic
    VULNERABLE NETWORKS:      2794 (68.4%) -> Exposes  63.3% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        841 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    34 ( 4.0%)   IPv6 verdict    82 ( 9.8%)
      VULNERABLE main verdict   776 (92.3%)   IPv6 verdict   741 (88.1%)

    ====================================================================================================
     THE ID CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS7713   | REGRESSED                      | REGRESSED                      | 3011     | 0%     | PT Telkom Indonesia Tbk
    AS136106 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 690      | -      | PT Mega Akses Persada
    AS4800   | REGRESSED                      | REGRESSED                      | 653      | 0%     | PT Aplikanusa Lintasarta
    AS23947  | VOLATILE                       | VOLATILE                       | 563      | -      | PT Mora Telematika Indonesia Tbk
    AS147094 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 547      | -      | PT Mitra Visioner Pratama
    AS138840 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 499      | 0%     | PT Parsaoran Global Datatrans
    AS38158  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 333      | -      | PT Cyberindo Aditama
    AS131111 | REGRESSED                      | REGRESSED                      | 237      | 0%     | PT Mora Telematika Indonesia Tbk
    AS4787   | REGRESSED                      | REGRESSED                      | 228      | 1%     | PT Cyberindo Aditama
    AS58389  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 220      | -      | PT Sumber Data Indonesia
    AS133095 | REGRESSED                      | REGRESSED                      | 191      | 1%     | PT Pusat Fiber Indonesia
    AS7717   | VULNERABLE                     | VULNERABLE                     | 191      | -      | OpenIXP Route Servers
    AS150506 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 177      | -      | PT Pusat Fiber Indonesia
    AS137366 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 176      | 0%     | PT iForte Solusi Infotek
    AS24534  | REGRESSED                      | REGRESSED                      | 168      | 0%     | PT Trans Hybrid Communication
    AS45147  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 143      | -      | PT NAP Info Lintas Nusa
    AS58495  | REGRESSED                      | REGRESSED                      | 137      | 0%     | PT Parsaoran Global Datatrans
    AS4761   | REGRESSED                      | REGRESSED                      | 135      | 46%    | PT Indosat Tbk
    AS17995  | REGRESSED                      | REGRESSED                      | 133      | 2%     | PT iForte Global Internet
    AS55685  | REGRESSED                      | REGRESSED                      | 125      | 0%     | PT Jala Lintas Media

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to ID?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS7713   | 467        | REGRESSED                      | PT Telkom Indonesia Tbk
    #2   | AS55655  | 274        | REGRESSED                      | PT Sarana Insan Muda Selaras
    #3   | AS4800   | 261        | REGRESSED                      | PT Aplikanusa Lintasarta
    #4   | AS138840 | 248        | PARTIAL: VULNERABLE (Mixed)    | PT Parsaoran Global Datatrans
    #5   | AS136106 | 234        | PARTIAL: VULNERABLE (Mixed)    | PT Mega Akses Persada
    #6   | AS23947  | 207        | VOLATILE                       | PT Mora Telematika Indonesia Tbk
    #7   | AS38158  | 187        | PARTIAL: VULNERABLE (Mixed)    | PT Cyberindo Aditama
    #8   | AS4761   | 139        | REGRESSED                      | PT Indosat Tbk
    #9   | AS4787   | 108        | REGRESSED                      | PT Cyberindo Aditama
    #10  | AS45296  | 99         | STUB: VULNERABLE               | PT Rabik Bangun Nusantara
    #11  | AS55685  | 98         | REGRESSED                      | PT Jala Lintas Media
    #12  | AS17995  | 90         | REGRESSED                      | PT iForte Global Internet
    #13  | AS58389  | 89         | PASSIVE (Clean Pipe)           | PT Sumber Data Indonesia
    #14  | AS58552  | 87         | STUB: VULNERABLE               | PT Multidata Rancana Prima
    #15  | AS24534  | 79         | REGRESSED                      | PT Trans Hybrid Communication
    #16  | AS134654 | 67         | PARTIAL: VULNERABLE (Mixed)    | PT Data Utama Dinamika
    #17  | AS45147  | 64         | PARTIAL: VULNERABLE (Mixed)    | PT NAP Info Lintas Nusa
    #18  | AS138128 | 58         | PARTIAL: VULNERABLE (Mixed)    | PT Solnet Indonesia
    #19  | AS137366 | 56         | PARTIAL: VULNERABLE (Mixed)    | PT iForte Solusi Infotek
    #20  | AS56258  | 52         | VULNERABLE                     | PT PGAS Telekomunikasi Nusantara

    ====================================================================================================
     IPv6 DIFFERENCES (ID networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS150506 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT Pusat Fiber Indonesia
    AS134654 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | PT Data Utama Dinamika
    AS55818  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | Matrix Cable Internet Exchange
    AS17922  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT Indosat Tbk
    AS24198  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | PT Datakom Padma Jaya
    AS56258  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT PGAS Telekomunikasi Nusantara
    AS137367 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/2            | PT iForte Solusi Infotek
    AS58463  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT PGAS Telekomunikasi Nusantara
    AS24538  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT Digital Satelite Indonesia
    AS133840 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Jala Lintas Media
    AS140481 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | PT Tonggak Teknologi Netikom
    AS139382 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT Multi Teknologi Telematika
    AS38154  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Pasifik Satelit Nusantara
    AS151000 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT Awan Data Indonesia
    AS149693 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Jaringan Datamedia Nusantara
    AS205018 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | Irsyad Khoirul Anwar
    AS140446 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Kingpolah Network Solutions
    AS140442 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Nusantara Teknologi Semesta
    AS138876 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CV Saranaindo
    AS139427 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Lintas Persada Optika
    AS151538 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Flashnet Inovasi Teknologi
    AS154146 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Global Asta Systelematika
    AS154344 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Java Internet Solution
    AS153968 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT MERDEKA TELEKOMUNIKASI CENTER
    AS153858 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | PT Sokka Tama Fiber
    AS147133 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Jafati Mitra Solusindo
    AS147121 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Marva Global Telekomunikasi
    AS150203 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT China Telecom Indonesia
    AS150490 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT General Media Network
    AS150510 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Kawan Lama Sejahtera
