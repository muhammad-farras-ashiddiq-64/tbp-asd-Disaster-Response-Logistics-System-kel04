# tests/test_bst.py

import unittest
from data_structures.bst import BST

class TestBSTRegistry(unittest.TestCase):
    def setUp(self):
        """Inisialisasi objek BST baru sebelum setiap pengujian dijalankan"""
        self.bst = BST()

    def test_insert_and_search_valid(self):
        """Menguji apakah penambahan node dan pencarian kode_lokasi berfungsi (O(log n))"""
        self.bst.insert("L03", "Desa Sleman", 1, 1500)
        self.bst.insert("L01", "Desa Bantul", 2, 800)
        self.bst.insert("L05", "Desa Kulon Progo", 3, 400)

        # Cari node yang ada di root (L03)
        node_root = self.bst.search("L03")
        self.assertIsNotNone(node_root)
        self.assertEqual(node_root.nama, "Desa Sleman")
        self.assertEqual(node_root.level, 1)

        # Cari node di cabang kiri (L01 < L03)
        node_kiri = self.bst.search("L01")
        self.assertIsNotNone(node_kiri)
        self.assertEqual(node_kiri.nama, "Desa Bantul")

        # Cari node di cabang kanan (L05 > L03)
        node_kanan = self.bst.search("L05")
        self.assertIsNotNone(node_kanan)
        self.assertEqual(node_kanan.nama, "Desa Kulon Progo")

    def test_search_not_found(self):
        """Menguji pencarian kode yang tidak terdaftar di sistem"""
        self.bst.insert("L01", "Desa Bantul", 2, 800)
        node_fiktif = self.bst.search("L99")
        self.assertIsNone(node_fiktif)

    def test_update_level_urgensi(self):
        """Menguji fungsionalitas pembaruan tingkatan urgensi bencana"""
        self.bst.insert("L02", "Desa Gunungkidul", 3, 600)
        
        # Lakukan pembaruan dari Level 3 (Ringan) ke Level 1 (Kritis)
        sukses_update = self.bst.update_level("L02", 1)
        self.assertTrue(sukses_update)
        
        node = self.bst.search("L02")
        self.assertEqual(node.level, 1)

    def test_update_level_invalid_code(self):
        """Menguji pembaruan level jika kode lokasi salah/tidak ada"""
        sukses_update = self.bst.update_level("L99", 1)
        self.assertFalse(sukses_update)

if __name__ == "__main__":
    unittest.main()
