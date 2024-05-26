# Operator dalam bahasa pemrograman Python

# Operator aritmatika
'''
x = 7
y = 6

# Penjumlahan
print("Penjumlahan, x(7) + y(6) = ", x + y)

# Pengurangan
print("Pengurangan, x(7) - y(6) = ", x - y)

# Perkalian
print("Perkalian, x(7) * y(6) = ", x * y)

# Pembagian
print("Pembagian, x(7) / y(6) = ", x / y)

# Modulo (Sisa hasil bagi)
print("Modulo, x(7) % y(6) = ", x % y)

# Eksponen/Perpangkatan
print("Eksponen, x(7)**y(6) = ", x**y)

# Pembagian bilangan bulat yang dibulatkan
print("Floor Division, x(7)//y(6) = ", x//y)
'''


# Operator perbandingan/relasional
'''
x = 17
y = 13

# Operasi cek persamaan
print("Cek persamaan, x(17) == y(13) ", x == y)

# Operasi cek ketidaksamaan
print("Cek ketidaksamaan, x(17) != y(13) ", x != y)

# Operasi cek lebih besar
print("Cek lebih besar, x(17) >y(13) ", x > y)

# Operasi cek lebih kecil
print("Cek lebih kecil, x(17) <y(13) ", x < y)

# Operasi cek lebih besar atau sama dengan
print("Cek lebih besar atau sama dengan, x(17) >= y(13) ", x >= y)

# Operasi cek lebih kecil atau sama dengan
print("Cek lebih kecil atau sama dengan, x(17) <= y(13) ", x <= y)
'''


# Operator penugasan (Assigns)
'''
x = 3
y = 5

x += y
print("Hasil dari operasi x+=y adalah: ", x)

x *= y
print("Hasil dari operasi x*=y adalah: ", x)    # x = x*y

x /= y
print("Hasil dari operasi x/=y adalah: ", x)

x %= y
print("Hasil dari operasi x%=y adalah: ", x)

x **= y
print("Hasil dari operasi x**=y adalah: ", x)   # x = x**5

x //= y
print("Hasil dari operasi x//=y adalah: ", x)
'''


# Operator bitwise
'''
x = 7      # 7 dalam bilangan biner = 0000 0111
y = 3      # 3 dalam bilangan biner = 0000 0011
print("x AND y: ", x & y)             # Bitwise AND
print("x OR y: ", x | y)              # Bitwise OR
print("x XOR y: ", x ^ y)             # Bitwise XOR
print("NOT x: ", ~x)                  # Bitwise NOT
print("x GESER KANAN y: ", x >> y)    # Right Shift
print("x GESER KIRI y: ", x << y)     # Left Shift
'''


# Operator Logika
'''
A = True
B = False
print('A and B = ', A and B)
print('A or B  = ', A or B)
print('not A   = ', not A)
print('not B   = ', not B)
'''

# Operator Keanggotaan (Membership)
'''
var1 = 'Sahabat Robonesia' 	    # string
var2 = {1:'a',2:'b',3:'c'}	    # dictionary

print('R' in var1)
print('Sahabat' not in var2)
print(1 in var2)
print('c' in var2)
print(3 in var2)
'''

# Penggunaan fungsi Identitas id()
'''
t = 157
print(id(t))    # Nilai id/identitas/alamat memori dari variabel 't'
'''

# Note: fungsi Identitas id() - Apabila nilai 2 variabel bertipe data int lebih dari 256
'''
t = 256
u = 256
v = 559
w = 559
print("Alamat memori variabel t: ", id(t))    # Nilai id variabel 't'
print("Alamat memori variabel u: ", id(u))    # Nilai id variabel 'u'
print("")
print("Alamat memori variabel v: ", id(v))    # Nilai id variabel 'v'
print("Alamat memori variabel w: ", id(w))    # Nilai id variabel 'w'
'''

# Operator Identitas

a = 10
b = 10
print("Alamat memori variabel a: ", id(a))      # Nilai id variabel 'a'
print("Alamat memori variabel b: ", id(b))      # Nilai id variabel 'b'
print("Apakah a adalah b:", a is b)             # Operator identitas
print("Apakah a bukanlah b:", a is not b)       # Operator identitas

print("")

c = [2,4,6,8]   
d = [2,7,6,9]
print("Alamat memori variabel c: ", id(c))    # Nilai id variabel 'c'
print("Alamat memori variabel d: ", id(d))    # Nilai id variabel 'd'
print("Apakah c adalah d:", c is d)           # Operator identitas
print("Apakah c bukanlah d:", c is not d)     # Operator identitas

print("")

e = 'Robonesia'
f = "Robonesia"
print("Alamat memori variabel e: ", id(e))    # Nilai id variabel 'e'
print("Alamat memori variabel f: ", id(f))    # Nilai id variabel 'f'
print("Apakah e adalah f:", e is f)           # Operator identitas
print("Apakah e bukanlah f:", e is not f)     # Operator identitas
