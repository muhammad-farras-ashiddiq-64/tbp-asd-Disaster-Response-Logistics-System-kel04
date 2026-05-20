import numpy as np
from src.main import generate_peta_bencana
from src.bst import BSTLokasi
from src.graph import GraphRute, dijkstra_logistik

def lakukan_audit_sistem():
    print("=" * 60)
    print("        AUDIT INTERNAL SYSTEM: ALGORITMA DIJKSTRA       ")
    print("=" * 60)
    
    # 1. Inisialisasi Graf dan Data Peta (Gunakan Seed yang Sama)
    bst_lokasi = BSTLokasi()
    graph = GraphRute()
    lokasi_list, edges = generate_peta_bencana(35, 3, seed=47)
    
    for lok in lokasi_list:
        bst_lokasi.insert(lok)
        graph.tambah_node(lok.kode)
    for u, v, j, k in edges:
        graph.tambah_rute(u, v, j, k)
        
    depots = ['DEPOT_0', 'DEPOT_1', 'DEPOT_2']
    total_rute_sukses = 0
    total_jarak_kumulatif = 0
    rute_terjauh = {"dari": "", "ke": "", "jarak": 0, "jalur": []}
    
    # 2. Proses Audit Menggunakan Dijkstra untuk Setiap Depot
    for depot in depots:
        print(f"\n[AUDIT] Memproses Distribusi Jarak dari: {depot}")
        print("-" * 50)
        
        # Jalankan fungsi Dijkstra yang sudah kita buat
        dist, parent = dijkstra_logistik(graph, depot)
        
        rute_lokal_sukses = 0
        rute_lokal_terisolasi = 0
        
        # Audit jarak ke seluruh lokasi L000 - L034
        for i in range(35):
            target_kode = f'L{i:03d}'
            jarak = dist[target_kode]
            
            if jarak == float('inf'):
                rute_lokal_terisolasi += 1
            else:
                rute_lokal_sukses += 1
                total_rute_sukses += 1
                total_jarak_kumulatif += jarak
                
                # Rekonstruksi rute untuk mencari rute terjauh
                path = []
                curr = target_kode
                while curr is not None:
                    path.append(curr)
                    curr = parent[curr]
                path.reverse()
                
                if jarak > rute_terjauh["jarak"]:
                    rute_terjauh = {
                        "dari": depot,
                        "ke": target_kode,
                        "jarak": jarak,
                        "jalur": path
                    }
        
        print(f"  > Lokasi Terjangkau : {rute_lokal_sukses} lokasi")
        print(f"  > Lokasi Terisolasi : {rute_lokal_terisolasi} lokasi")

    # 3. Ringkasan Laporan Audit Evaluasi Jarak
    print("\n" + "=" * 60)
    print("                  KESIMPULAN AUDIT JARAK                ")
    print("=" * 60)
    if total_rute_sukses > 0:
        rata_rata_jarak = total_jarak_kumulatif / total_rute_sukses
        print(f"Rata-rata Jarak Suplai Efektif : {rata_rata_jarak:.2f} km")
    else:
        print("Rata-rata Jarak Suplai Efektif : 0 km")
        
    print(f"Rute Distribusi Terjauh        : {rute_terjauh['dari']} ke {rute_terjauh['ke']}")
    print(f"Jarak Maksimum Jalur           : {rute_terjauh['jarak']} km")
    print(
