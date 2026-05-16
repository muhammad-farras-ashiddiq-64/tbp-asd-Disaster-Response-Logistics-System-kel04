# Modul 6: Utilitas Sistem Logistik & Selection Sort Laporan
from typing import List

def selection_sort_laporan(daftar_data: List[dict], key: str = "jarak") -> List[dict]:
    """Mengurutkan data laporan kebencanaan menggunakan Selection Sort."""
    n = len(daftar_data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if daftar_data[j][key] < daftar_data[min_idx][key]:
                min_idx = j
        daftar_data[i], daftar_data[min_idx] = daftar_data[min_idx], daftar_data[i]
    return daftar_data
