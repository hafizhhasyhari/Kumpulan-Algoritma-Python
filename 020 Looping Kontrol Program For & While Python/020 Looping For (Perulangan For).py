# Kontrol Program - For

# Uncomment blok program contoh yang akan dijalankan!

'''
# Menampilkan isi suatu list dengan perulangan "for"
# Perulangan berdasar data suatu list

list_lauk = ["Tahu","Tempe","Krupuk","Perkedel","Telor ceplok","Telor dadar"]
print("Daftar lauk: ")
for t in list_lauk:
    print(t)        # Menampilkan elemen list_lauk
'''

'''
# Menampilkan isi suatu list dengan perulangan "for"
# Perulangan berdasarkan indeks suatu list

list_olahraga = ["Basket","Volley","Futsal","Takraw","Soccer","Base ball"]
panjangList = len(list_olahraga)
print("Daftar Olahraga dengan Bola: ")
for s in range(panjangList):                                 # indeks dari list
    print("Olahraga dengan bola: ", list_olahraga[s])        # Menampilkan elemen list_olahraga
'''

'''
# Program menampilka indeks dan elemen tuple
# Perulangan for menggunakan fungsi enumerate()

tuple_kota = ("Lampung","Palembang","Jambi","Riau","Medan","Pekanbaru")
print("Nama kota di Sumatera:")
for index,elemen in enumerate(tuple_kota):   # Perulangan dengan fungsi enumerate()
    print(index+1,". ",elemen)               # Menampilkan index & elemen tuple
'''

'''
# Penggunaan fungsi range() format ke-1
awal=int(input("Masukkan nilai awal : "))   # Memasukkan nilai awal dari keyboard
akhir=int(input("Masukkan nilai akhir : "))   # Memasukkan nilai akhir dari keyboard
selisih=int(input("Masukkan nilai selisih : "))   # Memasukkan nilai selisih dari keyboard
print('')
print("Nilai dalam range adalah:")
print("-------------------------")
for t in range(awal,akhir,selisih):
    print(t)                                # Menampilkan nilai dalam range
'''

'''
# Penggunaan fungsi range() format ke-2
awal=int(input("Masukkan nilai awal : "))   # Memasukkan nilai awal dari keyboard
akhir=int(input("Masukkan nilai akhir : "))   # Memasukkan nilai akhir dari keyboard
print('')
print("Nilai dalam range adalah:")
print("-------------------------")
for u in range(awal,akhir):
    print(u)                                # Menampilkan nilai dalam range
'''

'''
# Penggunaan fungsi range() format ke-3 (1st)
akhir=int(input("Masukkan nilai akhir: "))   # Memasukkan nilai akhir dari keyboard
print("Silakan Masukkan Elemen List:")
print("-----------------------------")
data_list=[]                            # Buat list kosong
for v in range(akhir):
    elemen=input(v+1)          # Menunggu input dari keyboard
    data_list.insert(v,elemen)       # Menyisipkan elemen ke dalam data_list
print("")

print("Isi data_List adalah:")
print("---------------------")
for w in range(akhir):
    print(data_list[w])                         # Menampilkan nilai dalam data_list
'''

'''
# Penggunaan fungsi range() format ke-3 (2nd)
akhir = 3
for a in range(akhir):
    print ("Hello Sahabat Robonesia")
'''

'''
# Fungsi sorted() pada struktur for
# Menampilkan data list setelah diurutkan
nilai_list =[13,7,3,11]        # List yang belum diurutkan
print("Data list sebelum diurutkan:")
for b in nilai_list:
    print(b)

print()

print("Data list setelah diurutkan:")
for c in sorted(nilai_list):
    print(c)
'''

'''
# Fungsi reserved() pada struktur for
# Menampikan data tuple setelah dibalik urutannya
data_tuple=("Jogja","Surabaya","Bandung")  # Tuple yang belum diurutkan
print("Data nama kota sebelum dibalik:")
for d in data_tuple:
    print(d)

print()

print("Data nama kota setelah dibalik:")
for e in reversed(data_tuple):
    print(e)
'''

'''
# Fungsi zip() pada struktur for
data_nama=["Faruq","Farros","Farrel"]	# List nama
data_tahun=[2010,2017,2016]				# List tahun

for f,g in zip(data_nama,data_tahun):
    print(f," lahir pada tahun ",g)
'''

'''
# Statemen For Bersarang (Nested For)
list=[[1,2,3,4],["Jogja","Solo","Klaten"],["C","C++","Python"]]

for x in range(len(list)):
    print("------------","Baris", x+1)
    for y in range(len(list[x])):
        print(list[x][y])
'''
