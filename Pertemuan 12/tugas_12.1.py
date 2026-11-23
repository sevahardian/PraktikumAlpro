# Buatlah program dengan input dan fungsi untuk menghitung:

import os
import math

os.system("clear")

# a. Luas persegi panjang
def luasPersegiPanjang(panjang_pp, lebar_pp):
    luas_pp = panjang_pp * lebar_pp
    return luas_pp

print(" -- Luas Persegi Panjang -- ")
panjang_pp = float(input("Masukkan panjang persegi panjang: "))
lebar_pp = float(input("Masukkan lebar persegi panjang: "))
luas_pp = luasPersegiPanjang(panjang_pp, lebar_pp)
print(f"Luas persegi panjang dengan panjang {panjang_pp} cm dan lebar {lebar_pp} cm adalah {luas_pp} cm2 \n")

# b. Volume balok
def volumeBalok(panjang_balok, lebar_balok, tinggi_balok):
    volume_balok = panjang_balok * lebar_balok * tinggi_balok
    return volume_balok

print(" -- Volume Balok -- ")
panjang_balok = float(input("Masukkan panjang balok: "))
lebar_balok = float(input("Masukkan lebar balok: "))
tinggi_balok = float(input("Masukkan tinggi balok: "))
volume_balok = volumeBalok(panjang_balok, lebar_balok, tinggi_balok)
print(f"Volume balok dengan panjang {panjang_balok} cm, lebar {lebar_balok} cm dan tinggi {tinggi_balok} adalah {volume_balok} cm3 \n")

# c. Luas lingkaran
def luasLingkaran(jari2_lingkaran):
    luas_lingkaran = math.pi * (jari2_lingkaran ** 2)
    return luas_lingkaran

print(" -- Luas Lingkaran -- ")
jari2_lingkaran = float(input("Masukkan jari-jari lingkaran: "))
luas_lingkaran = luasLingkaran(jari2_lingkaran)
print(f"Luas lingkaran dengan jari2 {jari2_lingkaran} cm adalah {luas_lingkaran} cm2 \n")

# d. Volume bola
def volumeBola(jari2_bola):
    volume_bola = 4/3 * math.pi * (jari2_bola ** 3)
    return volume_bola

print(" -- Volume Bola -- ")
jari2_bola = float(input("Masukkan jari-jari bola: "))
volume_bola = volumeBola(jari2_bola)
print(f"Volume bola dengan jari2 {jari2_bola} cm adalah {volume_bola} cm3 \n")

