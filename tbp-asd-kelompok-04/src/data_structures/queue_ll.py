class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class PriorityQueueBantuan:
    """
    Prioritas kecil = lebih penting
    """

    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, bantuan):
        new_node = LLNode(bantuan)

        if not self.head or bantuan.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head

            while (
                current.next and
                current.next.data.prioritas <= bantuan.prioritas
            ):
                current = current.next

            new_node.next = current.next
            current.next = new_node

        self._size += 1

    def dequeue(self):
        if not self.head:
            return None

        data = self.head.data
        self.head = self.head.next
        self._size -= 1

        return data

    def __len__(self):
        return self._size
