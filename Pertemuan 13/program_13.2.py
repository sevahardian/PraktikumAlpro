angka = 0  
def ubah_angka(nilai_baru):  
    global angka # fungsi ini mendapat akses merubah angka  
    angka = nilai_baru  
    
print(f"Sebelum {angka}")  
ubah_angka(10)  
print(f"Sesudah {angka}") 