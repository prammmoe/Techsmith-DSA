# Di Python, Array disebut List (kalau dinamain arr atau array ntar muncul warning di filenya)

# Inisialisasi array kosong
arr1 = []

# Selain cara di atas, bisa juga gini
arr2 = list() # STL --> Standard Library

# Bisa juga langsung diisi dengan elemen yang sama
arr3 = [2, 4, 6, 8, 10, 12]

arr2.append(100)
arr2.append(200)

arr3.append(200)

arr4 = ["True", True, False, 'C', 100, 10.9]

data_mahasiswa = [
    "Pramuditha",
    22,
    True,
    4.00
]

data_mahasiswa.append(23000)
print(data_mahasiswa)