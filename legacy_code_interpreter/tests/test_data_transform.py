import unittest
class TestDataTransformation(unittest.TestCase):
    def test_legacy_date_conversion(self):
        legacy_date = "20260422"
        iso_date = f"{legacy_date[:4]}-{legacy_date[4:6]}-{legacy_date[6:]}"
        self.assertEqual(iso_date, "2026-04-22")
