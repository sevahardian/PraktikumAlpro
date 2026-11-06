## Dictionary

# list → array, mengakses dengan menggunakan index

data_list = ["ucup", "rendi", "salsa"]
print(data_list[0])

# dictionary (dict) → associative array
# identifier → key

data_dict = {
    "key": "value",
    "cp": "ucup",
    "rd": "rendi",
    "sl": "salsa",
    "number": 100,
    "list": data_list
}

# menambah petik di cp, number, dan list
print(data_dict["cp"])
print(data_dict["number"])
print(data_dict["list"])