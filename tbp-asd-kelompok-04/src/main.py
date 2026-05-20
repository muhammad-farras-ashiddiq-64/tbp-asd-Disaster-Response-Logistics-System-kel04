import numpy as np, time, random 
from dataclasses import dataclass 
from typing import Optional, List, Dict, Tuple  
np.random.seed(47) 
random.seed(47) 

LEVEL_BENCANA = {'KRITIS': 1, 'SEDANG': 2, 'RINGAN': 3} 
JENIS_BANTUAN = ['MAKANAN', 'AIR', 'OBAT', 'SELIMUT', 'TENDA'] 

@dataclass 
class Lokasi: 
    kode: str 
    nama: str 
    level: int 
    populasi: int 
    status: int = 0 

@dataclass 
class Bantuan: 
    bantuan_id: int 
    jenis: str 
    jumlah: int 
    asal: str 
    tujuan: str 
    prioritas: int 

class LLNode: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 

class PriorityQueueBantuan: 
    """Lokasi KRITIS (level=1) selalu dilayani lebih dulu.""" 
    def __init__(self): 
        self.head = None 
        self._size = 0 

    def enqueue(self, bantuan: Bantuan): 
        """Big-O: O(n) insertion terurut prioritas angka terkecil (1=Kritis, dst).""" 
        new_node = LLNode(bantuan)
        self._size += 1
        
        if self.head is None or bantuan.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None and current.next.data.prioritas <= bantuan.prioritas:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    def dequeue(self): 
        """Big-O: O(1). Ambil dari head.""" 
        if self.head is None:
            return None
        temp = self.head.data
        self.head = self.head.next
        self._size -= 1
        return temp

    def __len__(self): 
        return self._size 

class Stack: 
    def __init__(self): 
        self.top = None 
        self._size = 0 

    def push(self, data): 
        """Big-O O(1)"""
        new_node = LLNode(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self): 
        """Big-O O(1)"""
        if self.top is None:
            return None
        temp = self.top.data
        self.top = self.top.next
        self._size -= 1
        return temp

    def peek(self): 
        return self.top.data if self.top else None 

    def to_list(self): 
        """Kembalikan list dari top ke bottom"""
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result

class BSTNodeLok: 
    def __init__(self, lokasi): 
        self.lokasi = lokasi 
        self.left = self.right = None 

class BSTLokasi: 
    def __init__(self): 
        self.root = None 

    def insert(self, lokasi): 
        """Big-O: O(log n). Kunci = lokasi.kode.""" 
        new_node = BSTNodeLok(lokasi)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if lokasi.kode < current.lokasi.kode:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            elif lokasi.kode > current.lokasi.kode:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            else:
                current.lokasi = lokasi  
                break

    def search(self, kode) -> Optional[Lokasi]: 
        """Big-O: O(log n).""" 
        current = self.root
        while current:
            if kode == current.lokasi.kode:
                return current.lokasi
            elif kode < current.lokasi.kode:
                current = current.left
            else:
                current = current.right
        return None

    def update_level(self, kode, level): 
        """Big-O: O(log n).""" 
        lokasi = self.search(kode)
        if lokasi:
            lokasi.level = level
            return True
        return False

    def inorder(self) -> List[Lokasi]: 
        """Big-O: O(n).""" 
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.lokasi)
                _inorder(node.right)
        _inorder(self.root)
        return result

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

def dijkstra_logistik(graph: GraphRute, depot: str): 
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

