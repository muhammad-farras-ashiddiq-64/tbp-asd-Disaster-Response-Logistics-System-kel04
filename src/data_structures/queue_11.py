from dataclasses import dataclass
from typing import Optional, List
from src.data_structures.linked_list import LLNode

@dataclass
class Bantuan:
    bantuan_id: int
    jenis: str
    jumlah: int
    asal: str
    tujuan: str
    prioritas: int  # 1: KRITIS, 2: SEDANG, 3: RINGAN

class PriorityQueueBantuan:
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, outbound_bantuan: Bantuan):
        node = LLNode(outbound_bantuan)
        self._size += 1

        # Jika antrean kosong atau prioritas lebih tinggi (angka level lebih kecil)
        if self.head is None or outbound_bantuan.prioritas < self.head.data.prioritas:
            node.next = self.head
            self.head = node
            return

        curr = self.head
        while curr.next is not None and curr.next.data.prioritas <= outbound_bantuan.prioritas:
            curr = curr.next

        node.next = curr.next
        curr.next = node

    def dequeue(self) -> Optional[Bantuan]:
        if self.head is None: 
            return None
        target_data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return target_data

    def is_empty(self) -> bool:
        return self.head is None

    def to_list(self) -> List[Bantuan]:
        result, curr = [], self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result
