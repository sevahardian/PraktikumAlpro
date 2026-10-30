## --- Operasi LIST ---

# Index 0(-3)   1(-2)   2(-1)
data = ["Ucup", "Adit", "Dudung"]

# Mengambil Data dari List
data_0 = data[0]

print(f"data pertama (index 0) = {data_0}")
data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# Mengambil info jumlah Data dalam List
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# Manipulasi Data List

# Menambahkan Item pada List sesuai posisi
print(f"data sebelum ditambah = \n{data}")

#data.insert(posisi, item)
data.insert(1, "Asep")
print(f"data sesudah ditambah= \n{data}")

# Menambah di akhir List
data.append("Ririn")
print(f"data ditambah lagi = \n{data}")

# Menambahkan List dengan List
data_baru = ["Luffy", "Zoro", "Nami"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# Merubah Data

# Mengubah Data 2 menjadi Jarwo
data[2] = "Jarwo"
print(f"data rubah = \n{data}")

# Menghapus Data
data.remove("Ucup")
print(f"data hapus = \n{data}")

# Menghapus Data paling belakang
data.pop()
print(f"data akhir = \n{data}")