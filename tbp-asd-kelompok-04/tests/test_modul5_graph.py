import sys
import unittest
from pathlib import Path

FOLDER_UTAMA = str(Path(__file__).resolve().parents[1])
if FOLDER_UTAMA not in sys.path:
    sys.path.insert(0, FOLDER_UTAMA)

from src.main import GraphRute, dijkstra_logistik

class TestModul5Graph(unittest.TestCase):
    def test_rute_dan_dijkstra(self):
        print("\n[RUNNING] Menguji Modul 5: Grafik Rute & Dijkstra...")
        graph = GraphRute()
        
        # Daftarkan node rute rintisan
        graph.tambah_node("DEPOT_0")
        graph.tambah_node("L001")
        graph.tambah_node("L002")
        
        # Daftarkan jalur bercabang
        graph.tambah_rute("DEPOT_0", "L001", jarak=50, kapasitas=4)
        graph.tambah_rute("DEPOT_0", "L002", jarak=10, kapasitas=2)
        graph.tambah_rute("L002", "L001", jarak=15, kapasitas=3)
        
        # Hitung dengan Dijkstra dari DEPOT_0
        dist, parent = dijkstra_logistik(graph, "DEPOT_0")
        
        # Jarak ke L001 lewat L002 (10 + 15 = 25) harus dipilih dibanding jalur langsung (50)
        self.assertEqual(dist["L001"], 25)
        self.assertEqual(parent["L001"], "L002")
        print("[SUCCESS] Optimasi Jalur Logistik Dijkstra Akurat!")

    def test_keterjangkauan_bfs(self):
        print("[RUNNING] Menguji Modul 5: Konektivitas Wilayah BFS...")
        graph = GraphRute()
        graph.tambah_rute("DEPOT_0", "L001", jarak=10, kapasitas=3)
        graph.tambah_node("L099") # Desa terisolasi total tanpa rute jalan
        
        terjangkau = graph.bfs_akses("DEPOT_0")
        self.assertIn("L001", terjangkau)
        self.assertNotIn("L099", terjangkau)
        print("[SUCCESS] Deteksi Lokasi Terisolasi BFS Berjalan Baik!")

if __name__ == "__main__":
    unittest.main()
