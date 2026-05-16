import unittest
from src.modules.modul_4 import StackLog

class TestStackLog(unittest.TestCase):
    def setUp(self):
        self.stack = StackLog()

    def test_lifo_behavior(self):
        """Memastikan log transaksi terakhir keluar pertama saat proses rollback."""
        transaksi_1 = {"id": 1, "tujuan": "L001", "muatan": "MAKANAN"}
        transaksi_2 = {"id": 2, "tujuan": "L002", "muatan": "OBAT"}
        
        self.stack.push(transaksi_1)
        self.stack.push(transaksi_2)
        
        teratas = self.stack.pop()
        self.assertEqual(teratas["id"], 2)
        self.assertEqual(teratas["muatan"], "OBAT")

    def test_is_empty(self) -> bool:
        self.assertTrue(self.stack.is_empty())

if __name__ == "__main__":
    unittest.main()
