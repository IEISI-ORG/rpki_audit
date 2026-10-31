    [1] Loading Metadata & Geography...
        - Fetching BGP.Tools ASN Names... OK (5470 KB)
        - Fetching IPv4 Geo... OK (458,357 rows)
        - Fetching IPv6 Geo... OK (119,366 rows)
        - Cymru Fallback: resolving 930 ASNs... Fixed 0.
        - Total ASNs: 123,108, Unique Countries: 243
    [Sync] APNIC RPKI Data (243 Countries)...
        - Result: 0 Fetched, 243 Cached.
    [2] Loading Security Data...
        - Fetching BGP.Tools ROV Tags... OK (42 KB)
        - Fetching Cloudflare Safe List... OK (20 KB)
        - Security Data: 1426 ROV Tags, 470 CF-Safe, 18232 APNIC scores
        - Fetching ROVista overview... API OK, nothing measured in the last 7 days (newest 2026-10-09)
        - ROVista: 0 ASes measured in the last 7 days
        [!] WARNING: no fresh ROVista data — rovista_score column is empty (verdicts don't use it)
    [3] Loading Atlas Verification Results...
        - Atlas Data: 25 Secure, 158 Vulnerable, 496 Stale (queued for re-test)
    [Sync] APNIC Time Series (13632 ASNs)...
        - Result: 12595 Analysed, 0 Sparse/skipped, 1037 No data.
        - Loading Cones from final_as_rank.csv... OK (88086 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading Graph from data/downstream_graph_v6.json... OK
    [4] Generating Global Audit...

    ================================================================================
    AUDIT COMPLETE: 123,570 ASNs
    File Saved: rov_audit_v22_final.csv
    ================================================================================
