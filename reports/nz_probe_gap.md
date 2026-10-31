        - Loading Cones from final_as_rank.csv... OK (88086 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching connected RIPE Atlas probes for NZ...

    ====================================================================================================
     RIPE ATLAS PROBE COVERAGE: NZ (New Zealand)
    ====================================================================================================
    Connected probes:              115
    Distinct IPv4 / IPv6 ASNs:     34 / 23
    Networks in audit:             699
      with a probe inside (v4):    30
      with a probe inside (v6):    19
      testable via direct customer:   10
      NOT testable (IPv4):         659
    Probe ASNs not in NZ audit:   4 (probe registered in country, network registered elsewhere)

    ====================================================================================================
     TOP 30 UNTESTABLE NETWORKS (no IPv4 probe inside or in a direct customer)
    ====================================================================================================
    ASN        |  Cone |  APNIC n | Verdict                        | Name
    ----------------------------------------------------------------------------------------------------
    AS4768     |    31 |      156 | VULNERABLE                     | One New Zealand Group Limited
    AS18400    |    16 |       33 | VULNERABLE                     | Xtreme Networks Limited
    AS17705    |     6 |      586 | PASSIVE (Clean Pipe)           | InSPire Net Ltd
    AS45637    |     4 |      195 | PARTIAL: VULNERABLE (Mixed)    | UniFone New Zealand Ltd
    AS24183    |     4 |       58 | PASSIVE (Clean Pipe)           | DTS LTD
    AS55561    |     3 |      122 | PASSIVE (Clean Pipe)           | 2talk Global IP Network
    AS17492    |     3 |       34 | PARTIAL: VULNERABLE (Mixed)    | Vector Communications LTD.
    AS132040   |     1 |      108 | VULNERABLE                     | Vital Data Ltd
    AS135889   |     1 |       94 | VULNERABLE                     | Softsource Ltd
    AS18119    |     1 |       91 | PARTIAL: VULNERABLE (Mixed)    | ACSData
    AS18015    |     1 |       75 | PASSIVE (Clean Pipe)           | Fastcom Limited
    AS9303     |     1 |       34 | PARTIAL: VULNERABLE (Mixed)    | The Digital Lab 2007 Limited
    AS132231   |     0 |      570 | STUB: FORTUITOUS ROV           | Network For Learning Limited
    AS55872    |     0 |      478 | STUB: VULNERABLE               | ASN for Trusted Partner Peering
    AS132449   |     0 |      438 | STUB: VULNERABLE               | Wireless Nation
    AS45230    |     0 |      262 | STUB: PASSIVE (Clean Pipe)     | UberGroup Limited
    AS58610    |     0 |      208 | STUB: UNRELIABLE               | Telnet Telecommunication Limited
    AS134673   |     0 |      194 | STUB: VULNERABLE               | Gisborne/Eastcoast Internet Service
    AS134967   |     0 |      181 | STUB: VULNERABLE               | TopQuality Limited
    AS132815   |     0 |      147 | STUB: PASSIVE (Clean Pipe)     | Evolution Wireless Ltd
    AS133043   |     0 |      142 | STUB: VULNERABLE               | Enhanced Solutions Ltd
    AS140869   |     0 |      140 | STUB: VOLATILE                 | Turing Group Limited
    AS9431     |     0 |       98 | STUB: VULNERABLE               | The University of Auckland
    AS18159    |     0 |       86 | STUB: VULNERABLE               | Netspeed Data Ltd
    AS56068    |     0 |       80 | STUB: VULNERABLE               | Lightspeed Technology Group Limited
    AS9432     |     0 |       78 | STUB: VOLATILE                 | University of Canterbury
    AS24111    |     0 |       74 | STUB: UNRELIABLE               | nzwireless LTD
    AS133451   |     0 |       74 | STUB: VULNERABLE               | PC Soft Limited
    AS133192   |     0 |       68 | STUB: VULNERABLE               | Ultimate Mobile limited
    AS136524   |     0 |       62 | STUB: UNRELIABLE               | Zylex Computers Limited

    [*] Full table: reports/nz_probe_gap.csv
