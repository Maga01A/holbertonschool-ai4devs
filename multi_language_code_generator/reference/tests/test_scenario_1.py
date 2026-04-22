import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class UniqueTestClass1(unittest.TestCase):
    def test_p1(self): p=Product('1','A','C',10,['a']); e=RecommendationEngine([p]); self.assertEqual(e.calculate_similarity('1','1'), 1.0)

if __name__ == '__main__':
    unittest.main()
