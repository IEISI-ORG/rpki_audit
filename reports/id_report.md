    [*] Loading Global Audit for ID...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ID (Indonesia)
    ====================================================================================================
    Total Networks:      4,061
    Total Cone Gravity:  10,783
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   144 ( 3.5%) -> Protects 9.3% of Traffic
    VULNERABLE NETWORKS:      2763 (68.0%) -> Exposes  67.3% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        829 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    41 ( 4.9%)   IPv6 verdict    90 (10.9%)
      VULNERABLE main verdict   761 (91.8%)   IPv6 verdict   726 (87.6%)

    ====================================================================================================
     THE ID CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS7713   | REGRESSED                      | REGRESSED                      | 3650     | 0%     | PT Telkom Indonesia Tbk
    AS136106 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 690      | 0%     | PT Mega Akses Persada
    AS4800   | REGRESSED                      | REGRESSED                      | 649      | 0%     | PT Aplikanusa Lintasarta
    AS147094 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 545      | -      | PT Mitra Visioner Pratama
    AS23947  | VOLATILE                       | VOLATILE                       | 511      | -      | PT Mora Telematika Indonesia Tbk
    AS138840 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 430      | -      | PT Parsaoran Global Datatrans
    AS38158  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 325      | -      | PT Cyberindo Aditama
    AS131111 | REGRESSED                      | REGRESSED                      | 235      | 0%     | PT Mora Telematika Indonesia Tbk
    AS4787   | REGRESSED                      | REGRESSED                      | 228      | 1%     | PT Cyberindo Aditama
    AS58389  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 202      | -      | PT Sumber Data Indonesia
    AS7717   | VULNERABLE                     | VULNERABLE                     | 200      | -      | OpenIXP Route Servers
    AS133095 | REGRESSED                      | REGRESSED                      | 191      | -      | PT Pusat Fiber Indonesia
    AS150506 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 181      | -      | PT Pusat Fiber Indonesia
    AS137366 | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 171      | 0%     | PT iForte Solusi Infotek
    AS24534  | REGRESSED                      | REGRESSED                      | 168      | 0%     | PT Trans Hybrid Communication
    AS64315  | REGRESSED                      | REGRESSED                      | 151      | 3%     | PT Mitra Visioner Pratama
    AS45147  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 141      | -      | PT NAP Info Lintas Nusa
    AS17995  | REGRESSED                      | REGRESSED                      | 141      | 1%     | PT iForte Global Internet
    AS4761   | REGRESSED                      | REGRESSED                      | 132      | 46%    | PT Indosat Tbk
    AS55685  | REGRESSED                      | REGRESSED                      | 127      | 0%     | PT Jala Lintas Media

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
    AS138840 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | PT Parsaoran Global Datatrans
    AS150506 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT Pusat Fiber Indonesia
    AS134654 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | PT Data Utama Dinamika
    AS55818  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Matrix Cable Internet Exchange
    AS17922  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT Indosat Tbk
    AS56258  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT PGAS Telekomunikasi Nusantara
    AS24198  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT Datakom Padma Jaya
    AS137367 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/2            | PT iForte Solusi Infotek
    AS64313  | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/3            | PT NAP Info Lintas Nusa
    AS58463  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT PGAS Telekomunikasi Nusantara
    AS133840 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Jala Lintas Media
    AS140481 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | PT Tonggak Teknologi Netikom
    AS137331 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 3/3            | PT Cloud Teknologi Nusantara
    AS63862  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | PT Pascal Solusi Nusantara
    AS38154  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Pasifik Satelit Nusantara
    AS151000 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT Awan Data Indonesia
    AS45146  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT Raja Sepadan Abadi
    AS133800 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | PT Biznet Gio Nusantara
    AS205018 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | Irsyad Khoirul Anwar
    AS140446 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Kingpolah Network Solutions
    AS140442 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Nusantara Teknologi Semesta
    AS138876 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CV Saranaindo
    AS139427 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Lintas Persada Optika
    AS151538 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Flashnet Inovasi Teknologi
    AS153968 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT MERDEKA TELEKOMUNIKASI CENTER
    AS154146 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Global Asta Systelematika
    AS153858 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | PT Sokka Tama Fiber
    AS154344 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Java Internet Solution
    AS147133 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Jafati Mitra Solusindo
