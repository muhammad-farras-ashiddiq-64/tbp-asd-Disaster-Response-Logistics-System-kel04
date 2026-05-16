# experiments/benchmark.py

import sys
import os
import time
import random

# Memastikan Python mendeteksi folder src/ dari luar direktori experiments
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data_structures.queue_ll import PriorityQueue
from data_structures.graph import Graph
from modules.Modul_5_Dijkstra_dan_Audit_Jarak import hitung_dijkstra

def benchmark_priority_queue():
    print("\n--- BENCHMARK 1: PRIORITY QUEUE ENQUEUE O(N) ---")
    print(f"{'Jumlah Data (N)':<20} | {'Waktu Eksekusi (Detik)':<25}")
    print("-" * 50)
    
    # Skala data pengujian
    skala_n = [100, 500, 1000, 3000, 5000]
    
    for n in skala_n:
        pq = PriorityQueue()
        
        # Mulai pencatatan waktu presisi tinggi
        start_time = time.perf_counter()
        
        for i in range(n):
            level_acak = random.randint(1, 3)
            data_mock = {"kode": f"L{i}", "nama": f"Desa_{i}"}
            pq.enqueue(data_mock, level_acak)
            
        end_time = time.perf_counter()
        durasi = end_time - start_time
        
        print(f"{n:<20} | {durasi:<25.6f}")

def benchmark_dijkstra():
    print("\n--- BENCHMARK 2: ALGORITMA DIJKSTRA O(V^2 + E) ---")
    print(f"{'Jumlah Node (V)':<20} | {'Waktu Eksekusi (Detik)':<25}")
    print("-" * 50)
    
    # Skala jumlah node/wilayah dalam graf
    skala_v = [10, 50, 100, 200, 300]
    
    for v in skala_v:
        g = Graph()
        depot = "DEPOT_PUSAT"
        g.tambah_node(depot)
        
        # Generate node wilayah secara acak
        nama_nodes = [f"Posko_{i}" for i in range(v)]
        for node in nama_nodes:
            g.tambah_node(node)
            
        # Hubungkan setiap node ke beberapa node lain secara acak untuk membentuk rute (Sisi E)
        for node in nama_nodes:
            # Hubungkan ke depot pusat
            g.tambah_rute(depot, node, random.randint(5, 50))
            # Hubungkan ke 3 tetangga acak lainnya
            tetangga_acak = random.sample(nama_nodes, min(3, v))
            for t in tetangga_acak:
                if node != t:
                    g.tambah_rute(node, t, random.randint(2, 30))
                    
        # Mulai pencatatan waktu eksekusi Dijkstra
        start_time = time.perf_counter()
        hitung_dijkstra(g, depot)
        end_time = time.perf_counter()
        
        durasi = end_time - start_time
        print(f"{v:<20} | {durasi:<25.6f}")

if __name__ == "__main__":
    print("==================================================")
    print("      EXPERIMENTAL RUNTIME BENCHMARK SUITE       ")
    print("==================================================")
    
    # Menyetel seed agar hasil pengujian acak tetap konsisten saat running berulang
    random.seed(42)
    
    benchmark_priority_queue()
    benchmark_dijkstra()
    
    print("\n==================================================")
    print("✓ Eksperimen selesai. Salin tabel ini ke laporan.")
    print("==================================================")
