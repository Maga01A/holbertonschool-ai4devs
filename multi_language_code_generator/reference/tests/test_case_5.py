import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestScenario5(unittest.TestCase):
    def test_zero_price_logic(self): p1=Product('1','A','T',0,['a']); p2=Product('2','B','T',0,['a']); eng=RecommendationEngine([p1,p2]); self.assertEqual(eng.calculate_similarity('1','2'), 1.0)

if __name__ == '__main__':
    unittest.main()
