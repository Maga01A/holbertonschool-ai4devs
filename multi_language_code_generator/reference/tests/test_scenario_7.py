import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class UniqueTestClass7(unittest.TestCase):
    def test_p7(self): e=RecommendationEngine([]); self.assertEqual(e.calculate_similarity('1','x'), 0.0)

if __name__ == '__main__':
    unittest.main()
