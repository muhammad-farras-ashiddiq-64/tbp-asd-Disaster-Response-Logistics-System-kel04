# src/data_structures/queue_ll.py

from data_structures.linked_list import LLNode

class PriorityQueueBantuan:
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, outbound_bantuan):
        """Memasukkan data secara terurut berdasarkan prioritas. 
        Angka prioritas lebih kecil (1 = Kritis) akan ditaruh di depan."""
        new_node = LLNode(outbound_bantuan)
        self._size += 1
        
        # Kasus 1: Antrean masih kosong ATAU data baru memiliki prioritas lebih tinggi dari head
        if not self.head or outbound_bantuan.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node
            return

        # Kasus 2: Cari posisi penyisipan di tengah atau akhir antrean
        curr = self.head
        while curr.next and curr.next.data.prioritas <= outbound_bantuan.prioritas:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def dequeue(self):
        """Mengambil data terdepan (Prioritas Tertinggi) -> O(1)"""
        if not self.head:
            return None
        temp = self.head.data
        self.head = self.head.next
        self._size -= 1
        return temp

    def __len__(self):
        return self._size
