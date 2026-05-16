# Modul 4: Algoritma Dijkstra untuk Optimasi Jalur Logistik Darurat
from src.data_structures.graph import GraphRute

def dijkstra(graph: GraphRute, depot: str):
    """
    Menentukan rute terpendek dari simpul depot ke seluruh lokasi bencana.
    Kompleksitas Waktu: O(V² + E)
    """
    INF = float('inf')
    
    # Inisialisasi jarak ke semua simpul dengan nilai Tak Hingga (INF)
    dist = {v: INF for v in graph.adj}
    # Tracker simpul asal untuk rekonstruksi lintasan rute
    parent = {v: None for v in graph.adj}
    
    # Jarak dari depot ke dirinya sendiri adalah 0
    dist[depot] = 0
    visited = set()

    for _ in range(len(graph.adj)):
        # Cari simpul dengan jarak terkecil yang belum dikunjungi
        u = None
        for v in graph.adj:
            if v not in visited:
                if u is None or dist[v] < dist[u]:
                    u = v
                    
        # Jika simpul tidak ditemukan atau sisa simpul tidak terjangkau, hentikan loop
        if u is None or dist[u] == INF: 
            break
            
        visited.add(u)

        # Proses pembaruan jarak (relaxation) ke semua simpul tetangga u
        for (v, w) in graph.tetangga(u):
            if v not in visited and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                
    return dist, parent
