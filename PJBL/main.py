# ==============================================================================
# PROJECT BASED LEARNING (PJBL) - ALGORITMA DAN PEMROGRAMAN
# SISTEM PEMESANAN TIKET BIOSKOP (XXI MINI)
#
# Referensi Implementasi Materi Praktikum 1 - 12:
# - Pertemuan 1 : Output print(), escape sequence (\n, \t), komentar, identitas
# - Pertemuan 2 : Tipe data (int, float, str, bool), type casting, input data
# - Pertemuan 3 : Operasi aritmatika (+, -, *, //, %) & perbandingan (==, >, <)
# - Pertemuan 4 : Logika boolean (not, and, or) & percabangan if-elif-else (kategori usia)
# - Pertemuan 5 : Perulangan (for, while, range, break, continue)
# - Pertemuan 6 : Nested conditionals (nested if) & nested loop (grid kursi)
# - Pertemuan 7 : Manipulasi List (indexing, append, in, len)
# - Pertemuan 8 : Tuple (jadwal), Set (validasi duplikat), Dictionary (items, keys, update)
# - Pertemuan 11: Template dictionary (fromkeys), random key, format tabel f-string, datetime
# - Pertemuan 12: Pembuatan fungsi (def), argumen, return value, default argument
# ==============================================================================

# ## --- IMPORT MODUL (Pertemuan 11 & 12) ---
import datetime
import random
import string
import os


# Bersihkan layar konsol (Cross-platform support: Windows cls / Linux macOS clear)
# Sesuai contoh Pertemuan 11 & 12
os.system("cls" if os.name == "nt" else "clear")


# ==============================================================================
# 1. KONSTANTA & DATA MASTER (Pertemuan 2, 7 & 8)
# ==============================================================================
# Pertemuan 7 (List): Baris denah bioskop
BARIS = ["A", "B", "C", "D", "E"]
KOLOM = 6
MAKS_KURSI = 6

# Pertemuan 2 (Tipe Data Numerik & String)
BIAYA_LAYANAN = 3000
MAKS_DISKON = 30            # Maksimal batas diskon akumulatif (30%)
BATAS_BATAL_JAM = 2         # Pembatalan maksimal 2 jam sebelum tayang

# Pertemuan 7 (List) & Pertemuan 8 (Dictionary)
TANGGAL_MERAH = ["2026-12-25", "2027-01-01"]
KODE_PROMO = {
    "HEMAT5": 5,
    "XXI15": 15,
    "ALPRO20": 20
}

# Pertemuan 8 (Dictionary Cabang Bioskop)
cabang = {
    1: "XXI Grand Indonesia",
    2: "XXI Plaza Senayan",
    3: "XXI Kota Kasablanka"
}

# Pertemuan 8 (Nested Dictionary & Tuple): Daftar Film
# Setiap jadwal tayang disimpan dalam Tuple (jam, tipe_studio)
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


# ==============================================================================
# 2. TEMPLATE STRUKTUR DATA & PENYIMPANAN (Pertemuan 11: Dictionary Template)
# ==============================================================================
# Template pesanan sesuai pola Pertemuan 11 (program_11.2, program_11.3 & tugas_11.1)
pesanan_template = {
    "kode": "000000",
    "id_jadwal": 0,
    "id_cabang": 0,
    "id_film": 0,
    "waktu": datetime.datetime(1111, 1, 1),
    "studio": "Regular",
    "kursi": [],
    "total": 0,
    "metode": "Tunai",
    "status": "aktif"
}

# Tempat penyimpanan data utama (Pertemuan 8 & 11)
jadwal = []        # List of dictionary: jadwal tayangan dan denah kursi
data_pesanan = {}  # Dictionary of dictionary: database transaksi pesanan berdasarkan KEY


# ==============================================================================
# 3. SETUP JADWAL TAYANG (Pertemuan 5, 6, 8, 11)
# ==============================================================================
def buat_jadwal():
    """
    Membuat jadwal tayang 3 hari ke depan untuk semua cabang & film.
    Menggunakan nested for loop (Pertemuan 6), datetime (Pertemuan 11),
    dan representasi denah dengan dictionary (Pertemuan 8).
    """
    id_jadwal = 1
    hari_ini = datetime.date.today()

    for id_cabang in cabang:
        for id_film, f in films.items():
            for tambah in range(3):
                tgl = hari_ini + datetime.timedelta(days=tambah)
                for jam_str, studio in f["jam"]:
                    jam, menit = [int(x) for x in jam_str.split(":")]
                    waktu = datetime.datetime(tgl.year, tgl.month, tgl.day, jam, menit)

                    # Inisialisasi denah kursi bioskop (True = kursi kosong / tersedia)
                    denah = {}
                    for b in BARIS:
                        for k in range(1, KOLOM + 1):
                            denah[f"{b}{k}"] = True

                    jadwal.append({
                        "id": id_jadwal,
                        "id_cabang": id_cabang,
                        "id_film": id_film,
                        "waktu": waktu,
                        "studio": studio,
                        "kursi": denah
                    })
                    id_jadwal += 1


