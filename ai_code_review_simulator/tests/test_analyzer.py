import unittest
from src.code_analyzer import CodeAnalyzer

class TestCodeAnalyzer(unittest.TestCase):
    def test_security_vulnerability(self):
        bad_code = "query = 'SELECT * FROM x WHERE id = ' + input"
        analyzer = CodeAnalyzer(bad_code)
        report = analyzer.generate_report()
        self.assertEqual(report["metrics"]["security_risk"], "High")

    def test_low_complexity(self):
        simple_code = "print('Hello World')"
        analyzer = CodeAnalyzer(simple_code)
        report = analyzer.generate_report()
        self.assertEqual(report["metrics"]["complexity"], 0)

if __name__ == '__main__':
    unittest.main()
