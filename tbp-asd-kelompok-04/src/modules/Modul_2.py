class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    # O(1)
    def enqueue(self, data):

        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    # O(1)
    def dequeue(self):

        if self.front is None:
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1

        return temp.data

    # O(1)
    def peek(self):

        if self.front:
            return self.front.data

        return None

    # O(1)
    def is_empty(self):
        return self.front is None

    # O(1)
    def __len__(self):
        return self.size

    # O(n)
    def to_list(self):

        result = []
        current = self.front

        while current:
            result.append(current.data)
            current = current.next

        return result
