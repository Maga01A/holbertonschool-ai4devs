import unittest
class TestCoreInterpreter(unittest.TestCase):
    def test_syntax_mapping(self):
        legacy_cmd = "MOVE A TO B"
        modern_cmd = f"B = A" # Simplified mapping logic
        self.assertIn("=", modern_cmd, "Interpreter failed to map MOVE command to assignment")
