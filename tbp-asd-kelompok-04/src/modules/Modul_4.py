from src.data_structures.linked_list import LLNode

class StackLogPengiriman:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        """
        PUSH: Menyimpan transaksi objek pengiriman logistik terbaru.
        Big-O : O(1)
        """
        node_baru = LLNode(data)
        node_baru.next = self.top
        self.top = node_baru
        self._size += 1
        print("\n✔ Log pengiriman berhasil disimpan ke dalam Stack.")

    def pop(self):
        """
        POP / ROLLBACK: Membatalkan pengiriman terakhir (LIFO).
        Big-O : O(1)
        """
        if self.top is None:
            print("\n Tidak ada transaksi pengiriman yang dapat dibatalkan (Stack Kosong).")
            return None

        batal = self.top.data
        self.top = self.top.next
        self._size -= 1

        print("\n===================================")
        print("        ROLLBACK PENGIRIMAN")
        print("===================================")
        print("Bantuan ID      :", getattr(batal, 'bantuan_id', '-'))
        print("Depot Asal      :", getattr(batal, 'asal', '-'))
        print("Lokasi Tujuan   :", getattr(batal, 'tujuan', '-'))
        print("Jenis Bantuan   :", getattr(batal, 'jenis', '-'))
        print("Jumlah Bantuan  :", getattr(batal, 'jumlah', '-'))
        print("-----------------------------------")
        print("Status          : DIBATALKAN (ROLLBACK)")
        print("Keterangan      : Stok dikembalikan ke Depot asal.")
        print("===================================")
        
        return batal

    def to_list(self):
        """
        Mengonversi rantai pointer menjadi list Python standar untuk visualisasi.
        Big-O : O(n)
        """
        result = []
        current = self.top
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def tampilkan_log(self):
        """
        LOG_PENGIRIMAN: Menampilkan seluruh riwayat dari Top ke Bottom.
        Big-O : O(n)
        """
        if self.top is None:
            print("\n Belum ada riwayat transaksi distribusi logistik.")
            return

        current = self.top
        nomor = 1

        print("\n===================================")
        print("          LOG PENGIRIMAN")
        print("===================================")
        while current is not None:
            log_data = current.data
            print(f"Riwayat Ke-{nomor}")
            print("Bantuan ID     :", getattr(log_data, 'bantuan_id', '-'))
            print("Depot Asal     :", getattr(log_data, 'asal', '-'))
            print("Lokasi Tujuan  :", getattr(log_data, 'tujuan', '-'))
            print("Jenis Bantuan  :", getattr(log_data, 'jenis', '-'))
            print("Jumlah         :", getattr(log_data, 'jumlah', '-'))
            print("-----------------------------------")
            current = current.next
            nomor += 1

    def __len__(self):
        return self._size
