import unittest
class TestStringValidation(unittest.TestCase):
    def test_trim_logic(self):
        self.assertEqual("  rent  ".strip(), "rent")
if __name__ == '__main__':
    unittest.main()
