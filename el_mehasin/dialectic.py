"""
Dialectic analysis, polarity balance, and graph representation utilities.
"""
from dataclasses import asdict
from typing import List, Dict, Any, Optional
from .corpus import DialecticCorpus, DialecticPair


class DialecticAnalyzer:
    """
    Advanced analytical engine for exploring dialectic pairs, evidence balance,
    and relational graph structures in the corpus.
    """
    def __init__(self, corpus: DialecticCorpus):
        self.corpus = corpus

    def get_corpus_statistics(self) -> Dict[str, Any]:
        """Calculates macro metrics across the entire corpus."""
        total_pairs = len(self.corpus)
        total_quotes = 0
        devices_freq: Dict[str, int] = {}
        pole_evidence_counts: Dict[str, int] = {"thesis": 0, "antithesis": 0}

        for p in self.corpus.pairs:
            t_count = 1 + len(p.thesis.additional_quotes)
            a_count = 1 + len(p.antithesis.additional_quotes)
            total_quotes += t_count + a_count
            pole_evidence_counts["thesis"] += t_count
            pole_evidence_counts["antithesis"] += a_count

            for d in p.metadata.get("rhetorical_devices", []):
                devices_freq[d] = devices_freq.get(d, 0) + 1

        balance_ratio = (
            pole_evidence_counts["thesis"] / pole_evidence_counts["antithesis"]
            if pole_evidence_counts["antithesis"] > 0
            else 1.0
        )

        return {
            "total_pairs": total_pairs,
            "total_poles": total_pairs * 2,
            "total_quotes": total_quotes,
            "evidence_distribution": pole_evidence_counts,
            "dialectic_balance_ratio": round(balance_ratio, 3),
            "rhetorical_devices_frequency": devices_freq
        }

    def generate_dialectic_matrix(self) -> List[Dict[str, Any]]:
        """Generates a structured comparison matrix of all poles."""
        matrix = []
        for p in self.corpus.pairs:
            matrix.append({
                "entry_id": p.entry_id,
                "chapter_index": p.metadata.get("chapter_index", 0),
                "topic": p.topic_slug,
                "arabic_title": p.classical_arabic_title,
                "thesis_concept": p.thesis.concept,
                "thesis_premise": p.thesis.core_premise,
                "thesis_top_quote": asdict(p.thesis.top_quote),
                "antithesis_concept": p.antithesis.concept,
                "antithesis_premise": p.antithesis.core_premise,
                "antithesis_top_quote": asdict(p.antithesis.top_quote),
                "synthesis": p.dialectic_synthesis,
                "rhetorical_devices": p.metadata.get("rhetorical_devices", []),
                "attribution": p.metadata.get("traditional_attribution", "Pseudo-Jahiz / al-Bayhaqi")
            })
        return matrix

    def get_network_graph_data(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Builds a node-and-edge graph dataset suitable for D3.js or Cytoscape.
        """
        nodes = []
        edges = []

        for p in self.corpus.pairs:
            topic_node_id = f"topic_{p.entry_id}"
            thesis_node_id = f"thesis_{p.entry_id}"
            anti_node_id = f"antithesis_{p.entry_id}"

            nodes.append({
                "id": topic_node_id,
                "label": p.topic_slug.replace("-", " ").title(),
                "arabic": p.classical_arabic_title,
                "type": "topic",
                "group": "thematic_hub"
            })
            nodes.append({
                "id": thesis_node_id,
                "label": p.thesis.concept,
                "type": "thesis",
                "group": "mehasin",
                "evidence_count": p.thesis.evidence_count
            })
            nodes.append({
                "id": anti_node_id,
                "label": p.antithesis.concept,
                "type": "antithesis",
                "group": "ezdad",
                "evidence_count": p.antithesis.evidence_count
            })

            edges.append({
                "source": topic_node_id,
                "target": thesis_node_id,
                "relation": "has_thesis",
                "weight": 1
            })
            edges.append({
                "source": topic_node_id,
                "target": anti_node_id,
                "relation": "has_antithesis",
                "weight": 1
            })
            edges.append({
                "source": thesis_node_id,
                "target": anti_node_id,
                "relation": "opposes",
                "weight": 2,
                "synthesis": p.dialectic_synthesis
            })

        return {"nodes": nodes, "edges": edges}

    def compare_poles(self, entry_id: str) -> Optional[Dict[str, Any]]:
        """Provides side-by-side comparative analysis of a single dialectic pair."""
        pair = self.corpus.get_by_id(entry_id)
        if not pair:
            return None

        return {
            "entry_id": pair.entry_id,
            "title": pair.classical_arabic_title,
            "thesis": {
                "concept": pair.thesis.concept,
                "premise": pair.thesis.core_premise,
                "primary_evidence": asdict(pair.thesis.top_quote),
                "secondary_evidences": [asdict(q) for q in pair.thesis.additional_quotes],
                "total_quotes": 1 + len(pair.thesis.additional_quotes)
            },
            "antithesis": {
                "concept": pair.antithesis.concept,
                "premise": pair.antithesis.core_premise,
                "primary_evidence": asdict(pair.antithesis.top_quote),
                "secondary_evidences": [asdict(q) for q in pair.antithesis.additional_quotes],
                "total_quotes": 1 + len(pair.antithesis.additional_quotes)
            },
            "synthesis": pair.dialectic_synthesis,
            "devices": pair.metadata.get("rhetorical_devices", []),
            "attribution": pair.metadata.get("traditional_attribution", "Pseudo-Jahiz / al-Bayhaqi")
        }
