    [*] Loading Global Audit for IN...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: IN (India)
    ====================================================================================================
    Total Networks:      6,234
    Total Cone Gravity:  14,537
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   123 ( 2.0%) -> Protects 0.1% of Traffic
    VULNERABLE NETWORKS:      2832 (45.4%) -> Exposes  92.8% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1,132 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    45 ( 4.0%)   IPv6 verdict    62 ( 5.5%)
      VULNERABLE main verdict  1083 (95.7%)   IPv6 verdict  1060 (93.6%)

    ====================================================================================================
     THE IN CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS9498   | REGRESSED                      | REGRESSED                      | 7400     | 2%     | Bharti Airtel Ltd.
    AS4755   | REGRESSED                      | REGRESSED                      | 2597     | 5%     | TATA Communications (formerly VSNL)
    AS9583   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 554      | 73%    | Sify Limited
    AS18229  | REGRESSED                      | REGRESSED                      | 537      | 1%     | CtrlS
    AS45820  | REGRESSED                      | REGRESSED                      | 397      | 3%     | Tata Teleservices ISP
    AS55836  | Unverified (Transit/Peer?)     | VOLATILE                       | 387      | 92%    | Reliance Jio Infocomm Limited
    AS55410  | REGRESSED                      | REGRESSED                      | 384      | 8%     | Vodafone Idea Ltd
    AS9730   | VULNERABLE                     | VULNERABLE                     | 235      | -      | Bharti Telesonic Ltd
    AS17665  | REGRESSED                      | REGRESSED                      | 157      | 0%     | ONEOTT INTERTAINMENT LIMITED
    AS17762  | REGRESSED                      | REGRESSED                      | 155      | 2%     | Tata Teleservices Maharashtra Ltd
    AS45117  | REGRESSED                      | REGRESSED                      | 126      | 1%     | Ishan Netsol Pvt Ltd
    AS55824  | Unverified (Transit/Peer?)     | Unverified (Transit/Peer?)     | 85       | 47%    | NKN Core Network
    AS9829   | REGRESSED                      | REGRESSED                      | 83       | 5%     | BSNL (Bharat Sanchar Nigam Ltd)
    AS17439  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 66       | -      | NTT Communications India Pvt. Ltd.
    AS132770 | REGRESSED                      | REGRESSED                      | 65       | 0%     | Gazon Communications India Limited
    AS133296 | VULNERABLE                     | VULNERABLE                     | 64       | 2%     | Web Werks India Pvt. Ltd.
    AS135718 | VULNERABLE                     | VULNERABLE                     | 52       | 21%    | DISHAWAVES INFONET PVT. LTD
    AS136334 | REGRESSED                      | REGRESSED                      | 49       | 0%     | Vortex Netsol Private Limited
    AS137085 | REGRESSED                      | REGRESSED                      | 45       | 1%     | ANONET COMMUNICATIONS PVT LTD
    AS151690 | REGRESSED                      | REGRESSED                      | 45       | 3%     | FAB FIVE NETWORK PRIVATE LIMITED

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
    #7   | AS55836  | 143        | Unverified (Transit/Peer?)     | Reliance Jio Infocomm Limited
    #8   | AS18229  | 139        | REGRESSED                      | CtrlS
    #9   | AS45117  | 79         | REGRESSED                      | Ishan Netsol Pvt Ltd
    #10  | AS55824  | 78         | Unverified (Transit/Peer?)     | NKN Core Network
    #11  | AS17762  | 76         | REGRESSED                      | Tata Teleservices Maharashtra Ltd
    #12  | AS9829   | 71         | REGRESSED                      | BSNL (Bharat Sanchar Nigam Ltd)
    #13  | AS133296 | 48         | VULNERABLE                     | Web Werks India Pvt. Ltd.
    #14  | AS17439  | 48         | VULNERABLE (Atlas Verified)    | NTT Communications India Pvt. Ltd.
    #15  | AS132770 | 48         | REGRESSED                      | Gazon Communications India Limited
    #16  | AS17665  | 47         | REGRESSED                      | ONEOTT INTERTAINMENT LIMITED
    #17  | AS136334 | 40         | REGRESSED                      | Vortex Netsol Private Limited
    #18  | AS140641 | 38         | REGRESSED                      | YOTTA NETWORK SERVICES PRIVATE LIMITED
    #19  | AS132215 | 38         | REGRESSED                      | Powergrid Teleservices Limited
    #20  | AS135718 | 37         | VULNERABLE                     | DISHAWAVES INFONET PVT. LTD

    ====================================================================================================
     IPv6 DIFFERENCES (IN networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS55836  | Unverified (Transit/Peer?)     | VOLATILE                       | 1/1            | Reliance Jio Infocomm Limited
    AS24186  | UNRELIABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | RailTel Corporation of India Ltd
    AS132774 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Niss Internet services private limited
    AS45916  | UNRELIABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Gujarat Telelink Pvt Ltd
    AS55470  | UNRELIABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | Cyfuture India Pvt. Ltd.
    AS9885   | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | NKN INTERNET GATEWAY NETWORK
    AS7633   | UNRELIABLE                     | PARTIAL: VULNERABLE (Mixed)    | 4/5            | Software Technology Parks of India - Ban
    AS136695 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Zeroshell Networks Private Limited
    AS9430   | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Software Technology Parks of India,Block
    AS132717 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | NXTGEN CLOUD TECHNOLOGIES PRIVATE LIMITE
    AS140124 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Leeway Softtech Pvt Ltd
    AS138788 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Acushnet Communication Private Limited
    AS142501 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | BHARAT-PUBLIC-DNS
    AS141288 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | National Institute Of Science Education 
    AS141275 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Maxnet Digital Pvt Ltd
    AS141834 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Neolog Online Services Private Limited
    AS152488 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | BLUELINE BROADBAND PRIVATE LIMITED
    AS153759 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | De-cix Interwire Internet Services Priva
    AS146890 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SHARVA TELENET PRIVATE LIMITED
    AS149616 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Saileelas Internet Service Private Limit
    AS17753  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | DATA INGENIOUS GLOBAL LIMITED
    AS58758  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Tata Institute of Fundamental Research
    AS136667 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Space Applications Centre
    AS135257 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | DL GTPL Broadband Private Limited
    AS132931 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | FICUS TELECOM PRIVATE LIMITED
