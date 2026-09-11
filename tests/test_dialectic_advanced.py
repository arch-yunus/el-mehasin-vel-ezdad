"""
Tests for advanced dialectic analysis and graph data structures.
"""
import unittest
from el_mehasin import DialecticCorpus, DialecticAnalyzer, RhetoricClassifier


class TestAdvancedDialectic(unittest.TestCase):
    def setUp(self):
        self.corpus = DialecticCorpus()
        self.analyzer = DialecticAnalyzer(self.corpus)

    def test_polarity_balance(self):
        stats = self.analyzer.get_corpus_statistics()
        self.assertIn("dialectic_balance_ratio", stats)
        self.assertGreater(stats["dialectic_balance_ratio"], 0.8)
        self.assertLess(stats["dialectic_balance_ratio"], 1.2)

    def test_network_graph_structure(self):
        graph = self.analyzer.get_network_graph_data()
        self.assertIn("nodes", graph)
        self.assertIn("edges", graph)
        self.assertEqual(len(graph["nodes"]), len(self.corpus) * 3)
        self.assertEqual(len(graph["edges"]), len(self.corpus) * 3)

    def test_compare_poles(self):
        comp = self.analyzer.compare_poles("pair_001_samt_beyan")
        self.assertIsNotNone(comp)
        self.assertIn("thesis", comp)
        self.assertIn("antithesis", comp)
        self.assertIn("synthesis", comp)

    def test_rhetoric_classifier_rules(self):
        sample_text = "الصمت من ذهب والكلام من فضة والجهل يهدم ما بناه العلم"
        detected = RhetoricClassifier.analyze_text(sample_text)
        self.assertTrue(len(detected) > 0)
        density = RhetoricClassifier.calculate_rhetorical_density(sample_text)
        self.assertGreater(density, 0.0)


if __name__ == "__main__":
    unittest.main()
