# Menggunakan modul lingkaran Global
# Modul di copy-paste di directory C:\Program Files\Python310\Lib

import lingkaran                    # Memanggil modul "lingkaran" yang Global

print("Menghitung Luas & Keliling Lingkaran")

print("Phi = ", lingkaran.phi)      # Memanggil variabel "phi"
r = int(input("Masukkan nilai jari-jari lingkaran: "))

L = lingkaran.luas(r)               # Memanggil fungsi "luas"
K = lingkaran.keliling(r)           # Memanggil fungsi "keliling"
print("Luas lingkaran: ",L)         # Menghitung luas lingkaran
print("Keliling lingkaran: ",K)     # Menghitung keliling lingkaran
