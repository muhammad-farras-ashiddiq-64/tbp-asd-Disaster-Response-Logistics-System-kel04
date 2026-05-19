# ==============================================================================
# PROYEK ASD: SISTEM MANAJEMEN LOGISTIK TANGGAP BENCANA (CLI ENGINE)
# 
# Tim Pengembang:
# 1. Khairu Imtihan      (25051030052) - Modul 1 & 5 (Graph & Dijkstra)
# 2. Muh. Farras Ashiddiq (25051030064) - Modul 3 (Binary Search Tree)
# 3. Noomira Zakiah       (25051030072) - Modul 2 (Priority Queue & Linked List)
# 4. Restu Pamungkas      (25051030080) - Modul 4 & 6 (Stack, Audit, & CLI Integration)
# ==============================================================================

import random
from src.models import Lokasi, Bantuan
from src.data_structures.queue_ll import PriorityQueueBantuan
from src.data_structures.stack import Stack
from src.data_structures.bst import BSTLokasi
from src.data_structures.graph import GraphRute, dijkstra_logistik
from src.modules.audit import selection_sort_audit

# Aturan Data Validasi Kontrol Sistem
JENIS_BANTUAN = ['MAKANAN', 'AIR', 'OBAT', 'SELIMUT', 'TENDA']

def generate_peta_bencana(n_lokasi=35, n_depot=3, seed=47):
    """Generator Topologi Peta Bencana Konstan Sesuai Spesifikasi Proyek"""
    rng = random.Random(seed)
    lokasi = []
    
    # Inisialisasi Depot Utama
    for i in range(n_depot):
        lokasi.append(Lokasi(f'DEPOT_{i}', f'Gudang Logistik {i}', 3, 0))
        
    # Inisialisasi Titik Terdampak Bencana
    for i in range(n_lokasi):
        kode = f'L{i:03d}'
        level = int(rng.choice([1, 2, 3], p=[0.2, 0.4, 0.4]))
        pop = int(rng.integers(100, 5000))
        lokasi.append(Lokasi(kode, f'Desa/Kelurahan-{i}', level, pop))
    
    n_total = len(lokasi)
    perm = rng.permutation(n_total)
    edges = []
    
    # Jalur Utama (Minimum Connected Backbone)
    for i in range(1, n_total):
        u = lokasi[perm[i-1]].kode
        v = lokasi[perm[i]].kode
        edges.append((u, v, int(rng.integers(5, 100)), int(rng.integers(1, 5))))
        
    # Jalur Alternatif Acak
    for _ in range(15):
        i, j = rng.choice(n_total, 2, replace=False)
        edges.append((lokasi[i].kode, lokasi[j].kode, int(rng.integers(5, 100)), int(rng.integers(1, 5))))
        
    return lokasi, edges

