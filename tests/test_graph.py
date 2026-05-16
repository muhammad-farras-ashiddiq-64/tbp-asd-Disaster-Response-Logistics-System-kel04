import unittest
# Sesuaikan import dengan struktur folder src/modules/
from src.modules.modul_1 import GraphRute
from src.modules.modul_4 import dijkstra

class TestLogistikGraph(unittest.TestCase):
    def test_dijkstra_shortest_path(self):
        g = GraphRute()
        g.tambah_rute("DEPOT_PUSA", "L001", 5)
        g.tambah_rute("L001", "L002", 10)
        g.tambah_rute("DEPOT_PUSA", "L002", 20)
        
        dist, parent = dijkstra(g, "DEPOT_PUSA")
        # Jalur terpendek ke L002 harus lewat L001 (5 + 10 = 15)
        self.assertEqual(dist["L002"], 15)

if __name__ == "__main__":
    unittest.main()
