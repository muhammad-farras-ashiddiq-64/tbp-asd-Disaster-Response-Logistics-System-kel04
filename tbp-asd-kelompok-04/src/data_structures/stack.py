# src/data_structures/stack.py

from data_structures.linked_list import LLNode

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        """Big-O O(1)"""
        new_node = LLNode(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Big-O O(1)"""
        if not self.top:
            return None
        popped_node = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_node

    def peek(self):
        return self.top.data if self.top else None

    def to_list(self):
        """Kembalikan list dari top ke bottom untuk keperluan logging"""
        result = []
        curr = self.top
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result
