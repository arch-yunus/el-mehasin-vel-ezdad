"""
el-mehasin-vel-ezdad: Classical Arabic Bipolar Dialectic Corpus & Computational Rhetoric Suite
"""

from .corpus import DialecticCorpus, DialecticPair, DialecticPole, PoleQuote
from .dialectic import DialecticAnalyzer
from .rhetoric import RhetoricClassifier, RhetoricDetector

__version__ = "1.1.0"
__all__ = [
    "DialecticCorpus",
    "DialecticPair",
    "DialecticPole",
    "PoleQuote",
    "DialecticAnalyzer",
    "RhetoricClassifier",
    "RhetoricDetector"
]
