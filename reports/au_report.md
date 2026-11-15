    [*] Loading Global Audit for AU...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: AU (Australia)
    ====================================================================================================
    Total Networks:      2,997
    Total Cone Gravity:  12,559
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   696 (23.2%) -> Protects 84.3% of Traffic
    VULNERABLE NETWORKS:       951 (31.7%) -> Exposes  12.6% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        464 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict   147 (31.7%)   IPv6 verdict   178 (38.4%)
      VULNERABLE main verdict   275 (59.3%)   IPv6 verdict   258 (55.6%)

    ====================================================================================================
     THE AU CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS7575   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 8242     | 95%    | Australian Academic and Research Network
    AS137409 | REGRESSED                      | REGRESSED                      | 1192     | 0%     | GSL Networks Pty LTD
    AS4826   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 913      | 96%    | Vocus Connect International Backbone
    AS1221   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 566      | 96%    | Telstra Limited
    AS2764   | VOLATILE                       | VOLATILE                       | 341      | 94%    | AAPT Limited
    AS7474   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 279      | 0%     | SingTel Optus Pty Ltd
    AS38195  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 184      | 93%    | Superloop
    AS4764   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 176      | 93%    | Aussie Fibre Pty Ltd
    AS136557 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 83       | 0%     | Host Universal Pty Ltd
    AS9507   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 63       | 0%     | NextHop Pty Ltd
    AS58511  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 61       | -      | Swoop (Anycast Global Backbone)
    AS24516  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 49       | 0%     | Virtutel Pty Ltd
    AS63956  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 31       | -      | 5G NETWORK OPERATIONS PTY LTD
    AS9723   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 22       | -      | iseek Communications Pty Ltd
    AS9268   | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 18       | -      | Over The Wire Pty Ltd
    AS10143  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 17       | 96%    | Exetel Pty Ltd
    AS134090 | VULNERABLE                     | VULNERABLE                     | 16       | 0%     | Leaptel
    AS134143 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 14       | 0%     | Kinetix Networks
    AS8888   | VOLATILE                       | VOLATILE                       | 14       | 97%    | xTom Pty Ltd
    AS7594   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 14       | -      | On Q

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to AU?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS4826   | 336        | ACTIVE LOCAL ROV               | Vocus Connect International Backbone
    #2   | AS7545   | 257        | VULNERABLE (Atlas Verified)    | TPG Telecom Limited
    #3   | AS1221   | 205        | ACTIVE LOCAL ROV               | Telstra Limited
    #4   | AS7474   | 139        | VULNERABLE (Atlas Verified)    | SingTel Optus Pty Ltd
    #5   | AS4764   | 109        | ACTIVE LOCAL ROV               | Aussie Fibre Pty Ltd
    #6   | AS7575   | 89         | ACTIVE LOCAL ROV               | Australian Academic and Research Network
    #7   | AS38195  | 74         | ACTIVE LOCAL ROV               | Superloop
    #8   | AS15830  | 72         | REGRESSED                      | Equinix, Inc.
    #9   | AS49915  | 58         | PARTIAL: VULNERABLE (Mixed)    | Megaport Global Access
    #10  | AS2764   | 55         | VOLATILE                       | AAPT Limited
    #11  | AS137409 | 52         | REGRESSED                      | GSL Networks Pty LTD
    #12  | AS174    | 47         | INCONSISTENT                   | Cogent Communications, LLC
    #13  | AS6939   | 46         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #14  | AS9507   | 40         | PARTIAL: VULNERABLE (Mixed)    | NextHop Pty Ltd
    #15  | AS24516  | 40         | PARTIAL: VULNERABLE (Mixed)    | Virtutel Pty Ltd
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
    AS7604   | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Zettagrid Pty Ltd
    AS38220  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Amaze Intelligence
    AS9336   | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | XYZ Telecom Pty Ltd
    AS134555 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Encoo Pty Ltd
    AS56038  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | RackCorp
    AS55766  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Orro Pty Ltd
    AS132808 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | IP Telco
    AS7628   | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | CorpCloud Pty Ltd
    AS140967 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Steele Networks Pty Ltd
    AS31732  | VULNERABLE                     | PASSIVE (Clean Pipe)           | 0/1            | Parsun Network Solutions PTY LTD
    AS133434 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 2/2            | Plesi Pty Ltd
    AS132528 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | DIGICEL (AUS) PTY LTD
    AS132789 | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Pivotel Group Pty Limited
    AS18390  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | Spintel Pty Ltd
    AS58580  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Fastrack Technology
    AS56123  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | VERNet Pty Ltd
    AS45577  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/2            | Intervolve Pty Ltd
    AS17732  | PROVIDER UNKNOWN (In BGP)      | STUB: PASSIVE (Clean Pipe)     | 0/1            | ac3, Australian Centre for Advanced Comp
    AS17898  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Brennan IT
    AS18055  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Department of Human Services
    AS24565  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Netcraft Australia Pty Ltd
    AS4857   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TVP Operations Company
    AS38038  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Lit Networks Pty Ltd
    AS38474  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Department of Climate Change Energy the 
    AS45278  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Australian News Channel Pty Ltd
    AS56057  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Entity Data Pty Limited
    AS132158 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Australian Synchrotron
    AS132895 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Prodigy Communications Pty Ltd
    AS137399 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | KernWi-Fi Pty Ltd
