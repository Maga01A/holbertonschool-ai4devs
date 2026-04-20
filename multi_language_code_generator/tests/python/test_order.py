import unittest
import sys
import os

# Implimentasiya qovlugunu yola ?lav? edirik
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../implementations/python')))
from order_processor import process_order

class TestOrderProcessor(unittest.TestCase):
    def test_equivalence(self):
        result = process_order("Laptop", 1200, 2)
        self.assertEqual(result["total"], 2400)
        self.assertEqual(result["status"], "Processed")

if __name__ == '__main__':
    unittest.main()
