# Tugas: Noomira Zakiah (25051030072)
class LLNode:
    """
    Kelas dasar untuk simpul dalam Linked List.
    Digunakan secara universal oleh Stack dan Priority Queue.
    """
    def __init__(self, data=None):
        self.data = data  # Menyimpan objek (Bantuan, Lokasi, dsb)
        self.next = None  # Pointer ke simpul berikutnya

class LinkedList:
    """
    Implementasi Linked List dasar untuk manajemen data manual.
    """
    def __init__(self):
        self.head = None
        self._size = 0

    def add_first(self, data):
        """
        Menambahkan data di depan (Head). 
        Digunakan oleh Stack.push().
        Big-O: O(1)
        """
        new_node = LLNode(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def remove_first(self):
        """
        Menghapus dan mengambil data pertama.
        Digunakan oleh Stack.pop() dan Queue.dequeue().
        Big-O: O(1)
        """
        if self.is_empty():
            return None
        
        removed_data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return removed_data

    def add_sorted_priority(self, data):
        """
        Menyisipkan data secara terurut berdasarkan nilai prioritas.
        Digunakan oleh PriorityQueue.enqueue().
        Mekanisme: Mencari posisi di mana data.prioritas lebih kecil.
        Big-O: O(N)
        """
        new_node = LLNode(data)
        
        # Kasus 1: List kosong atau prioritas baru lebih tinggi (angka lebih kecil)
        if self.head is None or data.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node
        else:
            # Kasus 2: Cari posisi di tengah atau di akhir
            current = self.head
            while current.next is not None and current.next.data.prioritas <= data.prioritas:
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            
        self._size += 1

    def is_empty(self):
        """Mengecek apakah list kosong. Big-O: O(1)"""
        return self.head is None

    def get_size(self):
        """Mengambil jumlah elemen. Big-O: O(1)"""
        return self._size

    def display_all(self):
        """
        Mengonversi seluruh linked list menjadi list standard Python 
        hanya untuk kebutuhan tampilan/iterasi CLI.
        Big-O: O(N)
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
