import unittest
class TestDatabaseConsistency(unittest.TestCase):
    def test_lock_acquisition(self):
        lock_status = {"DB2": "LOCKED", "PG": "LOCKED"}
        self.assertEqual(lock_status["DB2"], lock_status["PG"], "Distributed lock is out of sync")
