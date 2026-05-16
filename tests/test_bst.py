import unittest
from src.modules.modul_3 import BSTLokasi, Lokasi

class TestBSTRegistry(unittest.TestCase):
    def setUp(self):
        self.bst = BSTLokasi()
        self.lok1 = Lokasi("L010", "Wilayah Godean", 2, 1500)
        self.lok2 = Lokasi("L002", "Posko Sleman", 1, 3000)
        self.bst.insert(self.lok1)
        self.bst.insert(self.lok2)

    def test_search_exist(self):
        """Memastikan lokasi yang terdaftar dapat dicari berdasarkan kodenya."""
        hasil = self.bst.search("L002")
        self.assertIsNotNone(hasil)
        self.assertEqual(hasil.lokasi.nama, "Posko Sleman")

    def test_update_level_bencana(self):
        """Memastikan fungsionalitas pengubahan tingkat kedaruratan wilayah sukses."""
        sukses = self.bst.update_level("L010", 1)  # Berubah dari SEDANG ke KRITIS
        self.assertTrue(sukses)
        
        node = self.bst.search("L010")
        self.assertEqual(node.lokasi.level, 1)

if __name__ == "__main__":
    unittest.main()
