package main

// Run: go test bgp-extractor.go bgp-extractor_test.go constants.go

import (
	"reflect"
	"testing"
)

func TestParseRouteAddressFamily(t *testing.T) {
	v4 := "TABLE_DUMP2|1700000000|B|192.0.2.1|64500|203.0.113.0/24|64500 3356 64501|IGP"
	v6 := "TABLE_DUMP2|1700000000|B|2001:db8::1|64500|2001:db8:100::/48|64500 6939 64502|IGP"
	path, af := parseRoute(v4)
	if af != 4 || !reflect.DeepEqual(path, []string{"64500", "3356", "64501"}) {
		t.Fatalf("v4: got %v %d", path, af)
	}
	path, af = parseRoute(v6)
	if af != 6 || !reflect.DeepEqual(path, []string{"64500", "6939", "64502"}) {
		t.Fatalf("v6: got %v %d", path, af)
	}
}

func TestParseRouteRemovesPrependingAndRejectsOtherRecords(t *testing.T) {
	path, _ := parseRoute("TABLE_DUMP2|1|B|192.0.2.1|64500|198.51.100.0/24|64500 64501 64501 64501 64502|IGP")
	if !reflect.DeepEqual(path, []string{"64500", "64501", "64502"}) {
		t.Fatalf("prepending: got %v", path)
	}
	if path, _ := parseRoute("BGP4MP|1|A|192.0.2.1|64500|198.51.100.0/24|64500 64502|IGP"); path != nil {
		t.Fatalf("non-TABLE_DUMP2 should be nil, got %v", path)
	}
}

// Path [64500 3356 64501 64502]: 64502 originates; 64501 passed its route to 3356 (a Tier 1),
// 3356 passed 64501's route to 64500. The link at the collector end (64500, 3356) is never
// passed further.
func TestRecordExports(t *testing.T) {
	m := map[exportKey]*exportCount{}
	recordExports(m, []string{"64500", "3356", "64501", "64502"}, 4)
	recordExports(m, []string{"64500", "3356", "64501", "64502"}, 4)

	want := map[exportKey]exportCount{
		{"64500", "3356", 4}:  {Paths: 2, Beyond: 0, ToTier1: 0},
		{"3356", "64501", 4}:  {Paths: 2, Beyond: 2, ToTier1: 0}, // X is a Tier 1: not counted
		{"64501", "64502", 4}: {Paths: 2, Beyond: 2, ToTier1: 2},
	}
	if len(m) != len(want) {
		t.Fatalf("got %d keys, want %d: %v", len(m), len(want), m)
	}
	for k, w := range want {
		if got := m[k]; got == nil || *got != w {
			t.Errorf("%v: got %+v, want %+v", k, got, w)
		}
	}
}

func TestRecordExportsKeepsFamiliesApart(t *testing.T) {
	m := map[exportKey]*exportCount{}
	recordExports(m, []string{"174", "6939", "64502"}, 6)
	recordExports(m, []string{"64500", "6939", "64502"}, 4)
	if c := m[exportKey{"6939", "64502", 6}]; c == nil || c.ToTier1 != 1 {
		t.Errorf("v6: got %+v, want ToTier1 1", c)
	}
	if c := m[exportKey{"6939", "64502", 4}]; c == nil || c.ToTier1 != 0 || c.Beyond != 1 {
		t.Errorf("v4: got %+v, want Beyond 1 ToTier1 0", c)
	}
}

// Path [64500 3356 64501 64502]: 3356 passed 64501's route on to 64500, and 64501 passed
// 64502's route on to 3356. The collector-end AS (64500) passed nothing on, so no triple has it
// as X; a repeated path adds nothing.
func TestRecordTriples(t *testing.T) {
	m := map[tripleKey]struct{}{}
	recordTriples(m, []string{"64500", "3356", "64501", "64502"}, 4)
	recordTriples(m, []string{"64500", "3356", "64501", "64502"}, 4)
	recordTriples(m, []string{"64500", "3356", "64501", "64502"}, 6)
	recordTriples(m, []string{"64500", "64502"}, 4)

	want := []tripleKey{
		{"64500", "3356", "64501", 4},
		{"3356", "64501", "64502", 4},
		{"64500", "3356", "64501", 6},
		{"3356", "64501", "64502", 6},
	}
	if len(m) != len(want) {
		t.Fatalf("got %d triples, want %d: %v", len(m), len(want), m)
	}
	for _, k := range want {
		if _, ok := m[k]; !ok {
			t.Errorf("missing %v", k)
		}
	}
}

// Cloudflare sells transit (Magic Transit, BYOIP); see reports/cloudflare_transit_rov.md.
func TestCloudflareIsTransit(t *testing.T) {
	if isNonTransit("13335") {
		t.Fatal("AS13335 must not be non-transit")
	}
	if !isNonTransit("3333") {
		t.Fatal("RIPE NCC AS3333 must stay non-transit")
	}
}

// IXP ASNs (PeeringDB info_type "Route Server") that publish AS0 ASPA (2026-10-15), e.g. AMS-IX, NIX.CZ.
func TestAS0IxpAsnsAreNonTransit(t *testing.T) {
	for _, asn := range []string{"6777", "47200", "51706", "55518", "219524"} {
		if !isNonTransit(asn) {
			t.Errorf("AS%s must be non-transit", asn)
		}
	}
}
