from dataclasses import dataclass
from typing import Optional, List
from structures.graph import LLNode

@dataclass
class Bantuan:
    bantuan_id: int
    jenis: str
    jumlah: int
    asal: str
    tujuan: str
    prioritas: int

class PriorityQueueBantuan:
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, bantuan: Bantuan):
        node = LLNode(bantuan)
        self._size += 1

        if self.head is None or bantuan.prioritas < self.head.data.prioritas:
            node.next = self.head
            self.head = node
            return

        curr = self.head
        while curr.next is not None and curr.next.data.prioritas <= bantuan.prioritas:
            curr = curr.next

        node.next = curr.next
        curr.next = node

    def dequeue(self) -> Optional[Bantuan]:
        if self.head is None:
            return None
        data      = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data

    def is_empty(self) -> bool:
        return self.head is None

    def __len__(self):
        return self._size

    def tampil(self) -> List[Bantuan]:
        hasil, curr = [], self.head
        while curr:
            hasil.append(curr.data)
            curr = curr.next
        return hasil
