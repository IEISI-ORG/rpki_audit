    [*] Loading Global Audit for NZ...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: NZ (New Zealand)
    ====================================================================================================
    Total Networks:      701
    Total Cone Gravity:  2,187
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    75 (10.7%) -> Protects 84.7% of Traffic
    VULNERABLE NETWORKS:       347 (49.5%) -> Exposes  13.1% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        158 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    32 (20.3%)   IPv6 verdict    38 (24.1%)
      VULNERABLE main verdict   120 (75.9%)   IPv6 verdict   115 (72.8%)

    ====================================================================================================
     THE NZ CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS64073  | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1667     | 0%     | Vetta Group
    AS9790   | ACTIVE (Atlas Verified)        | ACTIVE (Atlas Verified)        | 112      | 99%    | Two Degrees Networks Limited
    AS135069 | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 55       | 0%     | Feenix Communications Limited
    AS55850  | INCONSISTENT                   | INCONSISTENT                   | 51       | 0%     | Mercury NZ Limited
    AS45177  | REGRESSED                      | REGRESSED                      | 49       | 0%     | Devoli
    AS4648   | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 48       | 3%     | Spark New Zealand
    AS38022  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 32       | -      | REANNZ National Research and Education N
    AS4768   | VULNERABLE                     | VULNERABLE                     | 31       | 2%     | One New Zealand Group Limited
    AS23838  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 22       | -      | Solarix Networks Limited
    AS18400  | VULNERABLE                     | VULNERABLE                     | 16       | -      | Xtreme Networks Limited
    AS24324  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 14       | 0%     | Kordia Limited
    AS4049   | VULNERABLE                     | VULNERABLE                     | 13       | 1%     | CELLO GROUP LIMITED
    AS23655  | ACTIVE (Atlas Verified)        | ACTIVE (Atlas Verified)        | 11       | 96%    | 2degrees Networks Limited
    AS56030  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 10       | 0%     | Voyager Internet Ltd.
    AS151336 | VULNERABLE                     | VULNERABLE                     | 6        | -      | Verge
    AS17705  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 6        | 99%    | InSPire Net Ltd
    AS4771   | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 6        | 0%     | Spark New Zealand Trading Ltd.
    AS24183  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 4        | 100%   | DTS LTD
    AS45267  | VULNERABLE (Atlas Verified)    | VULNERABLE (Atlas Verified)    | 4        | 0%     | Lightwire LTD
    AS138398 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 4        | -      | Prodigi Technology Services Limited

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to NZ?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS9790   | 68         | ACTIVE (Atlas Verified)        | Two Degrees Networks Limited
    #2   | AS135069 | 54         | VULNERABLE (Atlas Verified)    | Feenix Communications Limited
    #3   | AS45177  | 42         | REGRESSED                      | Devoli
    #4   | AS4768   | 32         | VULNERABLE                     | One New Zealand Group Limited
    #5   | AS4648   | 31         | PASSIVE (Clean Pipe)           | Spark New Zealand
    #6   | AS38022  | 29         | PARTIAL: VULNERABLE (Mixed)    | REANNZ National Research and Education N
    #7   | AS55850  | 27         | INCONSISTENT                   | Mercury NZ Limited
    #8   | AS23838  | 24         | VULNERABLE (Atlas Verified)    | Solarix Networks Limited
    #9   | AS4826   | 18         | ACTIVE LOCAL ROV               | Vocus Connect International Backbone
    #10  | AS64073  | 14         | PASSIVE (Clean Pipe)           | Vetta Group
    #11  | AS18400  | 14         | VULNERABLE                     | Xtreme Networks Limited
    #12  | AS24324  | 13         | VULNERABLE (Atlas Verified)    | Kordia Limited
    #13  | AS13335  | 13         | ACTIVE LOCAL ROV (Hardcoded)   | Cloudflare, Inc.
    #14  | AS56030  | 12         | VULNERABLE (Atlas Verified)    | Voyager Internet Ltd.
    #15  | AS23655  | 12         | ACTIVE (Atlas Verified)        | 2degrees Networks Limited
    #16  | AS174    | 11         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #17  | AS6939   | 11         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #18  | AS32787  | 10         | PARTIAL: VULNERABLE (Mixed)    | Akamai (Prolexic)
    #19  | AS4049   | 9          | VULNERABLE                     | CELLO GROUP LIMITED
    #20  | AS9500   | 7          | PARTIAL: VULNERABLE (Mixed)    | One New Zealand Group Limited

    ====================================================================================================
     IPv6 DIFFERENCES (NZ networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS45637  | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2/3            | UniFone New Zealand Ltd
    AS17492  | PARTIAL: VULNERABLE (Mixed)    | VULNERABLE                     | 1/1            | Vector Communications LTD.
    AS9245   | PARTIAL: VULNERABLE (Mixed)    | UNRELIABLE                     | 1/1            | COMPASS NZ
    AS139074 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Prodigi Technology Services Limited - Co
    AS23869  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | InternetNZ infrastructure for NZ TLD SRS
    AS9559   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Plain Communications Ltd
    AS136797 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Turbo I.T Limited
    AS134433 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | REDSHIELD SECURITY LIMITED
    AS132857 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | FULL FLAVOUR LIMITED
