from src.datastructures.bst import BSTLokasi
from src.datastructures.graph import GraphRute
from src.datastructures.priority_queue import PriorityQueueBantuan
from src.datastructures.stack import Stack

from src.modules.models import Bantuan
from src.modules.generator import generate_peta_bencana
from src.modules.dijkstra import dijkstra_logistik


def main():

    bst_lokasi = BSTLokasi()
    graph = GraphRute()

    antrian_bantuan = PriorityQueueBantuan()
    log_kirim = Stack()

    bantuan_counter = 1

    lokasi_list, edges = generate_peta_bencana()

    for lok in lokasi_list:
        bst_lokasi.insert(lok)
        graph.tambah_node(lok.kode)

    for u, v, j, k in edges:
        graph.tambah_rute(u, v, j, k)

    print("=== Disaster Response Logistics System ===")

    while True:

        print("\n1. KIRIM")
        print("2. PROSES_BANTUAN")
        print("3. RUTE_OPTIMAL")
        print("4. LOG_PENGIRIMAN")
        print("5. KELUAR")

        pilih = input("Pilih: ")

        if pilih == "1":

            tujuan = input("Tujuan: ")

            lokasi = bst_lokasi.search(tujuan)

            if not lokasi:
                print("Lokasi tidak ditemukan")
                continue

            bantuan = Bantuan(
                bantuan_counter,
                "MAKANAN",
                100,
                "DEPOT_0",
                tujuan,
                lokasi.level
            )

            bantuan_counter += 1

            antrian_bantuan.enqueue(bantuan)

            print("Bantuan masuk antrian")

        elif pilih == "2":

            bantuan = antrian_bantuan.dequeue()

            if not bantuan:
                print("Antrian kosong")
                continue

            print("Diproses:", bantuan)

            log_kirim.push(bantuan)

        elif pilih == "3":

            depot = input("Depot: ")

            dist, parent = dijkstra_logistik(graph, depot)

            tujuan = input("Tujuan: ")

            print("Jarak optimal:", dist.get(tujuan))

        elif pilih == "4":

            logs = log_kirim.to_list()

            for l in logs:
                print(l)

        elif pilih == "5":
            break

        else:
            print("Menu tidak valid")


if __name__ == "__main__":
    main()