def generate_peta_bencana(n_lokasi=35, n_depot=3, seed=47): 
    rng = np.random.default_rng(seed) 
    lokasi = [] 
    for i in range(n_depot): 
        lokasi.append(Lokasi(f'DEPOT_{i}', f'Gudang Logistik {i}', 3, 0)) 
    for i in range(n_lokasi): 
        kode = f'L{i:03d}' 
        level = int(rng.choice([1,2,3], p=[0.2, 0.4, 0.4])) 
        pop = int(rng.integers(100, 5000)) 
        lokasi.append(Lokasi(kode, f'Desa/Kelurahan-{i}', level, pop)) 
    n_total = len(lokasi) 
    perm = rng.permutation(n_total) 
    edges = [] 
    for i in range(1, n_total): 
        u = lokasi[perm[i-1]].kode 
        v = lokasi[perm[i]].kode 
        edges.append((u, v, int(rng.integers(5, 100)), int(rng.integers(1, 5)))) 
    for _ in range(15): 
        i, j = rng.choice(n_total, 2, replace=False) 
        edges.append((lokasi[i].kode, lokasi[j].kode, int(rng.integers(5,100)), 
        int(rng.integers(1,5)))) 
    return lokasi, edges 

def main(): 
    bst_lokasi = BSTLokasi() 
    graph = GraphRute() 
    antrian_bantuan = PriorityQueueBantuan() 
    log_kirim = Stack() 
    bantuan_counter = 0 
    
    lokasi_list, edges = generate_peta_bencana(35, 3, seed=47) 
    for lok in lokasi_list: 
        bst_lokasi.insert(lok) 
        graph.tambah_node(lok.kode) 
    for u, v, j, k in edges: 
        graph.tambah_rute(u, v, j, k) 
    
    print('Disaster Response Logistics System. Ketik BANTUAN untuk daftar perintah.') 
    
    while True:
        try:
            pilihan = input('\nLogistik-CLI> ').strip()
            if not pilihan:
                continue
                
            parts = pilihan.split()
            command = parts[0].upper()
            
            if command == 'KELUAR':
                print('Keluar dari sistem. Terima kasih.')
                break
                
            elif command == 'BANTUAN':
                print('Daftar Perintah Tersedia:')
                print('  KIRIM <depot> <lokasi> <jenis_bantuan> <jumlah>')
                print('  PROSES_BANTUAN')
                print('  RUTE_OPTIMAL <depot> <tujuan>')
                print('  UPDATE_LEVEL <kode_lokasi> <level_baru>')
                print('  TIDAK_TERJANGKAU <depot>')
                print('  LOG_PENGIRIMAN')
                print('  LAPORAN_BENCANA')
                print('  ROLLBACK')
                print('  KELUAR')
                
            elif command == 'KIRIM':
                if len(parts) < 5:
                    print('Format salah! Gunakan: KIRIM <depot> <lokasi> <jenis> <jumlah>')
                    continue
                depot, lokasi_tujuan, jenis, jumlah_str = parts[1], parts[2], parts[3], parts[4]
                
                loc_asal = bst_lokasi.search(depot)
                loc_tujuan = bst_lokasi.search(lokasi_tujuan)
                
                if not loc_asal:
                    print(f'Error: Depot {depot} tidak ditemukan!')
                    continue
                if not loc_tujuan:
                    print(f'Error: Lokasi {lokasi_tujuan} tidak ditemukan!')
                    continue
                if jenis.upper() not in JENIS_BANTUAN:
                    print(f'Error: Jenis bantuan tidak valid! Pilih dari {JENIS_BANTUAN}')
                    continue
                    
                bantuan_counter += 1
                bantuan_baru = Bantuan(
                    bantuan_id=bantuan_counter,
                    jenis=jenis.upper(),
                    jumlah=int(jumlah_str),
                    asal=depot,
                    tujuan=lokasi_tujuan,
                    prioritas=loc_tujuan.level
                )
                antrian_bantuan.enqueue(bantuan_baru)
                print(f'Sukses: Bantuan ID {bantuan_counter} (Prioritas: {loc_tujuan.level}) dimasukkan ke antrian.')
                
            elif command == 'PROSES_BANTUAN':
                if len(antrian_bantuan) == 0:
                    print('Antrian kosong, tidak ada bantuan yang perlu diproses.')
                    continue
                
                bantuan_diproses = antrian_bantuan.dequeue()
                log_kirim.push(bantuan_diproses)
                print(f'[PENGIRIMAN] Memproses Bantuan ID {bantuan_diproses.bantuan_id}:')
                print(f'  Kirim {bantuan_diproses.jumlah} x {bantuan_diproses.jenis} dari {bantuan_diproses.asal} ke {bantuan_diproses.tujuan}')
                
            elif command == 'RUTE_OPTIMAL':
                if len(parts) < 3:
                    print('Format salah! Gunakan: RUTE_OPTIMAL <depot> <tujuan>')
                    continue
                depot, tujuan = parts[1], parts[2]
                
                if depot not in graph.adj or tujuan not in graph.adj:
                    print('Error: Depot atau Tujuan tidak terdaftar di grafik rute.')
                    continue
                    
                dist, parent = dijkstra_logistik(graph, depot)
                
                if dist[tujuan] == float('inf'):
                    print(f'Rute tidak ditemukan dari {depot} ke {tujuan}.')
                else:
                    path = []
                    curr = tujuan
                    while curr is not None:
                        path.append(curr)
                        curr = parent[curr]
                    path.reverse()
                    print(f'Rute Terpendek ({dist[tujuan]} km): {" -> ".join(path)}')
                    
            elif command == 'UPDATE_LEVEL':
                if len(parts) < 3:
                    print('Format salah! Gunakan: UPDATE_LEVEL <kode> <level (1-3 / KRITIS-RINGAN)>')
                    continue
                kode, lvl_input = parts[1], parts[2].upper()
                
                if lvl_input in LEVEL_BENCANA:
                    level_baru = LEVEL_BENCANA[lvl_input]
                else:
                    level_baru = int(lvl_input)
                    
                if bst_lokasi.update_level(kode, level_baru):
                    print(f'Sukses: Tingkat keparahan lokasi {kode} diubah ke level {level_baru}.')
                else:
                    print(f'Error: Lokasi {kode} tidak ditemukan.')
                    
            elif command == 'TIDAK_TERJANGKAU':
                if len(parts) < 2:
                    print('Format salah! Gunakan: TIDAK_TERJANGKAU <depot>')
                    continue
                depot = parts[1]
                
                terjangkau = graph.bfs_akses(depot)
                semua_lokasi = bst_lokasi.inorder()
                tidak_terjangkau = [l.kode for l in semua_lokasi if l.kode not in terjangkau]
                
                print(f'Lokasi terisolasi / tidak terjangkau dari {depot}:')
                if tidak_terjangkau:
                    print(", ".join(tidak_terjangkau))
                else:
                    print("Nihil (Semua lokasi terjangkau).")
                    
            elif command == 'LOG_PENGIRIMAN':
                riwayat = log_kirim.to_list()
                print('=== RIWAYAT TRANSAKSI PENGIRIMAN (LIFO) ===')
                if not riwayat:
                    print('Belum ada pengiriman yang diproses.')
                for b in riwayat:
                    print(f'ID {b.bantuan_id}: {b.jumlah} {b.jenis} ({b.asal} -> {b.tujuan})')
                    
            elif command == 'ROLLBACK':
                bantuan_batal = log_kirim.pop()
                if bantuan_batal:
                    print(f'Rollback Berhasil: Pengiriman Bantuan ID {bantuan_batal.bantuan_id} telah dibatalkan.')
                    antrian_bantuan.enqueue(bantuan_batal)
                else:
                    print('Gagal: Tidak ada riwayat transaksi pengiriman untuk di-rollback.')
                    
            elif command == 'LAPORAN_BENCANA':
                semua_lokasi = bst_lokasi.inorder()
                print(f'{"KODE":<10} | {"NAMA LOKASI":<22} | {"LEVEL":<6} | {"POPULASI":<8}')
                print('-' * 55)
                for l in semua_lokasi:
                    lbl_level = "KRITIS" if l.level == 1 else "SEDANG" if l.level == 2 else "RINGAN"
                    print(f'{l.kode:<10} | {l.nama:<22} | {lbl_level:<6} | {l.populasi:<8}')
                    
            else:
                print('Perintah tidak dikenali. Ketik BANTUAN untuk melihat daftar perintah.')
                
        except Exception as e:
            print(f'Terjadi Kesalahan Input/Sistem: {e}')

if __name__ == '__main__': 
    main()