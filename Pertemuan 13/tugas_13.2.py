def rekap_lembur(data):
    hasil = {}
    upah_lembur = 25000
    lembur = 8
    
    for item in data:
        nama = item["nama"]
        jam_kerja = item["jam_kerja"]
        if item["jam_kerja"] > lembur:
            jam_lembur = item["jam_kerja"] - lembur
        else:
            jam_lembur = 0
        total_upah_lembur = jam_lembur * upah_lembur
        
        if nama not in hasil:
            hasil[nama] = {"total_jam_kerja": 0, "total_uang_lembur": 0}
        hasil[nama]["total_jam_kerja"] += jam_kerja
        hasil[nama]["total_uang_lembur"] += total_upah_lembur
    return hasil
    
absensi = [  
    {"nama": "Dina", "jam_kerja": 9},  
    {"nama": "Riko", "jam_kerja": 8},  
    {"nama": "Dina", "jam_kerja": 10},  
    {"nama": "Santi", "jam_kerja": 7},  
    {"nama": "Riko", "jam_kerja": 11}  
] 

print(rekap_lembur(absensi))