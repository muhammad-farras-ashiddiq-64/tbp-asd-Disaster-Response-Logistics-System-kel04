PS C:\Users\DELL\OneDrive - uny.ac.id\Dokumen\GitHub\tbp-asd-Disaster-Response-Logistics-System-kel04> & C:\msys64\ucrt64\bin\python.exe "c:/Users/DELL/OneDrive - uny.ac.id/Dokumen/GitHub/tbp-asd-Disaster-Response-Logistics-System-kel04/tbp-asd-kelompok-04/src/main.py"
Disaster Response Logistics System. Ketik BANTUAN untuk daftar perintah.

Logistik-CLI> BANTUAN
Daftar Perintah Tersedia:
  KIRIM <depot> <lokasi> <jenis_bantuan> <jumlah>
  PROSES_BANTUAN
  RUTE_OPTIMAL <depot> <tujuan>
  UPDATE_LEVEL <kode_lokasi> <level_baru>
  TIDAK_TERJANGKAU <depot>
  LOG_PENGIRIMAN
  LAPORAN_BENCANA
  ROLLBACK
  KELUAR

Logistik-CLI> LAPORAN_BENCANA
KODE       | NAMA LOKASI            | LEVEL  | POPULASI
-------------------------------------------------------
DEPOT_0    | Gudang Logistik 0      | RINGAN | 0       
DEPOT_1    | Gudang Logistik 1      | RINGAN | 0       
DEPOT_2    | Gudang Logistik 2      | RINGAN | 0       
L000       | Desa/Kelurahan-0       | RINGAN | 2764    
L001       | Desa/Kelurahan-1       | SEDANG | 3792    
L002       | Desa/Kelurahan-2       | KRITIS | 485     
L003       | Desa/Kelurahan-3       | SEDANG | 4837    
L004       | Desa/Kelurahan-4       | SEDANG | 2196    
L005       | Desa/Kelurahan-5       | SEDANG | 4303    
L006       | Desa/Kelurahan-6       | KRITIS | 1533    
L007       | Desa/Kelurahan-7       | RINGAN | 3777    
L008       | Desa/Kelurahan-8       | SEDANG | 4154    
L009       | Desa/Kelurahan-9       | RINGAN | 4126    
L010       | Desa/Kelurahan-10      | SEDANG | 1513    
L011       | Desa/Kelurahan-11      | RINGAN | 1620    
L012       | Desa/Kelurahan-12      | RINGAN | 2797    
L013       | Desa/Kelurahan-13      | RINGAN | 1048    
L014       | Desa/Kelurahan-14      | KRITIS | 2077    
L015       | Desa/Kelurahan-15      | KRITIS | 2800    
L016       | Desa/Kelurahan-16      | RINGAN | 4796    
L017       | Desa/Kelurahan-17      | RINGAN | 4775    
L018       | Desa/Kelurahan-18      | RINGAN | 4305    
L019       | Desa/Kelurahan-19      | RINGAN | 3682    
L020       | Desa/Kelurahan-20      | SEDANG | 2767    
L021       | Desa/Kelurahan-21      | SEDANG | 1526    
L022       | Desa/Kelurahan-22      | RINGAN | 4373    
L023       | Desa/Kelurahan-23      | RINGAN | 4973    
L024       | Desa/Kelurahan-24      | RINGAN | 2474    
L025       | Desa/Kelurahan-25      | RINGAN | 2319    
L026       | Desa/Kelurahan-26      | RINGAN | 2724    
L027       | Desa/Kelurahan-27      | RINGAN | 4715    
L028       | Desa/Kelurahan-28      | KRITIS | 510     
L029       | Desa/Kelurahan-29      | SEDANG | 3187    
L030       | Desa/Kelurahan-30      | KRITIS | 932     
L031       | Desa/Kelurahan-31      | RINGAN | 348     
L032       | Desa/Kelurahan-32      | SEDANG | 1526    
L033       | Desa/Kelurahan-33      | RINGAN | 561     
L034       | Desa/Kelurahan-34      | SEDANG | 191     

Logistik-CLI> KIRIM DEPOT_0 L000 MAKANAN 100
Sukses: Bantuan ID 1 (Prioritas: 3) dimasukkan ke antrian.

Logistik-CLI> KIRIM DEPOT_0 L001 OBAT 50
Sukses: Bantuan ID 2 (Prioritas: 2) dimasukkan ke antrian.

Logistik-CLI> PROSES_BANTUAN
[PENGIRIMAN] Memproses Bantuan ID 2:
  Kirim 50 x OBAT dari DEPOT_0 ke L001

Logistik-CLI> PROSES_BANTUAN
[PENGIRIMAN] Memproses Bantuan ID 1:
  Kirim 100 x MAKANAN dari DEPOT_0 ke L000

Logistik-CLI> RUTE_OPTIMAL DEPOT_0 L001
Rute Terpendek (93 km): DEPOT_0 -> L018 -> L001

Logistik-CLI> LOG_PENGIRIMAN
=== RIWAYAT TRANSAKSI PENGIRIMAN (LIFO) ===
ID 1: 100 MAKANAN (DEPOT_0 -> L000)
ID 2: 50 OBAT (DEPOT_0 -> L001)

Logistik-CLI> KELUAR
Keluar dari sistem. Terima kasih.
