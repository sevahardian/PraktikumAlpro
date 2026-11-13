import datetime
import os
import string
import random

# template dict mahasiswa
mahasiswa_template = {
    'nama' : 'nama',
    'nim' : '00000000',
    'sks_lulus' : 0,
    'terbit' : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    # os.system("cls") # untuk windows
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    TAHUN_terbit = int(input("Tahun terbit (YYYY): "))
    BULAN_terbit = int(input("Bulan terbit (1-12): "))
    TANGGAL_terbit = int(input("Tanggal terbit (1-31): "))
    mahasiswa['terbit'] = datetime.datetime(TAHUN_terbit,BULAN_terbit,TANGGAL_terbit)
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    # dari program sebelumnya, hilangkan beasiswa
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal terbit':<10}")
    print('-'*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        terbit = data_mahasiswa[KEY]['terbit'].strftime("%x")
        
        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {terbit:^10}")
    
    print("\n")
    is_done = input("Mau tambah lagi bro (y/n)? ")
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih")