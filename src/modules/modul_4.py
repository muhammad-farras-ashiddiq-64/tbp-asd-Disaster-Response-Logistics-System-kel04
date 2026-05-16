# Modul 4: Algoritma Dijkstra Untuk Optimasi Jalur Logistik Darurat
from src.data_structures.graph import GraphRute

def dijkstra(graph: GraphRute, depot: str):
    """
    Menentukan jarak minimum dan penelusuran balik rute terpendek 
    dari simpul depot asal menuju seluruh lokasi bencana terdampak.
    Big-O Kompleksitas: O(V^2 + E)
    """
    INF = float('inf')
    
    # Inisialisasi awal seluruh node dengan jarak tak hingga (INF)
    dist = {v: INF for v in graph.adj}
    # Pelacak node pendahulu untuk rekonstruksi lintasan rute
    parent = {v: None for v in graph.adj}
    
    # Jarak dari simpul awal/depot ke dirinya sendiri adalah 0
    dist[depot] = 0
    visited = set()

    for _ in range(len(graph.adj)):
        # Linear scan mencari simpul non-visited dengan bobot terkecil
        u = None
        for v in graph.adj:
            if v not in visited:
                if u is None or dist[v] < dist[u]:
                    u = v
                    
        # Apabila sisa simpul tidak terhubung/terisolasi, keluar dari loop
        if u is None or dist[u] == INF: 
            break
            
        visited.add(u)

        # Proses relaksasi nilai bobot jarak rute untuk setiap tetangga simpul u
        for (v, w) in graph.tetangga(u):
            if v not in visited and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                
    return dist, parent

def rekonstruksi_jalur(parent: dict, start: str, target: str) -> list:
    """
    Mengubah riwayat data pointer penelusuran balik (parent) 
    menjadi daftar urutan lintasan rute jalan yang runtut.
    """
    jalur = []
    curr = target
    while curr is not None:
        jalur.append(curr)
        if curr == start: 
            break
        curr = parent[curr]
    jalur.reverse()
    return jalur if jalur and jalur[0] == start else []
