import sys
import os

# Memastikan Python mendeteksi folder internal root src/
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_structures.graph import Graph
from data_structures.queue_ll import PriorityQueue
from data_structures.bst import BST
from data_structures.stack import Stack
from modules.modul_1 import temukan_lokasi_terisolasi
from modules.modul_2 import hitung_dijkstra

# Inisialisasi Database Sistem
peta = Graph()
antrean_triage = PriorityQueue()
registri = BST()
riwayat_log = Stack()
DEPOT = "DEPOT_PUSAT"

peta.tambah_node(DEPOT)

def main():
    while True:
        print("\n========================================")
        print(" URBAN FOOD SUPPLY CHAIN & LOGISTIC ")
        print("========================================")
        print("1. KIRIM BANTUAN (Enqueue)")
        print("2. PROSES BANTUAN (Dequeue)")
        print("3. RUTE OPTIMAL (Dijkstra)")
        print("4. TIDAK TERJANGKAU (BFS)")
        print("5. LOG PENGIRIMAN & ROLLBACK")
        print("6. KELUAR")
        
        pilihan = input("Pilih menu [1-6]: ")
        
        if pilihan == "1":
            kode = input("Masukkan Kode Wilayah (ex: L01): ")
            nama = input("Masukkan Nama Wilayah: ")
            level = int(input("Tingkat Urgensi (1:Kritis, 2:Sedang, 3:Ringan): "))
            populasi = int(input("Jumlah Populasi: "))
            jarak = int(input(f"Jarak akses jalan dari {DEPOT} (km): "))
            
            registri.insert(kode, nama, level, populasi)
            peta.tambah_rute(DEPOT, nama, jarak)
            antrean_triage.enqueue({"kode": kode, "nama": nama, "level": level}, level)
            print(f"✓ Data Wilayah {nama} berhasil masuk antrean prioritas {level}.")
            
        elif pilihan == "2":
            bantuan = antrean_triage.dequeue()
            if not bantuan:
                print("! Antrean kosong.")
            else:
                riwayat_log.push(bantuan)
                node_bst = registri.search(bantuan['kode'])
                if node_bst: node_bst.status = "Sedang Dikirim"
                print(f"▶ Truk diberangkatkan menuju {bantuan['nama']} (Level {bantuan['level']}).")
                
        elif pilihan == "3":
            tujuan = input("Masukkan nama wilayah tujuan: ")
            if tujuan not in peta.nodes:
                print("! Wilayah tidak ditemukan.")
            else:
                hasil_jarak = hitung_dijkstra(peta, DEPOT)
                print(f"Rute terpendek ke {tujuan} adalah {hasil_jarak[tujuan]} km.")
                
        elif pilihan == "4":
            isolasi = temukan_lokasi_terisolasi(peta, DEPOT)
            print(f"Lokasi terisolasi dari pusat: {isolasi if isolasi else 'Tidak ada'}")
            
        elif pilihan == "5":
            print("a. Lihat Riwayat Log")
            print("b. Batalkan Transaksi Terakhir (Rollback)")
            opt = input("Pilih [a/b]: ")
            if opt == "a":
                curr = riwayat_log.top
                while curr:
                    print(f"[-] Terdistribusi ke: {curr.data['nama']}")
                    curr = curr.next
            elif opt == "b":
                batal = riwayat_log.pop()
                if batal:
                    antrean_triage.enqueue(batal, batal['level'])
                    print(f"✓ Transaksi logistik ke {batal['nama']} berhasil di-rollback!")
                    
        elif pilihan == "6":
            print("Sistem dimatikan. Terima kasih.")
            break

if __name__ == "__main__":
    main()
