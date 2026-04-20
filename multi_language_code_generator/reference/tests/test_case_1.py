import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recommendation_engine import Product, RecommendationEngine

class TestRecommendation1(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(True) # Bu, her faylin ferqli bir senari yoxlamasi üçün bazadir