# ==============================================================================
# 4. FUNGSI BANTU & UTILITAS (Pertemuan 2, 3, 11, 12)
# ==============================================================================
def input_angka(pesan, minimal, maksimal):
    """
    Validasi input angka dalam rentang tertentu.
    Menggunakan while loop (Pertemuan 5) & type casting (Pertemuan 2).
    """
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
    """
    Membuat kode booking transaksi acak 6 digit karakter unik.
    Sesuai teknik pembuatan KEY acak di Pertemuan 11 (program_11.3 & tugas_11.1).
    """
    while True:
        # 6 karakter acak huruf kapital (Pertemuan 11)
        KEY = "".join((random.choice(string.ascii_uppercase) for _ in range(6)))
        if KEY not in data_pesanan:
            return KEY


def cari_jadwal(id_jadwal):
    """Mencari jadwal berdasarkan id_jadwal dalam list (Pertemuan 7 & 12)."""
    for j in jadwal:
        if j["id"] == id_jadwal:
            return j
    return None


def sisa_kursi(j):
    """Menghitung total kursi yang masih kosong pada suatu jadwal (Pertemuan 5 & 8)."""
    sisa = 0
    for kosong in j["kursi"].values():
        if kosong:
            sisa += 1
    return sisa


def rp(angka):
    """Format tampilan mata uang Rupiah menggunakan f-string (Pertemuan 1 & 11)."""
    return f"Rp {angka:,}".replace(",", ".")


# ==============================================================================
# 5. ATURAN BISNIS & PERHITUNGAN (Pertemuan 3, 4, 12)
# ==============================================================================
def cek_usia(rating, usia):
    """
    Mengecek kesesuaian usia penonton terhadap klasifikasi rating film.
    Menggunakan struktur kontrol if-elif-else (Pertemuan 4/tugas_4.py).
    """
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
    """
    Menentukan harga tiket berdasarkan hari tayang dan tipe studio.
    Menggunakan percabangan dan perbandingan tanggal/hari (Pertemuan 3 & 4).
    """
    hari = waktu.weekday()   # 0 = Senin, ..., 4 = Jumat, 5 = Sabtu, 6 = Minggu
    tgl_str = waktu.strftime("%Y-%m-%d")

    # Tarif berdasarkan hari penayangan
    if tgl_str in TANGGAL_MERAH or hari >= 5:  # Weekend / Tanggal Merah
        harga = 50000
    elif hari == 4:                            # Hari Jumat
        harga = 40000
    else:                                      # Senin - Kamis
        harga = 35000

    # Penyesuaian tarif tipe studio
    if studio == "Premiere":
        harga += 25000
    elif studio == "IMAX":
        harga += 40000

    return harga


def hitungPemesanan(harga, jumlah, waktu, pelajar=False, kode=""):
    """
    Menghitung rincian biaya: subtotal, diskon, biaya layanan, dan total akhir.
    Menerapkan operasi aritmatika (Pertemuan 3), default argument (Pertemuan 12/program_12.4),
    serta pengembalian dictionary (Pertemuan 12/program_12.3).
    """
    # 1. Subtotal (Pertemuan 3: Perkalian)
    subtotal = harga * jumlah

    # 2. Perhitungan Diskon (Pertemuan 4: Logika if)
    persen = 0
    if waktu.weekday() == 2:        # Promo Hari Rabu (Nonton Hemat 10%)
        persen += 10
    if pelajar:                     # Diskon Pelajar / Mahasiswa (10%)
        persen += 10
    if kode in KODE_PROMO:          # Diskon Kode Promo Khusus
        persen += KODE_PROMO[kode]

    # Batasi maksimal diskon (Pertemuan 4)
    if persen > MAKS_DISKON:
        persen = MAKS_DISKON

    # Operasi pembagian bulat // (Pertemuan 3)
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

# Alias fungsi agar kompatibel dengan hitung_total
hitung_total = hitungPemesanan


# ==============================================================================
# 6. TAMPILAN ANTARMUKA & TABEL (Pertemuan 1, 6, 11)
# ==============================================================================
def tampilkan_header():
    """Header aplikasi dengan perataan tengah f-string (Pertemuan 11)."""
    print("=" * 60)
    print(f"{'SELAMAT DATANG DI CINEMA XXI':^60}")
    print(f"{'SISTEM PEMESANAN TIKET BIOSKOP MANDIRI':^60}")
    print("=" * 60)


