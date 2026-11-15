        - Loading Cones from final_as_rank.csv... OK (87904 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching connected RIPE Atlas probes for NZ...

    ====================================================================================================
     RIPE ATLAS PROBE COVERAGE: NZ (New Zealand)
    ====================================================================================================
    Connected probes:              120
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
    AS4768     |    31 |      107 | VULNERABLE                     | One New Zealand Group Limited
    AS18400    |    16 |       31 | VULNERABLE                     | Xtreme Networks Limited
    AS17705    |     6 |      595 | PASSIVE (Clean Pipe)           | InSPire Net Ltd
    AS45637    |     4 |      265 | PARTIAL: VULNERABLE (Mixed)    | UniFone New Zealand Ltd
    AS24183    |     4 |       42 | PASSIVE (Clean Pipe)           | DTS LTD
    AS55561    |     3 |      108 | PASSIVE (Clean Pipe)           | 2talk Global IP Network
    AS17492    |     3 |       37 | PARTIAL: VULNERABLE (Mixed)    | Vector Communications LTD.
    AS132040   |     1 |      112 | VULNERABLE                     | Vital Data Ltd
    AS135889   |     1 |       96 | VULNERABLE                     | Softsource Ltd
    AS18119    |     1 |       69 | PARTIAL: VULNERABLE (Mixed)    | ACSData
    AS18015    |     1 |       43 | PASSIVE (Clean Pipe)           | Fastcom Limited
    AS9303     |     1 |       31 | PARTIAL: VULNERABLE (Mixed)    | The Digital Lab 2007 Limited
    AS132231   |     0 |      771 | STUB: FORTUITOUS ROV           | Network For Learning Limited
    AS55872    |     0 |      614 | STUB: VULNERABLE               | ASN for Trusted Partner Peering
    AS132449   |     0 |      524 | STUB: VULNERABLE               | Wireless Nation
    AS45230    |     0 |      330 | STUB: PASSIVE (Clean Pipe)     | UberGroup Limited
    AS136524   |     0 |      198 | STUB: UNRELIABLE               | Zylex Computers Limited
    AS58610    |     0 |      169 | STUB: UNRELIABLE               | Telnet Telecommunication Limited
    AS134673   |     0 |      169 | STUB: VULNERABLE               | Gisborne/Eastcoast Internet Service
    AS134967   |     0 |      149 | STUB: VULNERABLE               | TopQuality Limited
    AS132815   |     0 |      145 | STUB: PASSIVE (Clean Pipe)     | Evolution Wireless Ltd
    AS45179    |     0 |      140 | STUB: VULNERABLE               | SiteHost New Zealand
    AS140869   |     0 |      140 | STUB: VOLATILE                 | Turing Group Limited
    AS133043   |     0 |      132 | STUB: VULNERABLE               | Enhanced Solutions Ltd
    AS18159    |     0 |       97 | STUB: VULNERABLE               | Netspeed Data Ltd
    AS38305    |     0 |       83 | STUB: VULNERABLE               | The University of Otago
    AS4770     |     0 |       82 | STUB: VULNERABLE               | ICONZ Ltd
    AS133192   |     0 |       82 | STUB: VULNERABLE               | Ultimate Mobile limited
    AS133878   |     0 |       77 | STUB: PASSIVE (Clean Pipe)     | UNICOM NEW ZEALAND LIMITED
    AS133187   |     0 |       71 | STUB: VULNERABLE               | Ashnet Limited

    [*] Full table: reports/nz_probe_gap.csv
