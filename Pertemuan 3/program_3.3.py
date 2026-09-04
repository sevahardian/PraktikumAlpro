# Operasi Komperasi di Python

# Setiap hasil dari operasi komperasi adalah boolean (T/F)

a = 4
b = 2

# Lebih besar dari (>)
print("\n ============== Lebih Besar Dari (>) ==============")

hasil = a > 3
print(a, ">", 3, "=", hasil)

hasil = b > 3
print(b, ">", 3, "=", hasil)

hasil = a > 4
print(a, ">", 4, "=", hasil)

hasil = b > 2
print(b, ">", 2, "=", hasil)

print(a, ">", b, "=", hasil)

# Kurang dari (<)
print("\n ============== Kurang Dari (<) ==============")

hasil = a < 3
print(a, "<", 3, "=", hasil)

hasil = b < 3
print(b, "<", 3, "=", hasil)

hasil = a < 4
print(a, "<", 4, "=", hasil)

hasil = b < 2
print(b, "<", 2, "=", hasil)

print(a, "<", b, "=", hasil)

# Lebih besar dari sama dengan (>=)
print("\n ============== Lebih Besar Dari Sama Dengan (>=) ==============")

hasil = a >= 3
print(a, ">=", 3, "=", hasil)

hasil = b >= 3
print(b, ">=", 3, "=", hasil)

hasil = a >= 4
print(a, ">=", 4, "=", hasil)

hasil = b >= 2
print(b, ">=", 2, "=", hasil)

print(a, ">=", b, "=", hasil)

# Kurang dari sama dengan (<=)
print("\n ============== Kurang Dari Sama Dengan (<=) ==============")

hasil = a <= 3
print(a, "<=", 3, "=", hasil)

hasil = b <= 3
print(b, "<=", 3, "=", hasil)

hasil = a <= 4
print(a, "<=", 4, "=", hasil)

hasil = b <= 2
print(b, "<=", 2, "=", hasil)

print(a, "<=", b, "=", hasil)

# Sama dengan (==)
print("\n ============== Sama Dengan (==) ==============")

hasil = a == 4
print(a, "==", 4, "=", hasil)

hasil = b == 4
print(b, "==", 4, "=", hasil)

# Tidak Sama Dengan (!=)
print("\n ============== Tidak Sama Dengan (!=) ==============")

hasil = a != 4
print(a, "!=", 4, "=", hasil)

hasil = b != 4
print(b, "!=", 4, "=", hasil)

# 'is' sebagai komperasi object identity (bukan literal)
print("\n ============== Object Identity (is) ==============")

x = 5 # ini adalah assignment membuat object
y = 5 # ini adalah assignment membuat object

hasil = x is y
print("x", "(", x, ") is y", "(", y, ") =", hasil)

# 'is not' sebagai komperasi object identity (bukan literal)
print("\n ============== Object Identity (is not) ==============")

x = 5 # ini adalah assignment membuat object
y = 5 # ini adalah assignment membuat object

hasil = x is not y
print("x", "(", x, ") is not y", "(", y, ") =", hasil)
