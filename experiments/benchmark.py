import time
import random
import numpy as np
from src.module_1 import GraphRute, dijkstra

def run_benchmark():
    print("=== EXPERIMENT: RUNTIME BENCHMARK ===")
    g = GraphRute()
    
    # Generate 500 node lokasi secara acak
    for i in range(500):
        g.tambah_node(f"L{i}")
    
    # Buat rute acak antar node
    for _ in range(1000):
        u = f"L{random.randint(0, 499)}"
        v = f"L{random.randint(0, 499)}"
        if u != v:
            g.tambah_rute(u, v, random.randint(5, 50))
            
    # Hitung waktu eksekusi Algoritma Dijkstra
    start_time = time.time()
    dist, parent = dijkstra(g, "L0")
    end_time = time.time()
    
    print(f"Waktu eksekusi Dijkstra untuk 500 Node: {end_time - start_time:.6f} detik")

if __name__ == "__main__":
    run_benchmark()
