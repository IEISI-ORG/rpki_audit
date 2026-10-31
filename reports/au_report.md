    [*] Loading Global Audit for AU...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: AU (Australia)
    ====================================================================================================
    Total Networks:      3,001
    Total Cone Gravity:  8,611
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   690 (23.0%) -> Protects 77.8% of Traffic
    VULNERABLE NETWORKS:       961 (32.0%) -> Exposes  15.3% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        471 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   147 (31.2%)   IPv6 verdict   181 (38.4%)
      VULNERABLE main verdict   281 (59.7%)   IPv6 verdict   261 (55.4%)

    ====================================================================================================
     THE AU CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS7575   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 4347     | 96%    | Australian Academic and Research Network
    AS137409 | REGRESSED                      | REGRESSED                      | 1148     | 0%     | GSL Networks Pty LTD
    AS4826   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 859      | 93%    | Vocus Connect International Backbone
    AS1221   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 572      | 97%    | Telstra Limited
    AS2764   | VOLATILE                       | VOLATILE                       | 345      | 95%    | AAPT Limited
    AS7474   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 284      | 0%     | SingTel Optus Pty Ltd
    AS38195  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 191      | 94%    | Superloop
    AS4764   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 177      | 95%    | Aussie Fibre Pty Ltd
    AS136557 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 85       | 0%     | Host Universal Pty Ltd
    AS9507   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 64       | 0%     | NextHop Pty Ltd
    AS58511  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 61       | -      | Swoop (Anycast Global Backbone)
    AS24516  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 51       | 0%     | Virtutel Pty Ltd
    AS63956  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 30       | -      | 5G NETWORK OPERATIONS PTY LTD
    AS9268   | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 30       | -      | Over The Wire Pty Ltd
    AS9723   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 22       | -      | iseek Communications Pty Ltd
    AS10143  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 19       | 96%    | Exetel Pty Ltd
    AS134090 | VULNERABLE                     | VULNERABLE                     | 16       | 0%     | Leaptel
    AS8888   | INCONSISTENT                   | INCONSISTENT                   | 13       | 0%     | xTom Pty Ltd
    AS7594   | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 13       | -      | On Q
    AS148968 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 13       | -      | Falcore Investments Pty Ltd

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to AU?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS4826   | 336        | ACTIVE LOCAL ROV               | Vocus Connect International Backbone
    #2   | AS7545   | 257        | PARTIAL: VULNERABLE (Mixed)    | TPG Telecom Limited
    #3   | AS1221   | 205        | ACTIVE LOCAL ROV               | Telstra Limited
    #4   | AS7474   | 139        | PARTIAL: VULNERABLE (Mixed)    | SingTel Optus Pty Ltd
    #5   | AS4764   | 109        | ACTIVE LOCAL ROV               | Aussie Fibre Pty Ltd
    #6   | AS7575   | 89         | ACTIVE LOCAL ROV               | Australian Academic and Research Network
    #7   | AS38195  | 74         | ACTIVE LOCAL ROV               | Superloop
    #8   | AS15830  | 72         | REGRESSED                      | Equinix, Inc.
    #9   | AS49915  | 58         | PARTIAL: VULNERABLE (Mixed)    | Megaport Global Access
    #10  | AS2764   | 55         | VOLATILE                       | AAPT Limited
    #11  | AS137409 | 52         | REGRESSED                      | GSL Networks Pty LTD
    #12  | AS174    | 47         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #13  | AS6939   | 46         | ACTIVE LOCAL ROV               | Hurricane Electric LLC
    #14  | AS9507   | 40         | PARTIAL: VULNERABLE (Mixed)    | NextHop Pty Ltd
    #15  | AS24516  | 40         | VULNERABLE (Atlas Verified)    | Virtutel Pty Ltd
    #16  | AS32787  | 38         | PARTIAL: VULNERABLE (Mixed)    | Akamai (Prolexic)
    #17  | AS58511  | 37         | PASSIVE (Clean Pipe)           | Swoop (Anycast Global Backbone)
    #18  | AS136557 | 34         | PARTIAL: VULNERABLE (Mixed)    | Host Universal Pty Ltd
    #19  | AS9268   | 33         | PASSIVE (Clean Pipe)           | Over The Wire Pty Ltd
    #20  | AS20473  | 31         | ACTIVE LOCAL ROV               | The Constant Company, LLC

    ====================================================================================================
     IPv6 DIFFERENCES (AU networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS134143 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1/2            | Kinetix Networks
    AS9336   | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | XYZ Telecom Pty Ltd
    AS38220  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Amaze Intelligence
    AS134555 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Encoo Pty Ltd
    AS56038  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | RackCorp
    AS55766  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Orro Pty Ltd
    AS132808 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | IP Telco
    AS7628   | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | CorpCloud Pty Ltd
    AS38561  | Unverified (Transit/Peer?)     | PASSIVE (Clean Pipe)           | 0/1            | NTT Australia Solutions Pty Ltd
    AS58580  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Fastrack Technology
    AS45577  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Intervolve Pty Ltd
    AS31732  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | Parsun Network Solutions PTY LTD
    AS132528 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | DIGICEL (AUS) PTY LTD
    AS56123  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | VERNet Pty Ltd
    AS18390  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | Spintel Pty Ltd
    AS140967 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Steele Networks Pty Ltd
    AS133434 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | Plesi Pty Ltd
    AS139006 | STUB: PASSIVE (Clean Pipe)     | STUB: VULNERABLE               | 2/3            | Zoho Corporation PTY LTD
    AS139002 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Andor Information Technology Pty Ltd
    AS139671 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | CHRISTIAN CONGREGATION OF JEHOVAH'S WITN
    AS151805 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | MU Cloud
    AS151496 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Department of Customer Service
    AS152884 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | NEP AUSTRALIA PTY LTD
    AS147016 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | WEBSCHOOL.AU PTY LTD
    AS24565  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Netcraft Australia Pty Ltd
    AS24446  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | 5G NETWORK OPERATIONS PTY LTD
    AS2713   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | BBIX Australia Pty Ltd
    AS17898  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Brennan IT
    AS18055  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Department of Human Services
    AS17732  | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | ac3, Australian Centre for Advanced Comp
