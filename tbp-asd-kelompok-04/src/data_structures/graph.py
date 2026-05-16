# src/data_structures/graph.py

class NodeLink:
    def __init__(self, tujuan, bobot_km):
        self.tujuan = tujuan
        self.bobot = bobot_km
        self.next = None

class AdjList:
    def __init__(self):
        self.head = None

    def insert(self, tujuan, bobot):
        new_node = NodeLink(tujuan, bobot)
        new_node.next = self.head
        self.head = new_node

class Graph:
    def __init__(self):
        self.adj_lists = {}  # Map dari nama_node ke objek AdjList
        self.nodes = []

    def tambah_node(self, nama):
        if nama not in self.adj_lists:
            self.adj_lists[nama] = AdjList()
            self.nodes.append(nama)

    def tambah_rute(self, u, v, jarak):
        # Graf tidak berarah, tambahkan kedua sisi
        self.tambah_node(u)
        self.tambah_node(v)
        self.adj_lists[u].insert(v, jarak)
        self.adj_lists[v].insert(u, jarak)

    def tetangga(self, nama):
        list_tetangga = []
        curr = self.adj_lists[nama].head
        while curr:
            list_tetangga.append((curr.tujuan, curr.bobot))
            curr = curr.next
        return list_tetangga

    def bfs_isolasi(self, start_node):
        """Mendeteksi lokasi tidak terjangkau dari depot"""
        visited = set()
        queue = [start_node]
        visited.add(start_node)

        while queue:
            curr = queue.pop(0)
            for tetangga, _ in self.tetangga(curr):
                if tetangga not in visited:
                    visited.add(tetangga)
                    queue.append(tetangga)
        
        # Lokasi tidak terjangkau = semua node graf minus yang berhasil dikunjungi
        tidak_terjangkau = [node for node in self.nodes if node not in visited]
        return tidak_terjangkau
