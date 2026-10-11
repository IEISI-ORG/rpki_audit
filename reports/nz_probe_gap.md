        - Loading Cones from final_as_rank.csv... OK (87459 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching connected RIPE Atlas probes for NZ...

    ====================================================================================================
     RIPE ATLAS PROBE COVERAGE: NZ (New Zealand)
    ====================================================================================================
    Connected probes:              115
    Distinct IPv4 / IPv6 ASNs:     36 / 25
    Networks in audit:             701
      with a probe inside (v4):    32
      with a probe inside (v6):    21
      testable via direct customer:    7
      NOT testable (IPv4):         662
    Probe ASNs not in NZ audit:   4 (probe registered in country, network registered elsewhere)

    ====================================================================================================
     TOP 30 UNTESTABLE NETWORKS (no IPv4 probe inside or in a direct customer)
    ====================================================================================================
    ASN        |  Cone |  APNIC n | Verdict                        | Name
    ----------------------------------------------------------------------------------------------------
    AS4768     |    31 |      104 | Unverified (Transit/Peer?)     | One New Zealand Group Limited
    AS18400    |    16 |       62 | VULNERABLE                     | Xtreme Networks Limited
    AS45637    |     4 |      201 | PARTIAL: VULNERABLE (Mixed)    | UniFone New Zealand Ltd
    AS24183    |     4 |       48 | PARTIAL: VULNERABLE (Mixed)    | DTS LTD
    AS55561    |     3 |      193 | PARTIAL: VULNERABLE (Mixed)    | 2talk Global IP Network
    AS17492    |     3 |       39 | PARTIAL: VULNERABLE (Mixed)    | Vector Communications LTD.
    AS132040   |     1 |      104 | PARTIAL: VULNERABLE (Mixed)    | Vital Data Ltd
    AS18119    |     1 |      100 | PARTIAL: VULNERABLE (Mixed)    | ACSData
    AS135889   |     1 |       89 | PARTIAL: VULNERABLE (Mixed)    | Softsource Ltd
    AS9303     |     1 |       43 | PARTIAL: VULNERABLE (Mixed)    | The Digital Lab 2007 Limited
    AS18015    |     1 |       33 | PARTIAL: VULNERABLE (Mixed)    | Fastcom Limited
    AS45230    |     0 |      599 | STUB: VULNERABLE               | UberGroup Limited
    AS55872    |     0 |      581 | STUB: VULNERABLE               | ASN for Trusted Partner Peering
    AS132449   |     0 |      515 | STUB: VULNERABLE               | Wireless Nation
    AS140869   |     0 |      266 | STUB: VOLATILE                 | Turing Group Limited
    AS58610    |     0 |      209 | STUB: UNRELIABLE               | Telnet Telecommunication Limited
    AS134967   |     0 |      198 | STUB: VULNERABLE               | TopQuality Limited
    AS134673   |     0 |      170 | STUB: VULNERABLE               | Gisborne/Eastcoast Internet Service
    AS9431     |     0 |      149 | STUB: VOLATILE                 | The University of Auckland
    AS133192   |     0 |      133 | STUB: VULNERABLE               | Ultimate Mobile limited
    AS132815   |     0 |      118 | STUB: PASSIVE (Clean Pipe)     | Evolution Wireless Ltd
    AS18159    |     0 |      106 | STUB: VULNERABLE               | Netspeed Data Ltd
    AS24006    |     0 |       97 | STUB: VULNERABLE               | Liverton Limited
    AS133043   |     0 |       90 | NOT ROUTED                     | Enhanced Solutions Ltd
    AS56068    |     0 |       87 | STUB: VULNERABLE               | Lightspeed Technology Group Limited
    AS23905    |     0 |       83 | STUB: VOLATILE                 | Victoria University of Wellington
    AS133451   |     0 |       74 | STUB: VULNERABLE               | PC Soft Limited
    AS133878   |     0 |       65 | STUB: PASSIVE (Clean Pipe)     | UNICOM NEW ZEALAND LIMITED
    AS152596   |     0 |       65 | STUB: UNRELIABLE               | Rodney Broadband Limited
    AS24111    |     0 |       64 | STUB: UNRELIABLE               | nzwireless LTD

    [*] Full table: reports/nz_probe_gap.csv
