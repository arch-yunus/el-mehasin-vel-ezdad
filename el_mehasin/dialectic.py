"""
Dialectic analysis and polarity balance utilities.
"""
from typing import List, Dict, Any
from .corpus import DialecticCorpus, DialecticPair

class DialecticAnalyzer:
    def __init__(self, corpus: DialecticCorpus):
        self.corpus = corpus

    def get_corpus_statistics(self) -> Dict[str, Any]:
        total_pairs = len(self.corpus)
        total_quotes = 0
        devices_freq: Dict[str, int] = {}

        for p in self.corpus.pairs:
            total_quotes += 1 + len(p.thesis.additional_quotes)
            total_quotes += 1 + len(p.antithesis.additional_quotes)
            for d in p.metadata.get("rhetorical_devices", []):
                devices_freq[d] = devices_freq.get(d, 0) + 1

        return {
            "total_pairs": total_pairs,
            "total_poles": total_pairs * 2,
            "total_quotes": total_quotes,
            "rhetorical_devices_frequency": devices_freq
        }

    def generate_dialectic_matrix(self) -> List[Dict[str, str]]:
        matrix = []
        for p in self.corpus.pairs:
            matrix.append({
                "entry_id": p.entry_id,
                "topic": p.topic_slug,
                "arabic_title": p.classical_arabic_title,
                "thesis": p.thesis.concept,
                "antithesis": p.antithesis.concept,
                "synthesis": p.dialectic_synthesis
            })
        return matrix
