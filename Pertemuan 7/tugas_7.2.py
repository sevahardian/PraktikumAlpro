# Diberikan list berikut:
angka = [75, 80, 90, 75, 85, 100, 65]

# a. Cari tahu di indeks ke berapa skor 100 berada.
index_100 = angka.index(100)
print(f"Skor 100 ada di indeks ke {index_100}.")

# b. Hitung ada berapa banyak siswa yang mendapatkan skor 75.
jumlah_skor_100 = angka.count(75)
print(f"Banyak siswa yang mendapatkan skor 75 adalah {jumlah_skor_100} orang.")

# c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar.
angka.sort()
print(f"Urutan skor ujian dari nilai terkecil hingga terbesar = \n{angka}")

# d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil.
angka.reverse()
print(f"Urutan skor ujian dari nilai terbesar ke terkecil = \n{angka}")