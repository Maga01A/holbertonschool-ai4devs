import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestRecommendation1(unittest.TestCase):
    def test_perfect_match(self): p1=Product('1','A','T',10,['a']); eng=RecommendationEngine([p1]); self.assertEqual(eng.calculate_similarity('1','1'), 1.0)

if __name__ == '__main__':
    unittest.main()
