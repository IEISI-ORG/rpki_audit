package main

// constants.go — shared topology classification constants for all Go binaries.
//
// This is the Go-side single source of truth, mirroring rov_utils.py:
//   TIER_1_ASNS       → isTier1()
//   NON_TRANSIT_ASNS  → isNonTransit()
//   PROVIDER_RATIO    → PROVIDER_RATIO
//
// To update these lists, edit BOTH this file AND rov_utils.py, then run:
//   python3 -m pytest tests/test_gao_rexford.py
// The sync test will catch any drift between the two.

// PROVIDER_RATIO is the minimum degree ratio for provider-customer inference.
// If degree(A) > PROVIDER_RATIO * degree(B), A is inferred as B's provider.
// Must match rov_utils.PROVIDER_RATIO in Python.
const PROVIDER_RATIO = 4.0

// isTier1 returns true for networks that are never a customer of anyone else.
// 2026-10-14: the 18 ASes that form a complete mesh of observed links (5 RIS collectors +
// CAIDA 20261001) with no provider per CAIDA; equals CAIDA's inferred clique.
// Must match rov_utils.TIER_1_ASNS (tests/test_gao_rexford.py checks).
func isTier1(asn string) bool {
	switch asn {
	case "174", // Cogent Communications
		"209",   // Lumen (ex-Qwest)
		"286",   // GTT (ex-KPN International)
		"701",   // Verizon Business
		"1299",  // Arelion (fka Telia Carrier)
		"2828",  // Verizon (ex-XO)
		"2914",  // NTT America
		"3257",  // GTT Communications
		"3320",  // Deutsche Telekom
		"3356",  // Lumen / Level 3
		"3491",  // PCCW Global
		"5511",  // Orange S.A.
		"6453",  // TATA Communications
		"6461",  // Zayo Bandwidth
		"6762",  // Telecom Italia Sparkle (Seabone)
		"6830",  // Liberty Global
		"7018",  // AT&T
		"12956": // Telxius (Telefonica Global)
		return true
	}
	return false
}

// isNonTransit returns true for ASNs that must be excluded from provider-customer
// inference. This includes DNS root servers, RIRs, and IXP ASNs.
//
// Root server ASNs sourced from bgp.tools icrit tag (verified 2026-04-26).
// Do NOT add CDN-tagged ASNs in bulk — some CDNs (e.g. OVH AS16276) also sell transit.
// Removed: AS3661 (Chinese U of HK, not A-Root), AS1941 (Renater, not B-Root),
//
//	AS15061 (Insurance Corp BC, not H-Root) — those ASNs were reassigned.
func isNonTransit(asn string) bool {
	switch asn {
	case "213241", // TECHIT.BE — IXP Route Server
		"3333",   // RIPE NCC
		"4608",   // APNIC (refuses ROV to avoid member lockout)
		"4777",   // APNIC (refuses ROV to avoid member lockout)
		"394353", // USC/ISI — B-Root
		"2149",   // Cogent Communications — C-Root
		"10886",  // University of Maryland — D-Root
		"21556",  // NASA Ames Research Center — E-Root
		"3557",   // ISC — F-Root
		"5927",   // US Dept of Defense — G-Root
		"1508",   // US Army Research Lab — H-Root
		"29216",  // Netnod — I-Root
		"26415",  // VeriSign — A-Root & J-Root
		"25152",  // RIPE NCC — K-Root
		"20144",  // ICANN — L-Root
		"7500",   // WIDE Project — M-Root
		"112",    // AS112 Project — RFC 7534 blackhole for private PTR
		// IXP ASNs (2026-10-15): PeeringDB info_type "Route Server" + AS0 ASPA record
		"6777",   // AMS-IX Route Servers
		"32801",  // IndyIX Route Servers
		"41441",  // SPEED-IX Route Servers
		"42064",  // France-IX Marseille Route Servers
		"43100",  // France-IX Lyon/AURA Route Servers
		"44596",  // Community-IX.ch Route Servers
		"46210",  // YXEIX Route Servers
		"47184",  // France-IX Toulouse Route Servers
		"47200",  // NIX.CZ Route Servers
		"47627",  // NIX.SK Route Servers
		"49624",  // LU-CIX Route Servers
		"51706",  // France-IX Paris Route Servers
		"53679",  // MICE Route Servers
		"55518",  // SGIX Route Servers
		"57328",  // DD-IX Route Servers
		"58171",  // Rheintal IX Route Servers
		"59552",  // SON-IX Route Servers
		"60247",  // LabIX Route Servers
		"62228",  // France-IX Lille Route Servers
		"197032", // TREX Route Servers
		"201376", // AuvernIX Route Exchange (mid-path for 3 neighbours on 80 RIS paths; kept: AS0 + PeeringDB type)
		"212557", // France-IX Bordeaux Route Servers
		"212674", // KA-NIX Route Servers
		"213874", // NSIX Route Servers
		"215405", // Free-IX Greece: Routeservers
		"218511", // Clue-IX Route Server
		"219524", // France-IX Paris Essentiel Route Servers
		"23456",  // AS_TRANS — RFC 6793 (4-byte ASN transition)
		"0":      // RFC 7607 reserved
		return true
	}
	return false
}
