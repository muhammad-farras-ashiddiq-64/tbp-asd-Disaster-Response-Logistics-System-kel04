class Node:
    def __init__(self, depot, lokasi, jenis, jumlah, level):

        self.depot = depot
        self.lokasi = lokasi
        self.jenis = jenis
        self.jumlah = jumlah
        self.level = level

        self.next = None


class PriorityQueue:

    def __init__(self):

        self.head = None


    # Big-O : O(n)
    def kirim(self, depot, lokasi, jenis, jumlah, level):

        node_baru = Node(
            depot,
            lokasi,
            jenis,
            jumlah,
            level
        )

        if self.head is None:

            self.head = node_baru

            print("\nBantuan berhasil masuk antrian")
            return


        if level < self.head.level:

            node_baru.next = self.head

            self.head = node_baru

            print("\nBantuan prioritas tinggi masuk")
            return


        current = self.head

        while (
            current.next is not None
            and current.next.level <= level
        ):

            current = current.next


        node_baru.next = current.next

        current.next = node_baru

        print("\nBantuan berhasil masuk antrian")


    # Big-O : O(1)
    def proses_bantuan(self):

        if self.head is None:

            print("\nAntrian bantuan kosong")
            return


        bantuan = self.head

        self.head = self.head.next


        print("\n===================================")
        print(" DISTRIBUSI BANTUAN KOTA YOGYAKARTA ")
        print("===================================")

        print("Depot Asal       :", bantuan.depot)
        print("Lokasi Tujuan    :", bantuan.lokasi)
        print("Jenis Bantuan    :", bantuan.jenis)
        print("Jumlah Bantuan   :", bantuan.jumlah)


        if bantuan.level == 1:

            status = "KRITIS"

        elif bantuan.level == 2:

            status = "SIAGA"

        else:

            status = "AMAN"


        print("Level Bencana    :", bantuan.level)
        print("Status Lokasi    :", status)

        print("-----------------------------------")
        print("Status Pengiriman : BERHASIL")
        print("Bantuan sedang dikirim...")
        print("===================================")


    # Big-O : O(n)
    def tampilkan_antrian(self):

        if self.head is None:

            print("\nAntrian kosong")
            return


        current = self.head

        nomor = 1

        print("\n===================================")
        print(" ANTRIAN BANTUAN YOGYAKARTA ")
        print("===================================")

        while current is not None:

            print("Antrian Ke-", nomor)
            print("Depot     :", current.depot)
            print("Lokasi    :", current.lokasi)
            print("Jenis     :", current.jenis)
            print("Jumlah    :", current.jumlah)
            print("Level     :", current.level)
            print("-----------------------------------")

            current = current.next

            nomor += 1


queue = PriorityQueue()


while True:

    print("\n===================================")
    print(" DISASTER RESPONSE YOGYAKARTA ")
    print("===================================")
    print("1. KIRIM")
    print("2. PROSES_BANTUAN")
    print("3. TAMPILKAN_ANTRIAN")
    print("4. KELUAR")

    pilihan = input("Pilih menu : ")


    if pilihan == "1":

        print("\nDaftar Lokasi Yogyakarta")
        print("- Kota Yogyakarta")
        print("- Sleman")
        print("- Bantul")
        print("- Kulon Progo")
        print("- Gunungkidul")

        depot = input("\nMasukkan depot asal   : ")

        lokasi = input("Masukkan lokasi tujuan: ")

        jenis = input("Masukkan jenis bantuan: ")

        jumlah = int(input("Masukkan jumlah       : "))

        print("\nLEVEL BENCANA")
        print("1 = KRITIS")
        print("2 = SIAGA")
        print("3 = AMAN")

        level = int(input("Masukkan level : "))


        queue.kirim(
            depot,
            lokasi,
            jenis,
            jumlah,
            level
        )


    elif pilihan == "2":

        queue.proses_bantuan()


    elif pilihan == "3":

        queue.tampilkan_antrian()


    elif pilihan == "4":

        print("\nProgram selesai")
        break


    else:

        print("\nMenu tidak tersedia")
