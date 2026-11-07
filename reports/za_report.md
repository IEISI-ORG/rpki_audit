    [*] Loading Global Audit for ZA...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ZA (South Africa)
    ====================================================================================================
    Total Networks:      751
    Total Cone Gravity:  858
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   119 (15.8%) -> Protects 7.0% of Traffic
    VULNERABLE NETWORKS:       526 (70.0%) -> Exposes  59.9% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        301 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    47 (15.6%)   IPv6 verdict    81 (26.9%)
      VULNERABLE main verdict   240 (79.7%)   IPv6 verdict   210 (69.8%)

    ====================================================================================================
     THE ZA CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS37271  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 171      | 4%     | Workonline Communications(Pty) Ltd
    AS3741   | REGRESSED                      | REGRESSED                      | 105      | 1%     | Dimension Data
    AS16637  | REGRESSED                      | REGRESSED                      | 90       | 0%     | MTN SA (Bayobab)
    AS36994  | REGRESSED                      | REGRESSED                      | 62       | 0%     | Vodacom
    AS5713   | REGRESSED                      | REGRESSED                      | 41       | 0%     | Telkom SA Ltd.
    AS37497  | VOLATILE                       | VOLATILE                       | 39       | 64%    | Network Platforms (PTY) LTD
    AS327782 | REGRESSED                      | REGRESSED                      | 36       | 1%     | Metrofibre Networx
    AS328748 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 35       | -      | Agile Solutions Provider (PTY) LTD
    AS327693 | VULNERABLE                     | VULNERABLE                     | 28       | 82%    | Echotel Pty Ltd
    AS9129   | VULNERABLE                     | VULNERABLE                     | 27       | 0%     | MTN Business Kenya
    AS36874  | REGRESSED                      | REGRESSED                      | 18       | 0%     | Cybersmart
    AS328333 | REGRESSED                      | REGRESSED                      | 16       | 11%    | Fixed Mobile Telecommunications (Pty) LT
    AS37179  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 15       | 0%     | Africa Independent Network Exchange (Pty
    AS37731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 15       | -      | Web Squad Connect (Pty) Ltd
    AS37239  | REGRESSED                      | REGRESSED                      | 12       | 0%     | ICTGlobe Management (Pty) Ltd
    AS37358  | REGRESSED                      | REGRESSED                      | 10       | 3%     | BitCo
    AS11845  | ACTIVE (Atlas Verified)        | ACTIVE (Atlas Verified)        | 10       | 97%    | Vox Telecom Ltd
    AS37153  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 10       | 3%     | Xneelo (Pty) Ltd
    AS25818  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 9        | -      | CMC NETWORK (PTY) LTD
    AS37739  | REGRESSED                      | REGRESSED                      | 8        | -      | Abantu Cloud Africa (Pty) Ltd

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to ZA?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS37100  | 130        | ACTIVE LOCAL ROV               | SEACOM Limited
    #2   | AS3741   | 98         | REGRESSED                      | Dimension Data
    #3   | AS37271  | 73         | PARTIAL: VULNERABLE (Mixed)    | Workonline Communications(Pty) Ltd
    #4   | AS6939   | 64         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #5   | AS30844  | 50         | PASSIVE (Clean Pipe)           | Liquid Intelligent Technologies 
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
    #18  | AS37179  | 17         | PARTIAL: VULNERABLE (Mixed)    | Africa Independent Network Exchange (Pty
    #19  | AS328333 | 17         | REGRESSED                      | Fixed Mobile Telecommunications (Pty) LT
    #20  | AS37731  | 14         | PARTIAL: VULNERABLE (Mixed)    | Web Squad Connect (Pty) Ltd

    ====================================================================================================
     IPv6 DIFFERENCES (ZA networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS37731  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Web Squad Connect (Pty) Ltd
    AS37153  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | Xneelo (Pty) Ltd
    AS41033  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | D2CLOUD NETWORK SERVICES (PTY) LTD
    AS328608 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Africa on Cloud
    AS328434 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Netovate (PTY) LTD
    AS328512 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/3            | Backspace Technologies (Pty) Ltd
    AS329350 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MTD Networx
    AS329126 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | IIP1 Pty Ltd
    AS329289 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Novasys IT (Pty) Ltd
    AS328306 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Avanti Communications South Africa (Pty)
    AS328336 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Rosewill Trading 324
    AS328464 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | The Computer Shop Plett
    AS328397 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | LUCKY CONNECT TECHNOLOGIES (PTY) LTD
    AS328388 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Internet NS (Pty) Ltd
    AS328384 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ComX Networks (PTY) LTD
    AS328024 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | JACQCO MANAGEMENT CC
    AS328041 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Hollywood Sportsbook Holdings (PTY) Ltd
    AS327923 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | South African Bankers Services Company L
    AS327966 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | FJ Wiese CC
    AS327960 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | PC Maniacs (Pty) Ltd
    AS328167 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TWK Communications
    AS328125 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Forbtech
    AS328917 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Sonic Computers & Wi-Fi cc
    AS328916 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MUBVUMELA CORPORATION PTY LTD
    AS328948 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NETELLIGENT CONSULTING cc
    AS328483 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Comput8 IT (Pty) Ltd
    AS328677 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | KorCom (Pty) Ltd
    AS327889 | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/3            | Watchtower Bible and Tract Society of So
    AS327808 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TESUCO TELECOMMUNICATIONS (PTY) LTD
    AS21739  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MAJUBA TECHNOLOGIES(PTY) Limited t/a T-S
