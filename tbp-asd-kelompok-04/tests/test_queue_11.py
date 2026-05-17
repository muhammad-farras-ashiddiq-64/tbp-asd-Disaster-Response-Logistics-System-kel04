# tests/test_queue.py

import unittest
from main import Bantuan
from data_structures.queue_ll import PriorityQueueBantuan

class TestPriorityQueueBantuan(unittest.TestCase):
    def setUp(self):
        """Inisialisasi Priority Queue kosong sebelum setiap fungsi uji dijalankan"""
        self.pq = PriorityQueueBantuan()
        
        # Sesuai blueprint objek halaman 41:
        # Bantuan(bantuan_id, jenis, jumlah, asal, tujuan, prioritas)
        self.bantuan_kritis = Bantuan(1, "MAKANAN", 100, "DEPOT_0", "L001", 1) # KRITIS (level=1)
        self.bantuan_sedang = Bantuan(2, "AIR", 200, "DEPOT_0", "L002", 2)    # SEDANG (level=2)
        self.bantuan_ringan = Bantuan(3, "OBAT", 50, "DEPOT_0", "L003", 3)     # RINGAN (level=3)

    def test_inisialisasi_kosong(self):
        """Memastikan antrean awal berukuran 0 dan head bernilai None"""
        self.assertEqual(len(self.pq), 0)
        self.assertIsNone(self.pq.head)

    def test_enqueue_terurut_prioritas(self):
        """Menguji apakah elemen terurut otomatis berdasarkan level urgensi bencana (O(n))"""
        # Dimasukkan secara acak/terbalik: Sedang (2) -> Ringan (3) -> Kritis (1)
        self.pq.enqueue(self.bantuan_sedang)
        self.pq.enqueue(self.bantuan_ringan)
        self.pq.enqueue(self.bantuan_kritis)

        # Total data dalam antrean harus tepat 3
        self.assertEqual(len(self.pq), 3)

        # Data terdepan (head) WAJIB bernilai prioritas 1 (Kritis) meskipun dimasukkan terakhir
        self.assertEqual(self.pq.head.data.prioritas, 1)
        self.assertEqual(self.pq.head.data.jenis, "MAKANAN")

    def test_dequeue_priority_order(self):
        """Menguji apakah proses pengambilan data (O(1)) mendahulukan Level Kritis"""
        self.pq.enqueue(self.bantuan_ringan)
        self.pq.enqueue(self.bantuan_kritis)
        self.pq.enqueue(self.bantuan_sedang)

        # Dequeue pertama harus mengembalikan bantuan KRITIS (prioritas=1)
        item1 = self.pq.dequeue()
        self.assertEqual(item1.prioritas, 1)
        self.assertEqual(item1.jenis, "MAKANAN")
        self.assertEqual(len(self.pq), 2)

        # Dequeue kedua harus mengembalikan bantuan SEDANG (prioritas=2)
        item2 = self.pq.dequeue()
        self.assertEqual(item2.prioritas, 2)
        self.assertEqual(item2.jenis, "AIR")
        self.assertEqual(len(self.pq), 1)

        # Dequeue ketiga harus mengembalikan bantuan RINGAN (prioritas=3)
        item3 = self.pq.dequeue()
        self.assertEqual(item3.prioritas, 3)
        self.assertEqual(item3.jenis, "OBAT")
        self.assertEqual(len(self.pq), 0)

    def test_dequeue_antrean_kosong(self):
        """Memastikan jika antrean kosong, fungsi dequeue mengembalikan None tanpa crash"""
        self.assertIsNone(self.pq.dequeue())

if __name__ == "__main__":
    unittest.main()
