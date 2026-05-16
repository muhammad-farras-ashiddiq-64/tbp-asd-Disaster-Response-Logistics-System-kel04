import time
import random
from src.modules.modul_1 import GraphRute
from src.modules.modul_4 import dijkstra

def run_benchmark():
    print("=== EXPERIMENT: RUNTIME BENCHMARK ===")
    g = GraphRute()
    
    for i in range(100):
        g.tambah_node(f"L{i}")
    
    for _ in range(200):
        u = f"L{random.randint(0, 99)}"
        v = f"L{random.randint(0, 99)}"
        if u != v:
            g.tambah_rute(u, v, random.randint(5, 50))
            
    start_time = time.time()
    dist, parent = dijkstra(g, "L0")
    end_time = time.time()
    
    print(f"Waktu eksekusi Dijkstra: {end_time - start_time:.6f} detik")

if __name__ == "__main__":
    run_benchmark()
