from typing import List, Dict, Tuple, Optional
from src.data_structures.linked_list import LLNode

class EdgeNode:
    def __init__(self, dest: str, jarak: int):
        self.dest = dest
        self.jarak = jarak
        self.next = None

class GraphRute:
    def __init__(self):
        self.adj: Dict[str, Optional[EdgeNode]] = {}

    def tambah_node(self, kode: str):
        if kode not in self.adj:
            self.adj[kode] = None

    def tambah_rute(self, u: str, v: str, jarak: int):
        self.tambah_node(u)
        self.tambah_node(v)
        
        # Graf Tidak Berarah (Saling terhubung dua arah)
        node_uv = EdgeNode(v, jarak)
        node_uv.next = self.adj[u]
        self.adj[u] = node_uv

        node_vu = EdgeNode(u, jarak)
        node_vu.next = self.adj[v]
        self.adj[v] = node_vu

    def tetangga(self, u: str) -> List[Tuple[str, int]]:
        hasil = []
        curr = self.adj.get(u)
        while curr:
            hasil.append((curr.dest, curr.jarak))
            curr = curr.next
        return hasil

    def bfs_akses(self, depot: str) -> set:
        """Mendeteksi seluruh node yang dapat dijangkau dari depot tertentu."""
        if depot not in self.adj: 
            return set()
        visited = {depot}
        q_head = LLNode(depot)
        q_tail = q_head

        while q_head is not None:
            curr_kode = q_head.data
            q_head = q_head.next
            for (nbr, _) in self.tetangga(curr_kode):
                if nbr not in visited:
                    visited.add(nbr)
                    new_node = LLNode(nbr)
                    q_tail.next = new_node
                    q_tail = new_node
        return visited
