import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class UniqueTestClass6(unittest.TestCase):
    def test_p6(self): p1=Product('1','A','C',10,[]); p2=Product('2','B','C',10,[]); e=RecommendationEngine([p1,p2]); self.assertEqual(e.calculate_similarity('1','2'), 0.7)

if __name__ == '__main__':
    unittest.main()
