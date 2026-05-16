def temukan_lokasi_terisolasi(graph, start_node):
    visited = {node: False for node in graph.nodes}
    queue = [start_node]
    visited[start_node] = True
    
    while queue:
        curr = queue.pop(0)
        curr_adj = graph.adj_list[curr]
        while curr_adj:
            if not visited[curr_adj.tujuan]:
                visited[curr_adj.tujuan] = True
                queue.append(curr_adj.tujuan)
            curr_adj = curr_adj.next
            
    return [node for node, v in visited.items() if not v]
