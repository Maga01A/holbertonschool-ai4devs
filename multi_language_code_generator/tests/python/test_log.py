import unittest

def analyze_logs(entries):
    if not entries:
        return {'total': 0, 'error_rate': 0.0}
    total = len(entries)
    errors = entries.count("404 NOT FOUND")
    return {'total': total, 'error_rate': round((errors / total) * 100, 1)}

class TestLogAnalyzer(unittest.TestCase):
    def test_standard_case(self):
        data = ["200 OK", "404 NOT FOUND", "200 OK"]
        result = analyze_logs(data)
        self.assertEqual(result['total'], 3)
        self.assertEqual(result['error_rate'], 33.3)

    def test_empty_case(self):
        result = analyze_logs([])
        self.assertEqual(result['total'], 0)
        self.assertEqual(result['error_rate'], 0.0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
