from typing import List, Tuple, Dict
from src.models import LLNode

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
        """Big-O: O(1).""" 
        if kode not in self.adj:
            self.adj[kode] = None 

    def tambah_rute(self, u, v, jarak, kapasitas): 
        """Big-O: O(1). Graf tidak berarah.""" 
        self.tambah_node(u)
        self.tambah_node(v)
        
        node_v = EdgeNode(v, jarak, kapasitas)
        node_v.next = self.adj[u]
        self.adj[u] = node_v
        
        node_u = EdgeNode(u, jarak, kapasitas)
        node_u.next = self.adj[v]
        self.adj[v] = node_u

    def tetangga(self, u) -> List[Tuple[str, int, int]]: 
        """Big-O: O(deg).""" 
        result = []
        current = self.adj.get(u, None)
        while current:
            result.append((current.dest, current.jarak, current.kapasitas))
            current = current.next
        return result

    def bfs_akses(self, depot) -> set: 
        """BFS dari depot menggunakan antrian manual. Big-O: O(V+E).""" 
        visited = set()
        if depot not in self.adj:
            return visited
            
        head = tail = LLNode(depot)
        visited.add(depot)
        
        while head:
            curr_node = head.data
            head = head.next
            if head is None:
                tail = None
                
            current_edge = self.adj.get(curr_node, None)
            while current_edge:
                if current_edge.dest not in visited:
                    visited.add(current_edge.dest)
                    new_queue_node = LLNode(current_edge.dest)
                    if tail is None:
                        head = tail = new_queue_node
                    else:
                        tail.next = new_queue_node
                        tail = new_queue_node
                current_edge = current_edge.next
        return visited

def dijkstra_logistik(graph: GraphRute, depot: str) -> Tuple[Dict[str, float], Dict[str, str]]: 
    """Shortest path dari depot. Big-O: O(V^2+E).""" 
    INF = float('inf') 
    dist = {v: INF for v in graph.adj} 
    parent = {v: None for v in graph.adj} 
    dist[depot] = 0 
    visited = set() 
    
    for _ in range(len(graph.adj)):
        u = None
        min_dist = INF
        for v in graph.adj:
            if v not in visited and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
                
        if u is None:
            break
            
        visited.add(u)
        
        current_edge = graph.adj.get(u, None)
        while current_edge:
            v = current_edge.dest
            if v not in visited:
                new_dist = dist[u] + current_edge.jarak
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u
            current_edge = current_edge.next
            
    return dist, parent
