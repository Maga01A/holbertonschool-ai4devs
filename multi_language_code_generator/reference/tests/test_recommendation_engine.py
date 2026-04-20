import unittest
import sys
import os

# Import ucun yol elave edilir
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        self.products = [
            Product("1", "L", "Elec", 100.0, ["a", "b"]),
            Product("2", "M", "Elec", 90.0, ["a", "c"]),
            Product("3", "B", "Book", 20.0, ["d"]),
            Product("4", "T", "Elec", 110.0, ["b", "e"]),
            Product("5", "C", "Furn", 50.0, ["f"])
        ]
        self.engine = RecommendationEngine(self.products)

    def test_1_cat_match(self): self.assertGreater(self.engine.calculate_similarity("1", "2"), 0.5)
    def test_2_cat_mismatch(self): self.assertLess(self.engine.calculate_similarity("1", "3"), 0.5)
    def test_3_purchased_out(self): self.assertNotIn("2", [r[0] for r in self.engine.get_recommendations(["1"], ["2"])])
    def test_4_no_self_rec(self): self.assertNotIn("1", [r[0] for r in self.engine.get_recommendations(["1"], [])])
    def test_5_threshold(self):
        self.engine.threshold = 0.99
        self.assertEqual(len(self.engine.get_recommendations(["1"], [])), 0)
    def test_6_empty_input(self): self.assertEqual(len(self.engine.get_recommendations([], [])), 0)
    def test_7_price_sim(self): self.assertGreater(self.engine.calculate_similarity("1", "2"), self.engine.calculate_similarity("1", "5"))
    def test_8_tag_sim(self): self.assertGreater(self.engine.calculate_similarity("1", "2"), self.engine.calculate_similarity("1", "5"))
    def test_9_sorting(self):
        recs = self.engine.get_recommendations(["1"], [])
        if len(recs) > 1: self.assertGreaterEqual(recs[0][1], recs[1][1])
    def test_10_invalid_id(self): self.assertEqual(len(self.engine.get_recommendations(["X"], [])), 0)

if __name__ == '__main__':
    unittest.main()
