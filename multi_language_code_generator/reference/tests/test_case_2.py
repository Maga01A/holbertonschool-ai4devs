import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestRecommendation2(unittest.TestCase):
    def test_different_category(self): p1=Product('1','A','T1',10,['a']); p2=Product('2','B','T2',10,['a']); eng=RecommendationEngine([p1,p2]); self.assertLess(eng.calculate_similarity('1','2'), 0.6)

if __name__ == '__main__':
    unittest.main()
