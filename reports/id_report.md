    [*] Loading Global Audit for ID...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ID (Indonesia)
    ====================================================================================================
    Total Networks:      4,089
    Total Cone Gravity:  11,116
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   131 ( 3.2%) -> Protects 8.1% of Traffic
    VULNERABLE NETWORKS:      2790 (68.2%) -> Exposes  63.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        839 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    35 ( 4.2%)   IPv6 verdict    81 ( 9.7%)
      VULNERABLE main verdict   771 (91.9%)   IPv6 verdict   736 (87.7%)

    ====================================================================================================
     THE ID CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS7713   | REGRESSED                      | REGRESSED                      | 3754     | 0%     | PT Telkom Indonesia Tbk
    AS136106 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 729      | -      | PT Mega Akses Persada
    AS4800   | REGRESSED                      | REGRESSED                      | 651      | 0%     | PT Aplikanusa Lintasarta
    AS23947  | VOLATILE                       | VOLATILE                       | 556      | -      | PT Mora Telematika Indonesia Tbk
    AS147094 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 540      | -      | PT Mitra Visioner Pratama
    AS138840 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 468      | -      | PT Parsaoran Global Datatrans
    AS38158  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 342      | -      | PT Cyberindo Aditama
    AS4787   | REGRESSED                      | REGRESSED                      | 229      | 1%     | PT Cyberindo Aditama
    AS131111 | REGRESSED                      | REGRESSED                      | 226      | 0%     | PT Mora Telematika Indonesia Tbk
    AS7717   | VULNERABLE                     | VULNERABLE                     | 225      | -      | OpenIXP Route Servers
    AS58389  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 217      | -      | PT Sumber Data Indonesia
    AS133095 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 197      | 5%     | PT Pusat Fiber Indonesia
    AS150506 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 184      | -      | PT Pusat Fiber Indonesia
    AS137366 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 180      | 0%     | PT iForte Solusi Infotek
    AS24534  | REGRESSED                      | REGRESSED                      | 158      | 0%     | PT Trans Hybrid Communication
    AS45147  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 147      | -      | PT NAP Info Lintas Nusa
    AS58495  | REGRESSED                      | REGRESSED                      | 134      | 0%     | PT Parsaoran Global Datatrans
    AS17995  | REGRESSED                      | REGRESSED                      | 132      | 2%     | PT iForte Global Internet
    AS4761   | REGRESSED                      | REGRESSED                      | 131      | 46%    | PT Indosat Tbk
    AS55685  | REGRESSED                      | REGRESSED                      | 126      | 0%     | PT Jala Lintas Media

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
    AS55818  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Matrix Cable Internet Exchange
    AS17922  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT Indosat Tbk
    AS56258  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT PGAS Telekomunikasi Nusantara
    AS137367 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/2            | PT iForte Solusi Infotek
    AS58463  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT PGAS Telekomunikasi Nusantara
    AS140481 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | PT Tonggak Teknologi Netikom
    AS137331 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 3/3            | PT Cloud Teknologi Nusantara
    AS133840 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Jala Lintas Media
    AS55653  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | PT Skyline Semesta
    AS149693 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Jaringan Datamedia Nusantara
    AS151000 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT Awan Data Indonesia
    AS55670  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT Universal Broadband
    AS38154  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Pasifik Satelit Nusantara
    AS205018 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | Irsyad Khoirul Anwar
    AS140446 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Kingpolah Network Solutions
    AS140442 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Nusantara Teknologi Semesta
    AS138876 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CV Saranaindo
    AS138818 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Internet Ini Saja
    AS139418 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Gasatek Bintang Nusantara
    AS139427 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Lintas Persada Optika
    AS151538 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Flashnet Inovasi Teknologi
    AS154146 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Global Asta Systelematika
    AS153858 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | PT Sokka Tama Fiber
    AS153968 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT MERDEKA TELEKOMUNIKASI CENTER
    AS154344 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Java Internet Solution
    AS147133 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Jafati Mitra Solusindo
    AS150203 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT China Telecom Indonesia
    AS150510 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Kawan Lama Sejahtera
