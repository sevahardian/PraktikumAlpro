import datetime
import random
import string
import os

os.system("cls")

BARIS = ["A", "B", "C", "D", "E"]
KOLOM = 6
MAKS_KURSI = 6
BIAYA_LAYANAN = 3000
MAKS_DISKON = 30
BATAS_BATAL_JAM = 2

films = {
    1: {
        "judul": "Petualangan Langit",
        "genre": "Aksi",
        "rating": "SU",
        "durasi": 110,
        "jam": (("13:00", "Regular"), ("16:30", "Premiere"), ("19:30", "IMAX"))
    },
    2: {
        "judul": "Malam Berdarah",
        "genre": "Horor",
        "rating": "D17+",
        "durasi": 100,
        "jam": (("15:00", "Regular"), ("20:00", "Regular"))
    },
    3: {
        "judul": "Cinta di Ujung Hujan",
        "genre": "Drama",
        "rating": "R13+",
        "durasi": 120,
        "jam": (("12:00", "Regular"), ("17:30", "Premiere"))
    },
    4: {
        "judul": "Kota Tanpa Tidur",
        "genre": "Thriller",
        "rating": "D21+",
        "durasi": 130,
        "jam": (("21:00", "Regular"),)
    }
}

pesanan_template = {
    "kode": "000000",
    "id_jadwal": 0,
    "id_film": 0,
    "waktu": datetime.datetime(1111, 1, 1),
    "studio": "Regular",
    "kursi": [],
    "total": 0,
    "metode": "Tunai",
    "status": "aktif"
}

jadwal = []
data_pesanan = {}

def buat_jadwal():
    id_jadwal = 1
    hari_ini = datetime.date.today()

    for id_film, f in films.items():
        for tambah in range(3):
            tgl = hari_ini + datetime.timedelta(days=tambah)
            for jam_str, studio in f["jam"]:
                jam, menit = [int(x) for x in jam_str.split(":")]
                waktu = datetime.datetime(tgl.year, tgl.month, tgl.day, jam, menit)

                denah = {}
                for b in BARIS:
                    for k in range(1, KOLOM + 1):
                        denah[f"{b}{k}"] = True

                jadwal.append({
                    "id": id_jadwal,
                    "id_film": id_film,
                    "waktu": waktu,
                    "studio": studio,
                    "kursi": denah
                })
                id_jadwal += 1

def input_angka(pesan, minimal, maksimal):
    while True:
        teks = input(pesan).strip()
        if not teks.isdigit():
            print("\t[!] Input harus berupa angka bulat!")
        else:
            nilai = int(teks)
            if nilai < minimal or nilai > maksimal:
                print(f"\t[!] Pilihan harus antara {minimal} sampai {maksimal}!")
            else:
                return nilai

def buat_kode():
    while True:
        KEY = "".join((random.choice(string.ascii_uppercase) for _ in range(6)))
        if KEY not in data_pesanan:
            return KEY

def cari_jadwal(id_jadwal):
    for j in jadwal:
        if j["id"] == id_jadwal:
            return j
    return None

def sisa_kursi(j):
    sisa = 0
    for kosong in j["kursi"].values():
        if kosong:
            sisa += 1
    return sisa

def rp(angka):
    return f"Rp {angka:,}".replace(",", ".")

def cek_usia(rating, usia):
    if rating == "SU":
        return True
    elif rating == "R13+":
        return usia >= 13
    elif rating == "D17+":
        return usia >= 17
    elif rating == "D21+":
        return usia >= 21
    else:
        return False

def harga_dasar(waktu, studio):
    hari = waktu.weekday()

    if hari >= 5:
        harga = 50000
    elif hari == 4:
        harga = 40000
    else:
        harga = 35000

    if studio == "Premiere":
        harga += 25000
    elif studio == "IMAX":
        harga += 40000

    return harga

def hitungPemesanan(harga, jumlah, waktu, pelajar=False):
    subtotal = harga * jumlah

    persen = 0
    if waktu.weekday() == 2:
        persen += 10
    if pelajar:
        persen += 10

    if persen > MAKS_DISKON:
        persen = MAKS_DISKON

    diskon = (subtotal * persen) // 100
    layanan = BIAYA_LAYANAN * jumlah
    total = subtotal - diskon + layanan

    return {
        "subtotal": subtotal,
        "persen": persen,
        "diskon": diskon,
        "layanan": layanan,
        "total": total
    }

