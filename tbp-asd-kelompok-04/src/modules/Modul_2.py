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

# src/data_structures/queue_ll.py

from data_structures.linked_list import LLNode

class PriorityQueueBantuan:
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, outbound_bantuan):
        """
        KIRIM: Menambahkan bantuan secara terurut ke dalam linked list.
        Kompleksitas: O(n)
        """
        new_node = LLNode(outbound_bantuan)
        self._size += 1
        
        # KONDISI 1: Antrean kosong atau bantuan baru memiliki prioritas lebih tinggi (angka lebih kecil) dari head
        if not self.head or outbound_bantuan.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node
            return

        # KONDISI 2: Cari posisi penyisipan di tengah atau di ujung akhir (O(n) traversal)
        curr = self.head
        while curr.next and curr.next.data.prioritas <= outbound_bantuan.prioritas:
            curr = curr.next
            
        new_node.next = curr.next
        curr.next = new_node

    def dequeue(self):
        """
        PROSES_BANTUAN: Mengambil armada logistik urutan terdepan.
        Kompleksitas: O(1)
        """
        if not self.head:
            return None
            
        temp_data = self.head.data
        self.head = self.head.next  # Geser pointer head ke belakang
        self._size -= 1
        return temp_data

    def __len__(self):
        return self._size
