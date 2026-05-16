import unittest
from src.modules.modul_2 import PriorityQueueBantuan, Bantuan

class TestPriorityQueueBantuan(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueueBantuan()

    def test_priority_sorting(self):
        """Memastikan item dengan prioritas KRITIS (1) keluar lebih dulu daripada RINGAN (3)."""
        bantuan_ringan = Bantuan(1, "TENDA", 10, "DEPOT_0", "L002", 3)
        bantuan_kritis = Bantuan(2, "OBAT", 50, "DEPOT_0", "L001", 1)
        
        self.pq.enqueue(bantuan_ringan)
        self.pq.enqueue(bantuan_kritis)
        
        # Dequeue pertama harus menghasilkan bantuan medis yang kritis
        item_pertama = self.pq.dequeue()
        self.assertEqual(item_pertama.bantuan_id, 2)
        self.assertEqual(item_pertama.prioritas, 1)

    def test_empty_queue(self):
        """Memastikan antrean kosong mengembalikan nilai None dan bernilai True pada is_empty."""
        self.assertTrue(self.pq.is_empty())
        self.assertIsNone(self.pq.dequeue())

if __name__ == "__main__":
    unittest.main()
