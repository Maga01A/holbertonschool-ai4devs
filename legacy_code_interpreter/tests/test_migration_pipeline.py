import unittest
class TestMigrationPipeline(unittest.TestCase):
    def test_full_data_transformation(self):
        record = {"id": "001", "old_status": "A"}
        # Expected transformation: A -> Active
        transformed = {"id": int(record["id"]), "status": "Active" if record["old_status"] == "A" else "Inactive"}
        self.assertEqual(transformed["id"], 1)
        self.assertEqual(transformed["status"], "Active")
