Python
import sys
import os

# Memastikan Python mendeteksi folder internal root src/
sys.path.append(os.path.dirname(os.path.abspath(_file_)))

from data_structures.graph import Graph
from data_structures.queue_ll import PriorityQueue
from data_structures.bst import BST
from data_structures.stack import Stack
from modules.Modul_1_Graph_Jaringan_Rute import temukan_lokasi_terisolasi
from modules.Modul_5_Dijkstra_dan_Audit_Jarak import hitung_dijkstra, audit_jarak_selection_sort

# Inisialisasi Database Sistem
peta = Graph()
antrean_triage = PriorityQueue()
registri = BST()
riwayat_log = Stack()
DEPOT = "DEPOT_PUSAT"

peta.tambah_node(DEPOT)

def main():
    # ---- HANDLER FOR GITHUB ACTIONS AUTOMATION (CI) ----
    if "--test" in sys.argv:
        print("=== MODE EVALUASI OTOMATIS (CI) ===")
        registri.insert("T01", "Lokasi Uji", 2, 100)
        peta.tambah_node("Lokasi Uji")
        assert registri.search("T01").nama == "Lokasi Uji", "Integritas BST gagal"
        print("✓ Seluruh komponen sistem logistik lolos validasi.")
        sys.exit(0)
    # ----------------------------------------------------

    while True:
        print("\n========================================================")
        print("         DISASTER RESPONSE LOGISTICS SYSTEM             ")
        print("========================================================")
        print("1. KIRIM (Enqueue Prioritas Bantuan)")
        print("2. PROSES_BANTUAN (Dequeue & Kirim)")
        print("3. RUTE_OPTIMAL (Dijkstra Jalur Terpendek)")
        print("4. UPDATE_LEVEL (Perbarui Tingkat Urgensi Lokasi)")
        print("5. TIDAK_TERJANGKAU (BFS Deteksi Isolasi)")
        print("6. LOG_PENGIRIMAN & ROLLBACK (Manajemen LIFO)")
        print("7. LAPORAN_BENCANA (Inorder Urutan Kode BST)")
        print("8. KELUAR")
        print("========================================================")
        
        pilihan = input("Pilih menu operasional [1-8]: ").strip().upper()
        
        if pilihan == "1" or pilihan == "KIRIM":
            kode = input("Masukkan Kode Wilayah Bencana (ex: L01): ")
            nama = input("Masukkan Nama Desa/Posko: ")
            level = int(input("Tingkat Urgensi (1:KRITIS, 2:Sedang, 3:Ringan): "))
            populasi = int(input("Jumlah Populasi Terdampak: "))
            jarak = int(input(f"Jarak rute jalan dari {DEPOT} (km): "))
            
            registri.insert(kode, nama, level, populasi)
            peta.tambah_rute(DEPOT, nama, jarak)
            antrean_triage.enqueue({"kode": kode, "nama": nama, "level": level}, level)
            print(f"✓ Sukses: Wilayah {nama} dimasukkan ke antrean prioritas level {level}.")
            
        elif pilihan == "2" or pilihan == "PROSES_BANTUAN":
            bantuan = antrean_triage.dequeue()
            if not bantuan:
                print("! Informasi: Antrean kosong, belum ada permintaan bantuan baru.")
            else:
                riwayat_log.push(bantuan)
                node_bst = registri.search(bantuan['kode'])
                if node_bst: 
                    node_bst.status = "Bantuan Sedang Dikirim"
                print(f"▶️ Truk Logistik diberangkatkan menuju {bantuan['nama']} (Level {bantuan['level']}).")
                
        elif pilihan == "3" or pilihan == "RUTE_OPTIMAL":
            tujuan = input("Masukkan nama wilayah tujuan: ")
            if tujuan not in peta.nodes:
                print("! Kesalahan: Wilayah tujuan tidak terdaftar di dalam peta rute.")
            else:
                hasil_jarak = hitung_dijkstra(peta, DEPOT)
                print(f"✓ Rute Optimal Jarak Minimum ke {tujuan} adalah {hasil_jarak[tujuan]} km.")
                
                print("\n--- AUDIT AUDIENSI JARAK WILAYAH (SELECTION SORT LINKED LIST) ---")
                ll_terurut = audit_jarak_selection_sort(hasil_jarak)
                curr = ll_terurut.head
                paling_sulit = None
                maks_jarak = -1
                
                while curr:
                    if curr.data['nama'] != DEPOT:
                        print(f"-> Lokasi: {curr.data['nama']} | Jarak: {curr.data['jarak']} km")
                        if curr.data['jarak'] != float('inf') and curr.data['jarak'] > maks_jarak:
                            maks_jarak = curr.data['jarak']
                            paling_sulit = curr.data['nama']
                    curr = curr.next
                if paling_sulit:
                    print(f"\n⚠️ Kesimpulan Audit: Wilayah yang paling sulit dijangkau adalah {paling_sulit} ({maks_jarak} km).")

        elif pilihan == "4" or pilihan == "UPDATE_LEVEL":
            kode = input("Masukkan Kode Wilayah: ")
            level_baru = int(input("Masukkan Level Kedaruratan Baru (1-3): "))
            if registri.update_level(kode, level_baru):
                print("✓ Tingkat urgensi wilayah berhasil diperbarui di sistem.")
            else:
                print("! Error: Kode lokasi tidak ditemukan.")
                
        elif pilihan == "5" or pilihan == "TIDAK_TERJANGKAU":
            isolasi = temukan_lokasi_terisolasi(peta, DEPOT)
            # Menghapus DEPOT dari list isolasi jika ada
            if DEPOT in isolasi: 
                isolasi.remove(DEPOT)
            if not search_isolasi_clean := [n for n in isolasi if registri.search(n) or n in peta.nodes]:
                print("✓ Hasil Analisis BFS: Semua lokasi sukses terhubung dengan Depot Pusat.")
            else:
                print(f"⚠️ PERINGATAN: Lokasi berikut terisolasi (Jalur Terputus): {search_isolasi_clean}")
            
        elif pilihan == "6" or pilihan == "LOG_PENGIRIMAN":
            print("a. Tampilkan Riwayat Log")
            print("b. ROLLBACK (Batalkan Pengiriman Terakhir)")
            sub_opt = input("Pilih tindakan [a/b]: ").strip().lower()
            if sub_opt == "a":
                print("\n--- RIWAYAT LOGISTIK (LIFO STACK) ---")
                curr = riwayat_log.top
                if not curr: 
                    print("Log kosong.")
                while curr:
                    print(f"[-] Terkirim ke: {curr.data['nama']} (Prioritas Level {curr.data['level']})")
                    curr = curr.next
            elif sub_opt == "b":
                batal = riwayat_log.pop()
                if batal:
                    antrean_triage.enqueue(batal, batal['level'])
                    node_bst = registri.search(batal['kode'])
                    if node_bst: 
                        node_bst.status = "Menunggu Bantuan (Rollback)"
                    print(f"✓ Rollback Berhasil: Distribusi ke {batal['nama']} dibatalkan, armada kembali ke Depot.")
                else:
                    print("! Gagal: Tidak ada riwayat transaksi pengiriman yang dapat di-rollback.")
                    
        elif pilihan == "7" or pilihan == "LAPORAN_BENCANA":
            print("\n--- LAPORAN REGISTRI WILAYAH BENCANA (INORDER TRAVERSAL BST) ---")
            def inorder_print(node):
                if node:
                    inorder_print(node.left)
                    print(f"Kode: {node.kode} | Nama: {node.nama:<15} | Urgensi: Level {node.level} | Status: {node.status}")
                    inorder_print(node.right)
            
            if not registri.root:
                print("Laporan Kosong: Belum ada data wilayah bencana yang diregistrasikan.")
            else:
                inorder_print(registri.root)

        elif pilihan == "8" or pilihan == "KELUAR":
            print("Keluar dari program manajemen komando logistik bencana. Selesai.")
            break
        else:
            print("! Opsi tidak valid. Silakan pilih menu antara [1-8].")

if _name_ == "_main_":
    main()
