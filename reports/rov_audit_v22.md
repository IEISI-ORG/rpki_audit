    [1] Loading Metadata & Geography...
        - Fetching BGP.Tools ASN Names... OK (5479 KB)
        - Fetching IPv4 Geo... OK (458,958 rows)
        - Fetching IPv6 Geo... OK (119,743 rows)
        - Cymru Fallback: resolving 920 ASNs... Fixed 0.
        - Total ASNs: 123,093, Unique Countries: 243
    [Sync] APNIC RPKI Data (243 Countries)...
        - Result: 0 Fetched, 243 Cached.
    [2] Loading Security Data...
        - Fetching BGP.Tools ROV Tags... OK (43 KB)
        - Fetching Cloudflare Safe List... OK (20 KB)
        - Security Data: 1444 ROV Tags, 470 CF-Safe, 15915 APNIC scores
        - Fetching ROVista overview... API OK, nothing measured in the last 7 days (newest 2026-10-09)
        - ROVista: 0 ASes measured in the last 7 days
        [!] WARNING: no fresh ROVista data — rovista_score column is empty (verdicts don't use it)
        [!] WARNING: ROVista's newest measurement is 2026-10-09, 37 days old (limit 30): stop relying on ROVista (TODO.md)
    [3] Loading Atlas Verification Results...
        - Atlas Data: 22 Secure, 168 Vulnerable, 489 Stale (queued for re-test)
    [Sync] APNIC Time Series (13808 ASNs)...
        - Result: 12785 Analysed, 0 Sparse/skipped, 1023 No data.
        - Loading Cones from final_as_rank.csv... OK (87904 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading Graph from data/downstream_graph_v6.json... OK
    [4] Generating Global Audit...

    ================================================================================
    AUDIT COMPLETE: 123,535 ASNs
    File Saved: rov_audit_v22_final.csv
    ================================================================================
