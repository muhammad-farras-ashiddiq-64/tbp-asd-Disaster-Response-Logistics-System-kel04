class AdjNode:
    def __init__(self, tujuan, bobot):
        self.tujuan = tujuan
        self.bobot = bobot
        self.next = None

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.nodes = []

    def tambah_node(self, nama):
        if nama not in self.adj_list:
            self.adj_list[nama] = None
            self.nodes.append(nama)

    def tambah_rute(self, u, v, bobot):
        self.tambah_node(u)
        self.tambah_node(v)
        
        # Sisi U -> V
        new_node = AdjNode(v, bobot)
        new_node.next = self.adj_list[u]
        self.adj_list[u] = new_node
        
        # Sisi V -> U (Tidak Berarah)
        new_node = AdjNode(u, bobot)
        new_node.next = self.adj_list[v]
        self.adj_list[v] = new_node
