import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestScenario11(unittest.TestCase):
    def test_multiple_views_score(self): p1=Product('1','A','T',10,['a']); p2=Product('2','B','T',11,['a']); p3=Product('3','C','T',50,['x']); eng=RecommendationEngine([p1,p2,p3]); recs=eng.get_recommendations(['1','3'],[]); self.assertTrue(len(recs) >= 1)

if __name__ == '__main__':
    unittest.main()
