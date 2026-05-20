# KELOMPOK-4-Disaster-Response-Logistics-system
TOPIK 9 Disaster Response Logistics system
# Team
1. MUHAMMAD FARRAS ASHIDDIQ 25051030064
2. NOOMIRA ZAKIAH 25051030072
3. FAHRI KHAIRU IMTIHAN 25051030052
4. RESTU PAMUNGKAS 25051030080
# Mata Kuliah
Algoritma dan Struktur Data                                                                                                                                                   
S1 Teknik Elektro                                                                                                                                                            
Universitas Negeri Yogyakarta

# Deskripsi Project
Proyek ini merupakan simulasi sistem logistik tanggap bencana
menggunakan struktur data Graph, Priority Queue, BST, dan Stack.

Sistem digunakan untuk:
- mengelola distribusi bantuan,
- mencari rute distribusi tercepat,
- memprioritaskan daerah kritis,
- menyimpan log distribusi bantuan.

# Latar Belakang
Indonesia memiliki risiko bencana tinggi sehingga diperlukan
sistem distribusi bantuan yang efisien dan terstruktur.

## Tujuan
- Mengimplementasikan struktur data dari nol
- Membangun simulasi logistik bencana berbasis CLI
- Menganalisis kompleksitas Big-O
- Menguji performa struktur data

## Struktur Data

| Struktur Data | Fungsi |
| Priority Queue | Prioritas bantuan |
| BST | Penyimpanan lokasi |
| Graph | Jalur distribusi |
| Stack | Log distribusi |
| Linked List | Implementasi node |

Project ini menggunakan beberapa struktur data utama yang dibangun secara manual (*from scratch*), yaitu:
* **Binary Search Tree (BST) :** Mengelola registrasi data lokasi desa/kelurahan terdampak dan melakukan pencarian serta pembaruan level bencana secara efisien.
* **Priority Queue :** Mengatur urutan antrean bantuan logistik menggunakan *Singly Linked List* terurut, di mana wilayah dengan level bencana `KRITIS` otomatis dilayani paling depan.
* **Stack :** Menyimpan log riwayat transaksi pengiriman sukses yang bersifat LIFO untuk mendukung fitur pembatalan distribusi (`ROLLBACK`).
* **Graph (Adjacency List) :** Merepresentasikan jaringan jalur transportasi antar depot logistik dan lokasi pengiriman, dilengkapi dengan fungsi penelusuran struktur Linked List.
* **BFS (Breadth-First Search) :** Mendeteksi dan memfilter lokasi-lokasi terisolasi yang tidak dapat dijangkau dari depot tertentu.
* **Algoritma Dijkstra :** Menentukan rute atau jalur distribusi logistik dengan jarak terpendek dari depot ke lokasi target.
* **Quick Sort :** Melakukan pengurutan data lokasi terdampak berdasarkan skor urgensi tertinggi untuk pembuatan laporan kebencanaan.

## Fitur Sistem

- KIRIM bantuan
- PROSES bantuan prioritas
- PENCARIAN lokasi
- RUTE tercepat
- LOG distribusi
- DFS/BFS graph traversal
- Dijkstra shortest path

# Struktur Folder
* `docs/`          -> laporan proyek dan slide presentasi
* `src/`           -> source code utama program
* `structures/`    -> modul struktur data kustom (graph, bst, priority queue, stack)
* `tests/`         -> pengujian keandalan program
