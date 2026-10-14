package main

import (
	"bufio"
	"compress/gzip"
	"encoding/csv"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"
	"runtime"
	"sort"
	"strings"
	"sync"
	"time"
)

// ASRelationship represents a neighbor relationship between two ASNs
type ASRelationship struct {
	FromASN string
	ToASN   string
	Type    string // "left" or "right"
	Count   int64
}

// ASNStats holds statistics for a single ASN
type ASNStats struct {
	ASN            string
	LeftNeighbors  map[string]int64 // upstream/providers
	RightNeighbors map[string]int64 // downstream/customers
	TotalPaths     int64
}

func main() {
	// Command line flags
	inputFile := flag.String("input", "", "Input BGPdump file (supports .gz)")
	outputDir := flag.String("output", "output", "Output directory for results")
	workers := flag.Int("workers", runtime.NumCPU(), "Number of worker goroutines")
	verbose := flag.Bool("verbose", false, "Verbose output")
	flag.Parse()

	if *inputFile == "" {
		log.Fatal("Usage: bgp-extractor -input <bgpdump-file>")
	}

	start := time.Now()

	// Create output directory
	if err := os.MkdirAll(*outputDir, 0755); err != nil {
		log.Fatal("Failed to create output directory:", err)
	}

	// Process the BGP dump
	stats, relationships, exports, triples := processBGPDump(*inputFile, *workers, *verbose)

	// Write outputs
	if err := writeASNStats(filepath.Join(*outputDir, "asn_stats.csv"), stats); err != nil {
		log.Fatal("Failed to write ASN stats:", err)
	}

	if err := writeRelationships(filepath.Join(*outputDir, "relationships.csv"), relationships); err != nil {
		log.Fatal("Failed to write relationships:", err)
	}

	if err := writeExports(filepath.Join(*outputDir, "exports.csv"), exports); err != nil {
		log.Fatal("Failed to write exports:", err)
	}

	if err := writeTriples(filepath.Join(*outputDir, "triples.csv"), triples); err != nil {
		log.Fatal("Failed to write triples:", err)
	}

	if err := writeTopASNs(filepath.Join(*outputDir, "top_asns.txt"), stats); err != nil {
		log.Fatal("Failed to write top ASNs:", err)
	}

	elapsed := time.Since(start)
	fmt.Printf("\n✓ Processing complete in %s\n", elapsed)
	fmt.Printf("✓ Analyzed %d unique ASNs\n", len(stats))
	fmt.Printf("✓ Found %d unique AS relationships\n", len(relationships))
	fmt.Printf("✓ Results written to: %s/\n", *outputDir)
}

func processBGPDump(filename string, workers int, verbose bool) (map[string]*ASNStats, map[string]*ASRelationship, map[exportKey]*exportCount, map[tripleKey]struct{}) {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal("Failed to open input file:", err)
	}
	defer file.Close()

	var reader io.Reader = file

	// Handle gzip compression
	if strings.HasSuffix(filename, ".gz") {
		gzReader, err := gzip.NewReader(file)
		if err != nil {
			log.Fatal("Failed to create gzip reader:", err)
		}
		defer gzReader.Close()
		reader = gzReader
	}

	// Create channels for work distribution
	linesChan := make(chan string, workers*100)
	resultsChan := make(chan *pathResult, workers*100)

	// Start worker goroutines
	var wg sync.WaitGroup
	for i := 0; i < workers; i++ {
		wg.Add(1)
		go worker(linesChan, resultsChan, &wg)
	}

	// Start result collector
	doneChan := make(chan struct{})
	stats := make(map[string]*ASNStats)
	relationships := make(map[string]*ASRelationship)
	exports := make(map[exportKey]*exportCount)
	triples := make(map[tripleKey]struct{})
	go collectResults(resultsChan, stats, relationships, exports, triples, doneChan, verbose)

	// Read and distribute lines
	scanner := bufio.NewScanner(reader)
	buf := make([]byte, 0, 1024*1024) // 1MB buffer
	scanner.Buffer(buf, 10*1024*1024) // 10MB max

	lineCount := int64(0)
	for scanner.Scan() {
		linesChan <- scanner.Text()
		lineCount++

		if verbose && lineCount%100000 == 0 {
			fmt.Fprintf(os.Stderr, "\rProcessed %d lines...", lineCount)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal("Error reading file:", err)
	}

	// Signal completion
	close(linesChan)
	wg.Wait()
	close(resultsChan)
	<-doneChan

	if verbose {
		fmt.Fprintf(os.Stderr, "\rProcessed %d lines total\n", lineCount)
	}

	return stats, relationships, exports, triples
}

