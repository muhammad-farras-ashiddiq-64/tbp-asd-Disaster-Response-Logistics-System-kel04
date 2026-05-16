from structures.graph import LLNode

class Stack:
    def __init__(self):
        self.top   = None
        self._size = 0

    def push(self, data):
        node      = LLNode(data)
        node.next = self.top
        self.top  = node
        self._size += 1

    def pop(self):
        if self.top is None:
            return None
        data     = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def is_empty(self) -> bool:
        return self.top is None

    def __len__(self):
        return self._size

    def to_list(self) -> list:
        hasil, curr = [], self.top
        while curr:
            hasil.append(curr.data)
            curr = curr.next
        return hasil
