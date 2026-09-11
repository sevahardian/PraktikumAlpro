usia = int(input("Masukkan usia anda: "))

if usia <= 12:
    kategori = "Anak-anak"
elif usia <= 17:
    kategori = "Remaja"
elif usia <= 59:
    kategori = "Dewasa"
elif usia >= 60:
    kategori = "Lansia"
else:
    kategori = "Tidak valid"

print("Usia anda adalah", usia, "tahun, anda dikategorikan sebagai", kategori)

print("Akhir dari program 'KATEGORI USIA BERDASARKAN KRITERIA TERTENTU'")
