import unittest
from src.modules.modul_1 import GraphRute
from src.modules.modul_5 import dijkstra, rekonstruksi_jalur

class TestGraphRouting(unittest.TestCase):
    def setUp(self):
        self.graph = GraphRute()
        # Membuat peta mini: DEPOT -> L001 (10 km), L001 -> L002 (5 km), DEPOT -> L002 (25 km)
        self.graph.tambah_rute("DEPOT_0", "L001", 10)
        self.graph.tambah_rute("L001", "L002", 5)
        self.graph.tambah_rute("DEPOT_0", "L002", 25)

    def test_bfs_connectivity(self):
        """Memastikan BFS dapat mengidentifikasi seluruh simpul yang terhubung."""
        terjangkau = self.graph.bfs_akses("DEPOT_0")
        self.assertIn("L002", terjangkau)
        self.assertIn("L001", terjangkau)

    def test_dijkstra_shortest_path(self):
        """Memastikan algoritma Dijkstra memilih jalur optimum lewat L001 (Jarak 15) bukan langsung (Jarak 25)."""
        dist, parent = dijkstra(self.graph, "DEPOT_0")
        self.assertEqual(dist["L002"], 15)
        
        jalur = rekonstruksi_jalur(parent, "DEPOT_0", "L002")
        self.assertEqual(jalur, ["DEPOT_0", "L001", "L002"])

if __name__ == "__main__":
    unittest.main()
