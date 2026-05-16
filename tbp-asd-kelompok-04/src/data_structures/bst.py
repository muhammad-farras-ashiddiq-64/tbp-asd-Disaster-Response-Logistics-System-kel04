class BSTNode:
    def __init__(self, kode, nama, level, populasi):
        self.kode = kode
        self.nama = nama
        self.level = level
        self.populasi = populasi
        self.status = "Menunggu"
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, kode, nama, level, populasi):
        def _insert(node, kode, nama, level, populasi):
            if not node:
                return BSTNode(kode, nama, level, populasi)
            if kode < node.kode:
                node.left = _insert(node.left, kode, nama, level, populasi)
            elif kode > node.kode:
                node.right = _insert(node.right, kode, nama, level, populasi)
            return node
        self.root = _insert(self.root, kode, nama, level, populasi)

    def search(self, kode):
        curr = self.root
        while curr:
            if kode == curr.kode: return curr
            curr = curr.left if kode < curr.kode else curr.right
        return None
