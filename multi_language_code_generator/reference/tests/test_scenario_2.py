import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class UniqueTestClass2(unittest.TestCase):
    def test_p2(self): p1=Product('1','A','C1',10,['a']); p2=Product('2','B','C2',10,['a']); e=RecommendationEngine([p1,p2]); self.assertLess(e.calculate_similarity('1','2'), 0.6)

if __name__ == '__main__':
    unittest.main()
