from data_structures.linked_list import LinkedList

def hitung_dijkstra(graph, start):
    """Dijkstra O(V^2 + E) menghasilkan rute jarak minimum dari depot pusat"""
    jarak = {node: float('inf') for node in graph.nodes}
    jarak[start] = 0
    unvisited = list(graph.nodes)
    
    while unvisited:
        curr = min(unvisited, key=lambda n: jarak[n])
        unvisited.remove(curr)
        
        if jarak[curr] == float('inf'):
            break
            
        adj = graph.adj_list[curr]
        while adj:
            if adj.tujuan in unvisited:
                path_alt = jarak[curr] + adj.bobot
                if path_alt < jarak[adj.tujuan]:
                    jarak[adj.tujuan] = path_alt
            adj = adj.next
    return jarak

def audit_jarak_selection_sort(jarak_dict):
    """Mengurutkan lokasi menggunakan Selection Sort pada Linked List manual"""
    ll = LinkedList()
    for nama, jarak in jarak_dict.items():
        ll.append({"nama": nama, "jarak": jarak})
        
    # Proses Selection Sort pada Linked List
    i = ll.head
    while i:
        min_node = i
        j = i.next
        while j:
            if j.data["jarak"] < min_node.data["jarak"]:
                min_node = j
            j = j.next
        # Tukar data objek
        i.data, min_node.data = min_node.data, i.data
        i = i.next
        
    return ll