hitung_total = hitungPemesanan

def tampilkan_header():
    print("=" * 60)
    print(f"{'SELAMAT DATANG DI CINEMA XXI':^60}")
    print(f"{'SISTEM PEMESANAN TIKET BIOSKOP MANDIRI':^60}")
    print("=" * 60)

def tampilkan_menu():
    tampilkan_header()
    print(" 1. Lihat Daftar Film Sedang Tayang")
    print(" 2. Pesan Tiket Bioskop")
    print(" 3. Lihat Pesanan Saya")
    print(" 4. Batalkan Pesanan")
    print(" 5. Keluar dari Program")
    print("-" * 60)

def tampilkan_film():
    print("\n" + "=" * 65)
    print(f"{'DAFTAR FILM SEDANG TAYANG':^65}")
    print("=" * 65)
    print(f"{'NO':<4} {'JUDUL FILM':<25} {'GENRE':<12} {'RATING':<8} {'DURASI':<10}")
    print("-" * 65)

    for id_film, f in films.items():
        durasi_str = f"{f['durasi']} Menit"
        print(f"{id_film:<4} {f['judul']:<25} {f['genre']:<12} {f['rating']:<8} {durasi_str:<10}")

    print("=" * 65)

def tampilkan_kursi(j):
    print("\n" + "=" * 45)
    print(f"{'DENAH KURSI BIOSKOP (' + j['studio'] + ')':^45}")
    print(f"{'=================== LAYAR ===================':^45}")
    for b in BARIS:
        print("\t", end="")
        for k in range(1, KOLOM + 1):
            kode = f"{b}{k}"
            if j["kursi"][kode]:
                print(f"[{kode}]", end=" ")
            else:
                print("[XX]", end=" ")
        print()
    print("=" * 45)
    print("\tKeterangan: [XX] = Kursi Terisi / Tidak Tersedia\n")

def cetak_tiket(p):
    print("\n" + "=" * 50)
    print(f"{'E-TICKET RESMI BIOSKOP XXI':^50}")
    print("=" * 50)
    print(f" Kode Booking    : {p['kode']}")
    print(f" Judul Film      : {films[p['id_film']]['judul']}")
    print(f" Studio          : {p['studio']}")
    print(f" Waktu Tayang    : {p['waktu'].strftime('%d-%m-%Y %H:%M')}")
    print(f" Nomor Kursi     : {', '.join(p['kursi'])}")
    print(f" Metode Bayar    : {p['metode']}")
    print(f" Total Bayar     : {rp(p['total'])}")
    print(f" Status Pesanan  : {p['status'].upper()}")
    print("=" * 50)
    print(f"{'Harap tunjukkan tiket ini saat masuk studio':^50}")
    print("=" * 50 + "\n")

def pilih_tanggal(id_film):
    sekarang = datetime.datetime.now()
    tanggal = []

    for j in jadwal:
        if j["id_film"] == id_film and j["waktu"] > sekarang:
            tgl = j["waktu"].strftime("%Y-%m-%d")
            if tgl not in tanggal:
                tanggal.append(tgl)

    if len(tanggal) == 0:
        print("\n\t[!] Tidak ada jadwal tayang yang tersedia untuk film ini.")
        return None

    print("\n" + "-" * 35)
    print(f"{'PILIH TANGGAL TAYANG':^35}")
    print("-" * 35)
    for i in range(len(tanggal)):
        print(f" {i + 1}. {tanggal[i]}")
    print("-" * 35)

    no = input_angka("Pilih nomor tanggal: ", 1, len(tanggal))
    return tanggal[no - 1]

