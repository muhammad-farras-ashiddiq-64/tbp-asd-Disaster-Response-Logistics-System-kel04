# src/data_structures/queue_ll.py

from src.data_structures.linked_list import LLNode

class PriorityQueueBantuan:
    """
    Priority Queue berbasis Linked List untuk antrian pengiriman bantuan.
    Lokasi KRITIS (level=1) selalu dilayani lebih dulu.
    """
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, bantuan):
        """
        Big-O: O(n) insertion terurut prioritas.
        Menyisipkan bantuan ke dalam antrian berdasarkan tingkat urgensi level bencana (1 > 2 > 3).
        """
        new_node = LLNode(bantuan)
        
        # Kondisi 1: Antrian masih kosong ATAU bantuan baru memiliki prioritas lebih tinggi (angka level lebih kecil)
        if self.head is None or bantuan.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node
        else:
            # Kondisi 2: Cari posisi penyisipan yang tepat di tengah atau akhir antrian
            current = self.head
            while current.next is not None and current.next.data.prioritas <= bantuan.prioritas:
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            
        self._size += 1

    def dequeue(self):
        """
        Big-O: O(1)
        Mengambil sekaligus menghapus elemen bantuan terdepan yang paling prioritas.
        """
        if self.head is None:
            return None
        
        removed_node = self.head.data
        self.head = self.head.next  # Geser head ke simpul berikutnya
        self._size -= 1
        return removed_node

    def __len__(self):
        """Mengembalikan jumlah item di dalam antrian."""
        return self._size