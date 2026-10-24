        - Loading Cones from final_as_rank.csv... OK (87912 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [*] Fetching connected RIPE Atlas probes for NZ...

    ====================================================================================================
     RIPE ATLAS PROBE COVERAGE: NZ (New Zealand)
    ====================================================================================================
    Connected probes:              116
    Distinct IPv4 / IPv6 ASNs:     36 / 24
    Networks in audit:             701
      with a probe inside (v4):    32
      with a probe inside (v6):    20
      testable via direct customer:   10
      NOT testable (IPv4):         659
    Probe ASNs not in NZ audit:   4 (probe registered in country, network registered elsewhere)

    ====================================================================================================
     TOP 30 UNTESTABLE NETWORKS (no IPv4 probe inside or in a direct customer)
    ====================================================================================================
    ASN        |  Cone |  APNIC n | Verdict                        | Name
    ----------------------------------------------------------------------------------------------------
    AS4768     |    31 |      155 | VULNERABLE                     | One New Zealand Group Limited
    AS18400    |    17 |       62 | VULNERABLE                     | Xtreme Networks Limited
    AS45637    |     4 |      210 | PARTIAL: VULNERABLE (Mixed)    | UniFone New Zealand Ltd
    AS24183    |     4 |       45 | PASSIVE (Clean Pipe)           | DTS LTD
    AS55561    |     3 |      148 | PASSIVE (Clean Pipe)           | 2talk Global IP Network
    AS17492    |     3 |       36 | PARTIAL: VULNERABLE (Mixed)    | Vector Communications LTD.
    AS135889   |     1 |       94 | VULNERABLE                     | Softsource Ltd
    AS18119    |     1 |       88 | PARTIAL: VULNERABLE (Mixed)    | ACSData
    AS9303     |     1 |       68 | PARTIAL: VULNERABLE (Mixed)    | The Digital Lab 2007 Limited
    AS18015    |     1 |       42 | PASSIVE (Clean Pipe)           | Fastcom Limited
    AS132040   |     1 |       31 | VULNERABLE                     | Vital Data Ltd
    AS132231   |     0 |      677 | STUB: FORTUITOUS ROV           | Network For Learning Limited
    AS55872    |     0 |      630 | STUB: VULNERABLE               | ASN for Trusted Partner Peering
    AS132449   |     0 |      414 | STUB: VULNERABLE               | Wireless Nation
    AS45230    |     0 |      265 | STUB: PASSIVE (Clean Pipe)     | UberGroup Limited
    AS132815   |     0 |      216 | STUB: PASSIVE (Clean Pipe)     | Evolution Wireless Ltd
    AS58610    |     0 |      195 | STUB: UNRELIABLE               | Telnet Telecommunication Limited
    AS134967   |     0 |      181 | STUB: VULNERABLE               | TopQuality Limited
    AS56068    |     0 |      169 | STUB: VULNERABLE               | Lightspeed Technology Group Limited
    AS134673   |     0 |      166 | STUB: VULNERABLE               | Gisborne/Eastcoast Internet Service
    AS140869   |     0 |      140 | STUB: VOLATILE                 | Turing Group Limited
    AS133043   |     0 |      131 | STUB: VULNERABLE               | Enhanced Solutions Ltd
    AS24006    |     0 |      126 | STUB: VULNERABLE               | Liverton Limited
    AS9431     |     0 |      101 | STUB: VOLATILE                 | The University of Auckland
    AS18159    |     0 |       82 | STUB: VULNERABLE               | Netspeed Data Ltd
    AS133451   |     0 |       74 | STUB: VULNERABLE               | PC Soft Limited
    AS56186    |     0 |       72 | STUB: VULNERABLE               | Digital Island Ltd
    AS132881   |     0 |       69 | STUB: VULNERABLE               | OmniNet Ltd
    AS133192   |     0 |       64 | STUB: VULNERABLE               | Ultimate Mobile limited
    AS4770     |     0 |       63 | STUB: VULNERABLE               | ICONZ Ltd

    [*] Full table: reports/nz_probe_gap.csv
