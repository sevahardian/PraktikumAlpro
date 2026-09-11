# Operasi logika atau Boolean

# NOT, OR, AND, XOR

print("=== NOT ===")

a = True
b = not a

print("data a adalah", a)

print("----- NOT")

print("data b adalah", b)

# OR (jika salah 1 nilai TRUE, maka hasilnya adalah TRUE)
print("=== OR ===")

a = False
b = False
c = a or b

print(a, "OR", b, "adalah", c)

a = False
b = True
c = a or b

print(a, "OR", b, "adalah", c)

a = True
b = False
c = a or b

print(a, "OR", b, "adalah", c)

a = True
b = True
c = a or b

print(a, "OR", b, "adalah", c)


# AND (jika 2 buah nilai TRUE, maka hasil TRUE)
print("=== AND ===")

a = False 
b = False 
c = a and b 

print(a, "AND", b, "adalah", c)
 
a = False 
b = True 
c = a and b
 
print(a, "AND", b, "adalah", c)
 
a = True 
b = False 
c = a and b 

print(a, "AND", b, "adalah", c) 

a = True 
b = True 
c = a and b
 
print(a, "AND", b, "adalah", c) 
 
# XOR (akan TRUE jika salah 1 nilai TRUE, sisanya akan bernilai FALSE, ke-2 nilai berbeda) 
print("=== XOR ===") 

a = False 
b = False 
c = a ^ b 

print(a, "XOR", b, "adalah", c) 

a = False 
b = True 
c = a ^ b 

print(a, "XOR", b, "adalah", c) 

a = True 
b = False 
c = a ^ b 

print(a, "XOR", b, "adalah", c) 

a = True 
b = True 
c = a ^ b 

print(a, "XOR", b, "adalah", c) 