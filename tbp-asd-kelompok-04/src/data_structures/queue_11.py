# src/data_structures/queue_ll.py

from data_structures.linked_list import LLNode

class PriorityQueueBantuan:
    """Lokasi KRITIS (level=1) selalu dilayani lebih dulu."""
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, outbound_bantuan):
        """Big-O: O(n) insertion terurut prioritas."""
        new_node = LLNode(outbound_bantuan)
        self._size += 1
        
        # Urutkan berdasarkan prioritas terkecil (nilai prioritas int rendah = utama)
        if not self.head or outbound_bantuan.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        while curr.next and curr.next.data.prioritas <= outbound_bantuan.prioritas:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def dequeue(self):
        """Big-O: O(1)"""
        if not self.head:
            return None
        temp = self.head.data
        self.head = self.head.next
        self._size -= 1
        return temp

    def __len__(self):
        return self._size
