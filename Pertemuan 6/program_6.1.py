## Nested If

status_akun = "aktif"
saldo = 750000
nominal_tarik = 500000

if status_akun == "aktif":
    if nominal_tarik <= saldo:
        if nominal_tarik >= 50000:
            saldo = saldo - nominal_tarik
            print(f"Penarikan saldo berhasil: Rp. {nominal_tarik: } ")
            print(f"Sisa saldo: Rp. {saldo: } ")
        else:
            print("Gagal: Penarikan minimal Rp.50.000,00.")
    else:
        print("Gagal: Saldo anda tidak mencukupi.")
else:
    print("Akses ditolak: Akun anda sedang diblokir.")