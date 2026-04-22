import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class UniqueTestClass3(unittest.TestCase):
    def test_p3(self): p1=Product('1','A','C',10,['a']); p2=Product('2','B','C',1000,['a']); e=RecommendationEngine([p1,p2]); self.assertLess(e.calculate_similarity('1','2'), 0.9)

if __name__ == '__main__':
    unittest.main()
