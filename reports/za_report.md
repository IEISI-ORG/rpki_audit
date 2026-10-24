    [*] Loading Global Audit for ZA...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ZA (South Africa)
    ====================================================================================================
    Total Networks:      751
    Total Cone Gravity:  877
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   123 (16.4%) -> Protects 6.8% of Traffic
    VULNERABLE NETWORKS:       525 (69.9%) -> Exposes  62.6% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        300 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    49 (16.3%)   IPv6 verdict    83 (27.7%)
      VULNERABLE main verdict   240 (80.0%)   IPv6 verdict   210 (70.0%)

    ====================================================================================================
     THE ZA CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS37271  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 169      | -      | Workonline Communications(Pty) Ltd
    AS3741   | REGRESSED                      | REGRESSED                      | 99       | 2%     | Dimension Data
    AS16637  | REGRESSED                      | REGRESSED                      | 92       | 0%     | MTN SA (Bayobab)
    AS36994  | REGRESSED                      | REGRESSED                      | 61       | 0%     | Vodacom
    AS5713   | REGRESSED                      | REGRESSED                      | 55       | 0%     | Telkom SA Ltd.
    AS37497  | VOLATILE                       | VOLATILE                       | 40       | -      | Network Platforms (PTY) LTD
    AS328748 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 36       | -      | Agile Solutions Provider (PTY) LTD
    AS327782 | REGRESSED                      | REGRESSED                      | 35       | 0%     | Metrofibre Networx
    AS327693 | VULNERABLE                     | VULNERABLE                     | 28       | 82%    | Echotel Pty Ltd
    AS9129   | VULNERABLE                     | VULNERABLE                     | 28       | 1%     | MTN Business Kenya
    AS36874  | REGRESSED                      | REGRESSED                      | 21       | 0%     | Cybersmart
    AS37179  | REGRESSED                      | REGRESSED                      | 17       | 1%     | Africa Independent Network Exchange (Pty
    AS37731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 15       | -      | Web Squad Connect (Pty) Ltd
    AS328333 | REGRESSED                      | REGRESSED                      | 14       | 12%    | Fixed Mobile Telecommunications (Pty) LT
    AS37358  | REGRESSED                      | REGRESSED                      | 13       | 4%     | BitCo
    AS37239  | REGRESSED                      | REGRESSED                      | 12       | 1%     | ICTGlobe Management (Pty) Ltd
    AS37153  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 10       | 1%     | Xneelo (Pty) Ltd
    AS25818  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 9        | -      | CMC NETWORK (PTY) LTD
    AS10798  | PARTIAL: VULNERABLE (Mixed)    | -                              | 9        | -      | The Standard Bank of South Africa (Propr
    AS37739  | REGRESSED                      | REGRESSED                      | 9        | -      | Abantu Cloud Africa (Pty) Ltd

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
    #17  | AS37358  | 17         | REGRESSED                      | BitCo
    #18  | AS37179  | 17         | REGRESSED                      | Africa Independent Network Exchange (Pty
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
    AS328608 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Africa on Cloud
    AS328434 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Netovate (PTY) LTD
    AS329350 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MTD Networx
    AS329289 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Novasys IT (Pty) Ltd
    AS328948 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NETELLIGENT CONSULTING cc
    AS329126 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | IIP1 Pty Ltd
    AS329785 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Boland Connect (PTY) Ltd
    AS328199 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Voimar (Pty) Ltd
    AS328167 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TWK Communications
    AS328336 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Rosewill Trading 324
    AS328306 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Avanti Communications South Africa (Pty)
    AS327960 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | PC Maniacs (Pty) Ltd
    AS327923 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | South African Bankers Services Company L
    AS327889 | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/3            | Watchtower Bible and Tract Society of So
    AS328041 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Hollywood Sportsbook Holdings (PTY) Ltd
    AS328024 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | JACQCO MANAGEMENT CC
    AS328677 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | KorCom (Pty) Ltd
    AS328917 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Sonic Computers & Wi-Fi cc
    AS328916 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MUBVUMELA CORPORATION PTY LTD
    AS328483 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Comput8 IT (Pty) Ltd
    AS328464 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | The Computer Shop Plett
    AS328397 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | LUCKY CONNECT TECHNOLOGIES (PTY) LTD
    AS328388 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Internet NS (Pty) Ltd
    AS328384 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ComX Networks (PTY) LTD
    AS327698 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Broadband Infraco
    AS21739  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MAJUBA TECHNOLOGIES(PTY) Limited t/a T-S
