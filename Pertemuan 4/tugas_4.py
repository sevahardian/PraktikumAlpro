usia = int(input("Masukkan usia anda: "))

if usia >= 60:
    kategori = "Lansia"
elif usia >= 18:
    kategori = "Dewasa"
elif usia >= 13:
    kategori = "Remaja"
elif usia >= 0:
    kategori = "Anak-anak"
else:
    kategori = "Tidak valid"

print("Usia anda adalah", usia, "tahun, anda dikategorikan sebagai", kategori)

print("Akhir dari program 'KATEGORI USIA BERDASARKAN KRITERIA TERTENTU'")