    [*] Loading Global Audit for KE...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: KE (Kenya)
    ====================================================================================================
    Total Networks:      249
    Total Cone Gravity:  305
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    19 ( 7.6%) -> Protects 1.0% of Traffic
    VULNERABLE NETWORKS:       200 (80.3%) -> Exposes  70.2% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        82 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict     6 ( 7.3%)   IPv6 verdict    15 (18.3%)
      VULNERABLE main verdict    67 (81.7%)   IPv6 verdict    58 (70.7%)

    ====================================================================================================
     THE KE CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS328977 | REGRESSED                      | REGRESSED                      | 185      | 0%     | Wavex Internet Service Provider LTD
    AS37061  | Unverified (Transit/Peer?)     | VULNERABLE                     | 36       | 0%     | Safaricom Limited
    AS15808  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 19       | 0%     | NTT DATA (Dimension Data)
    AS328490 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 12       | 0%     | Unwired Communications Limited
    AS36866  | VULNERABLE                     | VULNERABLE                     | 8        | 0%     | Jamii Telecommunications Limited
    AS12556  | REGRESSED                      | -                              | 6        | 9%     | Internet Solutions (Kenya)
    AS329621 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 6        | 25%    | Gawia Ltd
    AS36926  | VULNERABLE                     | VULNERABLE                     | 5        | 0%     | Airtel Networks Kenya Limited
    AS329029 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 4        | 0%     | Mymanga Networks
    AS37305  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 4        | 4%     | Frontier Optical Networks Ltd
    AS36914  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3        | 98%    | Kenya Education Network
    AS37684  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 3        | -      | Angani Limited
    AS33771  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 2        | 0%     | Safaricom Limited
    AS329538 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 2        | -      | SOMTEL (K) LIMITED
    AS329437 | VULNERABLE                     | -                              | 2        | 0%     | VENNET SOLUTIONS LIMITED
    AS328858 | REGRESSED                      | REGRESSED                      | 2        | 2%     | Express Data Networks Limited
    AS207113 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 2        | -      | Cyrus Mbitao trading as Wofbit Networks
    AS329387 | REGRESSED                      | -                              | 1        | 2%     | Skylink Networks LTD
    AS329014 | REGRESSED                      | REGRESSED                      | 1        | 1%     | Vilcom Networks Limited
    AS15399  | VULNERABLE                     | VULNERABLE                     | 1        | 7%     | Wananchi Group (Kenya) Limited

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
    #10  | AS58453  | 8          | PASSIVE (Clean Pipe)           | China Mobile International
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
    AS207113 | VULNERABLE                     | PARTIAL: VULNERABLE (Mixed)    | 3/5            | Cyrus Mbitao trading as Wofbit Networks
    AS329254 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | TRUTH WIRELESS LIMITED
    AS329246 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HANIF TELECOM LIMITED
    AS329792 | STUB: UNRELIABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | FIT INTERNET LTD
    AS329717 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Kuramanet Ltd
    AS329783 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | KEPTIS SYSTEMS LTD
    AS329693 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | ATLANTIC TECH FIBER LTD
    AS328739 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | KENYA PORTS AUTHORITY
    AS328835 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Easy BroadBand Limited
    AS36915  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Echotel International Kenya Limited
