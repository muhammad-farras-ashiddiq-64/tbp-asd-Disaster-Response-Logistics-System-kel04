class BSTNodeLok:
    def __init__(self, lokasi):
        self.lokasi = lokasi
        self.left = None
        self.right = None


class BSTLokasi:
    def __init__(self):
        self.root = None

    def insert(self, lokasi):
        """Big-O: O(log n). Kunci = lokasi.kode."""

        def _insert(node, lokasi):
            if node is None:
                return BSTNodeLok(lokasi)

            if lokasi.kode < node.lokasi.kode:
                node.left = _insert(node.left, lokasi)

            elif lokasi.kode > node.lokasi.kode:
                node.right = _insert(node.right, lokasi)

            return node

        self.root = _insert(self.root, lokasi)

    def search(self, kode):
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

    def inorder(self):
        """Big-O: O(n)."""

        hasil = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                hasil.append(node.lokasi)
                _inorder(node.right)

        _inorder(self.root)
        return hasil


class EdgeNode:
    def __init__(self, dest, jarak, kapasitas):
        self.dest = dest
        self.jarak = jarak
        self.kapasitas = kapasitas
        self.next = None
