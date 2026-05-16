# experiments/benchmark.py

import sys
import os
import time
import random
import numpy as np

# Mengarahkan path agar Python bisa membaca folder src/ dari direktori experiments
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import Bantuan, generate_peta_bencana
from data_structures.queue_ll import PriorityQueueBantuan
from data_structures.graph import GraphRute
from modules.Modul_5_Dijkstra_dan_Audit_Jarak import dijkstra_logistik

def benchmark_priority_queue():
    print("\n--- BENCHMARK 1: PRIORITY QUEUE ENQUEUE O(N) ---")
    print(f"{'Jumlah Data (N)':<20} | {'Waktu Eksekusi (Detik)':<25}")
    print("-" * 50)
    
    # Deret ukuran sampel data bantuan
    skala_n = [100, 500, 1000, 3000, 5000]
    
    for n in skala_n:
        pq = PriorityQueueBantuan()
        
        # Mulai pencatatan waktu presisi tinggi
        start_time = time.perf_counter()
        
        for i in range(n):
            prioritas_acak = random.randint(1, 3)
            # Membuat objek Bantuan tiruan sesuai dataclass halaman 41
            obj_bantuan = Bantuan(
                bantuan_id=i, 
                jenis="MAKANAN", 
                jumlah=100, 
                asal="DEPOT_0", 
                tujuan=f"L{i:03d}", 
                prioritas=prioritas_acak
            )
            pq.enqueue(obj_bantuan)
            
        end_time = time.perf_counter()
        durasi = end_time - start_time
        
        print(f"{n:<20} | {durasi:<25.6f}")

def benchmark_dijkstra():
    print("\n--- BENCHMARK 2: ALGORITMA DIJKSTRA O(V^2 + E) ---")
    print(f"{'Jumlah Lokasi (V)':<20} | {'Waktu Eksekusi (Detik)':<25}")
    print("-" * 50)
    
    # Skala jumlah titik lokasi bencana (Simulasi pertumbuhan graf)
    skala_v = [10, 35, 75, 150, 300]
    
    for v in skala_v:
        graph = GraphRute()
        
        # Gunakan fungsi bawaan generator peta untuk membuat data node dan edge
        # n_depot dipatok 3 sesuai template dokumen halaman 43
        lokasi_list, edges = generate_peta_bencana(n_lokasi=v, n_depot=3, seed=47)
        
        for lok in lokasi_list:
            graph.tambah_node(lok.kode)
        for u, v_edge, j, k in edges:
            graph.tambah_rute(u, v_edge, j, k)
            
        # Catat waktu proses kalkulasi rute terpendek Dijkstra dari DEPOT_0
        start_time = time.perf_counter()
        dijkstra_logistik(graph, "DEPOT_0")
        end_time = time.perf_counter()
        
        durasi = end_time - start_time
        print(f"{len(lokasi_list):<20} | {durasi:<25.6f}")

if __name__ == "__main__":
    print("==================================================")
    print("      EXPERIMENTAL RUNTIME BENCHMARK SUITE       ")
    print("==================================================")
    
    # Menyetel seed acak agar hasil pengujian tetap konsisten setiap running
    random.seed(42)
    
    benchmark_priority_queue()
    benchmark_dijkstra()
    
    print("\n==================================================")
    print("✓ Eksperimen selesai. Hasil siap dianalisis.")
    print("==================================================")
