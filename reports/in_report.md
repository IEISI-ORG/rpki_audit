    [*] Loading Global Audit for IN...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: IN (India)
    ====================================================================================================
    Total Networks:      6,226
    Total Cone Gravity:  14,248
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    98 ( 1.6%) -> Protects 0.2% of Traffic
    VULNERABLE NETWORKS:      2862 (46.0%) -> Exposes  93.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1,130 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    33 ( 2.9%)   IPv6 verdict    47 ( 4.2%)
      VULNERABLE main verdict  1094 (96.8%)   IPv6 verdict  1073 (95.0%)

    ====================================================================================================
     THE IN CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS9498   | REGRESSED                      | REGRESSED                      | 6995     | 2%     | Bharti Airtel Ltd.
    AS4755   | REGRESSED                      | REGRESSED                      | 2584     | 10%    | TATA Communications (formerly VSNL)
    AS18229  | REGRESSED                      | REGRESSED                      | 659      | 2%     | CtrlS
    AS9583   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 550      | 64%    | Sify Limited
    AS55836  | Unverified (Transit/Peer?)     | ACTIVE LOCAL ROV               | 418      | 42%    | Reliance Jio Infocomm Limited
    AS45820  | REGRESSED                      | REGRESSED                      | 396      | 3%     | Tata Teleservices ISP
    AS55410  | REGRESSED                      | REGRESSED                      | 386      | 3%     | Vodafone Idea Ltd
    AS9730   | VULNERABLE                     | VULNERABLE                     | 235      | -      | Bharti Telesonic Ltd
    AS17665  | REGRESSED                      | REGRESSED                      | 163      | 0%     | ONEOTT INTERTAINMENT LIMITED
    AS17762  | REGRESSED                      | REGRESSED                      | 142      | 1%     | Tata Teleservices Maharashtra Ltd
    AS45117  | REGRESSED                      | REGRESSED                      | 125      | 1%     | Ishan Netsol Pvt Ltd
    AS55824  | INCONSISTENT                   | INCONSISTENT                   | 86       | 17%    | NKN Core Network
    AS9829   | REGRESSED                      | REGRESSED                      | 83       | 2%     | BSNL (Bharat Sanchar Nigam Ltd)
    AS133296 | VULNERABLE                     | VULNERABLE                     | 68       | -      | Web Werks India Pvt. Ltd.
    AS132770 | REGRESSED                      | REGRESSED                      | 65       | 0%     | Gazon Communications India Limited
    AS17439  | REGRESSED                      | REGRESSED                      | 62       | -      | NTT Communications India Pvt. Ltd.
    AS135718 | REGRESSED                      | REGRESSED                      | 52       | 5%     | DISHAWAVES INFONET PVT. LTD
    AS136334 | REGRESSED                      | REGRESSED                      | 49       | 0%     | Vortex Netsol Private Limited
    AS137085 | REGRESSED                      | REGRESSED                      | 46       | 0%     | ANONET COMMUNICATIONS PVT LTD
    AS151690 | REGRESSED                      | REGRESSED                      | 44       | 1%     | FAB FIVE NETWORK PRIVATE LIMITED

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
    #10  | AS55824  | 78         | INCONSISTENT                   | NKN Core Network
    #11  | AS17762  | 76         | REGRESSED                      | Tata Teleservices Maharashtra Ltd
    #12  | AS9829   | 71         | REGRESSED                      | BSNL (Bharat Sanchar Nigam Ltd)
    #13  | AS133296 | 48         | VULNERABLE                     | Web Werks India Pvt. Ltd.
    #14  | AS17439  | 48         | REGRESSED                      | NTT Communications India Pvt. Ltd.
    #15  | AS132770 | 48         | REGRESSED                      | Gazon Communications India Limited
    #16  | AS17665  | 47         | REGRESSED                      | ONEOTT INTERTAINMENT LIMITED
    #17  | AS136334 | 40         | REGRESSED                      | Vortex Netsol Private Limited
    #18  | AS140641 | 38         | UNRELIABLE                     | YOTTA NETWORK SERVICES PRIVATE LIMITED
    #19  | AS132215 | 38         | REGRESSED                      | Powergrid Teleservices Limited
    #20  | AS135718 | 37         | REGRESSED                      | DISHAWAVES INFONET PVT. LTD

    ====================================================================================================
     IPv6 DIFFERENCES (IN networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS55836  | Unverified (Transit/Peer?)     | ACTIVE LOCAL ROV               | 1/1            | Reliance Jio Infocomm Limited
    AS140641 | UNRELIABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | YOTTA NETWORK SERVICES PRIVATE LIMITED
    AS24186  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | RailTel Corporation of India Ltd
    AS132774 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Niss Internet services private limited
    AS45916  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Gujarat Telelink Pvt Ltd
    AS9885   | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | NKN INTERNET GATEWAY NETWORK
    AS7633   | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 4/5            | Software Technology Parks of India - Ban
    AS59179  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | MINS Technologies Private Limited
    AS9430   | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Software Technology Parks of India,Block
    AS132717 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | NXTGEN CLOUD TECHNOLOGIES PRIVATE LIMITE
    AS140124 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Leeway Softtech Pvt Ltd
    AS138788 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Acushnet Communication Private Limited
    AS141275 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Maxnet Digital Pvt Ltd
    AS151845 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Scalewithus India
    AS152488 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | BLUELINE BROADBAND PRIVATE LIMITED
    AS153759 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | De-cix Interwire Internet Services Priva
    AS146890 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | SHARVA TELENET PRIVATE LIMITED
    AS149616 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Saileelas Internet Service Private Limit
    AS149268 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Roarnet Broadband Pvt Ltd
    AS17753  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | DATA INGENIOUS GLOBAL LIMITED
    AS135257 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | DL GTPL Broadband Private Limited
    AS132931 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | FICUS TELECOM PRIVATE LIMITED
