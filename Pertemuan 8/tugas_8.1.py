# a. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: ("Nama", "NIM", "Prodi").
mahasiswa = ("Muhammad Seva Hardian", "2605060046", "S1 Teknologi Informasi")

# b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya.
print(mahasiswa[1])
print(mahasiswa[2])

# c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi!
mahasiswa[2] = "Teknologi Informasi"

# d. Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali!
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka) # angka yang duplikat (10 dan 4), ketika di print() tidak akan muncul lebih dari 1x.