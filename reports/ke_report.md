    [*] Loading Global Audit for KE...

    ====================================================================================================
     NATIONAL ROUTING SECURITY: KE (Kenya)
    ====================================================================================================
    Total Networks:      247
    Total Cone Gravity:  308
    ------------------------------------------------------------
    SECURE (ACTIVE/PASSIVE):    25 (10.1%) -> Protects 1.0% of Traffic
    VULNERABLE NETWORKS:       193 (78.1%) -> Exposes  71.1% of Traffic
    ------------------------------------------------------------
    Seen in IPv6:        81 networks (verdict from IPv6 providers only, column v6_verdict)
      SECURE     main verdict    10 (12.3%)   IPv6 verdict    16 (19.8%)
      VULNERABLE main verdict    62 (76.5%)   IPv6 verdict    57 (70.4%)

    ====================================================================================================
     THE KE CORE (Top 20 Networks)
    ====================================================================================================
    ASN      | Verdict                        | IPv6 Verdict                   | Cone     | APNIC% | Name
    -------------------------------------------------------------------------------------------------------------------------------------
    AS328977 | REGRESSED                      | REGRESSED                      | 188      | 1%     | Wavex Internet Service Provider LTD
    AS37061  | Unverified (Transit/Peer?)     | VULNERABLE                     | 37       | 0%     | Safaricom Limited
    AS15808  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 19       | 1%     | NTT DATA (Dimension Data)
    AS328490 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 11       | 2%     | Unwired Communications Limited
    AS36866  | VULNERABLE                     | VULNERABLE                     | 8        | 0%     | Jamii Telecommunications Limited
    AS12556  | REGRESSED                      | -                              | 6        | 4%     | Internet Solutions (Kenya)
    AS36926  | VULNERABLE                     | VULNERABLE                     | 5        | 0%     | Airtel Networks Kenya Limited
    AS207113 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 4        | -      | Cyrus Mbitao trading as Wofbit Networks
    AS37305  | REGRESSED                      | REGRESSED                      | 4        | 2%     | Frontier Optical Networks Ltd
    AS329621 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 4        | 1%     | Gawia Ltd
    AS329029 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 4        | 1%     | Mymanga Networks
    AS36914  | ACTIVE LOCAL ROV               | ACTIVE LOCAL ROV               | 3        | 99%    | Kenya Education Network
    AS37684  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 3        | 77%    | Angani Limited
    AS329437 | VULNERABLE                     | -                              | 2        | 0%     | VENNET SOLUTIONS LIMITED
    AS329538 | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 2        | -      | SOMTEL (K) LIMITED
    AS33771  | PARTIAL: VULNERABLE (Mixed)    | PARTIAL: VULNERABLE (Mixed)    | 2        | 0%     | Safaricom Limited
    AS328858 | REGRESSED                      | REGRESSED                      | 2        | 1%     | Express Data Networks Limited
    AS15399  | VULNERABLE                     | VULNERABLE                     | 1        | 7%     | Wananchi Group (Kenya) Limited
    AS328482 | REGRESSED                      | -                              | 1        | 0%     | SKY TREND NETWORKS LIMITED
    AS329014 | REGRESSED                      | REGRESSED                      | 1        | 0%     | Vilcom Networks Limited

    ====================================================================================================
     TRANSIT SUPPLY CHAIN (Who provides to KE?)
    ====================================================================================================
    Rank | Upstream | Dependents | Global Status                  | Name
    ----------------------------------------------------------------------------------------------------
    #1   | AS37100  | 55         | ACTIVE LOCAL ROV               | SEACOM Limited
    #2   | AS30844  | 35         | PASSIVE (Clean Pipe)           | Liquid Intelligent Technologies 
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
    AS329246 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | HANIF TELECOM LIMITED
    AS329783 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | KEPTIS SYSTEMS LTD
    AS329717 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Kuramanet Ltd
    AS328739 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | KENYA PORTS AUTHORITY
    AS328835 | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Easy BroadBand Limited
    AS36915  | STUB: VULNERABLE               | STUB: PASSIVE (Clean Pipe)     | 0/1            | Echotel International Kenya Limited