type pathResult struct {
	asPath []string
	af     int
}

func worker(lines <-chan string, results chan<- *pathResult, wg *sync.WaitGroup) {
	defer wg.Done()

	for line := range lines {
		asPath, af := parseRoute(line)
		if len(asPath) >= 2 {
			results <- &pathResult{asPath: asPath, af: af}
		}
	}
}

// parseRoute returns the cleaned AS path and the address family (4 or 6) of a TABLE_DUMP2
// line from `bgpdump -m`; the prefix is field 5.
func parseRoute(line string) ([]string, int) {
	path := parseASPath(line)
	if path == nil {
		return nil, 0
	}
	if strings.Contains(strings.Split(line, "|")[5], ":") {
		return path, 6
	}
	return path, 4
}

// exportKey identifies one observed export: X passed the route it learned from C (its right
// neighbour, toward the origin) on to the AS on its left, in one address family.
type exportKey struct {
	X, C string
	AF   int
}

// exportCount counts paths per exportKey. Paths: the link X–C appears; Beyond: X passed C's
// route on to another AS (the link is not only at the collector end of the path); ToTier1: that
// AS is a Tier 1 and X is not, so by valley-free routing C is X's customer (or a route leak).
type exportCount struct {
	Paths, Beyond, ToTier1 int64
}

func recordExports(m map[exportKey]*exportCount, path []string, af int) {
	for i := 0; i < len(path)-1; i++ {
		k := exportKey{path[i], path[i+1], af}
		c := m[k]
		if c == nil {
			c = &exportCount{}
			m[k] = c
		}
		c.Paths++
		if i > 0 {
			c.Beyond++
			if isTier1(path[i-1]) && !isTier1(path[i]) {
				c.ToTier1++
			}
		}
	}
}

// tripleKey is one observed hand-on: X passed the route it learned from C (its right neighbour)
// on to Y (its left neighbour), in one address family. build_topology_from_go infers providers
// top-down from these: if Y is X's provider or a Tier 1 peer, C is X's customer.
type tripleKey struct {
	Y, X, C string
	AF      int
}

func recordTriples(m map[tripleKey]struct{}, path []string, af int) {
	for i := 1; i < len(path)-1; i++ {
		m[tripleKey{path[i-1], path[i], path[i+1], af}] = struct{}{}
	}
}

func writeTriples(filename string, m map[tripleKey]struct{}) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()
	if err := writer.Write([]string{"AF", "Y", "X", "C"}); err != nil {
		return err
	}
	for k := range m {
		if err := writer.Write([]string{fmt.Sprintf("%d", k.AF), k.Y, k.X, k.C}); err != nil {
			return err
		}
	}
	fmt.Printf("✓ Wrote %d triples to: %s\n", len(m), filename)
	return nil
}

func writeExports(filename string, m map[exportKey]*exportCount) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()
	if err := writer.Write([]string{"X", "C", "AF", "Paths", "Beyond", "ToTier1"}); err != nil {
		return err
	}
	for k, c := range m {
		if err := writer.Write([]string{k.X, k.C, fmt.Sprintf("%d", k.AF),
			fmt.Sprintf("%d", c.Paths), fmt.Sprintf("%d", c.Beyond), fmt.Sprintf("%d", c.ToTier1)}); err != nil {
			return err
		}
	}
	fmt.Printf("✓ Wrote %d export records to: %s\n", len(m), filename)
	return nil
}

