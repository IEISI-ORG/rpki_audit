    [1] Loading Metadata & Geography...
        - Fetching BGP.Tools ASN Names... FAIL (HTTPSConnectionPool(host='bgp.tools', port=443): Max retries exceeded with url: /asns.csv (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x7fc9fe1f01a0>, 'Connection to bgp.tools timed out. (connect timeout=30)')))
        - Fetching IPv4 Geo... OK (457,660 rows)
        - Fetching IPv6 Geo... OK (119,400 rows)
        - Total ASNs: 82,887, Unique Countries: 242
    [Sync] APNIC RPKI Data (242 Countries)...
        - Result: 0 Fetched, 242 Cached.
    [2] Loading Security Data...
        - Fetching BGP.Tools ROV Tags... FAIL (HTTPSConnectionPool(host='bgp.tools', port=443): Max retries exceeded with url: /tags/rpkirov.csv (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x7fc9fe687d90>, 'Connection to bgp.tools timed out. (connect timeout=30)')))
        - Fetching Cloudflare Safe List... OK (20 KB)
        - Security Data: 0 ROV Tags, 470 CF-Safe, 19501 APNIC scores
    [3] Loading Atlas Verification Results...
        - Atlas Data: 8 Secure, 86 Vulnerable, 643 Stale (queued for re-test)
    [Sync] APNIC Time Series (13261 ASNs)...
        - Result: 12161 Analysed, 0 Sparse/skipped, 1100 No data.
        - Loading Cones from final_as_rank.csv... OK (87459 ASNs)
        - Loading Graph from data/downstream_graph.json... OK
    [4] Generating Global Audit...

    ================================================================================
    AUDIT COMPLETE: 88,254 ASNs
    File Saved: rov_audit_v22_final.csv
    ================================================================================
