# 'is' sebagai komperasi object identity (bukan literal)
print("===== Object Identity (is) =====")

x = 5 # ini adalah assignment membuat object
y = 5 # ini adalah assignment membuat object

hasil = x is y
print("x", (x), "is y", (y), "=", hasil)