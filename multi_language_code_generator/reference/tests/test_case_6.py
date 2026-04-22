import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestScenario6(unittest.TestCase):
    def test_empty_tags_case(self): p1=Product('1','A','T',10,[]); p2=Product('2','B','T',10,[]); eng=RecommendationEngine([p1,p2]); self.assertEqual(eng.calculate_similarity('1','2'), 0.7)

if __name__ == '__main__':
    unittest.main()