def tampilkan_menu():
    """Menu utama program bioskop."""
    tampilkan_header()
    print(" 1. Lihat Daftar Film Sedang Tayang")
    print(" 2. Pesan Tiket Bioskop")
    print(" 3. Lihat Pesanan Saya")
    print(" 4. Batalkan Pesanan")
    print(" 5. Keluar dari Program")
    print("-" * 60)


def tampilkan_film():
    """
    Menampilkan daftar film dalam format tabel rapi.
    Menggunakan format lebar kolom f-string dari Pertemuan 11 (program_11.3).
    """
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
    """
    Menampilkan denah layout kursi bioskop secara visual.
    Menggunakan nested for loop dengan parameter end='' (Pertemuan 6/program_6.3).
    """
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
    """
    Mencetak e-ticket resmi dengan formatting rapi (Pertemuan 1 & 11).
    """
    print("\n" + "=" * 50)
    print(f"{'E-TICKET RESMI BIOSKOP XXI':^50}")
    print("=" * 50)
    print(f" Kode Booking    : {p['kode']}")
    print(f" Bioskop         : {cabang[p['id_cabang']]}")
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


# ==============================================================================
# 7. LANGKAH-LANGKAH PEMESANAN (Pertemuan 2, 6, 7, 8)
# ==============================================================================
def pilih_cabang():
    """Memilih cabang bioskop yang tersedia (Pertemuan 8: Dictionary)."""
    print("\n" + "-" * 35)
    print(f"{'PILIH BIOSKOP':^35}")
    print("-" * 35)
    for id_c, nama in cabang.items():
        print(f" {id_c}. {nama}")
    print("-" * 35)
    return input_angka("Pilih nomor bioskop: ", 1, len(cabang))


def pilih_tanggal(id_cabang, id_film):
    """
    Memilih tanggal penayangan yang tersedia.
    Menggunakan manipulasi List (Pertemuan 7).
    """
    sekarang = datetime.datetime.now()
    tanggal = []

    for j in jadwal:
        if j["id_cabang"] == id_cabang and j["id_film"] == id_film and j["waktu"] > sekarang:
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


def pilih_jadwal(id_cabang, id_film, tgl):
    """
    Memilih jam tayang dan studio pada tanggal yang dipilih.
    Format kolom rapi menggunakan f-string (Pertemuan 11).
    """
    sekarang = datetime.datetime.now()
    pilihan = []

    for j in jadwal:
        if j["id_cabang"] == id_cabang and j["id_film"] == id_film \
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
    """
    Memilih kursi dengan validasi ketersediaan dan keunikan kursi.
    Menggunakan Set untuk cek duplikasi (Pertemuan 8/tugas_8.1).
    """
    while True:
        tampilkan_kursi(j)
        teks = input(f"Pilih {jumlah} nomor kursi (pisahkan dengan koma, misal A1,A2): ")
        pilihan = [x.strip().upper() for x in teks.split(",")]

        valid = True
        if len(pilihan) != jumlah:
            print(f"\t[!] Anda harus memilih tepat {jumlah} kursi!")
            valid = False
        elif len(set(pilihan)) != len(pilihan):
            # Pertemuan 8: Set otomatis menghilangkan duplikat; jika panjang berkurang berarti ada duplikat
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
    """
    Memproses pembayaran melalui Tunai, E-Wallet, atau Transfer.
    Menggunakan nested if dan validasi transaksi (Pertemuan 6/program_6.1).
    """
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


