"""
Corpus data structures and loading utilities.
"""
import os
import json
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

@dataclass
class PoleQuote:
    arabic: str
    turkish: str
    source: str

@dataclass
class DialecticPole:
    pole: str
    concept: str
    core_premise: str
    evidence_count: int
    top_quote: PoleQuote
    additional_quotes: List[PoleQuote]

@dataclass
class DialecticPair:
    entry_id: str
    topic_slug: str
    classical_arabic_title: str
    thesis: DialecticPole
    antithesis: DialecticPole
    dialectic_synthesis: str
    metadata: Dict[str, Any]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DialecticPair":
        def make_quote(q_dict: Dict[str, str]) -> PoleQuote:
            return PoleQuote(
                arabic=q_dict.get("arabic", ""),
                turkish=q_dict.get("turkish", ""),
                source=q_dict.get("source", "")
            )

        def make_pole(p_dict: Dict[str, Any]) -> DialecticPole:
            tq = make_quote(p_dict.get("top_quote", {}))
            add_q = [make_quote(q) for q in p_dict.get("additional_quotes", [])]
            return DialecticPole(
                pole=p_dict.get("pole", ""),
                concept=p_dict.get("concept", ""),
                core_premise=p_dict.get("core_premise", ""),
                evidence_count=p_dict.get("evidence_count", 0),
                top_quote=tq,
                additional_quotes=add_q
            )

        return cls(
            entry_id=data["entry_id"],
            topic_slug=data["topic_slug"],
            classical_arabic_title=data["classical_arabic_title"],
            thesis=make_pole(data["thesis"]),
            antithesis=make_pole(data["antithesis"]),
            dialectic_synthesis=data.get("dialectic_synthesis", ""),
            metadata=data.get("metadata", {})
        )

class DialecticCorpus:
    def __init__(self, data_path: Optional[str] = None):
        if data_path is None:
            # find default path relative to repo root
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            data_path = os.path.join(base_dir, "data", "dialectic_pairs.jsonl")
        
        self.data_path = data_path
        self.pairs: List[DialecticPair] = []
        self._load()

    def _load(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Corpus file not found at {self.data_path}")
        with open(self.data_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    item = json.loads(line)
                    self.pairs.append(DialecticPair.from_dict(item))

    def __len__(self) -> int:
        return len(self.pairs)

    def __getitem__(self, idx: int) -> DialecticPair:
        return self.pairs[idx]

    def get_by_id(self, entry_id: str) -> Optional[DialecticPair]:
        for p in self.pairs:
            if p.entry_id == entry_id:
                return p
        return None

    def search(self, query: str) -> List[DialecticPair]:
        query = query.lower()
        results = []
        for p in self.pairs:
            searchable = f"{p.entry_id} {p.topic_slug} {p.classical_arabic_title} {p.thesis.concept} {p.antithesis.concept} {p.dialectic_synthesis}".lower()
            if query in searchable:
                results.append(p)
        return results
