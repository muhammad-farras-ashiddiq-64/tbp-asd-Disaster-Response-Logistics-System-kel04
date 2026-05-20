import sys
import unittest
from pathlib import Path

FOLDER_UTAMA = str(Path(__file__).resolve().parents[1])
if FOLDER_UTAMA not in sys.path:
    sys.path.insert(0, FOLDER_UTAMA)

from src.main import Lokasi, BSTLokasi

class TestModul4BST(unittest.TestCase):
    def test_operasi_bst(self):
        print("\n[RUNNING] Menguji Modul 4: Binary Search Tree...")
        bst = BSTLokasi()
        
        l1 = Lokasi("L020", "Desa Tengah", 2, 500)
        l2 = Lokasi("L010", "Desa Kiri", 1, 300)
        l3 = Lokasi("L030", "Desa Kanan", 3, 700)
        
        bst.insert(l1)
        bst.insert(l2)
        bst.insert(l3)
        
        # Uji Pencarian (Search)
        target = bst.search("L030")
        self.assertIsNotNone(target)
        self.assertEqual(target.nama, "Desa Kanan")
        
        # Uji Pembaruan Level (Update)
        bst.update_level("L010", 3)
        self.assertEqual(bst.search("L010").level, 3)
        
        # Uji Pengurutan (Inorder Traversal)
        urut = bst.inorder()
        self.assertEqual(urut[0].kode, "L010")
        self.assertEqual(urut[1].kode, "L020")
        self.assertEqual(urut[2].kode, "L030")
        print("[SUCCESS] Operasi Kamus Data BST Lolos Validasi!")

if __name__ == "__main__":
    unittest.main()
    
