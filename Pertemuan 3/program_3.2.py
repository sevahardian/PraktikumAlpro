# Latihan konversi satuan temperature (suhu?)

# Program konversi celcius (c) ke satuan temperature lainnya

print("\n \t PROGRAM KONVERSI TEMPERATURE")

celcius = float(input("\n Masukkan suhu dalam celcius: "))
print("\n Suhu saat ini adalah", celcius, "Celcius")

print("\n =====================================================")

# Reamur
reamur = (4/5) * celcius
print("\n Suhu saat ini dalam Reamur adalah", reamur, "Reamur")

# Fahrenheit
fahrenheit = (9/5) * celcius + 32
print("\n Suhu saat ini dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("\n Suhu saat ini dalam Kelvin adalah", kelvin, "Kelvin")