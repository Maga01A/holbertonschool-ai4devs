import unittest
import json
class TestLoggingSystem(unittest.TestCase):
    def test_json_log_structure(self):
        log_entry = '{"level": "ERROR", "module": "migration", "code": 500}'
        parsed = json.loads(log_entry)
        self.assertIn("level", parsed)
        self.assertEqual(parsed["level"], "ERROR")
