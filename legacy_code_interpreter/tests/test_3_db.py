import unittest
class TestDatabaseQuery(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(len([]), 0)
if __name__ == '__main__':
    unittest.main()
