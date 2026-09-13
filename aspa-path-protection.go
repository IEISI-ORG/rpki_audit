// aspa-path-protection.go — ranks real observed (AS_PATH, prefix) combinations
// by how many hops are actually validated by a real, published ASPA record.
//
// A hop (customer AS X -> next-hop AS Y, X closer to the collector per this
// project's documented path-direction convention) counts as protected when
// X has a real ASPA record whose declared Provider Set includes Y. This is
// ground truth against real RPKI objects (data/aspa_real.json, produced by
// rov_utils.fetch_real_aspa_deployment()), not a topology-inferred model.
//
// Standalone from bgp-extractor.go on purpose: bgp-extractor collapses
// AS_PATHs straight to pairwise adjacency counts and never retains the
// per-prefix path itself, which this needs. Re-reads the same `bgpdump -m`
// output bgp-extractor is piped from rather than touching that shared binary.
//
// Memory note: a full-table dump has ~1-7M+ routes; holding every qualifying
// record in memory before ranking (the first version of this tool) drove a
// 30GB-RAM machine into heavy swap and had to be killed. Only a bounded
// top-K candidate pool is ever kept in memory (a min-heap per collector,
// evicting the worst candidate as better ones are found) — the rest of each
// route's data is discarded immediately after its fraction is computed.
package main

import (
	"bufio"
	"container/heap"
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"os/exec"
	"sort"
	"strconv"
	"strings"
	"sync"
)

const minPathASNs = 2 // a path needs >=2 ASNs to have even one testable hop

type pathRecord struct {
	Collector     string
	Prefix        string
	Path          []int // de-duplicated (prepend-collapsed), peer-nearest-first
	TotalHops     int
	ProtectedHops int
	Fraction      float64
}

// worseThan reports whether a is a worse candidate than b under the same
// ranking used for the final output: higher fraction wins; for equal
// fractions on the same prefix, the shorter path wins (matches real BGP
// best-path selection — shorter AS_PATH is the more realistic "actual"
// route for that prefix). Equal fractions on different prefixes are
// incomparable here and treated as equal.
func worseThan(a, b pathRecord) bool {
	if a.Fraction != b.Fraction {
		return a.Fraction < b.Fraction
	}
	if a.Prefix == b.Prefix {
		return a.TotalHops > b.TotalHops
	}
	return false
}

// topKHeap is a bounded min-heap (by "worst first") of pathRecords: once
// full, a new candidate only enters by evicting the current worst, so
// memory never grows past capacity regardless of how many routes are scanned.
type topKHeap struct {
	items []pathRecord
	cap   int
}

func (h topKHeap) Len() int            { return len(h.items) }
func (h topKHeap) Less(i, j int) bool  { return worseThan(h.items[i], h.items[j]) }
func (h topKHeap) Swap(i, j int)       { h.items[i], h.items[j] = h.items[j], h.items[i] }
func (h *topKHeap) Push(x interface{}) { h.items = append(h.items, x.(pathRecord)) }
func (h *topKHeap) Pop() interface{} {
	old := h.items
	n := len(old)
	item := old[n-1]
	h.items = old[:n-1]
	return item
}

// offer considers rec for inclusion in the bounded top-K pool.
func (h *topKHeap) offer(rec pathRecord) {
	if h.Len() < h.cap {
		heap.Push(h, rec)
		return
	}
	if worseThan(h.items[0], rec) { // rec is better than the current worst kept
		heap.Pop(h)
		heap.Push(h, rec)
	}
}

// loadRealASPA reads data/aspa_real.json ({"customer_asn": [provider_asn, ...]})
// into an int-keyed map for fast lookup during path validation.
func loadRealASPA(path string) (map[int][]int, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}
	raw := map[string][]int{}
	if err := json.Unmarshal(data, &raw); err != nil {
		return nil, err
	}
	result := make(map[int][]int, len(raw))
	for k, v := range raw {
		asn, err := strconv.Atoi(k)
		if err != nil {
			continue
		}
		result[asn] = v
	}
	return result, nil
}

