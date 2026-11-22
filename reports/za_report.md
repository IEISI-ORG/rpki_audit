    [*] Loading Global Audit for ZA...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ZA (South Africa)
    ====================================================================================================
    Total Networks:      751
    Total Cone Gravity:  860
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   134 (17.8%) -> Protects 8.3% of Traffic
    VULNERABLE NETWORKS:       510 (67.9%) -> Exposes  57.4% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        303 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    57 (18.8%)   IPv6 verdict    94 (31.0%)
      VULNERABLE main verdict   232 (76.6%)   IPv6 verdict   197 (65.0%)

    ====================================================================================================
     THE ZA CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS37271  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 175      | -      | Workonline Communications(Pty) Ltd
    AS16637  | REGRESSED                      | REGRESSED                      | 93       | 0%     | MTN SA (Bayobab)
    AS3741   | REGRESSED                      | REGRESSED                      | 92       | 2%     | Dimension Data
    AS36994  | REGRESSED                      | REGRESSED                      | 63       | 0%     | Vodacom
    AS5713   | REGRESSED                      | REGRESSED                      | 44       | 0%     | Telkom SA Ltd.
    AS37497  | VOLATILE                       | VOLATILE                       | 41       | -      | Network Platforms (PTY) LTD
    AS328748 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 38       | -      | Agile Solutions Provider (PTY) LTD
    AS327782 | REGRESSED                      | REGRESSED                      | 35       | 0%     | Metrofibre Networx
    AS9129   | VULNERABLE                     | VULNERABLE                     | 29       | 0%     | MTN Business Kenya
    AS327693 | VULNERABLE                     | VULNERABLE                     | 28       | 75%    | Echotel Pty Ltd
    AS36874  | REGRESSED                      | REGRESSED                      | 19       | 0%     | Cybersmart
    AS37179  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 14       | 1%     | Africa Independent Network Exchange (Pty
    AS37731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 14       | -      | Web Squad Connect (Pty) Ltd
    AS328333 | REGRESSED                      | REGRESSED                      | 13       | 7%     | Fixed Mobile Telecommunications (Pty) LT
    AS37239  | REGRESSED                      | REGRESSED                      | 13       | 0%     | ICTGlobe Management (Pty) Ltd
    AS37358  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 11       | 5%     | BitCo
    AS37153  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 9        | 0%     | Xneelo (Pty) Ltd
    AS32437  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 8        | 0%     | Webdev CC T/A Cybertek
    AS11845  | ACTIVE (Atlas Verified)        | ACTIVE (Atlas Verified)        | 8        | 97%    | Vox Telecom Ltd
    AS37680  | VOLATILE                       | VOLATILE                       | 8        | 94%    | Cool Ideas Service Provider (Pty) Ltd

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to ZA?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS37100  | 130        | ACTIVE LOCAL ROV               | SEACOM Limited
    #2   | AS3741   | 98         | REGRESSED                      | Dimension Data
    #3   | AS37271  | 73         | PARTIAL: VULNERABLE (Mixed)    | Workonline Communications(Pty) Ltd
    #4   | AS6939   | 64         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #5   | AS30844  | 50         | PARTIAL: VULNERABLE (Mixed)    | Liquid Intelligent Technologies 
    #6   | AS60171  | 46         | ACTIVE LOCAL ROV               | AFR-IX TELECOM S.A.
    #7   | AS5713   | 40         | REGRESSED                      | Telkom SA Ltd.
    #8   | AS174    | 33         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #9   | AS37662  | 31         | PARTIAL: VULNERABLE (Mixed)    | West Indian Ocean Cable Company (WIOCC)
    #10  | AS327782 | 28         | REGRESSED                      | Metrofibre Networx
    #11  | AS327693 | 28         | VULNERABLE                     | Echotel Pty Ltd
    #12  | AS328748 | 27         | PARTIAL: VULNERABLE (Mixed)    | Agile Solutions Provider (PTY) LTD
    #13  | AS37497  | 26         | VOLATILE                       | Network Platforms (PTY) LTD
    #14  | AS37468  | 23         | VOLATILE                       | Angola Cables
    #15  | AS36874  | 20         | REGRESSED                      | Cybersmart
    #16  | AS36994  | 19         | REGRESSED                      | Vodacom
    #17  | AS37358  | 17         | PARTIAL: VULNERABLE (Mixed)    | BitCo
    #18  | AS37179  | 17         | PARTIAL: VULNERABLE (Mixed)    | Africa Independent Network Exchange (Pty
    #19  | AS328333 | 17         | REGRESSED                      | Fixed Mobile Telecommunications (Pty) LT
    #20  | AS13335  | 14         | ACTIVE LOCAL ROV (Hardcoded)   | Cloudflare, Inc.

    ====================================================================================================
     IPv6 DIFFERENCES (ZA networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS37271  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | Workonline Communications(Pty) Ltd
    AS37731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Web Squad Connect (Pty) Ltd
    AS37153  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | Xneelo (Pty) Ltd
    AS41033  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | D2CLOUD NETWORK SERVICES (PTY) LTD
    AS328434 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Netovate (PTY) LTD
    AS328270 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | WTTX Communications (PTY) LTD
    AS328608 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Africa on Cloud
    AS37650  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | CM Value Added Services (Pty) Ltd
    AS328644 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | World Sports Betting Services (Pty) Ltd
    AS328677 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | KorCom (Pty) Ltd
    AS328350 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Network & Computing Consultants (Pty) Lt
    AS328336 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Rosewill Trading 324
    AS328384 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ComX Networks (PTY) LTD
    AS328388 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Internet NS (Pty) Ltd
    AS328306 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Avanti Communications South Africa (Pty)
    AS328464 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | The Computer Shop Plett
    AS328483 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Comput8 IT (Pty) Ltd
    AS328397 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | LUCKY CONNECT TECHNOLOGIES (PTY) LTD
    AS329126 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | IIP1 Pty Ltd
    AS329350 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MTD Networx
    AS329289 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Novasys IT (Pty) Ltd
    AS328917 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Sonic Computers & Wi-Fi cc
    AS328916 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MUBVUMELA CORPORATION PTY LTD
    AS328948 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NETELLIGENT CONSULTING cc
    AS328125 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Forbtech
    AS328041 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Hollywood Sportsbook Holdings (PTY) Ltd
    AS328024 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | JACQCO MANAGEMENT CC
    AS328209 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Velocity Trade Financial Services (Pty) 
    AS328167 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TWK Communications
    AS327808 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TESUCO TELECOMMUNICATIONS (PTY) LTD
