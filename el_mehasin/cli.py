"""
Command-line interface for el-mehasin-vel-ezdad suite.
"""
import sys
import random
import argparse
import json
from .corpus import DialecticCorpus
from .dialectic import DialecticAnalyzer
from .rhetoric import RhetoricClassifier


def main():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    parser = argparse.ArgumentParser(
        prog="el-mehasin",
        description="el-mehasin-vel-ezdad: Classical Arabic Bipolar Dialectic Corpus CLI (v1.1.0)"
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

    # compare
    comp_parser = subparsers.add_parser("compare", help="Side-by-side comparative card view for a pair")
    comp_parser.add_argument("entry_id", type=str, help="e.g. pair_002_cud_buhl")

    # stats
    subparsers.add_parser("stats", help="Display corpus statistics and rhetorical device frequency")

    # graph
    subparsers.add_parser("graph", help="Export dialectic network graph JSON structure")

    # export-tei
    subparsers.add_parser("export-tei", help="Export corpus to TEI P5 XML format")

    # export-hf
    subparsers.add_parser("export-hf", help="Export corpus to Hugging Face dataset format")

    # rhetoric
    rhet_parser = subparsers.add_parser("rhetoric", help="Analyze rhetorical devices in text or an entry")
    rhet_parser.add_argument("target", type=str, help="Entry ID or raw text string")

    # quiz
    subparsers.add_parser("quiz", help="Interactive terminal game: Guess the dialectic pole for classical quotes")

    # validate
    subparsers.add_parser("validate", help="Run repository and schema validator")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    corpus = DialecticCorpus()
    analyzer = DialecticAnalyzer(corpus)

    if args.command == "list":
        print(f"\n{'='*76}")
        print(f"  📜 EL-MEHASIN-VEL-EZDAD CORPUS ({len(corpus)} DIALECTIC PAIRS)")
        print(f"{'='*76}")
        for idx, p in enumerate(corpus.pairs, 1):
            print(f"[{idx:02d}] {p.entry_id: <26} | {p.thesis.concept: <25} vs. {p.antithesis.concept}")
        print(f"{'='*76}\n")

    elif args.command == "search":
        results = corpus.search(args.query)
        print(f"\nFound {len(results)} matches for '{args.query}':")
        for p in results:
            print(f"• {p.entry_id}: {p.thesis.concept} vs. {p.antithesis.concept} ({p.classical_arabic_title})")
        print()

    elif args.command == "get":
        pair = corpus.get_by_id(args.entry_id)
        if not pair:
            print(f"Error: Pair '{args.entry_id}' not found.")
            sys.exit(1)
        print(f"\n{'='*76}")
        print(f"Entry ID : {pair.entry_id} ({pair.topic_slug})")
        print(f"Title    : {pair.classical_arabic_title}")
        print(f"{'-'*76}")
        print(f"🟢 THESIS ({pair.thesis.pole.upper()}): {pair.thesis.concept}")
        print(f"   Premise : {pair.thesis.core_premise}")
        print(f"   Quote   : {pair.thesis.top_quote.arabic}")
        print(f"   Meaning : {pair.thesis.top_quote.turkish} ({pair.thesis.top_quote.source})")
        for idx, q in enumerate(pair.thesis.additional_quotes, 1):
            print(f"   + [{idx}]   : {q.arabic} -> {q.turkish} ({q.source})")
        print(f"{'-'*76}")
        print(f"🔴 ANTITHESIS ({pair.antithesis.pole.upper()}): {pair.antithesis.concept}")
        print(f"   Premise : {pair.antithesis.core_premise}")
        print(f"   Quote   : {pair.antithesis.top_quote.arabic}")
        print(f"   Meaning : {pair.antithesis.top_quote.turkish} ({pair.antithesis.top_quote.source})")
        for idx, q in enumerate(pair.antithesis.additional_quotes, 1):
            print(f"   + [{idx}]   : {q.arabic} -> {q.turkish} ({q.source})")
        print(f"{'-'*76}")
        print(f"⚖️ SYNTHESIS : {pair.dialectic_synthesis}")
        print(f"🎭 DEVICES   : {', '.join(pair.metadata.get('rhetorical_devices', []))}")
        print(f"{'='*76}\n")

    elif args.command == "compare":
        comp = analyzer.compare_poles(args.entry_id)
        if not comp:
            print(f"Error: Pair '{args.entry_id}' not found.")
            sys.exit(1)
        print(f"\n{'='*80}")
        print(f"  ⚖️ DIALECTIC POLARITY COMPARISON: {comp['title']}")
        print(f"{'='*80}")
        print(f"🟢 [TEZ / EL-MEHÂSİN]                🔴 [ANTİTEZ / EL-EZDÂD]")
        print(f"Kavram : {comp['thesis']['concept']: <30} Kavram : {comp['antithesis']['concept']}")
        print(f"Delil  : {comp['thesis']['total_quotes']} Şahit                        Delil  : {comp['antithesis']['total_quotes']} Şahit")
        print(f"{'-'*80}")
        print("🟢 Tez Öncülü:")
        print(f"   {comp['thesis']['premise']}")
        print("\n🔴 Antitez Öncülü:")
        print(f"   {comp['antithesis']['premise']}")
        print(f"{'-'*80}")
        print("⚖️ Sentez (Tevâzün / İtidal):")
        print(f"   {comp['synthesis']}")
        print(f"{'='*80}\n")

    elif args.command == "stats":
        st = analyzer.get_corpus_statistics()
        print(f"\n{'='*56}")
        print("  📊 CORPUS ANALYTICS & METRICS")
        print(f"{'='*56}")
        print(f"Total Dialectic Pairs    : {st['total_pairs']}")
        print(f"Total Opposing Poles     : {st['total_poles']}")
        print(f"Total Poetry & Quotes    : {st['total_quotes']}")
        print(f"Evidence Balance Ratio   : {st['dialectic_balance_ratio']} (Thesis/Antithesis)")
        print(f"\nRhetorical Devices Distribution:")
        for dev, count in sorted(st["rhetorical_devices_frequency"].items(), key=lambda x: -x[1]):
            print(f"  • {dev: <22} : {count: >2} instances")
        print(f"{'='*56}\n")

    elif args.command == "graph":
        graph = analyzer.get_network_graph_data()
        print(json.dumps(graph, ensure_ascii=False, indent=2))

    elif args.command == "export-tei":
        from scripts.export_tei_xml import export_to_tei
        export_to_tei()

    elif args.command == "export-hf":
        from scripts.export_huggingface import export_to_huggingface
        export_to_huggingface()

    elif args.command == "rhetoric":
        pair = corpus.get_by_id(args.target)
        if pair:
            text_to_scan = f"{pair.thesis.top_quote.arabic} {pair.thesis.core_premise} {pair.antithesis.top_quote.arabic} {pair.antithesis.core_premise}"
            print(f"\nScanning entry '{pair.entry_id}' for Balaghah devices:")
        else:
            text_to_scan = args.target
            print(f"\nScanning raw text for Balaghah devices:")

        detected = RhetoricClassifier.analyze_text(text_to_scan)
        density = RhetoricClassifier.calculate_rhetorical_density(text_to_scan)
        print(f"Rhetorical Density Score: {density}%\n")
        if not detected:
            print("No specific rule-based rhetorical devices triggered.")
        for d in detected:
            print(f"• {d['device']} ({d['arabic_name']}) - {d['branch']}: {d['description']} ({d['match_count']} eşleşme)")
        print()

    elif args.command == "quiz":
        pair = random.choice(corpus.pairs)
        use_thesis = random.choice([True, False])
        pole = pair.thesis if use_thesis else pair.antithesis
        quote = pole.top_quote

        print(f"\n{'='*70}")
        print("  🎲 KLASİK DİYALEKTİK MÜNAZARA BİLGİ YARIŞMASI")
        print(f"{'='*70}")
        print(f"\nArapça Şahit : {quote.arabic}")
        print(f"Türkçe Meal  : \"{quote.turkish}\"")
        print(f"Kaynak       : {quote.source}")
        print(f"\nSoru: Bu şahit hangi kavramın savunulmasında (El-Mehâsin veya El-Ezdâd) kullanılmıştır?\n")
        print(f"1) {pair.thesis.concept} (El-Mehâsin)")
        print(f"2) {pair.antithesis.concept} (El-Ezdâd)")
        
        try:
            choice = input("\nCevabınız (1 veya 2): ").strip()
            correct = "1" if use_thesis else "2"
            if choice == correct:
                print(f"\n✅ TEBRİKLER! Doğru bildiniz! Bu şahit '{pole.concept}' kutbuna aittir.")
            else:
                print(f"\n❌ YANLIŞ! Doğru cevap ({correct}) '{pole.concept}' olmalıydı.")
            print(f"Diyalektik Sentez: {pair.dialectic_synthesis}\n")
        except EOFError:
            print()

    elif args.command == "validate":
        from scripts.validator import validate_repository
        validate_repository()


if __name__ == "__main__":
    main()
