# a. Buatlah dictionary bernama keranjang dengan data harga buah berikut: {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}

# b. Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: "Harga apel: Rp 5000"
for buah, harga in keranjang.items():
    print(f"\t Harga {buah}: Rp {harga}")
    
# c. Tampilkan total belanja
total_belanja = sum(keranjang.values())
print(f"\n Total belanjaan adalah sebanyak Rp {total_belanja}")
