import numpy as np
import random
import time
from dataclasses import dataclass
from typing import Optional, List, Dict

np.random.seed(25)
random.seed(25)

# =========================================
# LEVEL PRIORITAS BENCANA
# =========================================

PRIORITAS_BENCANA = {
    'DARURAT': 1,
    'WASPADA': 2,
    'AMAN': 3
}

# =========================================
# JENIS LOGISTIK
# =========================================

JENIS_LOGISTIK = [
    'MAKANAN',
    'AIR_BERSIH',
    'OBAT_MEDIS',
    'PAKAIAN',
    'GENSET'
]

# =========================================
# DATA LOKASI BENCANA
# =========================================

@dataclass
class Wilayah:
    kode: str
    nama: str
    prioritas: int
    jumlah_pengungsi: int
    sudah_dibantu: bool = False

# =========================================
# DATA DISTRIBUSI LOGISTIK
# =========================================

@dataclass
class Logistik:
    logistik_id: int
    jenis: str
    stok: int
    gudang_asal: str
    lokasi_tujuan: str
    prioritas_kirim: int

# =========================================
# NODE UNTUK ADJACENCY LIST
# =========================================

class JalurNode:
    def __init__(self, tujuan, jarak, kapasitas):
        self.tujuan = tujuan
        self.jarak = jarak
        self.kapasitas = kapasitas
        self.next = None

# =========================================
# GRAPH SISTEM LOGISTIK
# =========================================

class GraphLogistik:

    def __init__(self):
        self.adjacent = {}
        self.daftar_lokasi = []

    # =====================================
    # MENAMBAHKAN LOKASI
    # =====================================

    def tambah_lokasi(self, nama):

        if nama not in self.adjacent:
            self.adjacent[nama] = None
            self.daftar_lokasi.append(nama)

    # =====================================
    # MENAMBAHKAN JALUR DISTRIBUSI
    # =====================================

    def tambah_jalur(self, asal, tujuan, jarak, kapasitas):

        self.tambah_lokasi(asal)
        self.tambah_lokasi(tujuan)

        # asal -> tujuan
        node_baru = JalurNode(
            tujuan,
            jarak,
            kapasitas
        )

        node_baru.next = self.adjacent[asal]
        self.adjacent[asal] = node_baru

        # tujuan -> asal
        node_balik = JalurNode(
            asal,
            jarak,
            kapasitas
        )

        node_balik.next = self.adjacent[tujuan]
        self.adjacent[tujuan] = node_balik

    # =====================================
    # MENAMPILKAN JALUR
    # =====================================

    def tampilkan_jalur(self):

        for lokasi in self.adjacent:

            print(f"\n{lokasi}")

            curr = self.adjacent[lokasi]

            while curr:

                print(
                    f" -> {curr.tujuan} "
                    f"(Jarak: {curr.jarak} km, "
                    f"Kapasitas: {curr.kapasitas})"
                )

                curr = curr.next

# =========================================
# SIMULASI DATA
# =========================================

wilayah_1 = Wilayah(
    "W01",
    "Desa Harapan",
    PRIORITAS_BENCANA['DARURAT'],
    1500
)

wilayah_2 = Wilayah(
    "W02",
    "Posko Utama",
    PRIORITAS_BENCANA['WASPADA'],
    700
)

logistik_1 = Logistik(
    101,
    "MAKANAN",
    300,
    "Gudang Pusat",
    "Desa Harapan",
    1
)

# =========================================
# MEMBUAT GRAPH
# =========================================

graph = GraphLogistik()

graph.tambah_jalur(
    "Gudang Pusat",
    "Posko Utama",
    10,
    100
)

graph.tambah_jalur(
    "Posko Utama",
    "Desa Harapan",
    7,
    60
)

graph.tambah_jalur(
    "Gudang Pusat",
    "Rumah Sakit",
    12,
    80
)

# =========================================
# OUTPUT
# =========================================

print("=== SISTEM LOGISTIK TANGGAP BENCANA ===")

print("\nData Wilayah:")
print(wilayah_1)
print(wilayah_2)

print("\nData Logistik:")
print(logistik_1)

print("\nJalur Distribusi:")
graph.tampilkan_jalur()