// dedupePath collapses consecutive repeated ASNs (AS-path prepending) and
// rejects paths containing a non-numeric token (AS_SET/confederation
// segments) rather than silently dropping just that token, since a partial
// path would fabricate an adjacency between ASNs that were never really
// direct neighbours.
func dedupePath(tokens []string) ([]int, bool) {
	deduped := make([]int, 0, len(tokens))
	last := -1
	first := true
	for _, t := range tokens {
		asn, err := strconv.Atoi(t)
		if err != nil {
			return nil, false
		}
		if first || asn != last {
			deduped = append(deduped, asn)
			last = asn
			first = false
		}
	}
	return deduped, true
}

func containsInt(list []int, target int) bool {
	for _, v := range list {
		if v == target {
			return true
		}
	}
	return false
}

// processDump streams `bgpdump -m <dump>` and folds every route with a
// valid, sufficiently-long AS_PATH into a bounded top-K pool — it never
// holds more than poolSize records for this collector at once, regardless
// of how many million routes the dump contains. bgpdump handles the .gz
// decompression itself (matches how do_data_gathering invokes it).
func processDump(collector, dumpPath string, realASPA map[int][]int, poolSize int) []pathRecord {
	cmd := exec.Command("bgpdump", "-m", dumpPath)
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		fmt.Fprintf(os.Stderr, "    [!] %s: %v\n", collector, err)
		return nil
	}
	if err := cmd.Start(); err != nil {
		fmt.Fprintf(os.Stderr, "    [!] %s: %v\n", collector, err)
		return nil
	}

	pool := &topKHeap{cap: poolSize}
	scanner := bufio.NewScanner(stdout)
	scanner.Buffer(make([]byte, 0, 64*1024), 1024*1024)
	routeCount, qualifying := 0, 0
	for scanner.Scan() {
		routeCount++
		fields := strings.Split(scanner.Text(), "|")
		if len(fields) < 7 {
			continue
		}
		prefix := fields[5]
		pathTokens := strings.Fields(fields[6])
		if len(pathTokens) == 0 {
			continue
		}
		deduped, ok := dedupePath(pathTokens)
		if !ok || len(deduped) < minPathASNs {
			continue
		}

		totalHops := len(deduped) - 1
		protectedHops := 0
		for i := 0; i < totalHops; i++ {
			customer, provider := deduped[i], deduped[i+1]
			if providers, exists := realASPA[customer]; exists && containsInt(providers, provider) {
				protectedHops++
			}
		}

		qualifying++
		pool.offer(pathRecord{
			Collector:     collector,
			Prefix:        prefix,
			Path:          deduped,
			TotalHops:     totalHops,
			ProtectedHops: protectedHops,
			Fraction:      float64(protectedHops) / float64(totalHops),
		})
	}
	if err := cmd.Wait(); err != nil {
		fmt.Fprintf(os.Stderr, "    [!] %s: bgpdump exited with error: %v\n", collector, err)
	}
	fmt.Printf("    - %-6s %9d routes, %9d qualifying (>=%d ASNs after de-dup), top %d kept\n",
		collector, routeCount, qualifying, minPathASNs, pool.Len())
	return pool.items
}

func formatPath(path []int) string {
	parts := make([]string, len(path))
	for i, asn := range path {
		parts[i] = strconv.Itoa(asn)
	}
	return strings.Join(parts, " ")
}

func writeCSV(path string, records []pathRecord) error {
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()
	fmt.Fprintln(f, "collector,prefix,as_path,total_hops,protected_hops,fraction_protected")
	for _, r := range records {
		fmt.Fprintf(f, "%s,%s,\"%s\",%d,%d,%.4f\n",
			r.Collector, r.Prefix, formatPath(r.Path), r.TotalHops, r.ProtectedHops, r.Fraction)
	}
	return nil
}

