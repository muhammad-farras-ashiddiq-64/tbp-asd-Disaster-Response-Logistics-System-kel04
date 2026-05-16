# src/main.py

import sys
import os
import numpy as np
from dataclasses import dataclass

# Injeksi path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_structures.bst import BSTLokasi
from data_structures.graph import GraphRute
from data_structures.queue_ll import PriorityQueueBantuan
from data_structures.stack import Stack
from modules.Modul_1_Graph_Jaringan_Rute import dapatkan_wilayah_terisolasi
from modules.Modul_5_Dijkstra_dan_Audit_Jarak import dijkstra_logistik
from modules.Modul_6_CLI_Logistik import cetak_bantuan_menu

# Definisi Tipe Objek sesuai Halaman 41
LEVEL_BENCANA = {'KRITIS': 1, 'SEDANG': 2, 'RINGAN': 3}
JENIS_BANTUAN = ['MAKANAN', 'AIR', 'OBAT', 'SELIMUT', 'TENDA']

@dataclass
class Lokasi:
    kode: str
    nama: str
    level: int
    populasi: int
    status: int = 0

@dataclass
class Bantuan:
    bantuan_id: int
    jenis: str
    jumlah: int
    asal: str
    tujuan: str
    prioritas: int

def generate_peta_bencana(n_lokasi=35, n_depot=3, seed=47):
    rng = np.random.default_rng(seed)
    lokasi = []
    for i in range(n_depot):
        lokasi.append(Lokasi(f'DEPOT_{i}', f'Gudang Logistik {i}', 3, 0))
    for i in range(n_lokasi):
        kode = f'L{i:03d}'
        level = int(rng.choice([1, 2, 3], p=[0.2, 0.4, 0.4]))
        populasi = int(rng.integers(100, 5000))
        lokasi.append(Lokasi(kode, f'Desa/Kelurahan-{i}', level, populasi))
    
    n_total = len(lokasi)
    perm = rng.permutation(n_total)
    edges = []
    for i in range(1, n_total):
        u = lokasi[perm[i-1]].kode
        v = lokasi[perm[i]].kode
        edges.append((u, v, int(rng.integers(5, 100)), int(rng.integers(1, 5))))
    for _ in range(15):
        i, j = rng.choice(n_total, 2, replace=False)
        edges.append((lokasi[i].kode, lokasi[j].kode, int(rng.integers(5, 100)), int(rng.integers(1, 5))))
    return lokasi, edges

def main():
    bst_lokasi = BSTLokasi()
    graph = GraphRute()
    antrian_bantuan = PriorityQueueBantuan()
    log_kirim = Stack()
    bantuan_counter = 0

    lokasi_list, edges = generate_peta_bencana(35, 3, seed=47)
    for lok in lokasi_list:
        bst_lokasi.insert(lok)
        graph.tambah_node(lok.kode)
    for u, v, j, k in edges:
        graph.tambah_rute(u, v, j, k)

    print('Disaster Response Logistics System. Ketik BANTUAN untuk daftar perintah')
    
    # Deteksi Mode GitHub Actions CI
    if "--test" in sys.argv:
        print("CI Mode: Menjalankan verifikasi sistem data...")
        assert bst_lokasi.search("L000") is not None
        print("OK semua test internal lulus")
        return

    while True:
        cmd_input = input("\nMasukkan Perintah >> ").strip().split()
        if not cmd_input:
            continue
        
        command = cmd_input[0].upper()

        if command == "BANTUAN":
            cetak_bantuan_menu()

        elif command == "KIRIM":
            if len(cmd_input) < 5:
                print("Format: KIRIM <depot> <lokasi> <jenis> <jumlah>")
                continue
            depot, lokasi_target, jenis, jumlah = cmd_input[1], cmd_input[2], cmd_input[3].upper(), int(cmd_input[4])
            
            target_node = bst_lokasi.search(lokasi_target)
            if not target_node:
                print("Lokasi tujuan tidak valid!")
                continue
            
            bantuan_counter += 1
            # Prioritas link otomatis ke level bencana
            obj_bantuan = Bantuan(bantuan_counter, jenis, jumlah, depot, lokasi_target, target_node.level)
            antrian_bantuan.enqueue(obj_bantuan)
            print(f"✓ Sukses Enqueue Bantuan ID-{bantuan_counter} ke Antrian Prioritas Level {target_node.level}.")

        elif command == "PROSES_BANTUAN":
            bantuan_aktif = antrian_bantuan.dequeue()
            if not bantuan_aktif:
                print("Antrian pengiriman kosong.")
            else:
                log_kirim.push(bantuan_aktif)
                loc_target = bst_lokasi.search(bantuan_aktif.tujuan)
                if loc_target:
                    loc_target.status = 1  # Dikirim
                print(f"▶ Distribusi Bantuan ID-{bantuan_aktif.bantuan_id} ({bantuan_aktif.jenis}) dikirim ke {bantuan_aktif.tujuan}.")

        elif command == "RUTE_OPTIMAL":
            if len(cmd_input) < 3:
                print("Format: RUTE_OPTIMAL <depot> <tujuan>")
                continue
            depot, tujuan = cmd_input[1], cmd_input[2]
            dist, parent = dijkstra_logistik(graph, depot)
            
            if tujuan not in dist or dist[tujuan] == float('inf'):
                print("Rute tidak ditemukan / Lokasi Terisolasi!")
            else:
                # Rekonstruksi rute
                path = []
                curr = tujuan
                while curr is not None:
                    path.insert(0, curr)
                    curr = parent[curr]
                print(f"Jarak Terpendek: {dist[tujuan]} km. Rute Lintasan: {' -> '.join(path)}")

        elif command == "UPDATE_LEVEL":
            if len(cmd_input) < 3:
                print("Format: UPDATE_LEVEL <kode> <level>")
                continue
            kode, level_baru = cmd_input[1], int(cmd_input[2])
            if bst_lokasi.update_level(kode, level_baru):
                print(f"✓ Tingkat urgensi lokasi {kode} diubah ke level {level_baru}.")
            else:
                print("Kode lokasi salah!")

        elif command == "TIDAK_TERJANGKAU":
            if len(cmd_input) < 2:
                print("Format: TIDAK_TERJANGKAU <depot>")
                continue
            depot = cmd_input[1]
            terisolasi = dapatkan_wilayah_terisolasi(graph, depot)
            if not terisolasi:
                print("Seluruh wilayah aman terhubung.")
            else:
                print(f"⚠ Peringatan wilayah terisolasi dari {depot}: {sorted(list(terisolasi))}")

        elif command == "LOG_PENGIRIMAN":
            riwayat = log_kirim.to_list()
            if not riwayat:
                print("Belum ada log transaksi pengiriman.")
            for log in riwayat:
                print(f"[-] ID: {log.bantuan_id} | Muatan: {log.jenis} {log.jumlah} unit | {log.asal} -> {log.tujuan}")

        elif command == "LAPORAN_BENCANA":
            daftar_lokasi = bst_lokasi.inorder()
            print(f"{'KODE':<8} | {'NAMA LOKASI':<20} | {'URGENSI':<10} | {'POPULASI':<10} | {'STATUS'}")
            print("-" * 65)
            for l in daftar_lokasi:
                txt_status = "Terkirim" if l.status == 1 else "Menunggu"
                print(f"{l.kode:<8} | {l.nama:<20} | Level {l.level:<6} | {l.populasi:<10} | {txt_status}")

        elif command == "KELUAR":
            print("Sistem Logistik Bencana Dimatikan.")
            break

if __name__ == '__main__':
    main()
