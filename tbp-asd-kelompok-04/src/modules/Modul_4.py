import numpy as np
import time
import random
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple

np.random.seed(47)
random.seed(47)

LEVEL_BENCANA = {
    'KRITIS': 1,
    'SEDANG': 2,
    'RINGAN': 3
}

JENIS_BANTUAN = [
    'MAKANAN',
    'AIR',
    'OBAT',
    'SELIMUT',
    'TENDA'
]


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

class Node:
    def __init__(
        self,
        depot,
        lokasi,
        jenis,
        jumlah
    ):
        self.depot = depot
        self.lokasi = lokasi
        self.jenis = jenis
        self.jumlah = jumlah
        self.next = None
class StackLogPengiriman:
    def __init__(self):
        self.top = None
    """
    PUSH
    Menyimpan transaksi pengiriman terbaru
    Big-O : O(1)
    """
    def tambah_log(
        self,
        depot,
        lokasi,
        jenis,
        jumlah
    ):

        node_baru = Node(
            depot,
            lokasi,
            jenis,
            jumlah
        )

        node_baru.next = self.top

        self.top = node_baru

        print("\nLog pengiriman berhasil disimpan")


    """
    POP / ROLLBACK
    Membatalkan pengiriman terakhir

    Big-O : O(1)
    """

    def rollback(self):

        if self.top is None:

            print("\nTidak ada pengiriman yang dapat dibatalkan")
            return


        batal = self.top

        self.top = self.top.next


        print("\n===================================")
        print("      ROLLBACK PENGIRIMAN")
        print("===================================")

        print("Depot           :", batal.depot)
        print("Lokasi          :", batal.lokasi)
        print("Jenis Bantuan   :", batal.jenis)
        print("Jumlah Bantuan  :", batal.jumlah)

        print("-----------------------------------")
        print("Status          : DIBATALKAN")
        print("Stok kembali ke depot")
        print("===================================")


    """
    LOG_PENGIRIMAN
    Menampilkan seluruh riwayat pengiriman

    Big-O : O(n)
    """

    def tampilkan_log(self):

        if self.top is None:

            print("\nBelum ada riwayat pengiriman")
            return


        current = self.top

        nomor = 1


        print("\n===================================")
        print("         LOG PENGIRIMAN")
        print("===================================")


        while current is not None:

            print("Riwayat Ke-", nomor)
            print("Depot          :", current.depot)
            print("Lokasi         :", current.lokasi)
            print("Jenis Bantuan  :", current.jenis)
            print("Jumlah         :", current.jumlah)

            print("-----------------------------------")

            current = current.next

            nomor += 1


stack = StackLogPengiriman()


while True:

    print("\n===================================")
    print("     STACK LOG PENGIRIMAN")
    print("===================================")

    print("1. TAMBAH_LOG")
    print("2. LOG_PENGIRIMAN")
    print("3. ROLLBACK")
    print("4. KELUAR")

    pilihan = input("Pilih menu : ")


    if pilihan == "1":

        depot = input("Masukkan depot asal   : ")

        lokasi = input("Masukkan lokasi tujuan: ")

        jenis = input("Masukkan jenis bantuan: ")

        jumlah = int(
            input("Masukkan jumlah bantuan: ")
        )


        stack.tambah_log(
            depot,
            lokasi,
            jenis,
            jumlah
        )


    elif pilihan == "2":

        stack.tampilkan_log()


    elif pilihan == "3":

        stack.rollback()


    elif pilihan == "4":

        print("\nProgram selesai")
        break


    else:

        print("\nMenu tidak tersedia")
