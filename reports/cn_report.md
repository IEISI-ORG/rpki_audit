    [*] Loading Global Audit for CN...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: CN (China)
    ====================================================================================================
    Total Networks:      6,507
    Total Cone Gravity:  6,255
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    83 ( 1.3%) -> Protects 69.1% of Traffic
    VULNERABLE NETWORKS:      5085 (78.1%) -> Exposes  20.5% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        4,954 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    68 ( 1.4%)   IPv6 verdict    81 ( 1.6%)
      VULNERABLE main verdict  4866 (98.2%)   IPv6 verdict  4855 (98.0%)

    ====================================================================================================
     THE CN CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS38255  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 4183     | -      | China Education and Research Network (CE
    AS4134   | INCONSISTENT                   | INCONSISTENT                   | 420      | 0%     | China Telecom Backbone
    AS205794 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 301      | -      | JINZE YANG
    AS24429  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 269      | -      | Alibaba Cloud
    AS4837   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 131      | 3%     | China Unicom Backbone
    AS4808   | VULNERABLE                     | VULNERABLE                     | 99       | 2%     | China Unicom Beijing Province Network
    AS139317 | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 71       | -      | Ningbo Dahuamao Information Technology C
    AS4847   | VULNERABLE                     | VULNERABLE                     | 65       | 0%     | China Telecom Beijing Province Network
    AS9808   | VULNERABLE                     | VULNERABLE                     | 61       | 3%     | China Mobile Backbone
    AS56048  | VULNERABLE                     | VULNERABLE                     | 51       | 1%     | China Mobile Group Beijing Company
    AS4809   | REGRESSED                      | REGRESSED                      | 44       | 0%     | China Telecom Next Generation Carrier Ne
    AS4812   | ACTIVE (Atlas Verified)        | ACTIVE (Atlas Verified)        | 42       | 0%     | China Telecom Shanghai Province Network
    AS17621  | VULNERABLE                     | VULNERABLE                     | 42       | 2%     | China Unicom Shanghai network
    AS9425   | VULNERABLE                     | VULNERABLE                     | 40       | -      | Future Internet Technology Infrastructur
    AS38272  | VULNERABLE                     | VULNERABLE                     | 39       | -      | China Education and Research Network (CE
    AS23910  | VULNERABLE                     | VULNERABLE                     | 37       | 8%     | China Next Generation Internet CERNET2
    AS146788 | VULNERABLE                     | VULNERABLE                     | 33       | -      | China Broadcasting Network Co., Ltd
    AS24400  | VULNERABLE                     | VULNERABLE                     | 32       | 0%     | Shanghai Mobile Communications Co.,Ltd.
    AS56040  | VULNERABLE                     | VULNERABLE                     | 21       | 7%     | China Mobile Group GuangDong Company
    AS4538   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 20       | 7%     | China Education and Research Network Cen

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to CN?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS38255  | 3859       | PASSIVE (Clean Pipe)           | China Education and Research Network (CE
    #2   | AS4134   | 142        | INCONSISTENT                   | China Telecom Backbone
    #3   | AS20473  | 94         | ACTIVE LOCAL ROV               | The Constant Company, LLC
    #4   | AS139317 | 69         | PASSIVE (Clean Pipe)           | Ningbo Dahuamao Information Technology C
    #5   | AS4847   | 65         | VULNERABLE                     | China Telecom Beijing Province Network
    #6   | AS4808   | 62         | VULNERABLE                     | China Unicom Beijing Province Network
    #7   | AS4837   | 55         | VULNERABLE (Atlas Verified)    | China Unicom Backbone
    #8   | AS38272  | 40         | VULNERABLE                     | China Education and Research Network (CE
    #9   | AS9425   | 40         | VULNERABLE                     | Future Internet Technology Infrastructur
    #10  | AS9808   | 36         | VULNERABLE                     | China Mobile Backbone
    #11  | AS4812   | 35         | ACTIVE (Atlas Verified)        | China Telecom Shanghai Province Network
    #12  | AS6939   | 34         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #13  | AS53667  | 33         | ACTIVE LOCAL ROV               | FranTech Solutions
    #14  | AS56048  | 33         | VULNERABLE                     | China Mobile Group Beijing Company
    #15  | AS44324  | 31         | ACTIVE LOCAL ROV               | MoeDove LLC
    #16  | AS17621  | 29         | VULNERABLE                     | China Unicom Shanghai network
    #17  | AS34927  | 27         | PARTIAL: VULNERABLE (Mixed)    | iFog GmbH
    #18  | AS24400  | 24         | VULNERABLE                     | Shanghai Mobile Communications Co.,Ltd.
    #19  | AS7720   | 23         | VULNERABLE                     | Skywolf Technology LLC
    #20  | AS4809   | 21         | REGRESSED                      | China Telecom Next Generation Carrier Ne

    ====================================================================================================
     IPv6 DIFFERENCES (CN networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS134578 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | UNION FU WAH DIGITAL TECHNOLOGY LIMITED
    AS23911  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | China Next Generation Internet Beijing I
    AS137995 | PASSIVE (Clean Pipe)           | PARTIAL: VULNERABLE (Mixed)    | 1/3            | Shuangyu Communications Technology Co., 
    AS146762 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/2            | NATIONAL(SHANGHAI) NEW-TYPE INTERNET EXC
    AS4811   | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | China Telecom Shanghai IDC Network
    AS198681 | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/2            | Jinquan Zeng
    AS206843 | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | Jikai Ren
    AS201944 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HaoRan Liu
    AS142111 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Zhejiang Aiyun Network Technology Co Ltd
    AS146834 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SiChuan XunYou Network Technologe Limit,
    AS219016 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Zizhao Wang trading as Atelier Miku
    AS209294 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Fan Zhang
    AS24413  | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/3            | 263 Shanghai Communications Ltd.
    AS18257  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ChangZhou Bitcomm Software Technology Co
    AS17775  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | shanghai science and technology network 
    AS55967  | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Beijing Baidu Netcom Science and Technol
    AS59083  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Shanghai Kuanhui Tech. Co.,ltd
    AS58536  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CONAC (China Organizational Name Adminis
    AS138538 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | VPSOR-GLOBAL
    AS44421  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Yifu Yu
