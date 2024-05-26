  // Author by hafizhhasyhari

# List

# Mengakses elemen pada suatu list, menggunakan indeks positif

# List dengan tipe data yang sama
'''
angka = [0,1,2,3,4,5,6,7,8,9]

# Menampilkan nilai index pada suatu list
print("Elemen list ke-0 = ", angka[0])
print("Elemen list ke-7 = ", angka[7])
print("")
# Menampilkan 4 data pertama sebuah list
print('Empat data pertama = ', angka[:4])
print("")
# Menampilkan 4 data terakhir sebuah list
print('Empat data terakhir = ', angka[10-4:])
print("")
# Menampilkan data pada rentang indeks tertentu
print('Data rentang index 3 s/d 8 = ', angka[3:8])
'''


# List dengan tipe data yang berbeda-beda
'''
data_list = [ 1, 2, 3, "Hello", 4.9, "Robonesia", 5, 6.8]

print("Tiga data awal = ", data_list[:3])
print('Data setelah INDEKS ke-3 = ', data_list[4:])
print("Tiga data terakhir = ", data_list[len(data_list)-3:])
'''


# Mengakses elemen pada suatu list, menggunakan indeks negatif
'''
angka = [0,1,2,3,4,5,6,7,8,9]

print("Elemen list ke -10 = ", angka[-10])
print("Elemen list ke -8 = ", angka[-8])
print("Menampilkan 3 elemen pertama = ", angka[:-7])
print("Menampilkan elemen setelah indeks -7 = ", angka[-7:])
'''

# Mengetahui Panjang Suatu List
'''
A = len(data_list)
print("Panjang Data_list = ", A)
'''



# ----------------------------------
# Modifikasi List Menggunakan Indeks

# 1-Mengubah elemen list
'''
data_list1 = [ 7, 5, 9, "Belajar", 7.9, "Python", 10, 7.8]
print(data_list1)               # Tampilkan data list
data_list1[6]= "di Robonesia"   # Mengubah elemen ke-6
print(data_list1)               # Tampilkan data yang telah berubah
data_list1[0]= "Ayo ..."        # Mengubah elemen ke-0
print(data_list1)               # Tampilkan data yang telah berubah
'''


# 2-Menyisipkan elemen ke dalam List
'''
data_list2 = [8, 2, "Belajar", 7.9, "Python", 10.2]
print(data_list2)                           # Tampilkan data list
data_list2[:0]=["Sahabat Robonesia"]        # Menyisipkan elemen pada indeks pertama
data_list2[len(data_list2):]=["Yuks!"]      # Menyisipkan elemen pada indeks terakhir
print(data_list2)
'''


# 3-Menghapus Elemen dalam List
'''
data_list3 = ["Batam", 8, "Riau", "Jogja", 7.9, "Wonogiri", 10.2]
print(data_list3)
data_list3[3:6]=[]     # Menghapus elemen indeks 3 s/d 5
print(data_list3)
'''



# ----------------------------------
# Modifikasi List Menggunakan Fungsi

# 1.1-Menyisipkan elemen ke dalam List dengan fungsi append()
'''
A = [45, 90, 135]
print("List A = ", A)       # Tampilkan data list A
A.append(180)               # Sisipkan angka 180 di akhir list
print("List A baru = ", A)  # Tampilkan data list A setelah disisipi
'''

# 1.2-Menyisipkan elemen ke dalam List dengan fungsi insert()
'''
B = [30, 90, 120, 150]
print("List B = ", B)       # Tampilkan data list B
B.insert(1, "Enam puluh")   # Sisipkan "Enam puluh" pada indeks ke-1
print("List B baru = ", B)  # Tampilkan data list B setelah disisipi
'''

# 1.3-Menyisipkan List ke dalam list lain dengan fungsi extend()
'''
C = [70, 140, 210]
D = ["Apel", "Jeruk", "Mangga"]
print("List C = ", C)       # Tampilkan data list C
print("List D = ", D)       # Tampilkan data list D
C.extend(D)                 # Menyisipkan list D ke dalam list C
print("List baru setelah di extend = ", C)  # List baru setelah di extend
'''


# 2-Menghapus List dengan fungsi del dan remove()
'''
kota = ["Jogja", "Klaten", "Solo", "Sukoharjo", "Wonogiri"]
print(kota)         # Tampilkan list kota
del kota[2]         # Hapus elemen indeks 2
print(kota)
kota.remove("Klaten")   # Hapus elemen bernilai "Klaten"
print(kota)
'''


# 3.1-Mengurutkan list data integer & Membalik Elemennya
'''
bilangan = [25, 19, 35, 47, 77, 63, 81, 94, 101]
print("List angka = ", bilangan)
bilangan.sort()                     # Urutkan elemen list dengan 'sort'
print("Hasil sort = ", bilangan)

AA = sorted(bilangan)               # Urutkan elemen list dengan 'sorted'
print("Hasil sorted = ", AA)
bilangan.reverse()                  # Balik urutan list elemen
print("Hasil reverse = ", bilangan)
'''


# 3.2-Mengurutkan list data string & Membalik Elemennya
'''
sayur = ['bayam', 'kangkung', 'wortel', 'sawi', 'tomat', 'kubis']
print("List sayur = ", sayur)
sayur.sort()                        # Urutkan elemen list dengan 'sort'
print("Hasil sort = ", sayur)

BB = sorted(sayur)                  # Urutkan elemen list dengan 'sorted'
print("Hasil sorted = ", BB)
sayur.reverse()                     # Balik urutan list elemen
print("Hasil reverse = ", sayur)
'''


# 4-Operasi Aritmatika Pada List
'''
data = ["Robonesia"]*3
print(data)
data2 = ["Robonesia"] + ["More than robotics learning"]
print(data2)
'''


# 5-Menggunakan Operator in Pada List
'''
programming = ["java", "C", "C++", "python", "PHP"]
print("Apakah pemrograman C++ ada = ", "C++" in programming)
print("Apakah pemrograman Jawa ada = ", "Jawa" in programming)
print("Apakah pemrograman Python ada = ", "python" in programming)
'''


# List Bersarang/List 2-Dimensi
# ------------------------------

# 1-Membuat list 2-dimensi
'''
data1_2D = [["Raspberry", "Blueberry", "Blackberry"],[3, 5, 7]]
print(data1_2D)      # Tampilkan list 2D 2x3 (2 baris, 3 kolom)
'''

# 2-Mengakses list 2-dimensi
'''
data2_2D = [["Lampung", "Palembang", "Jambi"],[1, 2, 3]]
print(data2_2D)         # Tampilkan list 2D 2x3 (2 baris, 3 kolom)
print(data2_2D[0][1:])  # Menampilkan elemen pada baris-0
print(data2_2D[1][1:])  # Menampilkan elemen pada baris-1
'''

# 3-List 2-dimensi dengan jumlah elemen berbeda
'''
data3_2D = [["Bali", "Surabaya", "Semarang", "Bandung"],["Apel", "Peer"],["Red", "Green", "Blue"]]
print(data3_2D)         # Tampilkan list 2D
print(data3_2D[0][0:])  # Menampilkan elemen pada baris-0
print(data3_2D[1][0:])  # Menampilkan elemen pada baris-1
print(data3_2D[2][0:])  # Menampilkan elemen pada baris-2
'''
