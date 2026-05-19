def selection_sort_audit(arr):
    """Selection Sort untuk mengurutkan hasil audit jarak terdekat dari depot.
    Big-O: O(N^2)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # arr[j] berbentuk (kode_lokasi, jarak_km)
            if arr[j][1] < arr[min_idx][1]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr