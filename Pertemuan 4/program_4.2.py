# Latihan Logika dan Komparasi 
 
# membuat gabungan area rentang dari angka 
 
# +++++3-----10+++++ 
 
angka = float(input("Masukan angka yang bernilai \n kurang dari 3 \n atau \n lebih besar dari 10 \n :")) 
 
# +++++3-----
# memeriksa angka kurang dari 3 
isKurangDari = angka < 3 
print("Kurang dari 3 adalah", isKurangDari) 
 
# -----10+++++
# memeriksa angka lebih dari 10 
isLebihDari = angka > 10
print("Lebih dari 10 adalah", isLebihDari)

hasil = isKurangDari or isLebihDari 
print("angka yang anda masukan: ", hasil)

print("========================================") 
 
# -----3+++++10----- 
# kasus irisan 
 
angka = float(input("masukan angka yang bernilai \n lebih dari 3 \n dan \n kurang dari 10 \n :")) 
 
# -----3+++++ 
# lebih dari 3 
isLebihDari = angka > 3 
print("Lebih dari 3 = ",isLebihDari) 
 
# +++++10----- 
# kurang dari 10 
isKurangDari = angka < 10 
print("Kurang dari 10 = ",isKurangDari) 
 
hasil = isKurangDari and isLebihDari 
print("angka yang anda masukan: ", hasil)