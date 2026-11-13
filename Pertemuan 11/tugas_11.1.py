import datetime
import os
import string
import random

# template dict perpustakaan
perpustakaan_template = {
    'judul_buku' : 'judul_buku',
    'penulis' : 'penulis',
    'tahun_terbit' : 'tahun_terbit',
    'tanggal_terakhir_pinjam' : datetime.datetime(1111,1,11),
    'status' : "status"
}

data_perpustakaan = {}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG': ^20}")
    print(f"{'DATA perpustakaan': ^20}")
    print("-"*20)
    perpustakaan = dict.fromkeys(perpustakaan_template.keys())
    perpustakaan['judul_buku'] = input("Judul buku: ")
    perpustakaan['penulis'] = (input("Penulis buku: "))
    TAHUN_TERBIT = int(input("Tahun terbit (YYYY): "))
    BULAN_TERBIT = int(input("Bulan terbit (1-12): "))
    TANGGAL_TERBIT = int(input("Tanggal terbit (1-31): "))
    perpustakaan['tahun_terbit'] = datetime.datetime(TAHUN_TERBIT,BULAN_TERBIT,TANGGAL_TERBIT)
    TAHUN_PINJAM = int(input("Tahun pinjam (YYYY): "))
    BULAN_PINJAM = int(input("Bulan pinjam (1-12): "))
    TANGGAL_PINJAM = int(input("Tanggal pinjam (1-31): "))
    perpustakaan['tanggal_pinjam'] = datetime.datetime(TAHUN_PINJAM,BULAN_PINJAM,TANGGAL_PINJAM)
    perpustakaan['status'] = input("Status buku: ")
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_perpustakaan.update({KEY:perpustakaan})

    # dari program sebelumnya, hilangkan beasiswa
    print(f"\n{'KEY': <6} {'Judul': <50} {'Penulis': <17} {'Tahun terbit': <10} {'Tanggal pinjam': <10} {'Status': <15}")
    print('-' * 60)

    for perpustakaan in data_perpustakaan:
        KEY = perpustakaan
        JUDUL = data_perpustakaan[KEY]['judul_buku']
        PENULIS = data_perpustakaan[KEY]['penulis']
        tahun_terbit = data_perpustakaan[KEY]['tahun_terbit'].strftime("%x")
        tanggal_pinjam = data_perpustakaan[KEY]['tanggal_pinjam'].strftime("%x")
        STATUS = data_perpustakaan[KEY]['status']
        
        
        print(f"{KEY: <6} {JUDUL: <50} {PENULIS: <17} {tahun_terbit:^10} {tanggal_pinjam:^10} {STATUS: <15}")
    
    print("\n")
    is_done = input("Mau ditambah lagi datanya? (y/n)? ")
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih")