for angka in range(2, 101):
    for i in range(2, angka):
        if angka % i == 0:
            break
    else:
        print(f"\n Angka {angka} -> angka prima")