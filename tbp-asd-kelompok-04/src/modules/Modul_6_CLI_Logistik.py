# Modul ini menangani fungsi pencetakan antarmuka CLI
def cetak_bantuan_menu():
    print("\n--- PERINTAH OPERASIONAL DISASTER RESPONSE LOGISTIC ---")
    print("1. KIRIM <depot> <lokasi> <jenis> <jumlah>   : Enqueue armada")
    print("2. PROSES_BANTUAN                            : Dequeue logistik terdepan")
    print("3. RUTE_OPTIMAL <depot> <tujuan>             : Lintasan terpendek Dijkstra")
    print("4. UPDATE_LEVEL <kode> <level>               : Ubah urgensi bencana (1-3)")
    print("5. TIDAK_TERJANGKAU <depot>                  : Deteksi BFS wilayah terisolasi")
    print("6. LOG_PENGIRIMAN                            : Tampilkan riwayat log (LIFO)")
    print("7. LAPORAN_BENCANA                           : Cetak urutan kode (BST Inorder)")
    print("8. KELUAR                                    : Keluar sistem")
