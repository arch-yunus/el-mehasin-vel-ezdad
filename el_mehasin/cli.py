"""
Command-line interface for el-mehasin-vel-ezdad suite.
"""
import sys
import argparse
import json
from .corpus import DialecticCorpus
from .dialectic import DialecticAnalyzer

def main():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    parser = argparse.ArgumentParser(
        prog="el-mehasin",
        description="el-mehasin-vel-ezdad: Classical Arabic Bipolar Dialectic Corpus CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # list
    subparsers.add_parser("list", help="List all 20 dialectic pairs in the corpus")

    # search
    search_parser = subparsers.add_parser("search", help="Search dialectic pairs by keyword")
    search_parser.add_argument("query", type=str, help="Search query string")

    # get
    get_parser = subparsers.add_parser("get", help="Get full details for a specific dialectic pair")
    get_parser.add_argument("entry_id", type=str, help="e.g. pair_001_samt_beyan")

    # stats
    subparsers.add_parser("stats", help="Display corpus statistics and rhetorical device frequency")

    # validate
    subparsers.add_parser("validate", help="Run repository and schema validator")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    corpus = DialecticCorpus()
    analyzer = DialecticAnalyzer(corpus)

    if args.command == "list":
        print(f"\n{'='*70}")
        print(f"  📜 EL-MEHASIN-VEL-EZDAD CORPUS ({len(corpus)} DIALECTIC PAIRS)")
        print(f"{'='*70}")
        for idx, p in enumerate(corpus.pairs, 1):
            print(f"[{idx:02d}] {p.entry_id: <26} | {p.thesis.concept}  vs.  {p.antithesis.concept}")
        print(f"{'='*70}\n")

    elif args.command == "search":
        results = corpus.search(args.query)
        print(f"\nFound {len(results)} matches for '{args.query}':")
        for p in results:
            print(f"- {p.entry_id}: {p.thesis.concept} vs. {p.antithesis.concept} ({p.classical_arabic_title})")
        print()

    elif args.command == "get":
        pair = corpus.get_by_id(args.entry_id)
        if not pair:
            print(f"Error: Pair '{args.entry_id}' not found.")
            sys.exit(1)
        print(f"\n{'='*70}")
        print(f"Entry ID : {pair.entry_id} ({pair.topic_slug})")
        print(f"Title    : {pair.classical_arabic_title}")
        print(f"{'-'*70}")
        print(f"🟢 THESIS ({pair.thesis.pole.upper()}): {pair.thesis.concept}")
        print(f"   Premise : {pair.thesis.core_premise}")
        print(f"   Quote   : {pair.thesis.top_quote.arabic}")
        print(f"   Meaning : {pair.thesis.top_quote.turkish} ({pair.thesis.top_quote.source})")
        print(f"{'-'*70}")
        print(f"🔴 ANTITHESIS ({pair.antithesis.pole.upper()}): {pair.antithesis.concept}")
        print(f"   Premise : {pair.antithesis.core_premise}")
        print(f"   Quote   : {pair.antithesis.top_quote.arabic}")
        print(f"   Meaning : {pair.antithesis.top_quote.turkish} ({pair.antithesis.top_quote.source})")
        print(f"{'-'*70}")
        print(f"⚖️ SYNTHESIS : {pair.dialectic_synthesis}")
        print(f"🎭 DEVICES   : {', '.join(pair.metadata.get('rhetorical_devices', []))}")
        print(f"{'='*70}\n")

    elif args.command == "stats":
        st = analyzer.get_corpus_statistics()
        print(f"\n{'='*50}")
        print("  📊 CORPUS ANALYTICS & METRICS")
        print(f"{'='*50}")
        print(f"Total Dialectic Pairs : {st['total_pairs']}")
        print(f"Total Opposing Poles  : {st['total_poles']}")
        print(f"Total Poetry & Quotes : {st['total_quotes']}")
        print(f"\nRhetorical Devices Distribution:")
        for dev, count in sorted(st["rhetorical_devices_frequency"].items(), key=lambda x: -x[1]):
            print(f"  • {dev: <20} : {count} instances")
        print(f"{'='*50}\n")

    elif args.command == "validate":
        from scripts.validator import validate_repository
        validate_repository()

if __name__ == "__main__":
    main()
