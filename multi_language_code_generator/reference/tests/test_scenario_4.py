import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class UniqueTestClass4(unittest.TestCase):
    def test_p4(self): p1=Product('1','A','C',10,['a','b']); p2=Product('2','B','C',10,['a','c']); e=RecommendationEngine([p1,p2]); self.assertAlmostEqual(e.calculate_similarity('1','2'), 0.8, delta=0.1)

if __name__ == '__main__':
    unittest.main()
