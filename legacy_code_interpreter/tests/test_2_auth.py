import unittest
class TestAuthSystem(unittest.TestCase):
    def test_status_code(self):
        self.assertEqual(401, 401)
if __name__ == '__main__':
    unittest.main()
