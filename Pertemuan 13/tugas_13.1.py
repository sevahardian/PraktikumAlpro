def rekap_denda(data):
    hasil = {}
    tarif_denda = 2000
    
    for item in data:
        nama = item["nama"]
        denda = item["hari_terlambat"] * tarif_denda
        
        if nama not in hasil:
            hasil[nama] = {"total_buku": 0, "total_denda": 0}
        hasil[nama]["total_buku"] += 1
        hasil[nama]["total_denda"] += denda
    return hasil
    
peminjaman = [ 
    {"nama": "Rina", "judul": "Algoritma Dasar", "hari_terlambat": 2},     
    {"nama": "Bima", "judul": "Struktur Data", "hari_terlambat": 0},   
    {"nama": "Rina", "judul": "Basis Data", "hari_terlambat": 4},  
    {"nama": "Sari", "judul": "Jaringan Komputer", "hari_terlambat": 1},  
    {"nama": "Bima", "judul": "Pemrograman Web", "hari_terlambat": 3}  
]

print(rekap_denda(peminjaman))