        - Loading Cones from final_as_rank.csv... OK (88077 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching connected RIPE Atlas probes for NZ...

    ====================================================================================================
     RIPE ATLAS PROBE COVERAGE: NZ (New Zealand)
    ====================================================================================================
    Connected probes:              122
    Distinct IPv4 / IPv6 ASNs:     37 / 24
    Networks in audit:             698
      with a probe inside (v4):    33
      with a probe inside (v6):    20
      testable via direct customer:   11
      NOT testable (IPv4):         654
    Probe ASNs not in NZ audit:   4 (probe registered in country, network registered elsewhere)

    ====================================================================================================
     TOP 30 UNTESTABLE NETWORKS (no IPv4 probe inside or in a direct customer)
    ====================================================================================================
    ASN        |  Cone |  APNIC n | Verdict                        | Name
    ----------------------------------------------------------------------------------------------------
    AS18400    |    16 |       44 | VULNERABLE                     | Xtreme Networks Limited
    AS17705    |     6 |      492 | PASSIVE (Clean Pipe)           | InSPire Net Ltd
    AS45637    |     4 |      312 | PARTIAL: VULNERABLE (Mixed)    | UniFone New Zealand Ltd
    AS24183    |     4 |       52 | PASSIVE (Clean Pipe)           | DTS LTD
    AS55561    |     3 |      287 | PASSIVE (Clean Pipe)           | 2talk Global IP Network
    AS17492    |     2 |      135 | PARTIAL: VULNERABLE (Mixed)    | Vector Communications LTD.
    AS18015    |     1 |      374 | PASSIVE (Clean Pipe)           | Fastcom Limited
    AS132040   |     1 |      112 | VULNERABLE                     | Vital Data Ltd
    AS135889   |     1 |       91 | VULNERABLE                     | Softsource Ltd
    AS18119    |     1 |       67 | PARTIAL: VULNERABLE (Mixed)    | ACSData
    AS9303     |     1 |       51 | PARTIAL: VULNERABLE (Mixed)    | The Digital Lab 2007 Limited
    AS55872    |     0 |      672 | STUB: VULNERABLE               | ASN for Trusted Partner Peering
    AS132449   |     0 |      558 | STUB: VULNERABLE               | Wireless Nation
    AS132231   |     0 |      528 | STUB: FORTUITOUS ROV           | Network For Learning Limited
    AS134673   |     0 |      273 | STUB: VULNERABLE               | Gisborne/Eastcoast Internet Service
    AS45230    |     0 |      245 | STUB: PASSIVE (Clean Pipe)     | UberGroup Limited
    AS58610    |     0 |      211 | STUB: UNRELIABLE               | Telnet Telecommunication Limited
    AS136524   |     0 |      203 | STUB: UNRELIABLE               | Zylex Computers Limited
    AS134967   |     0 |      149 | STUB: VULNERABLE               | TopQuality Limited
    AS140869   |     0 |      140 | STUB: VULNERABLE               | Turing Group Limited
    AS133043   |     0 |      126 | STUB: VULNERABLE               | Enhanced Solutions Ltd
    AS132815   |     0 |      114 | STUB: PASSIVE (Clean Pipe)     | Evolution Wireless Ltd
    AS18159    |     0 |      112 | STUB: VULNERABLE               | Netspeed Data Ltd
    AS45179    |     0 |      101 | STUB: VULNERABLE               | SiteHost New Zealand
    AS133187   |     0 |       97 | STUB: VULNERABLE               | Ashnet Limited
    AS133192   |     0 |       79 | STUB: VULNERABLE               | Ultimate Mobile limited
    AS56068    |     0 |       73 | STUB: VULNERABLE               | Lightspeed Technology Group Limited
    AS38305    |     0 |       66 | STUB: VULNERABLE               | The University of Otago
    AS132268   |     0 |       62 | STUB: PASSIVE (Clean Pipe)     | Velocity Net Limited
    AS24006    |     0 |       61 | STUB: VULNERABLE               | Liverton Limited

    [*] Full table: reports/nz_probe_gap.csv
