    [*] Loading Global Audit for ID...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ID (Indonesia)
    ====================================================================================================
    Total Networks:      4,070
    Total Cone Gravity:  10,546
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   142 ( 3.5%) -> Protects 7.6% of Traffic
    VULNERABLE NETWORKS:      2768 (68.0%) -> Exposes  65.6% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        812 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    39 ( 4.8%)   IPv6 verdict    70 ( 8.6%)
      VULNERABLE main verdict   746 (91.9%)   IPv6 verdict   726 (89.4%)

    ====================================================================================================
     THE ID CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS7713   | REGRESSED                      | REGRESSED                      | 3331     | 0%     | PT Telkom Indonesia Tbk
    AS4800   | REGRESSED                      | REGRESSED                      | 686      | 0%     | PT Aplikanusa Lintasarta
    AS136106 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 686      | -      | PT Mega Akses Persada
    AS23947  | VOLATILE                       | VOLATILE                       | 553      | -      | PT Mora Telematika Indonesia Tbk
    AS147094 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 548      | -      | PT Mitra Visioner Pratama
    AS138840 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 434      | 0%     | PT Parsaoran Global Datatrans
    AS38158  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 324      | -      | PT Cyberindo Aditama
    AS58389  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 239      | 0%     | PT Sumber Data Indonesia
    AS131111 | REGRESSED                      | REGRESSED                      | 234      | 0%     | PT Mora Telematika Indonesia Tbk
    AS4787   | REGRESSED                      | REGRESSED                      | 226      | 1%     | PT Cyberindo Aditama
    AS133095 | REGRESSED                      | REGRESSED                      | 191      | -      | PT Pusat Fiber Indonesia
    AS7717   | VULNERABLE                     | -                              | 190      | -      | OpenIXP Route Servers
    AS137366 | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 172      | 0%     | PT iForte Solusi Infotek
    AS150506 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 170      | -      | PT Pusat Fiber Indonesia
    AS24534  | REGRESSED                      | REGRESSED                      | 164      | 0%     | PT Trans Hybrid Communication
    AS45147  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 156      | -      | PT NAP Info Lintas Nusa
    AS17995  | REGRESSED                      | REGRESSED                      | 135      | 1%     | PT iForte Global Internet
    AS4761   | REGRESSED                      | REGRESSED                      | 132      | 46%    | PT Indosat Tbk
    AS55685  | REGRESSED                      | REGRESSED                      | 125      | 0%     | PT Jala Lintas Media
    AS58495  | REGRESSED                      | REGRESSED                      | 124      | 0%     | PT Parsaoran Global Datatrans

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
    #13  | AS58389  | 89         | PARTIAL: VULNERABLE (Mixed)    | PT Sumber Data Indonesia
    #14  | AS58552  | 87         | STUB: VULNERABLE               | PT Multidata Rancana Prima
    #15  | AS24534  | 79         | REGRESSED                      | PT Trans Hybrid Communication
    #16  | AS134654 | 67         | PARTIAL: VULNERABLE (Mixed)    | PT Data Utama Dinamika
    #17  | AS45147  | 64         | PARTIAL: VULNERABLE (Mixed)    | PT NAP Info Lintas Nusa
    #18  | AS138128 | 58         | PARTIAL: VULNERABLE (Mixed)    | PT Solnet Indonesia
    #19  | AS137366 | 56         | PASSIVE (Clean Pipe)           | PT iForte Solusi Infotek
    #20  | AS56258  | 52         | VULNERABLE                     | PT PGAS Telekomunikasi Nusantara

    ====================================================================================================
     IPv6 DIFFERENCES (ID networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS136106 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/5            | PT Mega Akses Persada
    AS58389  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | PT Sumber Data Indonesia
    AS150506 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT Pusat Fiber Indonesia
    AS134654 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | PT Data Utama Dinamika
    AS17922  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT Indosat Tbk
    AS24198  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | PT Datakom Padma Jaya
    AS56258  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT PGAS Telekomunikasi Nusantara
    AS137367 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/2            | PT iForte Solusi Infotek
    AS58463  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT PGAS Telekomunikasi Nusantara
    AS140481 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | PT Tonggak Teknologi Netikom
    AS133840 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Jala Lintas Media
    AS137331 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 3/3            | PT Cloud Teknologi Nusantara
    AS151000 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT Awan Data Indonesia
    AS133800 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | PT Biznet Gio Nusantara
    AS205018 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | Irsyad Khoirul Anwar
    AS140442 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Nusantara Teknologi Semesta
    AS139427 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Lintas Persada Optika
    AS154146 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Global Asta Systelematika
    AS153858 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | PT Sokka Tama Fiber
    AS147121 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Marva Global Telekomunikasi
    AS149688 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Satelit Nusantara Tiga
    AS150203 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT China Telecom Indonesia
    AS149400 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Cyber Akses Indonesia
    AS214882 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Data Kencang Hutama
    AS23953  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Artha Telekomindo
    AS4833   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Gaharu Sejahtera
    AS18004  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Wireless Indonesia
    AS58392  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Sewiwi Indonesia
    AS138070 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Jejaring Mitra Persada
    AS132645 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Politeknik Perkapalan Negeri Surabaya
