    [*] Loading Global Audit for KE...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: KE (Kenya)
    ====================================================================================================
    Total Networks:      250
    Total Cone Gravity:  291
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    21 ( 8.4%) -> Protects 0.7% of Traffic
    VULNERABLE NETWORKS:       199 (79.6%) -> Exposes  71.5% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        83 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict     6 ( 7.2%)   IPv6 verdict    15 (18.1%)
      VULNERABLE main verdict    68 (81.9%)   IPv6 verdict    60 (72.3%)

    ====================================================================================================
     THE KE CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS328977 | REGRESSED                      | REGRESSED                      | 175      | 0%     | Wavex Internet Service Provider LTD
    AS37061  | Unverified (Transit/Peer?)     | VULNERABLE                     | 36       | 1%     | Safaricom Limited
    AS15808  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 19       | 0%     | NTT DATA (Dimension Data)
    AS328490 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 10       | 1%     | Unwired Communications Limited
    AS36866  | VULNERABLE                     | VULNERABLE                     | 8        | 1%     | Jamii Telecommunications Limited
    AS329621 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 7        | 29%    | Gawia Ltd
    AS36926  | VULNERABLE                     | VULNERABLE                     | 6        | 1%     | Airtel Networks Kenya Limited
    AS329029 | REGRESSED                      | REGRESSED                      | 4        | 0%     | Mymanga Networks
    AS37305  | REGRESSED                      | REGRESSED                      | 3        | 1%     | Frontier Optical Networks Ltd
    AS37684  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 3        | -      | Angani Limited
    AS12556  | REGRESSED                      | -                              | 2        | 1%     | Internet Solutions (Kenya)
    AS36914  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 2        | 98%    | Kenya Education Network
    AS33771  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 2        | 0%     | Safaricom Limited
    AS328858 | REGRESSED                      | REGRESSED                      | 2        | 0%     | Express Data Networks Limited
    AS329437 | VULNERABLE                     | -                              | 2        | 0%     | VENNET SOLUTIONS LIMITED
    AS329538 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 2        | -      | SOMTEL (K) LIMITED
    AS207113 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 1        | -      | Cyrus Mbitao trading as Wofbit Networks
    AS15399  | VULNERABLE                     | VULNERABLE                     | 1        | 0%     | Wananchi Group (Kenya) Limited
    AS328578 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 1        | 0%     | KEMNET TECHNOLOGIES LIMITED
    AS328271 | REGRESSED                      | REGRESSED                      | 1        | 1%     | Syokinet Solutions Limited

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to KE?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS37100  | 55         | ACTIVE LOCAL ROV               | SEACOM Limited
    #2   | AS30844  | 35         | PARTIAL: VULNERABLE (Mixed)    | Liquid Intelligent Technologies 
    #3   | AS37061  | 30         | Unverified (Transit/Peer?)     | Safaricom Limited
    #4   | AS37662  | 26         | PARTIAL: VULNERABLE (Mixed)    | West Indian Ocean Cable Company (WIOCC)
    #5   | AS15808  | 20         | PARTIAL: VULNERABLE (Mixed)    | NTT DATA (Dimension Data)
    #6   | AS9129   | 19         | VULNERABLE                     | MTN Business Kenya
    #7   | AS6939   | 18         | ACTIVE (Atlas Verified)        | Hurricane Electric LLC
    #8   | AS37271  | 16         | PARTIAL: VULNERABLE (Mixed)    | Workonline Communications(Pty) Ltd
    #9   | AS6774   | 9          | REGRESSED                      | BICS (Belgacom)
    #10  | AS58453  | 8          | PARTIAL: VULNERABLE (Mixed)    | China Mobile International
    #11  | AS36866  | 7          | VULNERABLE                     | Jamii Telecommunications Limited
    #12  | AS16637  | 6          | REGRESSED                      | MTN SA (Bayobab)
    #13  | AS36926  | 6          | VULNERABLE                     | Airtel Networks Kenya Limited
    #14  | AS60171  | 5          | ACTIVE LOCAL ROV               | AFR-IX TELECOM S.A.
    #15  | AS329437 | 5          | VULNERABLE                     | VENNET SOLUTIONS LIMITED
    #16  | AS328490 | 5          | PARTIAL: VULNERABLE (Mixed)    | Unwired Communications Limited
    #17  | AS33771  | 4          | PARTIAL: VULNERABLE (Mixed)    | Safaricom Limited
    #18  | AS8966   | 4          | REGRESSED                      | Etisalat (E&)
    #19  | AS37027  | 4          | PARTIAL: VULNERABLE (Mixed)    | Simbanet (T) Limited
    #20  | AS15399  | 4          | VULNERABLE                     | Wananchi Group (Kenya) Limited

    ====================================================================================================
     IPv6 DIFFERENCES (KE networks whose IPv6 verdict class differs)
    ====================================================================================================
    IPv6 verdict: the same evidence judged with the network's IPv6 providers only (IPv6 graph).
    E.g. Hurricane Electric gives its peers IPv6 transit and filters invalids (reports/he_ipv6_peering.md).
    ASN      | Verdict                        | IPv6 Verdict                   | v6 dirty/feeds | Name
    ------------------------------------------------------------------------------------------------------------------------
    AS37061  | Unverified (Transit/Peer?)     | VULNERABLE                     | 1/1            | Safaricom Limited
    AS207113 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/4            | Cyrus Mbitao trading as Wofbit Networks
    AS329101 | PARTIAL: VULNERABLE (Mixed)    | PASSIVE (Clean Pipe)           | 0/1            | Icon Fiber Solutions ltd
    AS36915  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/2            | Echotel International Kenya Limited
    AS328739 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | KENYA PORTS AUTHORITY
    AS328835 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Easy BroadBand Limited
    AS329246 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HANIF TELECOM LIMITED
    AS329254 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TRUTH WIRELESS LIMITED
    AS329693 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ATLANTIC TECH FIBER LTD
    AS329717 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Kuramanet Ltd
    AS329783 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | KEPTIS SYSTEMS LTD