func parseASPath(line string) []string {
	fields := strings.Split(line, "|")

	// Check if it's a TABLE_DUMP2 entry
	if len(fields) < 7 || fields[0] != "TABLE_DUMP2" {
		return nil
	}

	// AS path is field 6 (0-indexed)
	asPathStr := fields[6]
	if asPathStr == "" {
		return nil
	}

	// Split AS path and clean it
	rawPath := strings.Fields(asPathStr)
	var cleanPath []string
	var prevASN string

	for _, asn := range rawPath {
		// Remove AS sets (curly braces)
		asn = strings.Trim(asn, "{}")

		// Skip if it's part of an AS set with commas
		if strings.Contains(asn, ",") {
			parts := strings.Split(asn, ",")
			asn = parts[0] // Take first ASN from set
		}

		// Remove consecutive duplicates (AS path prepending)
		if asn != prevASN && asn != "" {
			cleanPath = append(cleanPath, asn)
			prevASN = asn
		}
	}

	return cleanPath
}

func collectResults(results <-chan *pathResult, stats map[string]*ASNStats,
	relationships map[string]*ASRelationship, exports map[exportKey]*exportCount,
	triples map[tripleKey]struct{}, done chan<- struct{}, verbose bool) {

	count := int64(0)

	for result := range results {
		count++

		if verbose && count%10000 == 0 {
			fmt.Fprintf(os.Stderr, "\rCollected %d paths...", count)
		}

		recordExports(exports, result.asPath, result.af)
		recordTriples(triples, result.asPath, result.af)

		// Process each AS in the path
		for i, asn := range result.asPath {
			// Initialize ASN stats if needed
			if stats[asn] == nil {
				stats[asn] = &ASNStats{
					ASN:            asn,
					LeftNeighbors:  make(map[string]int64),
					RightNeighbors: make(map[string]int64),
				}
			}
			stats[asn].TotalPaths++

			// Record left neighbor (toward-collector / data-plane downstream / customer direction).
			// In TABLE_DUMP2 paths [peer, ..., origin], position i-1 is closer to the
			// route collector.  In Gao-Rexford terms this is the side that receives
			// transit FROM this ASN — i.e. its customers or its own peer at the top.
			// Do NOT confuse with "upstream" in the route-announcement sense.
			if i > 0 {
				leftASN := result.asPath[i-1]
				stats[asn].LeftNeighbors[leftASN]++

				// Record relationship
				relKey := fmt.Sprintf("%s->%s:left", asn, leftASN)
				if relationships[relKey] == nil {
					relationships[relKey] = &ASRelationship{
						FromASN: asn,
						ToASN:   leftASN,
						Type:    "left",
					}
				}
				relationships[relKey].Count++
			}

			// Record right neighbor (toward-origin / data-plane upstream / provider direction).
			// Position i+1 is closer to the route origin.  In Gao-Rexford terms this
			// is the side that provides transit TO this ASN — i.e. its providers or
			// its own peer at the top of the valley.
			// Do NOT confuse with "downstream" in the route-announcement sense.
			if i < len(result.asPath)-1 {
				rightASN := result.asPath[i+1]
				stats[asn].RightNeighbors[rightASN]++

				// Record relationship
				relKey := fmt.Sprintf("%s->%s:right", asn, rightASN)
				if relationships[relKey] == nil {
					relationships[relKey] = &ASRelationship{
						FromASN: asn,
						ToASN:   rightASN,
						Type:    "right",
					}
				}
				relationships[relKey].Count++
			}
		}
	}

	if verbose {
		fmt.Fprintf(os.Stderr, "\rCollected %d paths total\n", count)
	}

	done <- struct{}{}
}