def pilih_jadwal(id_film, tgl):
    sekarang = datetime.datetime.now()
    pilihan = []

    for j in jadwal:
        if j["id_film"] == id_film \
                and j["waktu"].strftime("%Y-%m-%d") == tgl \
                and j["waktu"] > sekarang:
            pilihan.append(j)

    if len(pilihan) == 0:
        print("\n\t[!] Tidak ada jam tayang yang tersedia.")
        return None

    print("\n" + "-" * 60)
    print(f"{'PILIH JAM TAYANG & STUDIO':^60}")
    print("-" * 60)
    print(f" {'NO':<4} {'JAM':<8} {'STUDIO':<12} {'HARGA':<14} {'KETERANGAN':<16}")
    print("-" * 60)

    for i in range(len(pilihan)):
        j = pilihan[i]
        harga = harga_dasar(j["waktu"], j["studio"])
        sisa = sisa_kursi(j)
        info = "SOLD OUT" if sisa == 0 else f"Sisa {sisa} Kursi"
        jam_tayang = j["waktu"].strftime("%H:%M")
        print(f" {i + 1:<4} {jam_tayang:<8} {j['studio']:<12} {rp(harga):<14} {info:<16}")
    print("-" * 60)

    while True:
        no = input_angka("Pilih nomor jam tayang: ", 1, len(pilihan))
        if sisa_kursi(pilihan[no - 1]) == 0:
            print("\t[!] Jadwal ini telah SOLD OUT, silakan pilih jam yang lain!")
        else:
            return pilihan[no - 1]

def pilih_kursi(j, jumlah):
    while True:
        tampilkan_kursi(j)
        teks = input(f"Pilih {jumlah} nomor kursi (pisahkan dengan koma, misal A1,A2): ")
        pilihan = [x.strip().upper() for x in teks.split(",")]

        valid = True
        if len(pilihan) != jumlah:
            print(f"\t[!] Anda harus memilih tepat {jumlah} kursi!")
            valid = False
        elif len(set(pilihan)) != len(pilihan):
            print("\t[!] Terdapat kursi duplikat dalam pilihan Anda!")
            valid = False
        else:
            for k in pilihan:
                if k not in j["kursi"]:
                    print(f"\t[!] Kursi {k} tidak terdaftar pada denah!")
                    valid = False
                    break
                elif not j["kursi"][k]:
                    print(f"\t[!] Kursi {k} sudah terisi oleh penonton lain!")
                    valid = False
                    break

        if valid:
            return pilihan

def proses_bayar(total):
    print("\n" + "-" * 35)
    print(f"{'METODE PEMBAYARAN':^35}")
    print("-" * 35)
    print(" 1. Tunai (Cash)")
    print(" 2. E-Wallet (GoPay / OVO / Dana)")
    print(" 3. Transfer Bank (Virtual Account)")
    print("-" * 35)
    metode = input_angka("Pilih metode pembayaran (1-3): ", 1, 3)

    if metode == 1:
        while True:
            teks = input(f"Total tagihan: {rp(total)}. Masukkan nominal uang tunai: Rp ")
            if not teks.isdigit():
                print("\t[!] Input pembayaran harus berupa angka nominal!")
            else:
                uang = int(teks)
                if uang < total:
                    print(f"\t[!] Uang Anda kurang {rp(total - uang)}!")
                else:
                    kembalian = uang - total
                    if kembalian > 0:
                        print(f"\t[✓] Kembalian Anda: {rp(kembalian)}")
                    print("\t[✓] Pembayaran tunai lunas dan diterima.")
                    return "Tunai"
    elif metode == 2:
        print("\t[✓] Pembayaran E-Wallet berhasil dikonfirmasi.")
        return "E-Wallet"
    else:
        print("\t[✓] Transfer bank terverifikasi otomatis.")
        return "Transfer Bank"

