import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class UniqueTestClass10(unittest.TestCase):
    def test_p10(self): p1=Product('1','A','C1',10,['a']); p2=Product('2','B','C2',100,['z']); e=RecommendationEngine([p1,p2], threshold=0.9); r=e.get_recommendations(['1'],[]); self.assertEqual(len(r), 0)

if __name__ == '__main__':
    unittest.main()
