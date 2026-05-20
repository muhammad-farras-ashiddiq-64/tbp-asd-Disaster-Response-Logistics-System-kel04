import sys
import unittest
from pathlib import Path

FOLDER_UTAMA = str(Path(__file__).resolve().parents[1])
if FOLDER_UTAMA not in sys.path:
    sys.path.insert(0, FOLDER_UTAMA)

from src.main import Bantuan, PriorityQueueBantuan

class TestModul2PriorityQueue(unittest.TestCase):
    def test_antrean_prioritas(self):
        print("\n[RUNNING] Menguji Modul 2: Priority Queue Bantuan...")
        pq = PriorityQueueBantuan()
        
        b1 = Bantuan(1, "MAKANAN", 100, "DEPOT_0", "L001", prioritas=2)  # Sedang
        b2 = Bantuan(2, "OBAT", 50, "DEPOT_0", "L002", prioritas=1)     # Kritis
        b3 = Bantuan(3, "AIR", 200, "DEPOT_0", "L003", prioritas=3)      # Ringan
        
        pq.enqueue(b1)
        pq.enqueue(b2)
        pq.enqueue(b3)
        
        self.assertEqual(len(pq), 3)
        
        # Dequeue pertama harus mengembalikan prioritas terendah angkanya (Prioritas 1 = Kritis)
        item1 = pq.dequeue()
        self.assertEqual(item1.bantuan_id, 2)
        self.assertEqual(item1.jenis, "OBAT")
        
        # Dequeue kedua (Prioritas 2 = Sedang)
        item2 = pq.dequeue()
        self.assertEqual(item2.bantuan_id, 1)
        print("[SUCCESS] Priority Queue Urut Berdasarkan Level Bencana!")

if __name__ == "__main__":
    unittest.main()
