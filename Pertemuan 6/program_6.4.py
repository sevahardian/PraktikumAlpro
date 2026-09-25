## for in while

sesi = 1

while sesi <= 2:
    print(f"Sesi ke-{sesi}: ")
    
    for antrean in range(1, 4):
        print(f"Melayani pasien nomor: {antrean}.")
    sesi += 1
    print("===")