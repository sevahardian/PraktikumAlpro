# Membuat program dengan inputan sesuai tipe datanya

# a. Meminta input usia (integer)
usia = int (input ("Masukkan usia anda: ")) # Menggunakan fungsi int() untuk mengubah tipe data ke integer
print ("Usia anda adalah ", usia, "tahun, bertipe data", type(usia))

# b. Meminta input tinggi badan (float)
tinggi_badan = float (input ("Masukkan tinggi badan anda: ")) # Menggunakan fungsi float() untuk mengubah tipe data ke float
print ("Tinggi badan anda adalah ", tinggi_badan, "cm, bertipe data", type(tinggi_badan))

# c. Meminta input nama (string)
nama = input ("Masukkan nama anda: ") # Tidak perlu menggunakan str() untuk mengubah tipe data, karena otomatis tipe data string (default)
print ("Nama anda adalah ", nama, ", bertipe data", type(nama))