import sys
import unittest
from pathlib import Path

FOLDER_UTAMA = str(Path(__file__).resolve().parents[1])
if FOLDER_UTAMA not in sys.path:
    sys.path.insert(0, FOLDER_UTAMA)

from src.main import Stack

class TestModul3Stack(unittest.TestCase):
    def test_mekanisme_lifo(self):
        print("\n[RUNNING] Menguji Modul 3: Struktur Data Stack...")
        tumpukan = Stack()
        tumpukan.push("LOG_PENGIRIMAN_A")
        tumpukan.push("LOG_PENGIRIMAN_B")
        
        # Elemen terakhir masuk harus keluar pertama (LIFO)
        self.assertEqual(tumpukan.peek(), "LOG_PENGIRIMAN_B")
        self.assertEqual(tumpukan.pop(), "LOG_PENGIRIMAN_B")
        
        # Tersisa elemen pertama
        self.assertEqual(tumpukan.pop(), "LOG_PENGIRIMAN_A")
        self.assertIsNone(tumpukan.pop())
        print("[SUCCESS] Mekanisme Stack LIFO Berjalan Sempurna!")

if __name__ == "__main__":
    unittest.main()
