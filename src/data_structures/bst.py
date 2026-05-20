# src/data_structures/bst.py

class BSTNodeLok:
    def __init__(self, lokasi):
        self.lokasi = lokasi
        self.left = None
        self.right = None

class BSTLokasi:
    def __init__(self):
        self.root = None

    def insert(self, lokasi):
        """Big-O: O(log n). Kunci = lokasi.kode"""
        new_node = BSTNodeLok(lokasi)
        if not self.root:
            self.root = new_node
            return
        
        curr = self.root
        while True:
            if lokasi.kode < curr.lokasi.kode:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left
            elif lokasi.kode > curr.lokasi.kode:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right
            else:
                curr.lokasi = lokasi  # Update jika kode sudah ada
                break

    def search(self, kode):
        """Big-O: O(log n)"""
        curr = self.root
        while curr:
            if kode == curr.lokasi.kode:
                return curr.lokasi
            curr = curr.left if kode < curr.lokasi.kode else curr.right
        return None

    def update_level(self, kode, level):
        """Big-O: O(log n)"""
        lokasi = self.search(kode)
        if lokasi:
            lokasi.level = level
            return True
        return False

    def inorder(self):
        """Big-O: O(n)"""
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.lokasi)
                _inorder(node.right)
        _inorder(self.root)
        return result
