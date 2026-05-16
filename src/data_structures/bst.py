from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Lokasi:
    kode: str
    nama: str
    level: int       # 1: KRITIS, 2: SEDANG, 3: RINGAN
    populasi: int

class BSTNodeLok:
    def __init__(self, lokasi: Lokasi):
        self.lokasi = lokasi
        self.left = self.right = None

class BSTLokasi:
    def __init__(self):
        self.root = None

    def insert(self, lokasi: Lokasi):
        self.root = self._insert(self.root, lokasi)

    def _insert(self, node, lokasi: Lokasi):
        if node is None: 
            return BSTNodeLok(lokasi)
        if lokasi.kode < node.lokasi.kode:
            node.left = self._insert(node.left, lokasi)
        elif lokasi.kode > node.lokasi.kode:
            node.right = self._insert(node.right, lokasi)
        else:
            node.lokasi = lokasi  # Update data jika kode sama
        return node

    def search(self, kode: str) -> Optional[BSTNodeLok]:
        return self._search(self.root, kode)

    def _search(self, node, kode: str):
        if node is None or node.lokasi.kode == kode: 
            return node
        if kode < node.lokasi.kode: 
            return self._search(node.left, kode)
        return self._search(node.right, kode)

    def inorder(self) -> List[Lokasi]:
        hasil: List[Lokasi] = []
        self._inorder(self.root, hasil)
        return hasil

    def _inorder(self, node, hasil: List[Lokasi]):
        if node:
            self._inorder(node.left, hasil)
            hasil.append(node.lokasi)
            self._inorder(node.right, hasil)
