class QueueNode:
    def __init__(self, data, prioritas):
        self.data = data
        self.prioritas = prioritas  # Angka lebih kecil = prioritas lebih tinggi (Level 1)
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, data, prioritas):
        new_node = QueueNode(data, prioritas)
        if not self.head or prioritas < self.head.prioritas:
            new_node.next = self.head
            self.head = new_node
            return
        
        curr = self.head
        while curr.next and curr.next.prioritas <= prioritas:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def dequeue(self):
        if not self.head:
            return None
        temp = self.head.data
        self.head = self.head.next
        return temp
