def hitung_dijkstra(graph, start):
    jarak = {node: float('inf') for node in graph.nodes}
    jarak[start] = 0
    unvisited = list(graph.nodes)
    
    while unvisited:
        curr = min(unvisited, key=lambda n: jarak[n])
        unvisited.remove(curr)
        
        if jarak[curr] == float('inf'): break
        
        adj = graph.adj_list[curr]
        while adj:
            if adj.tujuan in unvisited:
                path_alt = jarak[curr] + adj.bobot
                if path_alt < jarak[adj.tujuan]:
                    jarak[adj.tujuan] = path_alt
            adj = adj.next
    return jarak
