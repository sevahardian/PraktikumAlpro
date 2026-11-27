# akses variabel global dalam fungsi

nama_global = "Ridwan" # <- variabel global  

def fungsi():  
    print(f"fungsi menampilkan {nama_global}")
fungsi() 