# Penanggung Jawab: Restu Pamungkas (25051030080)
from dataclasses import dataclass

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