# tests/test_graph.py

import unittest
from data_structures.graph import Graph
from modules.Modul_1_Graph_Jaringan_Rute import temukan_lokasi_terisolasi

class TestGraphAndBFS(unittest.TestCase):
    def setUp(self):
        """Inisialisasi graf kosong dan depot pusat sebelum pengujian"""
        self.graph = Graph()
        self.depot = "DEPOT_PUSAT"
        self.graph.tambah_node(self.depot)

    def test_tambah_node_dan_rute(self):
        """Menguji apakah penambahan lokasi dan jalan berbobot (km) masuk ke Adjacency List"""
        self.graph.tambah_rute(self.depot, "Posko_A", 15)
        
        # Pastikan node terdaftar di list master graf
        self.assertIn("Posko_A", self.graph.nodes)
        
        # Cek apakah Posko_A terhubung dari DEPOT_PUSAT (Graf Tidak Berarah)
        head_depot = self.graph.adj_list[self.depot]
        self.assertIsNotNone(head_depot)
        self.assertEqual(head_depot.tujuan, "Posko_A")
        self.assertEqual(head_depot.bobot, 15)

        # Cek arah sebaliknya (DEPOT_PUSAT harus menjadi tetangga Posko_A)
        head_posko = self.graph.adj_list["Posko_A"]
        self.assertIsNotNone(head_posko)
        self.assertEqual(head_posko.tujuan, self.depot)

    def test_bfs_semua_terhubung(self):
        """Menguji kasus jika seluruh wilayah aman terhubung ke depot pusat"""
        self.graph.tambah_rute(self.depot, "Posko_A", 10)
        self.graph.tambah_rute("Posko_A", "Posko_B", 5)
        
        # Jalankan BFS dari depot pusat
        lokasi_terisolasi = temukan_lokasi_terisolasi(self.graph, self.depot)
        
        # Depot Pusat sendiri dicoret dari list isolasi, harusnya tidak ada daerah terputus []
        if self.depot in lokasi_terisolasi:
            lokasi_terisolasi.remove(self.depot)
            
        self.assertEqual(len(lokasi_terisolasi), 0, "Harusnya semua lokasi bisa dijangkau")

    def test_bfs_deteksi_lokasi_terisolasi(self):
        """Menguji kemampuan BFS O(V+E) menemukan desa yang jalannya terputus/longsor"""
        self.graph.tambah_rute(self.depot, "Posko_A", 10)
        
        # Tambahkan Posko_C dan Posko_D yang saling terhubung namun terpisah dari jalur Depot Pusat
        self.graph.tambah_node("Posko_C")
        self.graph.tambah_node("Posko_D")
        self.graph.tambah_rute("Posko_C", "Posko_D", 8)
        
        lokasi_terisolasi = temukan_lokasi_terisolasi(self.graph, self.depot)
        
        # Bersihkan instansi depot pusat dari evaluasi
        if self.depot in lokasi_terisolasi:
            lokasi_terisolasi.remove(self.depot)

        # Posko_C dan Posko_D wajib terdeteksi sebagai area tidak terjangkau
        self.assertIn("Posko_C", lokasi_terisolasi)
        self.assertIn("Posko_D", lokasi_terisolasi)
        self.assertEqual(len(lokasi_terisolasi), 2)

if __name__ == "__main__":
    unittest.main()
  
