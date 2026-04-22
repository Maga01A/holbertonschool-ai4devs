import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestRecommendation9(unittest.TestCase):
    def test_exclude_purchased(self): p1=Product('1','A','T',10,['a']); p2=Product('2','B','T',11,['a']); eng=RecommendationEngine([p1,p2]); recs=eng.get_recommendations(['1'],['2']); self.assertEqual(len(recs), 0)

if __name__ == '__main__':
    unittest.main()