def buat_pesanan():
    tampilkan_film()
    id_film = input_angka("Pilih nomor film yang ingin ditonton: ", 1, len(films))
    film = films[id_film]

    if film["rating"] != "SU":
        print(f"\n[INFO] Film '{film['judul']}' memiliki klasifikasi usia: {film['rating']}")
        usia = input_angka("Masukkan usia Anda: ", 1, 100)
        if not cek_usia(film["rating"], usia):
            print(f"\n[!] Mohon maaf, usia Anda ({usia} tahun) tidak memenuhi syarat rating {film['rating']}!")
            return

    tgl = pilih_tanggal(id_film)
    if tgl is None:
        return

    j = pilih_jadwal(id_film, tgl)
    if j is None:
        return

    sisa = sisa_kursi(j)
    jumlah = input_angka(f"Jumlah tiket yang ingin dipesan (1-{min(MAKS_KURSI, sisa)}): ", 1, min(MAKS_KURSI, sisa))
    kursi = pilih_kursi(j, jumlah)

    print("\n--- Promo & Penawaran Spesial ---")
    pelajar = input_angka("Apakah Anda Pelajar / Mahasiswa? (1=Ya, 2=Tidak): ", 1, 2) == 1

    harga = harga_dasar(j["waktu"], j["studio"])
    r = hitung_total(harga, jumlah, j["waktu"], pelajar=pelajar)

    print("\n" + "=" * 45)
    print(f"{'RINCIAN PEMBAYARAN':^45}")
    print("=" * 45)
    print(f" Tiket ({jumlah}x @ {rp(harga)}) : {rp(r['subtotal'])}")
    print(f" Diskon ({r['persen']}%)         : -{rp(r['diskon'])}")
    print(f" Biaya Layanan           : {rp(r['layanan'])}")
    print("-" * 45)
    print(f" TOTAL TAGIHAN           : {rp(r['total'])}")
    print("=" * 45)

    metode = proses_bayar(r["total"])

    for k in kursi:
        j["kursi"][k] = False

    KEY = buat_kode()
    pesanan_baru = dict.fromkeys(pesanan_template.keys())
    pesanan_baru["kode"] = KEY
    pesanan_baru["id_jadwal"] = j["id"]
    pesanan_baru["id_film"] = id_film
    pesanan_baru["waktu"] = j["waktu"]
    pesanan_baru["studio"] = j["studio"]
    pesanan_baru["kursi"] = kursi
    pesanan_baru["total"] = r["total"]
    pesanan_baru["metode"] = metode
    pesanan_baru["status"] = "aktif"

    data_pesanan.update({KEY: pesanan_baru})
    cetak_tiket(pesanan_baru)

def lihat_pesanan():
    if len(data_pesanan) == 0:
        print("\n\t[!] Belum ada data pesanan tiket yang tersimpan.")
        return

    print("\n" + "=" * 92)
    print(f"{'DAFTAR PESANAN TIKET SAYA':^92}")
    print("=" * 92)
    print(f"{'KODE':<8} {'JUDUL FILM':<22} {'JADWAL':<16} {'STUDIO':<10} {'KURSI':<12} {'TOTAL':<12} {'STATUS':<10}")
    print("-" * 92)

    for KEY in data_pesanan:
        p = data_pesanan[KEY]
        judul = films[p["id_film"]]["judul"]
        waktu_str = p["waktu"].strftime("%d/%m %H:%M")
        kursi_str = ", ".join(p["kursi"])
        total_str = rp(p["total"])
        status_str = p["status"].capitalize()

        print(f"{KEY:<8} {judul:<22} {waktu_str:<16} {p['studio']:<10} {kursi_str:<12} {total_str:<12} {status_str:<10}")

    print("=" * 92 + "\n")

def batalkan_pesanan():
    if len(data_pesanan) == 0:
        print("\n\t[!] Belum ada pesanan yang dapat dibatalkan.")
        return

    kode = input("Masukkan kode booking tiket yang ingin dibatalkan: ").strip().upper()

    if kode in data_pesanan:
        p = data_pesanan[kode]

        if p["status"] != "aktif":
            print(f"\n\t[!] Pesanan dengan kode '{kode}' sudah dibatalkan sebelumnya.")
            return

        sisa_waktu = p["waktu"] - datetime.datetime.now()
        if sisa_waktu < datetime.timedelta(hours=BATAS_BATAL_JAM):
            print(f"\n\t[!] Pembatalan ditolak: Pembatalan hanya diperbolehkan maksimal {BATAS_BATAL_JAM} jam sebelum tayang.")
            return

        p["status"] = "dibatalkan"

        j = cari_jadwal(p["id_jadwal"])
        if j is not None:
            for k in p["kursi"]:
                j["kursi"][k] = True

        print(f"\n\t[✓] Pesanan '{kode}' berhasil dibatalkan. Kursi {', '.join(p['kursi'])} telah dikosongkan.")
        return

    print(f"\n\t[!] Kode booking '{kode}' tidak ditemukan dalam database!")

def main():
    buat_jadwal()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tampilkan_film()
        elif pilihan == "2":
            buat_pesanan()
        elif pilihan == "3":
            lihat_pesanan()
        elif pilihan == "4":
            batalkan_pesanan()
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan sistem pemesanan tiket XXI!")
            print("Akhir dari program, terima kasih.\n")
            break
        else:
            print("\n[!] Pilihan menu tidak valid! Silakan masukkan angka 1-5.\n")

if __name__ == "__main__":
    main()
