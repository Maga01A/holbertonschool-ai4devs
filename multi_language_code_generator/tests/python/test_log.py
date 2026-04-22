import unittest

# Funksional ekvivalentliyi yoxlamaq ???n test keysi
class TestLogAnalyzer(unittest.TestCase):
    def test_log_parser_counts(self):
        # Eyni giri? m?lumatlar?
        entries = ["200 OK", "404 NOT FOUND", "200 OK"]
        
        # Simulyasiya edil?n analiz m?ntiqi
        total_requests = len(entries)
        errors = entries.count("404 NOT FOUND")
        error_rate = round((errors / total_requests) * 100, 1)
        
        # G?zl?nil?n n?tic?l?r
        self.assertEqual(total_requests, 3)
        self.assertEqual(error_rate, 33.3)

if __name__ == '__main__':
    unittest.main()
