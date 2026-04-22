import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestRecommendation10(unittest.TestCase):
    def test_threshold_filter(self): p1=Product('1','A','T1',10,['a']); p2=Product('2','B','T2',100,['z']); eng=RecommendationEngine([p1,p2], threshold=0.9); recs=eng.get_recommendations(['1'],[]); self.assertEqual(len(recs), 0)

if __name__ == '__main__':
    unittest.main()
