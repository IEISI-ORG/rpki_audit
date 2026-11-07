    [*] Loading Global Audit for NZ...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: NZ (New Zealand)
    ====================================================================================================
    Total Networks:      698
    Total Cone Gravity:  2,218
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    72 (10.3%) -> Protects 84.2% of Traffic
    VULNERABLE NETWORKS:       341 (48.9%) -> Exposes  7.3% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        160 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    26 (16.2%)   IPv6 verdict    32 (20.0%)
      VULNERABLE main verdict   119 (74.4%)   IPv6 verdict   117 (73.1%)

    ====================================================================================================
     THE NZ CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS64073  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1671     | 0%     | Vetta Group
    AS9790   | ACTIVE (Atlas Verified)        | ACTIVE (Atlas Verified)        | 112      | 97%    | Two Degrees Networks Limited
    AS55850  | VOLATILE                       | VOLATILE                       | 67       | 94%    | Mercury NZ Limited
    AS135069 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 56       | 0%     | Feenix Communications Limited
    AS45177  | REGRESSED                      | REGRESSED                      | 54       | 0%     | Devoli
    AS4648   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 48       | 0%     | Spark New Zealand
    AS38022  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 32       | -      | REANNZ National Research and Education N
    AS4768   | VULNERABLE                     | VULNERABLE                     | 31       | 3%     | One New Zealand Group Limited
    AS23838  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 22       | -      | Solarix Networks Limited
    AS18400  | VULNERABLE                     | VULNERABLE                     | 17       | -      | Xtreme Networks Limited
    AS24324  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 14       | 0%     | Kordia Limited
    AS4049   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 12       | 0%     | CELLO GROUP LIMITED
    AS23655  | INCONSISTENT                   | INCONSISTENT                   | 12       | 98%    | 2degrees Networks Limited
    AS56030  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 11       | 0%     | Voyager Internet Ltd.
    AS4771   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 7        | 0%     | Spark New Zealand Trading Ltd.
    AS151336 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 6        | -      | Verge
    AS17705  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 6        | 96%    | InSPire Net Ltd
    AS138398 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 5        | -      | Prodigi Technology Services Limited
    AS45637  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 4        | 0%     | UniFone New Zealand Ltd
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
    #10  | AS64073  | 14         | PASSIVE (Clean Pipe)           | Vetta Group
    #11  | AS18400  | 14         | VULNERABLE                     | Xtreme Networks Limited
    #12  | AS24324  | 13         | VULNERABLE (Atlas Verified)    | Kordia Limited
    #13  | AS56030  | 12         | PARTIAL: VULNERABLE (Mixed)    | Voyager Internet Ltd.
    #14  | AS23655  | 12         | INCONSISTENT                   | 2degrees Networks Limited
    #15  | AS13335  | 12         | ACTIVE LOCAL ROV (Hardcoded)   | Cloudflare, Inc.
    #16  | AS174    | 11         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #17  | AS6939   | 11         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #18  | AS32787  | 10         | PARTIAL: VULNERABLE (Mixed)    | Akamai (Prolexic)
    #19  | AS4049   | 9          | PARTIAL: VULNERABLE (Mixed)    | CELLO GROUP LIMITED
    #20  | AS9500   | 7          | PARTIAL: VULNERABLE (Mixed)    | One New Zealand Group Limited

    ====================================================================================================
     IPv6 DIFFERENCES (NZ networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS38022  | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | REANNZ National Research and Education N
    AS17492  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Vector Communications LTD.
    AS9303   | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | The Digital Lab 2007 Limited
    AS9245   | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | COMPASS NZ
    AS139074 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Prodigi Technology Services Limited - Co
    AS23869  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | InternetNZ infrastructure for NZ TLD SRS
    AS136797 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Turbo I.T Limited
    AS132857 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | FULL FLAVOUR LIMITED
