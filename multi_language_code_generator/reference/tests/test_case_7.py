import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestRecommendation7(unittest.TestCase):
    def test_invalid_id(self): eng=RecommendationEngine([]); self.assertEqual(eng.calculate_similarity('1','2'), 0.0)

if __name__ == '__main__':
    unittest.main()
