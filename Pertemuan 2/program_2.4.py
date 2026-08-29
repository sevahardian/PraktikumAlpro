# Kita belajar Casting
# merubah tipe data ke tipe data lainnya
# tipe data = integer (int), float, string (str), boolean (bool)

# INTEGER ke Tipe data lainnya

data_int = 9

data_float = float(data_int)
data_string = str(data_int)
data_boolean = bool(data_int) # akan False jika nilai integer = 0

print ("data = ", data_float, ", type = ", type(data_float))
print ("data = ", data_string, ", type = ", type(data_string))
print ("data = ", data_boolean, ", type = ", type(data_boolean))

# FLOAT ke Tipe data lainnya

data_float = 9.9

data_integer = int(data_float)
data_string = str(data_float)
data_boolean = bool(data_float) # akan False jika nilai float = 0

print ("data = ", data_integer, ", type = ", type(data_integer))
print ("data = ", data_string, ", type = ", type(data_string))
print ("data = ", data_boolean, ", type = ", type(data_boolean))

# STRING ke Tipe data lainnya

data_string = "100"

data_integer = int(data_string)
data_float = float(data_string)
data_boolean = bool(data_string)

print ("data = ", data_integer, ", type = ", type(data_integer))
print ("data = ", data_float, ", type = ", type(data_float))
print ("data = ", data_boolean, ", type = ", type(data_boolean))