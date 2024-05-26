# Tipe Data

# Tipe data integer - bil. bulat
A = 167
B = -237

print("A adalah bilangan bulat positif:", A)
print("B adalah bilangan bulat negatif:", B)

# 300 dalam format biner, oktal, desimal, dan heksadesimal
C = 300             # Bilangan desimal
D = 0b100101100     # Bilangan biner
E = 0o454           # Bilangan oktal
F = 0x12c           # Bilangan heksadesimal

print(C); print(D); print(E); print(F)

# Tipe data float - bil. pecahan
G = 457.97  # Bilangan pecahan positif
H = -35.90  # Bilangan pecahan negatif
I = G + H

print("Hasil perjumlahan bilangan float:", I)

# Bilangan imaginer (komplek)
P = 5               # Bilangan integer
Q = 3*(7+3j)        # Bilangan komplek(1)
R = complex(5,7)    # Bilangan komplek(2)
S = P + Q + R

print("Hasil perjumlahan bilangan komplek:", S)


# Fungsi real & imag
bilKomp = 7+3j    # Bilangan komplek

print("Bilangan komplek", bilKomp)
print("Bagian real:", bilKomp.real)
print("Bagian imaginer:", bilKomp.imag)
