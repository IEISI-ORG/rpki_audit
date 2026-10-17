    [*] Loading Global Audit for ZA...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: ZA (South Africa)
    ====================================================================================================
    Total Networks:      751
    Total Cone Gravity:  867
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   135 (18.0%) -> Protects 8.7% of Traffic
    VULNERABLE NETWORKS:       512 (68.2%) -> Exposes  61.6% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        298 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    56 (18.8%)   IPv6 verdict    88 (29.5%)
      VULNERABLE main verdict   231 (77.5%)   IPv6 verdict   203 (68.1%)

    ====================================================================================================
     THE ZA CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS37271  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 168      | -      | Workonline Communications(Pty) Ltd
    AS3741   | REGRESSED                      | REGRESSED                      | 113      | 2%     | Dimension Data
    AS16637  | REGRESSED                      | REGRESSED                      | 86       | 0%     | MTN SA (Bayobab)
    AS36994  | REGRESSED                      | REGRESSED                      | 61       | 0%     | Vodacom
    AS5713   | REGRESSED                      | REGRESSED                      | 53       | 0%     | Telkom SA Ltd.
    AS37497  | VOLATILE                       | VOLATILE                       | 40       | 84%    | Network Platforms (PTY) LTD
    AS328748 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 36       | -      | Agile Solutions Provider (PTY) LTD
    AS327782 | REGRESSED                      | REGRESSED                      | 34       | 0%     | Metrofibre Networx
    AS9129   | VULNERABLE                     | VULNERABLE                     | 28       | 0%     | MTN Business Kenya
    AS327693 | VULNERABLE                     | VULNERABLE                     | 28       | 86%    | Echotel Pty Ltd
    AS36874  | REGRESSED                      | REGRESSED                      | 18       | 0%     | Cybersmart
    AS37179  | REGRESSED                      | REGRESSED                      | 16       | 1%     | Africa Independent Network Exchange (Pty
    AS37731  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 15       | -      | Web Squad Connect (Pty) Ltd
    AS328333 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 14       | 14%    | Fixed Mobile Telecommunications (Pty) LT
    AS37358  | REGRESSED                      | REGRESSED                      | 13       | 2%     | BitCo
    AS37239  | REGRESSED                      | REGRESSED                      | 10       | 1%     | ICTGlobe Management (Pty) Ltd
    AS37153  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 10       | 3%     | Xneelo (Pty) Ltd
    AS37739  | REGRESSED                      | REGRESSED                      | 9        | -      | Abantu Cloud Africa (Pty) Ltd
    AS37680  | REGRESSED                      | REGRESSED                      | 8        | 0%     | Cool Ideas Service Provider (Pty) Ltd
    AS37236  | REGRESSED                      | REGRESSED                      | 7        | 0%     | Reflex Solutions

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
    #14  | AS37468  | 23         | ACTIVE LOCAL ROV               | Angola Cables
    #15  | AS36874  | 20         | REGRESSED                      | Cybersmart
    #16  | AS36994  | 19         | REGRESSED                      | Vodacom
    #17  | AS37358  | 17         | REGRESSED                      | BitCo
    #18  | AS37179  | 17         | REGRESSED                      | Africa Independent Network Exchange (Pty
    #19  | AS328333 | 17         | PARTIAL: VULNERABLE (Mixed)    | Fixed Mobile Telecommunications (Pty) LT
    #20  | AS13335  | 14         | ACTIVE LOCAL ROV (Hardcoded)   | Cloudflare, Inc.

    ====================================================================================================
     IPv6 DIFFERENCES (ZA networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS37271  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/4            | Workonline Communications(Pty) Ltd
    AS37153  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | Xneelo (Pty) Ltd
    AS32437  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Webdev CC T/A Cybertek
    AS41033  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | D2CLOUD NETWORK SERVICES (PTY) LTD
    AS328608 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Africa on Cloud
    AS328434 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Netovate (PTY) LTD
    AS329350 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | MTD Networx
    AS329386 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Neurotel Communications
    AS328948 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NETELLIGENT CONSULTING cc
    AS328199 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Voimar (Pty) Ltd
    AS328125 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Forbtech
    AS328306 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Avanti Communications South Africa (Pty)
    AS328336 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Rosewill Trading 324
    AS327889 | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 1/3            | Watchtower Bible and Tract Society of So
    AS327923 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | South African Bankers Services Company L
    AS328024 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | JACQCO MANAGEMENT CC
    AS328041 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Hollywood Sportsbook Holdings (PTY) Ltd
    AS327960 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | PC Maniacs (Pty) Ltd
    AS328677 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | KorCom (Pty) Ltd
    AS328917 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Sonic Computers & Wi-Fi cc
    AS328916 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MUBVUMELA CORPORATION PTY LTD
    AS328464 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | The Computer Shop Plett
    AS328483 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Comput8 IT (Pty) Ltd
    AS328397 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | LUCKY CONNECT TECHNOLOGIES (PTY) LTD
    AS328388 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Internet NS (Pty) Ltd
    AS328384 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ComX Networks (PTY) LTD
    AS327698 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Broadband Infraco
    AS21739  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MAJUBA TECHNOLOGIES(PTY) Limited t/a T-S
    AS37356  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Huge Networks (Pty) Ltd
    AS37403  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Info-Gro (PTY) Ltd
