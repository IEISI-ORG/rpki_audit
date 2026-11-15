    [*] Loading Global Audit for CN...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: CN (China)
    ====================================================================================================
    Total Networks:      6,493
    Total Cone Gravity:  6,076
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    77 ( 1.2%) -> Protects 70.5% of Traffic
    VULNERABLE NETWORKS:      5091 (78.4%) -> Exposes  21.9% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        4,951 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    64 ( 1.3%)   IPv6 verdict    68 ( 1.4%)
      VULNERABLE main verdict  4873 (98.4%)   IPv6 verdict  4868 (98.3%)

    ====================================================================================================
     THE CN CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS38255  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 4183     | -      | China Education and Research Network (CE
    AS4134   | REGRESSED                      | REGRESSED                      | 418      | 0%     | China Telecom Backbone
    AS24429  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 261      | -      | Alibaba Cloud
    AS205794 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 133      | -      | JINZE YANG
    AS4837   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 130      | 4%     | China Unicom Backbone
    AS4808   | VULNERABLE                     | VULNERABLE                     | 99       | 3%     | China Unicom Beijing Province Network
    AS139317 | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 70       | -      | Ningbo Dahuamao Information Technology C
    AS4847   | REGRESSED                      | REGRESSED                      | 64       | 0%     | China Telecom Beijing Province Network
    AS9808   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 57       | 0%     | China Mobile Backbone
    AS56048  | VULNERABLE                     | VULNERABLE                     | 51       | 0%     | China Mobile Group Beijing Company
    AS4809   | REGRESSED                      | REGRESSED                      | 45       | 4%     | China Telecom Next Generation Carrier Ne
    AS17621  | VULNERABLE                     | VULNERABLE                     | 43       | 3%     | China Unicom Shanghai network
    AS4812   | REGRESSED                      | REGRESSED                      | 42       | 0%     | China Telecom Shanghai Province Network
    AS9425   | VULNERABLE                     | VULNERABLE                     | 40       | -      | Future Internet Technology Infrastructur
    AS38272  | VULNERABLE                     | VULNERABLE                     | 39       | -      | China Education and Research Network (CE
    AS23910  | REGRESSED                      | REGRESSED                      | 36       | -      | China Next Generation Internet CERNET2
    AS146788 | VULNERABLE                     | VULNERABLE                     | 34       | -      | China Broadcasting Network Co., Ltd
    AS24400  | VULNERABLE                     | VULNERABLE                     | 33       | 0%     | Shanghai Mobile Communications Co.,Ltd.
    AS4538   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 22       | 0%     | China Education and Research Network Cen
    AS56040  | VULNERABLE                     | VULNERABLE                     | 19       | 0%     | China Mobile Group GuangDong Company

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to CN?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS38255  | 3859       | PASSIVE (Clean Pipe)           | China Education and Research Network (CE
    #2   | AS4134   | 142        | REGRESSED                      | China Telecom Backbone
    #3   | AS20473  | 89         | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #4   | AS139317 | 68         | PASSIVE (Clean Pipe)           | Ningbo Dahuamao Information Technology C
    #5   | AS4847   | 65         | REGRESSED                      | China Telecom Beijing Province Network
    #6   | AS4808   | 62         | VULNERABLE                     | China Unicom Beijing Province Network
    #7   | AS4837   | 55         | VULNERABLE (Atlas Verified)    | China Unicom Backbone
    #8   | AS38272  | 40         | VULNERABLE                     | China Education and Research Network (CE
    #9   | AS9425   | 40         | VULNERABLE                     | Future Internet Technology Infrastructur
    #10  | AS9808   | 36         | VULNERABLE (Atlas Verified)    | China Mobile Backbone
    #11  | AS4812   | 35         | REGRESSED                      | China Telecom Shanghai Province Network
    #12  | AS56048  | 33         | VULNERABLE                     | China Mobile Group Beijing Company
    #13  | AS53667  | 32         | ACTIVE LOCAL ROV               | FranTech Solutions
    #14  | AS6939   | 31         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #15  | AS44324  | 31         | ACTIVE LOCAL ROV               | MoeDove LLC
    #16  | AS17621  | 29         | VULNERABLE                     | China Unicom Shanghai network
    #17  | AS34927  | 26         | PARTIAL: VULNERABLE (Mixed)    | iFog GmbH
    #18  | AS24400  | 24         | VULNERABLE                     | Shanghai Mobile Communications Co.,Ltd.
    #19  | AS4809   | 21         | REGRESSED                      | China Telecom Next Generation Carrier Ne
    #20  | AS7720   | 21         | VULNERABLE (Atlas Verified)    | Skywolf Technology LLC

    ====================================================================================================
     IPv6 DIFFERENCES (CN networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS153185 | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Wang Dehong
    AS134578 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | UNION FU WAH DIGITAL TECHNOLOGY LIMITED
    AS204211 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Shanghai Yingyun Network Technology Co.,
    AS23911  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | China Next Generation Internet Beijing I
    AS146762 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/3            | NATIONAL(SHANGHAI) NEW-TYPE INTERNET EXC
    AS137995 | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/3            | Shuangyu Communications Technology Co., 
    AS7497   | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | Computer Network Information Center of C
    AS18257  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ChangZhou Bitcomm Software Technology Co
    AS24413  | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/3            | 263 Shanghai Communications Ltd.
    AS44421  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Yifu Yu
    AS55967  | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Beijing Baidu Netcom Science and Technol
    AS132479 | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/2            | Xue Desen
    AS146834 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SiChuan XunYou Network Technologe Limit,
    AS153057 | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/2            | Li Ruizhi
    AS201944 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HaoRan Liu
    AS206843 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | Jikai Ren
    AS219210 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ZiMo Wang
