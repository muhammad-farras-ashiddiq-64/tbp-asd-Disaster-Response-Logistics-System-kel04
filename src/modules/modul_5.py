# Modul 5: Algoritma Dijkstra Untuk Optimasi Rute Terpendek Logistik
from src.modules.modul_1 import GraphRute

def dijkstra(graph: GraphRute, depot: str):
    INF = float('inf')
    dist = {v: INF for v in graph.adj}
    parent = {v: None for v in graph.adj}
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

        for (v, w) in graph.tetangga(u):
            if v not in visited and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
    return dist, parent

def rekonstruksi_jalur(parent: dict, start: str, target: str) -> list:
    jalur = []
    curr = target
    while curr is not None:
        jalur.append(curr)
        if curr == start: 
            break
        curr = parent[curr]
    jalur.reverse()
    return jalur if jalur and jalur[0] == start else []
