from src.models import Bantuan, LLNode

class PriorityQueueBantuan: 
    """Lokasi KRITIS (level=1) selalu dilayani lebih dulu.""" 
    def __init__(self): 
        self.head = None 
        self._size = 0 

    def enqueue(self, bantuan: Bantuan): 
        """Big-O: O(n) insertion terurut prioritas angka terkecil (1=Kritis, dst).""" 
        new_node = LLNode(bantuan)
        self._size += 1
        
        if self.head is None or bantuan.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None and current.next.data.prioritas <= bantuan.prioritas:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    def dequeue(self): 
        """Big-O: O(1). Ambil dari head.""" 
        if self.head is None:
            return None
        temp = self.head.data
        self.head = self.head.next
        self._size -= 1
        return temp

    def __len__(self): 
        return self._size
