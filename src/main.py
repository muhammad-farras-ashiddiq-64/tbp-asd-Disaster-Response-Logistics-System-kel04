# Berkas Driver Utama Pengontrol Sistem Logistik Respons Bencana Kelompok 4
import sys
import numpy as np
from src.data_structures.queue_ll import PriorityQueueBantuan, Bantuan
from src.modules.modul_1 import GraphRute
from src.modules.modul_2 import BSTLokasi, Lokasi
from src.modules.modul_3 import StackLog
from src.modules.modul_4 import dijkstra

_id_generator = 0

def dapatkan_jalur(parent: dict, start: str, target: str) -> list:
    jalur = []
    curr = target
    while curr is not None:
        jalur.append(curr)
        if curr == start: 
            break
        curr = parent[curr]
    jalur.reverse()
    return jalur if jalur and jalur[0] == start else []

def main():
    global _id_generator
    bst = BSTLokasi()
    graph = GraphRute()
    pq = PriorityQueueBantuan()
    log_history = StackLog()

    # Inisialisasi Peta & Wilayah Sesuai Aturan Komputasi NumPy
    np.random.seed(47)
    
    # Registrasi Node Awal
    graph.tambah_node("DEPOT_PUSA")
    bst.insert(Lokasi("L001", "Posko Utama Sleman", 1, 3400)) # Status Kritis
    bst.insert(Lokasi("L002", "Wilayah Godean", 2, 1500))      # Status Sedang
    bst.insert(Lokasi("L003", "Cangkringan Atas", 3, 800))     # Status Ringan

    # Pemetaan Jalur Hubungan Antar Sektor
    graph.tambah_rute("DEPOT_PUSA", "L001", 12)
    graph.tambah_rute("DEPOT_PUSA", "L002", 22)
    graph.tambah_rute("L001", "L003", 8)

    print("=========================================================")
    print("      DISASTER RESPONSE LOGISTICS SYSTEM (KELOMPOK 4)    ")
    print("=========================================================")
    print("[INFO] Data spasial wilayah bencana telah sukses dimuat.")
    print("Daftar Perintah: ")
    print(" 1. KIRIM <tujuan> <jenis_bantuan> <jumlah>")
    print(" 2. RUTE_OPTIMAL <asal> <tujuan>")
    print(" 3. PROSES_ANTREAN")
    print(" 4. LOG_PENGIRIMAN")
    print(" 5. KELUAR")
    print("---------------------------------------------------------")

    while True:
        try:
            line = input("K4-LOGISTIK> ").strip()
            if not line: 
                continue
            args = line.split()
            cmd = args[0].upper()

            if cmd == "KIRIM":
                if len(args) < 4:
                    print("[PANDUAN] Format keliru. Gunakan: KIRIM <tujuan> <jenis> <jumlah>")
                    continue
                tujuan, jenis, jumlah = args[1], args[2], int(args[3])
                node_target = bst.search(tujuan)
                if node_target:
                    _id_generator += 1
                    urgensi = node_target.lokasi.level
                    bantuan_baru = Bantuan(_id_generator, jenis, jumlah, "DEPOT_PUSA", tujuan, urgensi)
                    pq.enqueue(bantuan_baru)
                    print(f"[PQ] Sukses masuk antrean! ID: {bantuan_baru.bantuan_id} [Prioritas: {urgensi}]")
                else:
                    print(f"[ERROR] Kode lokasi '{tujuan}' tidak ditemukan dalam database BST.")

            elif cmd == "RUTE_OPTIMAL":
                if len(args) < 3:
                    print("[PANDUAN] Format keliru. Gunakan: RUTE_OPTIMAL <asal> <tujuan>")
                    continue
                asal, target = args[1], args[2]
                if asal in graph.adj and target in graph.adj:
                    dist, parent = dijkstra(graph, asal)
                    jalur_terpendek = dapatkan_jalur(parent, asal, target)
                    print(f"[DIJKSTRA] Jarak Optimum: {dist[target]} KM")
                    print(f"[RUTE] Lintasan: {' -> '.join(jalur_terpendek)}")
                else:
                    print("[ERROR] Simpul lokasi asal atau tujuan tidak terdaftar dalam Graph.")

            elif cmd == "PROSES_ANTREAN":
                if pq.is_empty():
                    print("[INFO] Antrean pengiriman bantuan logistik kosong.")
                    continue
                item_bantuan = pq.dequeue()
                dist, parent = dijkstra(graph, item_bantuan.asal)
                
                print(f"[PROSES] Mengirim ID {item_bantuan.bantuan_id}: {item_bantuan.jumlah} {item_bantuan.jenis} ke {item_bantuan.tujuan}.")
                print(f"[LOGISTIK] Menggunakan jalur terpendek berjarak {dist[item_bantuan.tujuan]} KM.")
                
                log_history.push({
                    "id": item_bantuan.bantuan_id,
                    "target": item_bantuan.tujuan,
                    "isi": item_bantuan.jenis,
                    "vol": item_bantuan.jumlah
                })

            elif cmd == "LOG_PENGIRIMAN":
                riwayat = log_history.to_list()
                if not riwayat:
                    print("[INFO] Belum ada transaksi pengiriman logistik yang selesai.")
                    continue
                print("--- DAFTAR LOG TRANSAKSI SUKSES (STACK - LIFO) ---")
                for i, log in enumerate(riwayat, 1):
                    print(f" [{i}] Bantuan ID: {log['id']} | Tujuan: {log['target']} | Muatan: {log['vol']} unit {log['isi']}")

            elif cmd == "KELUAR":
                print("[INFO] Keluar dari sistem logistik. Terima kasih Kelompok 4.")
                break
            else:
                print("[INFO] Perintah tidak dikenal.")
        except Exception as err:
            print(f"[PERINGATAN] Terjadi kegagalan parsing parameter: {err}")

if __name__ == "__main__":
    main()
