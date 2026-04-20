import unittest
import sys
import os

# Testlerin recommendation_engine-i tapa bilmesi ucun yolu elave edirik
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from recommendation_engine import Product, RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        self.products = [
            Product("1", "Laptop", "Electronics", 1000.0, ["tech", "work"]),
            Product("2", "Mouse", "Electronics", 50.0, ["tech", "office"]),
            Product("3", "Book", "Media", 20.0, ["reading", "education"]),
            Product("4", "Tablet", "Electronics", 800.0, ["tech", "mobile"]),
            Product("5", "Chair", "Furniture", 150.0, ["office", "home"])
        ]
        self.engine = RecommendationEngine(self.products)

    def test_1_category_match(self):
        sim = self.engine.calculate_similarity("1", "2")
        self.assertGreaterEqual(sim, 0.5)

    def test_2_purchased_exclusion(self):
        recs = self.engine.get_recommendations(["1"], ["2"])
        ids = [r[0] for r in recs]
        self.assertNotIn("2", ids)

    def test_3_self_recommendation_exclusion(self):
        recs = self.engine.get_recommendations(["1"], [])
        ids = [r[0] for r in recs]
        self.assertNotIn("1", ids)

    def test_4_threshold_filtering(self):
        self.engine.threshold = 0.99
        recs = self.engine.get_recommendations(["1"], [])
        self.assertEqual(len(recs), 0)

    def test_5_empty_views(self):
        recs = self.engine.get_recommendations([], [])
        self.assertEqual(len(recs), 0)

    def test_6_different_category_low_score(self):
        sim = self.engine.calculate_similarity("1", "3")
        self.assertLess(sim, 0.5)

    def test_7_tag_overlap_score(self):
        # 1 ve 2 her ikisinde "tech" tag-i var
        sim_1_2 = self.engine.calculate_similarity("1", "2")
        # 1 ve 3 arasinda tag yoxdur
        sim_1_3 = self.engine.calculate_similarity("1", "3")
        self.assertGreater(sim_1_2, sim_1_3)

    def test_8_price_similarity(self):
        # Qiymetleri yaxin olanlar daha yuksek bal almalidir
        sim_close = self.engine.calculate_similarity("1", "4") # 1000 vs 800
        sim_far = self.engine.calculate_similarity("1", "2")   # 1000 vs 50
        self.assertGreater(sim_close, sim_far)

    def test_9_sorting_order(self):
        recs = self.engine.get_recommendations(["1"], [])
        if len(recs) > 1:
            self.assertGreaterEqual(recs[0][1], recs[1][1])

    def test_10_invalid_product_id(self):
        recs = self.engine.get_recommendations(["999"], [])
        self.assertEqual(len(recs), 0)

if __name__ == '__main__':
    unittest.main()
