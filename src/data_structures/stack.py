# Tugas: Restu Pamungkas (25051030080)
from src.data_structures.linked_list import LLNode

class Stack:
    """Stack Log Pengiriman untuk menampung riwayat transaksi (LIFO)."""
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        """Big-O: O(1) - Menambahkan riwayat ke atas stack."""
        new_node = LLNode(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Big-O: O(1) - Mengambil log paling terakhir (untuk keperluan ROLLBACK)."""
        if self.top is None:
            return None
        popped = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped

    def to_list(self):
        """Big-O: O(n) - Mengonversi log ke bentuk list python standard untuk iterasi eksternal."""
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result
        
    def __len__(self):
        return self._size
