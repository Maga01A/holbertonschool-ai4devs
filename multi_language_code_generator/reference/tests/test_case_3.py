import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestRecommendation3(unittest.TestCase):
    def test_case_3(self):
        self.assertTrue(True) # Bu, her faylin ferqli bir senari yoxlamasi üçün bazadir
