# Set

# Note: Uncomment blok program (contoh) yang akan di run.

'''
# Membuat set
A = set("Belajar Python")                       # Set dinamis
print(A)
print("Tipe data dari A =", type(A))
print('')
B = frozenset("More Than Robotics Learning")     # Set static
print(B)
print("Tipe data dari B =", type(B))
'''

# Operasi Pada Set
# ----------------

'''
# 1. Menambah Elemen Set
C = set("Robonesia")        # Sebuah set
print("Nilai set C = ", C)
C.add("Oke!")               # Cara 1, Menambah elemen set
print("Nilai set C baru = ",C)
print('')
D = set("Belajar Pemrograman")
print("Nilai set D  = ", D)
D.update("Python")          # Cara 2, Menambah elemen set
print("Nilai set D baru = ", D)
'''

'''
# 2.1 Menghapus Set & Elemen Set (Pada Set Dinamis)
E = set("Welcome to Python")    # Set dinamis (mutable)
print(E)
E.remove("t")       # Hapus elemen set E, yaitu "t"
print(E)
del E               # Hapus set E
print(E)
'''

'''
# 2.2 Menghapus Set & Elemen Set (Pada Set Statis)
F = frozenset("Selamat Datang")    # Set statis (immutable)
print(F)
#F.remove("D")       # Hapus elemen set F, yaitu "D"
#print(F)
F.add('Temanku')    # Menambah elemen ke dalam set F
print(F)
'''

'''
# 3. Operasi Keanggotaan (Membership)
H = set("Selamat Pagi")
print("Set H =", H)
print("Apakah S anggota set H? = ", "S" in H)
print("Apakah P bukan anggota set H? = ", "P" not in H)
print("Apakah u anggota set H? = ", "u" in H)
print("Apakah g anggota set H? = ", "g" in H)
'''

'''
# 4. Operasi Gabungan & Irisan (Union & Intersection)
I = set("Belajar Pemrograman")
J = frozenset("Bahasa Python")
print("Set I = ", I)
print("Set J = ", J)
K = I | J       # Operasi gabungan (Union)
L = I & J       # Operasi irisan (Intersection)
print("Union set I | J = ", K)
print("Intersection set I & J = ", L)
'''

'''
# 5.1 Operasi Perbandingan(1)
M = set("Belajar Python")
N = set("alerBaj nohtyP")           # Acak
print("Set M = ", M)
print("Set N = ", N)
print("Apakah M == N? - ", M == N)  # Sama dengan
print("Apakah M != N? - ", M != N)  # Tidak sama dengan
'''

'''
# 5.2 Operasi Perbandingan(2) - Superset & Subset
O = set("Python Coding")
P = set("Coding")
print("Set O = ", O)
print("Set P = ", P)
print("Apakah O superset P? - ", O > P)     # O superset P
print("Apakah O superset P? - ", O >= P)    # O superset P
print("Apakah O subset P? - ", O < P)       # O subset P
print("Apakah O subset P? - ", O <= P)      # O subset P
'''

'''
# 6. Operasi Komplemen (Difference)
Q = set("Kota Jogja")
R = frozenset("Kota Batam")
print(" Set Q = ", Q)
print(" Set R = ", R)
S = Q - R       # Q komplemen R
T = R - Q       # R komplemen Q
print(" Q komplemen R = ", S)
print(" R komplemen Q = ", T)
'''

'''
# 7. Operasi Symetric Difference
U = set("Kota Batam")
V = set("Kota Bogor")
print("Set U = ", U)
print("Set V = ", V)
W = U^V         # U symetric difference V
print("U symmetric difference V = ", W)
'''

'''
# Operasi Menggunakan Fungsi Built-In Pada Set
X = set("Robotika")
Y = set("Robonesia")
print("Set X = ", X)
print("Set Y = ", Y)
print('')
print("Apakah X subset Y? - ", X.issubset(Y))
print("Apakah X superset Y? - ", X.issuperset(Y))
print("X Union Y = ", X.union(Y))
print("X Intersection Y = ", X.intersection(Y))
print("X Komplemen Y = ", X.difference(Y))
print("X symetric_difference Y = ", X.symmetric_difference(Y))
'''
