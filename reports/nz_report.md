    [*] Loading Global Audit for NZ...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: NZ (New Zealand)
    ====================================================================================================
    Total Networks:      699
    Total Cone Gravity:  2,225
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    85 (12.2%) -> Protects 8.6% of Traffic
    VULNERABLE NETWORKS:       330 (47.2%) -> Exposes  6.9% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        160 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    33 (20.6%)   IPv6 verdict    40 (25.0%)
      VULNERABLE main verdict   113 (70.6%)   IPv6 verdict   109 (68.1%)

    ====================================================================================================
     THE NZ CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS64073  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 1696     | 0%     | Vetta Group
    AS9790   | ACTIVE (Atlas Verified)        | ACTIVE (Atlas Verified)        | 112      | 98%    | Two Degrees Networks Limited
    AS135069 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 55       | 0%     | Feenix Communications Limited
    AS45177  | REGRESSED                      | REGRESSED                      | 55       | 0%     | Devoli
    AS55850  | VOLATILE                       | VOLATILE                       | 51       | 95%    | Mercury NZ Limited
    AS4648   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 48       | 1%     | Spark New Zealand
    AS38022  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 32       | -      | REANNZ National Research and Education N
    AS4768   | VULNERABLE                     | VULNERABLE                     | 31       | 4%     | One New Zealand Group Limited
    AS23838  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 22       | -      | Solarix Networks Limited
    AS18400  | VULNERABLE                     | VULNERABLE                     | 16       | -      | Xtreme Networks Limited
    AS24324  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 14       | 0%     | Kordia Limited
    AS4049   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 13       | 0%     | CELLO GROUP LIMITED
    AS23655  | ACTIVE (Atlas Verified)        | ACTIVE (Atlas Verified)        | 12       | 97%    | 2degrees Networks Limited
    AS56030  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 11       | 0%     | Voyager Internet Ltd.
    AS4771   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 6        | 0%     | Spark New Zealand Trading Ltd.
    AS17705  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 6        | 97%    | InSPire Net Ltd
    AS151336 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 6        | -      | Verge
    AS138398 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 5        | -      | Prodigi Technology Services Limited
    AS9500   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 4        | 0%     | One New Zealand Group Limited
    AS24183  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 4        | -      | DTS LTD

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to NZ?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS9790   | 68         | ACTIVE (Atlas Verified)        | Two Degrees Networks Limited
    #2   | AS135069 | 54         | PARTIAL: VULNERABLE (Mixed)    | Feenix Communications Limited
    #3   | AS45177  | 42         | REGRESSED                      | Devoli
    #4   | AS4768   | 32         | VULNERABLE                     | One New Zealand Group Limited
    #5   | AS4648   | 31         | PARTIAL: VULNERABLE (Mixed)    | Spark New Zealand
    #6   | AS38022  | 29         | PARTIAL: VULNERABLE (Mixed)    | REANNZ National Research and Education N
    #7   | AS55850  | 27         | VOLATILE                       | Mercury NZ Limited
    #8   | AS23838  | 24         | VULNERABLE (Atlas Verified)    | Solarix Networks Limited
    #9   | AS4826   | 18         | ACTIVE LOCAL ROV               | Vocus Connect International Backbone
    #10  | AS64073  | 14         | PARTIAL: VULNERABLE (Mixed)    | Vetta Group
    #11  | AS18400  | 14         | VULNERABLE                     | Xtreme Networks Limited
    #12  | AS24324  | 13         | VULNERABLE (Atlas Verified)    | Kordia Limited
    #13  | AS56030  | 12         | PARTIAL: VULNERABLE (Mixed)    | Voyager Internet Ltd.
    #14  | AS23655  | 12         | ACTIVE (Atlas Verified)        | 2degrees Networks Limited
    #15  | AS13335  | 12         | ACTIVE LOCAL ROV (Hardcoded)   | Cloudflare, Inc.
    #16  | AS174    | 11         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #17  | AS6939   | 11         | ACTIVE LOCAL ROV               | Hurricane Electric LLC
    #18  | AS32787  | 10         | PARTIAL: VULNERABLE (Mixed)    | Akamai (Prolexic)
    #19  | AS4049   | 9          | PARTIAL: VULNERABLE (Mixed)    | CELLO GROUP LIMITED
    #20  | AS9500   | 7          | VULNERABLE (Atlas Verified)    | One New Zealand Group Limited

    ====================================================================================================
     IPv6 DIFFERENCES (NZ networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS17492  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Vector Communications LTD.
    AS9245   | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | COMPASS NZ
    AS9303   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | The Digital Lab 2007 Limited
    AS139074 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Prodigi Technology Services Limited - Co
    AS23869  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | InternetNZ infrastructure for NZ TLD SRS
    AS9559   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Plain Communications Ltd
    AS136797 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Turbo I.T Limited
    AS132857 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | FULL FLAVOUR LIMITED
    AS134433 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | REDSHIELD SECURITY LIMITED
