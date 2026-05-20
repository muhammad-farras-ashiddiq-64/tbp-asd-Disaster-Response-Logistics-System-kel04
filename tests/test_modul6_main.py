import sys
import unittest
from pathlib import Path

FOLDER_UTAMA = str(Path(__file__).resolve().parents[1])
if FOLDER_UTAMA not in sys.path:
    sys.path.insert(0, FOLDER_UTAMA)

from src.main import generate_peta_bencana

class TestModul6MainGenerator(unittest.TestCase):
    def test_pembangkit_peta(self):
        print("\n[RUNNING] Menguji Modul 6: Generator Peta CLI Simulasi...")
        # Bangun peta tiruan dengan 10 desa dan 2 depot gudang logistik
        lokasi_list, edges = generate_peta_bencana(n_lokasi=10, n_depot=2, seed=47)
        
        # Total entitas lokasi harus sama dengan n_lokasi + n_depot (10 + 2 = 12)
        self.assertEqual(len(lokasi_list), 12)
        
        # Pastikan data yang digenerate memiliki properti objek yang tepat
        self.assertTrue(lokasi_list[0].kode.startswith("DEPOT_"))
        self.assertTrue(lokasi_list[2].kode.startswith("L000"))
        print("[SUCCESS] Generator Peta CLI Mengeluarkan Data Konsisten!")

if __name__ == "__main__":
    unittest.main()
