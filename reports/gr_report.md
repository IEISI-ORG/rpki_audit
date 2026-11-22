    [*] Loading Global Audit for GR...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: GR (Greece)
    ====================================================================================================
    Total Networks:      265
    Total Cone Gravity:  589
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):   128 (48.3%) -> Protects 91.0% of Traffic
    VULNERABLE NETWORKS:        99 (37.4%) -> Exposes  5.6% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        93 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    48 (51.6%)   IPv6 verdict    53 (57.0%)
      VULNERABLE main verdict    41 (44.1%)   IPv6 verdict    37 (39.8%)

    ====================================================================================================
     THE GR CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS8280   | VOLATILE                       | VOLATILE                       | 358      | -      | SYNAPSECOM S.A. Provider of Telecommunic
    AS6799   | ACTIVE (Atlas Verified)        | ACTIVE (Atlas Verified)        | 39       | 99%    | Ote SA (Hellenic Telecommunications Orga
    AS1241   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 30       | 98%    | Nova Telecommunications & Media Single M
    AS5408   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 29       | 100%   | National Infrastructures for Research an
    AS3329   | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 29       | 99%    | Vodafone Greece
    AS199081 | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 25       | 100%   | Lancom Ltd.
    AS198477 | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 20       | -      | TI SPARKLE GREECE SA
    AS25472  | REGRESSED                      | REGRESSED                      | 19       | 0%     | Nova Telecommunications & Media Single M
    AS56910  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 14       | -      | Digital Realty Hellas Single Member S.A
    AS206735 | REGRESSED                      | REGRESSED                      | 11       | 1%     | Novelcomm LP
    AS216285 | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 3        | -      | MYIP NETWORKS G.P.
    AS213835 | PARTIAL: VULNERABLE (Mixed)    | -                              | 2        | -      | Solidity Technology Services SA
    AS4601   | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 2        | -      | Antonios A. Chariton
    AS12713  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 1        | -      | Ote SA (Hellenic Telecommunications Orga
    AS215492 | PASSIVE (Clean Pipe)           | PASSIVE (Clean Pipe)           | 1        | -      | BUTLER CHAT I.K.E.
    AS35506  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1        | 100%   | INFORMATION SOCIETY S.A.
    AS196945 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 1        | -      | Microbase PC
    AS56457  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 1        | -      | FASTPATH IKE
    AS51505  | REGRESSED                      | REGRESSED                      | 1        | 0%     | Dimosia Epicheirisi Ilektrismou Anonymi 
    AS50919  | REGRESSED                      | REGRESSED                      | 1        | -      | INTERWORKS Single Member S.A.

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to GR?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS1241   | 31         | ACTIVE LOCAL ROV               | Nova Telecommunications & Media Single M
    #2   | AS6799   | 30         | ACTIVE (Atlas Verified)        | Ote SA (Hellenic Telecommunications Orga
    #3   | AS174    | 29         | CORE: ACTIVE PROTECTOR         | Cogent Communications, LLC
    #4   | AS5408   | 28         | ACTIVE LOCAL ROV               | National Infrastructures for Research an
    #5   | AS3329   | 24         | ACTIVE LOCAL ROV               | Vodafone Greece
    #6   | AS198477 | 22         | PASSIVE (Clean Pipe)           | TI SPARKLE GREECE SA
    #7   | AS199081 | 21         | ACTIVE LOCAL ROV               | Lancom Ltd.
    #8   | AS25472  | 20         | REGRESSED                      | Nova Telecommunications & Media Single M
    #9   | AS6939   | 18         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #10  | AS56910  | 18         | PARTIAL: VULNERABLE (Mixed)    | Digital Realty Hellas Single Member S.A
    #11  | AS6762   | 17         | CORE: ACTIVE PROTECTOR         | Telecom Italia Sparkle (Seabone)
    #12  | AS206735 | 12         | REGRESSED                      | Novelcomm LP
    #13  | AS8280   | 10         | VOLATILE                       | SYNAPSECOM S.A. Provider of Telecommunic
    #14  | AS3356   | 8          | CORE: ACTIVE PROTECTOR         | Lumen (Level 3)
    #15  | AS3491   | 6          | CORE: ACTIVE PROTECTOR         | PCCW Global (HK) Ltd.
    #16  | AS32787  | 6          | PARTIAL: VULNERABLE (Mixed)    | Akamai (Prolexic)
    #17  | AS1299   | 5          | CORE: ACTIVE PROTECTOR         | Arelion (fka. Telia Carrier)
    #18  | AS57463  | 5          | PARTIAL: VULNERABLE (Mixed)    | NetIX Communications JSC
    #19  | AS13335  | 4          | ACTIVE LOCAL ROV (Hardcoded)   | Cloudflare, Inc.
    #20  | AS9002   | 4          | ACTIVE LOCAL ROV               | RETN Limited

    ====================================================================================================
     IPv6 DIFFERENCES (GR networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS196945 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Microbase PC
    AS214618 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/3            | Hack The Box Single Member Private Compa
    AS8522   | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Foundation of Research and Technology He
    AS60325  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Optiland Telecommunications I.K.E.
    AS50520  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HOSTMEIN IKE
