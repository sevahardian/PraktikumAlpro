# Diberikan data nested list berupa informasi nama barang dan harganya:
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut.
print(f"Harga Pensil adalah {data_barang[1][1]}.")

# b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format: "Nama: [nama barang], Harga: [harga]" untuk setiap elemen di dalamnya.
for barang in data_barang:
    print(f"Nama\t : {barang[0]}")
    print(f"Harga\t : {barang[1]}")
    print("\n")