import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class UniqueTestClass9(unittest.TestCase):
    def test_p9(self): p1=Product('1','A','C',10,['a']); p2=Product('2','B','C',11,['a']); e=RecommendationEngine([p1,p2]); r=e.get_recommendations(['1'],['2']); self.assertEqual(len(r), 0)

if __name__ == '__main__':
    unittest.main()
