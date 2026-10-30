# Diberikan list berikut:
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# a. Tambahkan 'truk' di akhir list.
kendaraan.append("truk")
print(f"List kendaraan setelah menambah 'truk' di akhir list = \n{kendaraan}")

# b. Sisipkan 'becak' pada index ke-1
kendaraan.insert(1, "becak")
print(f"List kendaraan setelah menyisipkan 'becak' pada index ke-1 = \n{kendaraan}")

# c. Hapus data yang berada paling belakang dari list tersebut.
kendaraan.pop()
print(f"List kendaraan setelah menghapus data paling belakang = \n{kendaraan}")

# d. Ubah elemen 'sepeda' menjadi 'skuter'.
kendaraan[3] = "skuter"
print(f"List kendaraan setelah mengubah elemen 'sepeda' menjadi 'skuter' = \n{kendaraan}")

# e. Tampilkan informasi jumlah total data di dalam list tersebut.
total_kendaraan = len(kendaraan)
print(f"Jumlah total data kendaraan di dalam list = \n{total_kendaraan}")