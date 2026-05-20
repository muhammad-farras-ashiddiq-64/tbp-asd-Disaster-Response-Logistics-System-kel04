import sys
import unittest
from pathlib import Path

# Jalur Absolut Penembus OneDrive
FOLDER_UTAMA = str(Path(__file__).resolve().parents[1])
if FOLDER_UTAMA not in sys.path:
    sys.path.insert(0, FOLDER_UTAMA)

# Import komponen dari src.main
from src.main import Lokasi, Bantuan, LLNode

class TestModul1Models(unittest.TestCase):
    def test_inisialisasi_lokasi(self):
        print("\n[RUNNING] Menguji Modul 1: Inisialisasi Model Lokasi...")
        lok = Lokasi(kode="L001", nama="Desa A", level=1, populasi=1500)
        self.assertEqual(lok.kode, "L001")
        self.assertEqual(lok.level, 1)
        self.assertEqual(lok.status, 0)
        print("[SUCCESS] Model Lokasi Valid!")

    def test_inisialisasi_node_linked_list(self):
        print("[RUNNING] Menguji Modul 1: Node Linked List...")
        node2 = LLNode(data="Simpul Belakang")
        node1 = LLNode(data="Simpul Depan")
        node1.next = node2
        
        self.assertEqual(node1.data, "Simpul Depan")
        self.assertEqual(node1.next.data, "Simpul Belakang")
        print("[SUCCESS] Struktur LLNode Valid!")

if __name__ == "__main__":
    unittest.main()
