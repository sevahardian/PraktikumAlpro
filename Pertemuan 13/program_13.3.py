input_user =  int(input("masukan angka: "))  
hasil = 0  

try:  
    hasil = 10/input_user  
except:  
    print("input tidak boleh 0")  
    
print(f"hasil = {hasil}") 