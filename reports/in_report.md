    [*] Loading Global Audit for IN...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: IN (India)
    ====================================================================================================
    Total Networks:      6,232
    Total Cone Gravity:  15,220
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   125 ( 2.0%) -> Protects 3.1% of Traffic
    VULNERABLE NETWORKS:      2839 (45.6%) -> Exposes  92.6% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1,131 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    43 ( 3.8%)   IPv6 verdict    56 ( 5.0%)
      VULNERABLE main verdict  1084 (95.8%)   IPv6 verdict  1071 (94.7%)

    ====================================================================================================
     THE IN CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS9498   | REGRESSED                      | REGRESSED                      | 7867     | 3%     | Bharti Airtel Ltd.
    AS4755   | REGRESSED                      | REGRESSED                      | 2658     | 3%     | TATA Communications (formerly VSNL)
    AS18229  | REGRESSED                      | REGRESSED                      | 607      | 1%     | CtrlS
    AS9583   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 560      | 68%    | Sify Limited
    AS55836  | VOLATILE                       | VOLATILE                       | 448      | 87%    | Reliance Jio Infocomm Limited
    AS45820  | REGRESSED                      | REGRESSED                      | 398      | 1%     | Tata Teleservices ISP
    AS55410  | REGRESSED                      | REGRESSED                      | 389      | 4%     | Vodafone Idea Ltd
    AS9730   | VULNERABLE                     | VULNERABLE                     | 237      | -      | Bharti Telesonic Ltd
    AS17665  | REGRESSED                      | REGRESSED                      | 163      | 0%     | ONEOTT INTERTAINMENT LIMITED
    AS17762  | REGRESSED                      | REGRESSED                      | 143      | 2%     | Tata Teleservices Maharashtra Ltd
    AS45117  | REGRESSED                      | REGRESSED                      | 127      | 2%     | Ishan Netsol Pvt Ltd
    AS55824  | Unverified (Transit/Peer?)     | Unverified (Transit/Peer?)     | 84       | 42%    | NKN Core Network
    AS9829   | REGRESSED                      | REGRESSED                      | 83       | 5%     | BSNL (Bharat Sanchar Nigam Ltd)
    AS133296 | VULNERABLE                     | VULNERABLE                     | 68       | -      | Web Werks India Pvt. Ltd.
    AS132770 | REGRESSED                      | REGRESSED                      | 67       | 0%     | Gazon Communications India Limited
    AS17439  | REGRESSED                      | REGRESSED                      | 66       | -      | NTT Communications India Pvt. Ltd.
    AS135718 | VULNERABLE                     | VULNERABLE                     | 52       | 48%    | DISHAWAVES INFONET PVT. LTD
    AS136334 | REGRESSED                      | REGRESSED                      | 49       | 0%     | Vortex Netsol Private Limited
    AS137085 | REGRESSED                      | REGRESSED                      | 47       | 1%     | ANONET COMMUNICATIONS PVT LTD
    AS151690 | REGRESSED                      | REGRESSED                      | 46       | 6%     | FAB FIVE NETWORK PRIVATE LIMITED

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to IN?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS9498   | 682        | REGRESSED                      | Bharti Airtel Ltd.
    #2   | AS4755   | 561        | REGRESSED                      | TATA Communications (formerly VSNL)
    #3   | AS45820  | 186        | REGRESSED                      | Tata Teleservices ISP
    #4   | AS9730   | 170        | VULNERABLE                     | Bharti Telesonic Ltd
    #5   | AS9583   | 167        | PARTIAL: VULNERABLE (Mixed)    | Sify Limited
    #6   | AS55410  | 156        | REGRESSED                      | Vodafone Idea Ltd
    #7   | AS55836  | 143        | VOLATILE                       | Reliance Jio Infocomm Limited
    #8   | AS18229  | 139        | REGRESSED                      | CtrlS
    #9   | AS45117  | 79         | REGRESSED                      | Ishan Netsol Pvt Ltd
    #10  | AS55824  | 78         | Unverified (Transit/Peer?)     | NKN Core Network
    #11  | AS17762  | 76         | REGRESSED                      | Tata Teleservices Maharashtra Ltd
    #12  | AS9829   | 71         | REGRESSED                      | BSNL (Bharat Sanchar Nigam Ltd)
    #13  | AS133296 | 48         | VULNERABLE                     | Web Werks India Pvt. Ltd.
    #14  | AS17439  | 48         | REGRESSED                      | NTT Communications India Pvt. Ltd.
    #15  | AS132770 | 48         | REGRESSED                      | Gazon Communications India Limited
    #16  | AS17665  | 47         | REGRESSED                      | ONEOTT INTERTAINMENT LIMITED
    #17  | AS136334 | 40         | REGRESSED                      | Vortex Netsol Private Limited
    #18  | AS140641 | 38         | UNRELIABLE                     | YOTTA NETWORK SERVICES PRIVATE LIMITED
    #19  | AS132215 | 38         | REGRESSED                      | Powergrid Teleservices Limited
    #20  | AS135718 | 37         | VULNERABLE                     | DISHAWAVES INFONET PVT. LTD

    ====================================================================================================
     IPv6 DIFFERENCES (IN networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS136695 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Zeroshell Networks Private Limited
    AS9430   | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Software Technology Parks of India,Block
    AS140124 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Leeway Softtech Pvt Ltd
    AS142501 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | BHARAT-PUBLIC-DNS
    AS141288 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | National Institute Of Science Education 
    AS141275 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Maxnet Digital Pvt Ltd
    AS151845 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Scalewithus India
    AS152488 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | BLUELINE BROADBAND PRIVATE LIMITED
    AS149616 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Saileelas Internet Service Private Limit
    AS17753  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | DATA INGENIOUS GLOBAL LIMITED
    AS136667 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Space Applications Centre
    AS135257 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | DL GTPL Broadband Private Limited
    AS138788 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Acushnet Communication Private Limited
    AS132931 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | FICUS TELECOM PRIVATE LIMITED