def main():
    # Mengunci seed agar kondisi data awal konsisten saat pengujian/demonstrasi
    np.random.seed(47)
    random.seed(47)

    bst_lokasi = BSTLokasi()
    graph = GraphRute()
    antrian_bantuan = PriorityQueueBantuan()
    log_kirim = Stack()
    bantuan_counter = 0

    # Memuat data peta simulasi ke dalam memori struktur data
    lokasi_list, edges = generate_peta_bencana(35, 3, seed=47)
    for lok in lokasi_list:
        bst_lokasi.insert(lok)
        graph.tambah_node(lok.kode)
    for u, v, j, k in edges:
        graph.tambah_rute(u, v, j, k)

    print("="*65)
    print("      SISTEM MANAJEMEN LOGISTIK TANGGAP BENCANA (CLI)      ")
    print("="*65)
    print("Ketik 'BANTUAN' untuk melihat daftar format perintah lengkap.")

    while True:
        try:
            cmd_line = input("\nLogistik-CLI> ").strip().split()
            if not cmd_line:
                continue
            
            cmd = cmd_line[0].upper()

            if cmd == 'BANTUAN':
                print("\nDaftar Perintah Sistem:")
                print(" -> KIRIM <depot> <lokasi> <jenis> <jumlah>")
                print(" -> PROSES_BANTUAN")
                print(" -> RUTE_OPTIMAL <depot> <tujuan>")
                print(" -> UPDATE_LEVEL <kode> <level>")
                print(" -> TIDAK_TERJANGKAU <depot>")
                print(" -> AUDIT_JARAK <depot>")
                print(" -> LOG_PENGIRIMAN")
                print(" -> ROLLBACK")
                print(" -> LAPORAN_BENCANA")
                print(" -> KELUAR")

            elif cmd == 'KIRIM':
                if len(cmd_line) != 5:
                    print("❌ Format Salah! Gunakan: KIRIM <depot> <lokasi> <jenis> <jumlah>")
                    continue
                _, depot, lokasi_tujuan, jenis, jumlah = cmd_line
                
                # Cari data lokasi di BST untuk mengecek keaslian kode & level prioritas
                target = bst_lokasi.search(lokasi_tujuan.upper())
                if not target:
                    print(f"❌ Kesalahan: Kode lokasi {lokasi_tujuan.upper()} tidak terdaftar di database.")
                    continue
                if jenis.upper() not in JENIS_BANTUAN:
                    print(f"❌ Kesalahan: Jenis bantuan tidak valid. Harus salah satu dari: {JENIS_BANTUAN}")
                    continue
                
                bantuan_counter += 1
                payload = Bantuan(
                    bantuan_id=bantuan_counter,
                    jenis=jenis.upper(),
                    jumlah=int(jumlah),
                    asal=depot.upper(),
                    tujuan=lokasi_tujuan.upper(),
                    prioritas=target.level
                )
                antrian_bantuan.enqueue(payload)
                print(f"✔ Berhasil: Permintaan bantuan ID {bantuan_counter} [{jenis.upper()}] masuk antrian (Prioritas Level: {target.level}).")

            elif cmd == 'PROSES_BANTUAN':
                if len(antrian_bantuan) == 0:
                    print("⚠ Info: Antrian distribusi logistik saat ini kosong.")
                    continue
                item_lepas = antrian_bantuan.dequeue()
                log_kirim.push(item_lepas) # Disimpan ke Stack untuk kebutuhan Rollback LIFO
                print(f"🚚 [PROSES] Mengirim {item_lepas.jumlah} paket {item_lepas.jenis} dari {item_lepas.asal} menuju {item_lepas.tujuan} (Level: {item_lepas.prioritas})")

            elif cmd == 'RUTE_OPTIMAL':
                if len(cmd_line) != 3:
                    print("❌ Format Salah! Gunakan: RUTE_OPTIMAL <depot> <tujuan>")
                    continue
                _, depot, tujuan = cmd_line
                
                dist, parent = dijkstra_logistik(graph, depot.upper())
                jarak_total = dist.get(tujuan.upper(), float('inf'))
                
                if jarak_total == float('inf'):
                    print(f"❌ Kesalahan: Rute jalur menuju {tujuan.upper()} terputus/terisolasi.")
                else:
                    # Rekonstruksi lintasan rute dari simpul penunjuk jalan parent
                    path = []
                    curr = tujuan.upper()
                    while curr is not None:
                        path.append(curr)
                        curr = parent[curr]
                    path.reverse()
                    print(f"📍 Jarak Minimum Optimum: {jarak_total} km")
                    print(f"🗺 Jalur Lintasan Peta: {' -> '.join(path)}")

            elif cmd == 'UPDATE_LEVEL':
                if len(cmd_line) != 3:
                    print("❌ Format Salah! Gunakan: UPDATE_LEVEL <kode> <level>")
                    continue
                _, kode, level_baru = cmd_line
                
                if bst_lokasi.update_level(kode.upper(), int(level_baru)):
                    print(f"✔ Berhasil: Level kedaruratan wilayah {kode.upper()} kini diubah ke Level {level_baru}.")
                else:
                    print(f"❌ Gagal: Lokasi {kode.upper()} tidak ditemukan di registry.")

            elif cmd == 'TIDAK_TERJANGKAU':
                if len(cmd_line) != 2:
                    print("❌ Format Salah! Gunakan: TIDAK_TERJANGKAU <depot>")
                    continue
                _, depot = cmd_line
                
                terjangkau = graph.bfs_akses(depot.upper())
                semua_node = list(graph.adj.keys())
                terisolasi = [node for node in semua_node if node not in terjangkau]
                print(f"⚠️ Daerah Terisolasi dari {depot.upper()}: {terisolasi if terisolasi else 'Nihil (Semua Wilayah Dapat Diakses)'}")

            elif cmd == 'AUDIT_JARAK':
                if len(cmd_line) != 2:
                    print("❌ Format Salah! Gunakan: AUDIT_JARAK <depot>")
                    continue
                _, depot = cmd_line
                
                dist, _ = dijkstra_logistik(graph, depot.upper())
                list_data = [(k, v) for k, v in dist.items() if v != float('inf') and k != depot.upper()]
                
                # Diurutkan menggunakan algoritma manual Selection Sort (Modul 5)
                sorted_data = selection_sort_audit(list_data)
                
                print(f"📊 Hasil Audit Jarak Distribusi Terdekat dari Gudang {depot.upper()}:")
                for area, km in sorted_data:
                    print(f"   * Ke Simpul {area} -> {km} km")

            elif cmd == 'LOG_PENGIRIMAN':
                logs = log_kirim.to_list()
                if not logs:
                    print("📋 Arsip log pengiriman kosong.")
                else:
                    print("📋 Riwayat Transaksi Distribusi Logistik (LIFO - Terbaru di Atas):")
                    for log in logs:
                        print(f"   [ID: {log.bantuan_id}] {log.jumlah} {log.jenis} | Rute: {log.asal} ➔ {log.tujuan}")

            elif cmd == 'ROLLBACK':
                if len(log_kirim) == 0:
                    print("❌ Gagal Batalkan: Log transaksi kosong, tidak ada operasi untuk ditarik kembali.")
                    continue
                item_batal = log_kirim.pop()
                print(f"🔄 [ROLLBACK] Berhasil! Distribusi ID {item_batal.bantuan_id} dibatalkan. Armada dipaksa kembali ke {item_batal.asal}.")

            elif cmd == 'LAPORAN_BENCANA':
                data_inorder = bst_lokasi.inorder()
                print("\n" + "="*55)
                print("📑 REKAP LAPORAN DATA REGISTRY WILAYAH (Urutan Kode BST)")
                print("="*55)
                print(f"{'KODE':<8} | {'NAMA AREA':<22} | {'SKALA DARURAT':<13} | {'POPULASI'}")
                print("-"*55)
                for l in data_inorder:
                    # Filter agar baris depot penampungan logistik tidak ikut dicetak sebagai korban
                    if "DEPOT" not in l.kode:
                        print(f"{l.kode:<8} | {l.nama:<22} | Level {l.level:<7} | {l.populasi} Jiwa")

            elif cmd == 'KELUAR':
                print("👋 Menonaktifkan konsol kendali logistik. Program ditutup.")
                break
            else:
                print("❌ Perintah tidak dikenali atau argumen input salah. Gunakan perintah 'BANTUAN'.")
                
        except Exception as e:
            print(f"⚠️ Terjadi Galat Operasi Sistem: {str(e)}")

if __name__ == '__main__':
    main()