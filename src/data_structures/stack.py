from typing import Any, List
from src.data_structures.linked_list import LLNode

class StackLog:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data: Any):
        node = LLNode(data)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self) -> Any:
        if self.top is None: 
            return None
        target_data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return target_data

    def is_empty(self) -> bool:
        return self.top is None

    def to_list(self) -> List[Any]:
        hasil, curr = [], self.top
        while curr:
            hasil.append(curr.data)
            curr = curr.next
        return hasil
