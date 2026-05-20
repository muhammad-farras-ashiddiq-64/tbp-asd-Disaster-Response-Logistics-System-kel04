from typing import Optional, List
from src.models import Lokasi

class BSTNodeLok: 
    def __init__(self, lokasi): 
        self.lokasi = lokasi 
        self.left = self.right = None 

class BSTLokasi: 
    def __init__(self): 
        self.root = None 

    def insert(self, lokasi): 
        """Big-O: O(log n). Kunci = lokasi.kode.""" 
        new_node = BSTNodeLok(lokasi)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if lokasi.kode < current.lokasi.kode:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            elif lokasi.kode > current.lokasi.kode:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            else:
                current.lokasi = lokasi  
                break

    def search(self, kode) -> Optional[Lokasi]: 
        """Big-O: O(log n).""" 
        current = self.root
        while current:
            if kode == current.lokasi.kode:
                return current.lokasi
            elif kode < current.lokasi.kode:
                current = current.left
            else:
                current = current.right
        return None

    def update_level(self, kode, level): 
        """Big-O: O(log n).""" 
        lokasi = self.search(kode)
        if lokasi:
            lokasi.level = level
            return True
        return False

    def inorder(self) -> List[Lokasi]: 
        """Big-O: O(n).""" 
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.lokasi)
                _inorder(node.right)
        _inorder(self.root)
        return result
