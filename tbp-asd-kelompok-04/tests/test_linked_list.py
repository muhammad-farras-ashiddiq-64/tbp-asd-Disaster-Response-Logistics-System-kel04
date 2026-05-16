# tests/test_linked_list.py

import unittest
from data_structures.linked_list import LinkedList, Node

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """Inisialisasi Linked List kosong sebelum setiap pengujian dijalankan"""
        self.list = LinkedList()

    def test_inisialisasi_kosong(self):
        """Memastikan Linked List yang baru dibuat dalam keadaan kosong (head = None)"""
        self.assertIsNone(self.list.head)

    def test_append_satu_elemen(self):
        """Menguji penambahan satu data ke dalam Linked List"""
        self.list.append("DEPOT_PUSAT")
        
        # Head tidak boleh kosong dan harus menyimpan data yang benar
        self.assertIsNotNone(self.list.head)
        self.assertEqual(self.list.head.data, "DEPOT_PUSAT")
        # Elemen pertama harus menunjuk ke None karena belum ada elemen kedua
        self.assertIsNone(self.list.head.next)

    def test_append_banyak_elemen(self):
        """Menguji penambahan beberapa data secara berurutan (Sequential Order)"""
        self.list.append("Posko_A")
        self.list.append("Posko_B")
        self.list.append("Posko_C")

        # Cek data pada head (elemen pertama)
        node_1 = self.list.head
        self.assertEqual(node_1.data, "Posko_A")

        # Cek elemen kedua (next dari head)
        node_2 = node_1.next
        self.assertIsNotNone(node_2)
        self.assertEqual(node_2.data, "Posko_B")

        # Cek elemen ketiga
        node_3 = node_2.next
        self.assertIsNotNone(node_3)
        self.assertEqual(node_3.data, "Posko_C")

        # Elemen terakhir harus menunjuk ke None
        self.assertIsNone(node_3.next)

    def test_append_berbagai_tipe_data(self):
        """Memastikan Linked List mampu menyimpan objek kamus (dictionary) logistik"""
        data_bantuan = {"kode": "L01", "nama": "Desa Bantul", "jarak": 15}
        self.list.append(data_bantuan)

        self.assertIsNotNone(self.list.head)
        self.assertEqual(self.list.head.data["kode"], "L01")
        self.assertEqual(self.list.head.data["nama"], "Desa Bantul")
        self.assertEqual(self.list.head.data["jarak"], 15)

if __name__ == "__main__":
    unittest.main()