func main() {
	outputDir := flag.String("output-dir", "output", "directory containing <rrc>-bview.gz dumps")
	aspaFile := flag.String("aspa-file", "data/aspa_real.json", "path to the cached real ASPA JSON")
	csvOut := flag.String("csv-out", "aspa_path_protection.csv", "path to write the top candidate pool as CSV")
	topN := flag.Int("top", 10, "number of top records to print")
	poolSize := flag.Int("pool-size", 1000, "candidate pool kept per collector (bounds memory use, not just output size)")
	flag.Parse()

	realASPA, err := loadRealASPA(*aspaFile)
	if err != nil {
		fmt.Fprintf(os.Stderr, "[!] Failed to load %s: %v\n", *aspaFile, err)
		fmt.Fprintf(os.Stderr, "    Run analyze_aspa_real_deployment.py first to populate this cache.\n")
		os.Exit(1)
	}
	fmt.Printf("[*] Loaded %d real ASPA records from %s\n", len(realASPA), *aspaFile)

	// The 5 collector dumps are fully independent (separate files, separate
	// bgpdump subprocesses, no shared mutable state until the final merge),
	// and a single-collector test run showed this is dominated by I/O/decompress
	// time (sys) rather than CPU, so processing them concurrently is a safe,
	// direct win rather than running one after another.
	collectors := []string{"rrc00", "rrc14", "rrc19", "rrc23", "rrc24"}
	fmt.Println("[*] Processing collector dumps concurrently (bgpdump -m, dual-stack)...")
	results := make([][]pathRecord, len(collectors))
	var wg sync.WaitGroup
	for i, rrc := range collectors {
		dumpPath := fmt.Sprintf("%s/%s-bview.gz", *outputDir, rrc)
		if _, err := os.Stat(dumpPath); err != nil {
			fmt.Printf("    - %-6s dump not found at %s, skipping\n", rrc, dumpPath)
			continue
		}
		wg.Add(1)
		go func(idx int, collector, path string) {
			defer wg.Done()
			results[idx] = processDump(collector, path, realASPA, *poolSize)
		}(i, rrc, dumpPath)
	}
	wg.Wait()

	var all []pathRecord
	for _, recs := range results {
		all = append(all, recs...)
	}

	fmt.Printf("[*] Ranking %d pooled candidates (top %d per collector)...\n", len(all), *poolSize)

	// Final sort over the small pooled set only — see worseThan for the
	// ranking rule (fraction of hops protected primary, same-prefix
	// shorter-path tie-break secondary).
	sort.SliceStable(all, func(i, j int) bool { return worseThan(all[j], all[i]) })

	if err := writeCSV(*csvOut, all); err != nil {
		fmt.Fprintf(os.Stderr, "[!] Failed to write %s: %v\n", *csvOut, err)
	} else {
		fmt.Printf("[+] Top candidate pool (%d records) saved to %s\n", len(all), *csvOut)
	}

	fmt.Println()
	fmt.Println(strings.Repeat("=", 100))
	fmt.Printf(" TOP %d MOST-PROTECTED OBSERVED (AS_PATH, PREFIX) COMBINATIONS\n", *topN)
	fmt.Println(strings.Repeat("=", 100))
	fmt.Printf("%-9s | %-8s | %-23s | %-19s | AS_PATH\n", "Collector", "Fraction", "Hops (protected/total)", "Prefix")
	fmt.Println(strings.Repeat("-", 100))
	n := *topN
	if n > len(all) {
		n = len(all)
	}
	for _, r := range all[:n] {
		fmt.Printf("%-9s | %7.1f%% | %11d / %-10d | %-19s | %s\n",
			r.Collector, r.Fraction*100, r.ProtectedHops, r.TotalHops, r.Prefix, formatPath(r.Path))
	}
}
