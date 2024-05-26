import lingkaran                    # Memanggil modul "lingkaran"

print("Menghitung Luas & Keliling Lingkaran")

print("Phi = ", lingkaran.phi)	   # Memanggil variabel “phi”
r = int(input("Masukkan nilai jari-jari lingkaran: "))

L = lingkaran.luas(r)		   # Memanggil fungsi “luas”
K = lingkaran.keliling(r)		   # Memanggil fungsi “keliling”
print("Luas lingkaran: ",L)         # Menghitung luas lingkaran
print("Keliling lingkaran: ",K)     # Menghitung keliling lingkaran