func writeASNStats(filename string, stats map[string]*ASNStats) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	// Write header
	if err := writer.Write([]string{"ASN", "Left_Count", "Right_Count", "Total_Neighbors", "Total_Paths"}); err != nil {
		return err
	}

	// Sort ASNs by total neighbor count
	type asnSort struct {
		asn   string
		count int
	}
	var sortable []asnSort
	for asn, stat := range stats {
		sortable = append(sortable, asnSort{
			asn:   asn,
			count: len(stat.LeftNeighbors) + len(stat.RightNeighbors),
		})
	}
	sort.Slice(sortable, func(i, j int) bool {
		return sortable[i].count > sortable[j].count
	})

	// Write data
	for _, item := range sortable {
		stat := stats[item.asn]
		if err := writer.Write([]string{
			stat.ASN,
			fmt.Sprintf("%d", len(stat.LeftNeighbors)),
			fmt.Sprintf("%d", len(stat.RightNeighbors)),
			fmt.Sprintf("%d", len(stat.LeftNeighbors)+len(stat.RightNeighbors)),
			fmt.Sprintf("%d", stat.TotalPaths),
		}); err != nil {
			return err
		}
	}

	fmt.Printf("✓ Wrote ASN statistics to: %s\n", filename)
	return nil
}

func writeRelationships(filename string, relationships map[string]*ASRelationship) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	// Write header
	if err := writer.Write([]string{"From_ASN", "To_ASN", "Type", "Count"}); err != nil {
		return err
	}

	// Sort by count
	var rels []*ASRelationship
	for _, rel := range relationships {
		rels = append(rels, rel)
	}
	sort.Slice(rels, func(i, j int) bool {
		return rels[i].Count > rels[j].Count
	})

	// Write data
	for _, rel := range rels {
		if err := writer.Write([]string{
			rel.FromASN,
			rel.ToASN,
			rel.Type,
			fmt.Sprintf("%d", rel.Count),
		}); err != nil {
			return err
		}
	}

	fmt.Printf("✓ Wrote relationships to: %s\n", filename)
	return nil
}

func writeTopASNs(filename string, stats map[string]*ASNStats) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	// Sort ASNs by total neighbor count
	type asnRank struct {
		asn   string
		left  int
		right int
		total int
	}
	var rankings []asnRank
	for asn, stat := range stats {
		rankings = append(rankings, asnRank{
			asn:   asn,
			left:  len(stat.LeftNeighbors),
			right: len(stat.RightNeighbors),
			total: len(stat.LeftNeighbors) + len(stat.RightNeighbors),
		})
	}
	sort.Slice(rankings, func(i, j int) bool {
		return rankings[i].total > rankings[j].total
	})

	// Write top 100
	fmt.Fprintf(file, "Top 100 ASNs by Total Neighbor Count\n")
	fmt.Fprintf(file, "=====================================\n\n")

	limit := 100
	if len(rankings) < limit {
		limit = len(rankings)
	}

	for i := 0; i < limit; i++ {
		rank := rankings[i]
		fmt.Fprintf(file, "%3d. AS%-6s - Left: %4d, Right: %4d, Total: %4d\n",
			i+1, rank.asn, rank.left, rank.right, rank.total)
	}

	// Add some interesting analysis
	fmt.Fprintf(file, "\n\nTier 1 Analysis (ASNs with very few left neighbors)\n")
	fmt.Fprintf(file, "===================================================\n\n")

	var tier1Candidates []asnRank
	for _, rank := range rankings {
		if rank.total > 50 && rank.left < 10 && rank.right > 20 {
			tier1Candidates = append(tier1Candidates, rank)
		}
	}

	sort.Slice(tier1Candidates, func(i, j int) bool {
		return tier1Candidates[i].left < tier1Candidates[j].left
	})

	for i, rank := range tier1Candidates {
		if i >= 20 {
			break
		}
		fmt.Fprintf(file, "AS%-6s - Left: %4d, Right: %4d (%.1f%% downstream)\n",
			rank.asn, rank.left, rank.right,
			float64(rank.right)/float64(rank.total)*100)
	}

	fmt.Printf("✓ Wrote top ASNs analysis to: %s\n", filename)
	return nil
}
