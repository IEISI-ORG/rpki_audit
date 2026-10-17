    [1] Loading Metadata & Geography...
        - Fetching BGP.Tools ASN Names... OK (5462 KB)
        - Fetching IPv4 Geo... OK (457,449 rows)
        - Fetching IPv6 Geo... OK (119,669 rows)
        - Cymru Fallback: resolving 938 ASNs... Fixed 0.
        - Total ASNs: 122,899, Unique Countries: 243
    [Sync] APNIC RPKI Data (243 Countries)...
        - Result: 0 Fetched, 243 Cached.
    [2] Loading Security Data...
        - Fetching BGP.Tools ROV Tags... OK (43 KB)
        - Fetching Cloudflare Safe List... OK (20 KB)
        - Security Data: 1441 ROV Tags, 470 CF-Safe, 19269 APNIC scores
        - Fetching ROVista overview... FAIL (response has no usable fresh rows)
          -> using cached copy data/rovista/overview.json (2.4 days old)
        - ROVista: 0 ASes measured in the last 7 days
        [!] WARNING: no fresh ROVista data — this audit is APNIC-only
    [3] Loading Atlas Verification Results...
        - Atlas Data: 23 Secure, 149 Vulnerable, 549 Stale (queued for re-test)
    [Sync] APNIC Time Series (13379 ASNs)...
        - Result: 12465 Analysed, 0 Sparse/skipped, 914 No data.
        - Loading Cones from final_as_rank.csv... OK (87712 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
        - Loading Graph from data/downstream_graph_v6.json... OK
    [4] Generating Global Audit...

    ================================================================================
    AUDIT COMPLETE: 123,387 ASNs
    File Saved: rov_audit_v22_final.csv
    ================================================================================
