    [*] Loading Global Audit for ID...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ID (Indonesia)
    ====================================================================================================
    Total Networks:      4,105
    Total Cone Gravity:  10,627
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   118 ( 2.9%) -> Protects 8.5% of Traffic
    VULNERABLE NETWORKS:      2805 (68.3%) -> Exposes  64.7% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        843 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    26 ( 3.1%)   IPv6 verdict    72 ( 8.5%)
      VULNERABLE main verdict   789 (93.6%)   IPv6 verdict   754 (89.4%)

    ====================================================================================================
     THE ID CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS7713   | REGRESSED                      | REGRESSED                      | 3284     | 0%     | PT Telkom Indonesia Tbk
    AS136106 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 719      | -      | PT Mega Akses Persada
    AS4800   | REGRESSED                      | REGRESSED                      | 647      | 0%     | PT Aplikanusa Lintasarta
    AS23947  | VOLATILE                       | VOLATILE                       | 548      | -      | PT Mora Telematika Indonesia Tbk
    AS147094 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 533      | -      | PT Mitra Visioner Pratama
    AS138840 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 427      | -      | PT Parsaoran Global Datatrans
    AS38158  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 346      | -      | PT Cyberindo Aditama
    AS4787   | REGRESSED                      | REGRESSED                      | 232      | 2%     | PT Cyberindo Aditama
    AS7717   | VULNERABLE                     | VULNERABLE                     | 230      | -      | OpenIXP Route Servers
    AS131111 | REGRESSED                      | REGRESSED                      | 225      | 0%     | PT Mora Telematika Indonesia Tbk
    AS58389  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 217      | -      | PT Sumber Data Indonesia
    AS133095 | REGRESSED                      | REGRESSED                      | 192      | -      | PT Pusat Fiber Indonesia
    AS150506 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 186      | -      | PT Pusat Fiber Indonesia
    AS137366 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 176      | 1%     | PT iForte Solusi Infotek
    AS24534  | REGRESSED                      | REGRESSED                      | 155      | 0%     | PT Trans Hybrid Communication
    AS58495  | REGRESSED                      | REGRESSED                      | 151      | 0%     | PT Parsaoran Global Datatrans
    AS45147  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 147      | -      | PT NAP Info Lintas Nusa
    AS64315  | REGRESSED                      | REGRESSED                      | 146      | 0%     | PT Mitra Visioner Pratama
    AS4761   | REGRESSED                      | REGRESSED                      | 132      | 46%    | PT Indosat Tbk
    AS17995  | REGRESSED                      | REGRESSED                      | 131      | 1%     | PT iForte Global Internet

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
    AS136106 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | PT Mega Akses Persada
    AS150506 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT Pusat Fiber Indonesia
    AS24198  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | PT Datakom Padma Jaya
    AS55818  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Matrix Cable Internet Exchange
    AS17922  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT Indosat Tbk
    AS56258  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | PT PGAS Telekomunikasi Nusantara
    AS137367 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/2            | PT iForte Solusi Infotek
    AS58463  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT PGAS Telekomunikasi Nusantara
    AS140481 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | PT Tonggak Teknologi Netikom
    AS133840 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Jala Lintas Media
    AS55653  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | PT Skyline Semesta
    AS149693 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Jaringan Datamedia Nusantara
    AS151000 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | PT Awan Data Indonesia
    AS38154  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | PT Pasifik Satelit Nusantara
    AS18004  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Wireless Indonesia
    AS23953  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Artha Telekomindo
    AS4833   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Gaharu Sejahtera
    AS38515  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Grahamedia Informasi
    AS38523  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT. SRIWIJAYA INTERNET SERVICES
    AS38567  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Rekayasa Industri
    AS38767  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Awan Media Semesta
    AS45146  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Raja Sepadan Abadi
    AS45312  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Media Lintas Data
    AS46023  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Quantum Tera Network
    AS55683  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CV Argon Data Interkoneksi
    AS58392  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Sewiwi Indonesia
    AS133809 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Artorius Telemetri Sentosa
    AS134127 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Zona Sejahtera Mandiri
    AS134632 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Lippo Malls Indonesia
    AS134658 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | PT Julia Multimedia Nusantara
