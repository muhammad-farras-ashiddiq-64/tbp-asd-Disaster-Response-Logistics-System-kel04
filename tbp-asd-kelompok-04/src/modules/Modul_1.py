class AdjNode:
    def __init__(self, tujuan, bobot):
        self.tujuan = tujuan
        self.bobot = bobot
        self.next = None

class Graph:
    def __init__(self):
        self.adj_list = {}  # Memetakan nama node ke Head dari Linked List tetangganya
        self.nodes = []     # Menyimpan daftar nama semua node

    def tambah_node(self, nama):
        if nama not in self.adj_list:
            self.adj_list[nama] = None
            self.nodes.append(nama)

    def tambah_rute(self, u, v, bobot):
        """O(1) - Menambahkan ke head dari Linked List masing-masing node"""
        self.tambah_node(u)
        self.tambah_node(v)
        
        # U -> V
        new_node = AdjNode(v, bobot)
        new_node.next = self.adj_list[u]
        self.adj_list[u] = new_node
        
        # V -> U (Tidak Berarah)
        new_node = AdjNode(u, bobot)
        new_node.next = self.adj_list[v]
        self.adj_list[v] = new_node
