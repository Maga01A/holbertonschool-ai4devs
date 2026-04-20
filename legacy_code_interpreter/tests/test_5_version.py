import unittest
class TestSystemMetaData(unittest.TestCase):
    def test_version_tag(self):
        self.assertTrue("legacy" in "v1.0-legacy")
if __name__ == '__main__':
    unittest.main()
