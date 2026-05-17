import sys
import os
import time
import random
import numpy as np

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'src')
    )
)

from main import Bantuan, Lokasi, generate_peta_bencana
from data_structures.queue_ll import PriorityQueueBantuan
from data_structures.graph import GraphRute
from data_structures.bst import BSTLokasi
from data_structures.stack import Stack
from modules.Modul_5_Dijkstra_dan_Audit_Jarak import dijkstra_logistik


def benchmark_priority_queue():
    print("\n--- BENCHMARK 1: PRIORITY QUEUE ENQUEUE O(N) ---")
    print(f"{'Jumlah Data (N)':<20} | {'Waktu Eksekusi (Detik)':<25}")
    print("-" * 50)

    skala_n = [100, 500, 1000, 3000, 5000]

    for n in skala_n:
        pq = PriorityQueueBantuan()

        start_time = time.perf_counter()

        for i in range(n):
            prioritas_acak = random.randint(1, 3)

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


def benchmark_bst():
    print("\n--- BENCHMARK 2: BST INSERT O(log N) ---")
    print(f"{'Jumlah Data (N)':<20} | {'Waktu Eksekusi (Detik)':<25}")
    print("-" * 50)

    skala_n = [100, 500, 1000, 3000, 5000]

    for n in skala_n:
        bst = BSTLokasi()

        start_time = time.perf_counter()

        for i in range(n):
            lokasi = Lokasi(
                kode=f"L{i:05d}",
                nama=f"Lokasi-{i}",
                level=random.randint(1,3),
                populasi=random.randint(100,5000)
            )

            bst.insert(lokasi)

        end_time = time.perf_counter()
        durasi = end_time - start_time

        print(f"{n:<20} | {durasi:<25.6f}")


def benchmark_stack():
    print("\n--- BENCHMARK 3: STACK PUSH O(1) ---")
    print(f"{'Jumlah Data (N)':<20} | {'Waktu Eksekusi (Detik)':<25}")
    print("-" * 50)

    skala_n = [100, 500, 1000, 3000, 5000]

    for n in skala_n:
        stack = Stack()

        start_time = time.perf_counter()

        for i in range(n):
            stack.push(i)

        end_time = time.perf_counter()
        durasi = end_time - start_time

        print(f"{n:<20} | {durasi:<25.6f}")


def benchmark_dijkstra():
    print("\n--- BENCHMARK 4: ALGORITMA DIJKSTRA O(V² + E) ---")
    print(f"{'Jumlah Lokasi (V)':<20} | {'Waktu Eksekusi (Detik)':<25}")
    print("-" * 50)

    skala_v = [10, 35, 75, 150, 300]

    for v in skala_v:
        graph = GraphRute()

        lokasi_list, edges = generate_peta_bencana(
            n_lokasi=v,
            n_depot=3,
            seed=47
        )

        for lok in lokasi_list:
            graph.tambah_node(lok.kode)

        for u, v_edge, j, k in edges:
            graph.tambah_rute(u, v_edge, j, k)

        start_time = time.perf_counter()

        dijkstra_logistik(graph, "DEPOT_0")

        end_time = time.perf_counter()
        durasi = end_time - start_time

        print(f"{len(lokasi_list):<20} | {durasi:<25.6f}")


if __name__ == "__main__":

    print("==================================================")
    print("      EXPERIMENTAL RUNTIME BENCHMARK SUITE       ")
    print("==================================================")

    random.seed(42)

    benchmark_priority_queue()
    benchmark_bst()
    benchmark_stack()
    benchmark_dijkstra()

    print("\n==================================================")
    print("Eksperimen selesai. Hasil siap dianalisis.")
    print("==================================================")
