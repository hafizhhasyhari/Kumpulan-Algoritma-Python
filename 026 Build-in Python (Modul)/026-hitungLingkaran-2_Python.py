# Menggunakan modul lingkaran yang directory penyimpannya didaftarkan terlebihdahulu

import sys
sys.path.append("E:\PROGRAMMING\Pemrograman Python - 2 - PyCharm\pycharm_workspace\lingkaran")

import lingkaran                    # Memanggil modul "lingkaran"

print("Menghitung Luas & Keliling Lingkaran")

print("Phi = ", lingkaran.phi)
r = int(input("Masukkan nilai jari-jari lingkaran: "))

L = lingkaran.luas(r)
K = lingkaran.keliling(r)
print("Luas lingkaran: ",L)         # Menghitung luas lingkaran
print("Keliling lingkaran: ",K)     # Menghitung keliling lingkaran
