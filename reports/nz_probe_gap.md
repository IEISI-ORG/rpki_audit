        - Loading Cones from final_as_rank.csv... OK (87992 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching connected RIPE Atlas probes for NZ...

    ====================================================================================================
     RIPE ATLAS PROBE COVERAGE: NZ (New Zealand)
    ====================================================================================================
    Connected probes:              118
    Distinct IPv4 / IPv6 ASNs:     37 / 24
    Networks in audit:             698
      with a probe inside (v4):    33
      with a probe inside (v6):    20
      testable via direct customer:   10
      NOT testable (IPv4):         655
    Probe ASNs not in NZ audit:   4 (probe registered in country, network registered elsewhere)

    ====================================================================================================
     TOP 30 UNTESTABLE NETWORKS (no IPv4 probe inside or in a direct customer)
    ====================================================================================================
    ASN        |  Cone |  APNIC n | Verdict                        | Name
    ----------------------------------------------------------------------------------------------------
    AS4768     |    31 |       91 | VULNERABLE                     | One New Zealand Group Limited
    AS18400    |    17 |       36 | VULNERABLE                     | Xtreme Networks Limited
    AS17705    |     6 |      551 | PASSIVE (Clean Pipe)           | InSPire Net Ltd
    AS45637    |     4 |      241 | PARTIAL: VULNERABLE (Mixed)    | UniFone New Zealand Ltd
    AS24183    |     4 |       45 | PASSIVE (Clean Pipe)           | DTS LTD
    AS55561    |     3 |       82 | PASSIVE (Clean Pipe)           | 2talk Global IP Network
    AS17492    |     3 |       33 | PARTIAL: VULNERABLE (Mixed)    | Vector Communications LTD.
    AS132040   |     1 |      109 | VULNERABLE                     | Vital Data Ltd
    AS135889   |     1 |       94 | VULNERABLE                     | Softsource Ltd
    AS18119    |     1 |       69 | PARTIAL: VULNERABLE (Mixed)    | ACSData
    AS18015    |     1 |       60 | PASSIVE (Clean Pipe)           | Fastcom Limited
    AS9303     |     1 |       57 | PARTIAL: VULNERABLE (Mixed)    | The Digital Lab 2007 Limited
    AS132231   |     0 |      662 | STUB: FORTUITOUS ROV           | Network For Learning Limited
    AS55872    |     0 |      577 | STUB: VULNERABLE               | ASN for Trusted Partner Peering
    AS132449   |     0 |      519 | STUB: VULNERABLE               | Wireless Nation
    AS45230    |     0 |      317 | STUB: PASSIVE (Clean Pipe)     | UberGroup Limited
    AS136524   |     0 |      200 | STUB: UNRELIABLE               | Zylex Computers Limited
    AS58610    |     0 |      181 | STUB: UNRELIABLE               | Telnet Telecommunication Limited
    AS134673   |     0 |      178 | STUB: VULNERABLE               | Gisborne/Eastcoast Internet Service
    AS132815   |     0 |      166 | STUB: PASSIVE (Clean Pipe)     | Evolution Wireless Ltd
    AS134967   |     0 |      149 | STUB: VULNERABLE               | TopQuality Limited
    AS140869   |     0 |      140 | STUB: VOLATILE                 | Turing Group Limited
    AS18159    |     0 |      128 | STUB: VULNERABLE               | Netspeed Data Ltd
    AS56186    |     0 |      101 | STUB: VULNERABLE               | Digital Island Ltd
    AS133043   |     0 |       99 | STUB: VULNERABLE               | Enhanced Solutions Ltd
    AS45179    |     0 |       94 | STUB: VULNERABLE               | SiteHost New Zealand
    AS38305    |     0 |       87 | STUB: VOLATILE                 | The University of Otago
    AS133878   |     0 |       83 | STUB: PASSIVE (Clean Pipe)     | UNICOM NEW ZEALAND LIMITED
    AS133192   |     0 |       79 | STUB: VULNERABLE               | Ultimate Mobile limited
    AS56068    |     0 |       78 | STUB: VULNERABLE               | Lightspeed Technology Group Limited

    [*] Full table: reports/nz_probe_gap.csv
