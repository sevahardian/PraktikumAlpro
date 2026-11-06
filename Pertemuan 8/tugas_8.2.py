# a. Buatlah sebuah dictionary bernama data_mahasiswa dengan pasangan key-value berikut:
#   - "nim": "240101"
#   - "nama": "Budi Santoso"
#   - "prodi": "Teknologi Informasi"

data_mahasiswa = {
    "nim" : "240101",
    "nama" : "Budi Santoso",
    "prodi" : "Teknologi Informasi"
}

# b. Ubah nilai "prodi" menjadi "Sastra Mesin " sekaligus menambahkan key baru "angkatan" dengan nilai 2026.
data_mahasiswa.update({"prodi" : "Sastra Mesin"})
data_mahasiswa.update({"angkatan" : 2026})

# c. Hapus data "nim", lalu tampilkan hasil akhir dictionary ke layar.
del data_mahasiswa["nim"]

print(data_mahasiswa)