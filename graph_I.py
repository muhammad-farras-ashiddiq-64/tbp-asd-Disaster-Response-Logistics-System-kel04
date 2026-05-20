# src/data_structures/graph.py

class EdgeNode:
    def __init__(self, dest, jarak, kapasitas):
        self.dest = dest
        self.jarak = jarak
        self.kapasitas = kapasitas
        self.next = None

class GraphRute:
    def __init__(self):
        self.adj = {}

    def tambah_node(self, kode):
        """Big-O: O(1)"""
        if kode not in self.adj:
            self.adj[kode] = None

    def tambah_rute(self, u, v, jarak, kapasitas):
        """Big-O: O(1). Graf Tidak Berarah (Sesuai deskripsi Tugas Esai)"""
        self.tambah_node(u)
        self.tambah_node(v)
        
        # Jalur u -> v
        node_uv = EdgeNode(v, jarak, kapasitas)
        node_uv.next = self.adj[u]
        self.adj[u] = node_uv
        
        # Jalur v -> u
        node_vu = EdgeNode(u, jarak, kapasitas)
        node_vu.next = self.adj[v]
        self.adj[v] = node_vu

    def tetangga(self, u):
        """Big-O: O(deg(u))"""
        nodes = []
        curr = self.adj.get(u, None)
        while curr:
            nodes.append((curr.dest, curr.jarak, curr.kapasitas))
            curr = curr.next
        return nodes

    def bfs_akses(self, depot):
        """BFS dari depot menghasilkan himpunan lokasi yang dapat dijangkau. Big-O: O(V+E)"""
        visited = set()
        if depot not in self.adj:
            return visited
            
        queue = [depot]
        visited.add(depot)
        
        while queue:
            curr = queue.pop(0)
            edge = self.adj.get(curr, None)
            while edge:
                if edge.dest not in visited:
                    visited.add(edge.dest)
                    queue.append(edge.dest)
                edge = edge.next
        return visited
