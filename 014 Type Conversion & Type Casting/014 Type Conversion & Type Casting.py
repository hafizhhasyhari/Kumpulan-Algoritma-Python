# Data Type COnversion & Type Casting

# Converting integer to float
'''
angka_int = 175     # Type data integer
angka_flo = 1.75    # Type data float
penjumlahan = angka_int + angka_flo

print("Tipe data angka_int:",type(angka_int))
print("Tipe data angka_flo:",type(angka_flo))

print("Hasil penjumlahan:",penjumlahan)
print("Tipe data hasil penjumlahan:",type(penjumlahan))
'''

# Converting penjumalahan data integer dan string -> error
'''
data_int = 179
data_str = "654"

print("Tipe data data_int:",type(data_int))
print("Tipe data data_str:",type(data_str))

print(data_int + data_str)
'''

# Contoh type casting (Konversi antara data string, integer, dan float)
'''
a = int("123")      # Konversi string to integer
print(a)

b = str(342)         # Konversi integer to string
print(b)

c = int(144.7)       # Konversi float to integer
print(c)

d = float('77')      # Konversi string to float
print(d)
'''


# Penjumalahan data integer dan string,
# dengan data string dikonversi ke integer terlebihdahulu
'''
data_int = 179      # Data integer
data_str = "654"    # Data string

print("Tipe data data_int:",type(data_int))
print("Tipe data data_str:",type(data_str))

data_str = int(data_str)    # data string dikonversi menjadi data integer
penjumlahan = data_int + data_str

print("Hasil penjumlahan: ",penjumlahan)
print("Tipe data Hasil penjumlahan:",type(penjumlahan))
'''
