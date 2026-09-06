"""
el_mehasin: Classical Arabic Bipolar Dialectic & Rhetorical Corpus Library.
"""

__version__ = "1.0.0"
__author__ = "Bahattin Yunus ÇETİN"

from .corpus import DialecticCorpus, DialecticPair
from .dialectic import DialecticAnalyzer
from .rhetoric import RhetoricDetector

__all__ = ["DialecticCorpus", "DialecticPair", "DialecticAnalyzer", "RhetoricDetector"]