# ==============================================================================
# 8. FITUR UTAMA SISTEM (Pertemuan 8 & 11)
# ==============================================================================
def buat_pesanan():
    """
    Alur pemesanan tiket bioskop dari pemilihan hingga pencetakan e-ticket.
    Mengintegrasikan rating film, diskon, dan penyimpanan data dictionary.
    """
    id_cabang = pilih_cabang()

    tampilkan_film()
    id_film = input_angka("Pilih nomor film yang ingin ditonton: ", 1, len(films))
    film = films[id_film]

    # Validasi kesesuaian rating dan usia penonton (Pertemuan 4)
    if film["rating"] != "SU":
        print(f"\n[INFO] Film '{film['judul']}' memiliki klasifikasi usia: {film['rating']}")
        usia = input_angka("Masukkan usia Anda: ", 1, 100)
        if not cek_usia(film["rating"], usia):
            print(f"\n[!] Mohon maaf, usia Anda ({usia} tahun) tidak memenuhi syarat rating {film['rating']}!")
            return

    tgl = pilih_tanggal(id_cabang, id_film)
    if tgl is None:
        return

    j = pilih_jadwal(id_cabang, id_film, tgl)
    if j is None:
        return

    sisa = sisa_kursi(j)
    jumlah = input_angka(f"Jumlah tiket yang ingin dipesan (1-{min(MAKS_KURSI, sisa)}): ", 1, min(MAKS_KURSI, sisa))
    kursi = pilih_kursi(j, jumlah)

    # Diskon dan kode promo
    print("\n--- Promo & Penawaran Spesial ---")
    pelajar = input_angka("Apakah Anda Pelajar / Mahasiswa? (1=Ya, 2=Tidak): ", 1, 2) == 1
    kode_promo = input("Masukkan kode promo (tekan Enter jika tidak ada): ").strip().upper()
    if kode_promo != "" and kode_promo not in KODE_PROMO:
        print("\t[!] Kode promo tidak ditemukan, diskon kode promo diabaikan.")
        kode_promo = ""

    harga = harga_dasar(j["waktu"], j["studio"])
    r = hitung_total(harga, jumlah, j["waktu"], pelajar=pelajar, kode=kode_promo)

    # Rincian perhitungan biaya (Pertemuan 1 & 3)
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

    # Update denah kursi: tandai False (terisi)
    for k in kursi:
        j["kursi"][k] = False

    # Buat entri dictionary menggunakan template dari Pertemuan 11
    KEY = buat_kode()
    pesanan_baru = dict.fromkeys(pesanan_template.keys())
    pesanan_baru["kode"] = KEY
    pesanan_baru["id_jadwal"] = j["id"]
    pesanan_baru["id_cabang"] = id_cabang
    pesanan_baru["id_film"] = id_film
    pesanan_baru["waktu"] = j["waktu"]
    pesanan_baru["studio"] = j["studio"]
    pesanan_baru["kursi"] = kursi
    pesanan_baru["total"] = r["total"]
    pesanan_baru["metode"] = metode
    pesanan_baru["status"] = "aktif"

    # Simpan ke data_pesanan dictionary menggunakan update() (Pertemuan 8 & 11)
    data_pesanan.update({KEY: pesanan_baru})

    # Cetak tiket
    cetak_tiket(pesanan_baru)


def lihat_pesanan():
    """
    Menampilkan seluruh riwayat pesanan dalam format tabel rapi.
    Sesuai gaya penulisan tabel di Pertemuan 11 (program_11.3 & tugas_11.1).
    """
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
    """
    Membatalkan pesanan tiket berdasarkan kode booking (KEY).
    Menerapkan pengecekan key in dict (Pertemuan 8) dan nested if (Pertemuan 6).
    """
    if len(data_pesanan) == 0:
        print("\n\t[!] Belum ada pesanan yang dapat dibatalkan.")
        return

    kode = input("Masukkan kode booking tiket yang ingin dibatalkan: ").strip().upper()

    # Cek apakah key terdapat di dalam dictionary (Pertemuan 8)
    if kode in data_pesanan:
        p = data_pesanan[kode]

        if p["status"] != "aktif":
            print(f"\n\t[!] Pesanan dengan kode '{kode}' sudah dibatalkan sebelumnya.")
            return

        # Validasi batas waktu pembatalan
        sisa_waktu = p["waktu"] - datetime.datetime.now()
        if sisa_waktu < datetime.timedelta(hours=BATAS_BATAL_JAM):
            print(f"\n\t[!] Pembatalan ditolak: Pembatalan hanya diperbolehkan maksimal {BATAS_BATAL_JAM} jam sebelum tayang.")
            return

        # Ubah status pesanan menjadi dibatalkan (Pertemuan 8)
        p["status"] = "dibatalkan"

        # Kembalikan kursi menjadi kosong (True)
        j = cari_jadwal(p["id_jadwal"])
        if j is not None:
            for k in p["kursi"]:
                j["kursi"][k] = True

        print(f"\n\t[✓] Pesanan '{kode}' berhasil dibatalkan. Kursi {', '.join(p['kursi'])} telah dikosongkan.")
        return

    print(f"\n\t[!] Kode booking '{kode}' tidak ditemukan dalam database!")


# ==============================================================================
# 9. PROGRAM UTAMA / MAIN LOOP (Pertemuan 5, 11, 12)
# ==============================================================================
def main():
    """
    Fungsi utama program (Pertemuan 12).
    Menggunakan while loop untuk interaksi menu berkelanjutan (Pertemuan 5 & 11).
    """
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


# Eksekusi program utama
if __name__ == "__main__":
    main()
