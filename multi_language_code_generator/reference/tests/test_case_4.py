import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestScenario4(unittest.TestCase):
    def test_tag_jaccard(self): p1=Product('1','A','T',10,['a','b']); p2=Product('2','B','T',10,['a','c']); eng=RecommendationEngine([p1,p2]); self.assertAlmostEqual(eng.calculate_similarity('1','2'), 0.8, delta=0.1)

if __name__ == '__main__':
    unittest.main()
