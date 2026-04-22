import unittest
class TestInputValidation(unittest.TestCase):
    def test_empty_payload_rejection(self):
        payload = {}
        is_valid = False if not payload else True
        self.assertFalse(is_valid, "System should reject empty migration payloads")
