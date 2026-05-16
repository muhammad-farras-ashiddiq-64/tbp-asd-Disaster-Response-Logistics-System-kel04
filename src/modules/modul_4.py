# Modul 4: Log Riwayat Transaksi Distribusi via Stack (LIFO)
from src.data_structures.linked_list import LLNode

class StackLog:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = LLNode(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None: 
            return None
        target_data = self.top.data
        self.top = self.top.next
        return target_data

    def is_empty(self) -> bool:
        return self.top is None

    def to_list(self) -> list:
        hasil, curr = [], self.top
        while curr:
            hasil.append(curr.data)
            curr = curr.next
        return hasil
