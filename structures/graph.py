from typing import List, Dict, Tuple, Optional

class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class EdgeNode:
    def __init__(self, dest: str, jarak: int, kapasitas: int):
        self.dest      = dest
        self.jarak     = jarak
        self.kapasitas = kapasitas
        self.next      = None

class GraphRute:
    def __init__(self):
        self.adj: Dict[str, Optional[EdgeNode]] = {}

    def tambah_node(self, kode: str):
        if kode not in self.adj:
            self.adj[kode] = None

    def tambah_rute(self, u: str, v: str, jarak: int, kapasitas: int):
        self.tambah_node(u)
        self.tambah_node(v)

        node_uv       = EdgeNode(v, jarak, kapasitas)
        node_uv.next  = self.adj[u]
        self.adj[u]   = node_uv

        node_vu       = EdgeNode(u, jarak, kapasitas)
        node_vu.next  = self.adj[v]
        self.adj[v]   = node_vu

    def tetangga(self, u: str) -> List[Tuple[str, int, int]]:
        hasil = []
        curr  = self.adj.get(u)
        while curr:
            hasil.append((curr.dest, curr.jarak, curr.kapasitas))
            curr = curr.next
        return hasil

    def bfs_akses(self, depot: str) -> set:
        if depot not in self.adj:
            return set()

        visited  = {depot}
        q_head   = LLNode(depot)
        q_tail   = q_head

        while q_head is not None:
            curr_kode = q_head.data
            q_head    = q_head.next

            for (nbr, _, _) in self.tetangga(curr_kode):
                if nbr not in visited:
                    visited.add(nbr)
                    new_node   = LLNode(nbr)
                    q_tail.next = new_node
                    q_tail     = new_node

        return visited

def dijkstra_logistik(graph: GraphRute, depot: str):
    INF    = float('inf')
    dist   = {v: INF   for v in graph.adj}
    parent = {v: None  for v in graph.adj}
    dist[depot] = 0
    visited = set()

    for _ in range(len(graph.adj)):
        u = None
        for v in graph.adj:
            if v not in visited:
                if u is None or dist[v] < dist[u]:
                    u = v

        if u is None or dist[u] == INF:
            break

        visited.add(u)

        for (v, w, _) in graph.tetangga(u):
            if v not in visited and dist[u] + w < dist[v]:
                dist[v]   = dist[u] + w
                parent[v] = u

    return dist, parent

def rekonstruksi_jalur(parent: dict, sumber: str, tujuan: str) -> List[str]:
    jalur = []
    curr  = tujuan
    while curr is not None:
        jalur.append(curr)
        if curr == sumber:
            break
        curr = parent[curr]
    jalur.reverse()
    if not jalur or jalur[0] != sumber:
        return []
    return jalur
