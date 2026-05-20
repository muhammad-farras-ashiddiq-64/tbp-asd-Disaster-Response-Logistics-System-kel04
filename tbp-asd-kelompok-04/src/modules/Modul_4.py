from src.models import LLNode

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
        if self.top is None:
            return None
        temp = self.top.data
        self.top = self.top.next
        self._size -= 1
        return temp

    def peek(self): 
        return self.top.data if self.top else None 

    def to_list(self): 
        """Kembalikan list dari top ke bottom"""
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result
