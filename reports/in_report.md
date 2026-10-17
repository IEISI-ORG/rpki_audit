    [*] Loading Global Audit for IN...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: IN (India)
    ====================================================================================================
    Total Networks:      6,218
    Total Cone Gravity:  14,212
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    70 ( 1.1%) -> Protects 0.2% of Traffic
    VULNERABLE NETWORKS:      2891 (46.5%) -> Exposes  96.0% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        1,129 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    30 ( 2.7%)   IPv6 verdict    36 ( 3.2%)
      VULNERABLE main verdict  1097 (97.2%)   IPv6 verdict  1091 (96.6%)

    ====================================================================================================
     THE IN CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS9498   | REGRESSED                      | REGRESSED                      | 7027     | 1%     | Bharti Airtel Ltd.
    AS4755   | REGRESSED                      | REGRESSED                      | 2591     | 3%     | TATA Communications (formerly VSNL)
    AS18229  | REGRESSED                      | REGRESSED                      | 617      | 0%     | CtrlS
    AS9583   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 536      | 53%    | Sify Limited
    AS55836  | INCONSISTENT                   | INCONSISTENT                   | 408      | 0%     | Reliance Jio Infocomm Limited
    AS45820  | REGRESSED                      | REGRESSED                      | 392      | 1%     | Tata Teleservices ISP
    AS55410  | REGRESSED                      | REGRESSED                      | 383      | 2%     | Vodafone Idea Ltd
    AS9730   | VULNERABLE                     | VULNERABLE                     | 235      | -      | Bharti Telesonic Ltd
    AS17665  | REGRESSED                      | REGRESSED                      | 156      | 0%     | ONEOTT INTERTAINMENT LIMITED
    AS17762  | REGRESSED                      | REGRESSED                      | 145      | 0%     | Tata Teleservices Maharashtra Ltd
    AS45117  | REGRESSED                      | REGRESSED                      | 124      | 3%     | Ishan Netsol Pvt Ltd
    AS55824  | INCONSISTENT                   | INCONSISTENT                   | 86       | 4%     | NKN Core Network
    AS9829   | REGRESSED                      | REGRESSED                      | 85       | 0%     | BSNL (Bharat Sanchar Nigam Ltd)
    AS133296 | VULNERABLE                     | VULNERABLE                     | 65       | -      | Web Werks India Pvt. Ltd.
    AS132770 | REGRESSED                      | REGRESSED                      | 64       | 0%     | Gazon Communications India Limited
    AS17439  | REGRESSED                      | REGRESSED                      | 63       | -      | NTT Communications India Pvt. Ltd.
    AS137085 | REGRESSED                      | REGRESSED                      | 53       | 0%     | ANONET COMMUNICATIONS PVT LTD
    AS135718 | REGRESSED                      | REGRESSED                      | 52       | 0%     | DISHAWAVES INFONET PVT. LTD
    AS136334 | REGRESSED                      | REGRESSED                      | 49       | 0%     | Vortex Netsol Private Limited
    AS151690 | REGRESSED                      | REGRESSED                      | 44       | 0%     | FAB FIVE NETWORK PRIVATE LIMITED

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
    #7   | AS55836  | 143        | INCONSISTENT                   | Reliance Jio Infocomm Limited
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
    AS137645 | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | Macro Signal Pvt Ltd
    AS141275 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Maxnet Digital Pvt Ltd
    AS153759 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | De-cix Interwire Internet Services Priva
    AS149616 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Saileelas Internet Service Private Limit
    AS17753  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | DATA INGENIOUS GLOBAL LIMITED
    AS132931 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | FICUS TELECOM PRIVATE LIMITED
