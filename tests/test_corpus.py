import unittest
from el_mehasin.corpus import DialecticCorpus

class TestDialecticCorpus(unittest.TestCase):
    def setUp(self):
        self.corpus = DialecticCorpus()

    def test_corpus_size(self):
        self.assertEqual(len(self.corpus), 20, "Corpus should contain exactly 20 dialectic pairs.")

    def test_get_by_id(self):
        pair = self.corpus.get_by_id("pair_001_samt_beyan")
        self.assertIsNotNone(pair)
        self.assertEqual(pair.topic_slug, "sukut-ve-kelam")
        self.assertEqual(pair.thesis.pole, "mehasin")
        self.assertEqual(pair.antithesis.pole, "ezdad")

    def test_search(self):
        results = self.corpus.search("comertlik")
        self.assertTrue(len(results) > 0)

if __name__ == "__main__":
    unittest.main()
