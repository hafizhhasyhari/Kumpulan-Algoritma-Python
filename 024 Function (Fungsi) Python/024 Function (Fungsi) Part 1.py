# Fungsi - Part 1
# Uncomment blok program yang akan dijalankan!

# Cara Pemanggilan fungsi
'''
def fungsi1():
    print("Aku fungsi1")

def fungsi2():
    print("Aku fungsi2")
    fungsi1()                       # Memanggil fungsi1() dari fungsi2()

def main():
    print("\nPanggil semua fungsi!")
    fungsi2()                       # Memanggil fungsi2() dari fungsi main()

# Program Utama
main()                             # Memanggil main()
'''

# Nilai Balik Fungsi
# Contoh Fungsi tanpa Nilai Balik (Default)
'''
def tampilkan():    # Fungsi tanpa nilai balik (default)
    print("Hello Sahabat Robonesia!")

# Program Utama
tampilkan()         # Panggil fungsi tampilkan() 
t = tampilkan()
print(t)            # Tampilkan nilai balik fungsi default
'''
'''
# Contoh Fungsi Dengan Nilai Balik

def penjumlahan():        # Fungsi dengan nilai balik tunggal
    hasil = 7+8+9
    return hasil

def kota():               # Fungsi dengan nilai balik berupa list
    a = ['Batam','Jogja','Wonogiri','Surabaya']
    return a

def sayur():              # Fungsi dengan nilai balik berupa tuple
    b = ('Bayam',"Kangkung",'Wortel',"Sawi")
    return b

# Program Utama
c = penjumlahan()       # Menugaskan nilai balik fungsi penjumlahan() pada variabel c
print(c)
print(kota())           # Menampilkan nilai balik fungsi kota() secara langsung
print(sayur())          # Menampilkan nilai balik fungsi sayur() secara langsung
'''


# Fungsi dengan argument integer/float
'''
def penjumlahan(a,b):           # Melewatkan argument integer/float
    jum = a+b
    print(a,"+",b," = ", jum)

# Program Utama
pilih = 'y'
while(pilih=="y" or pilih=="Y"):
    c = float(input("A: "))
    d = float(input("B: "))
    penjumlahan(c,d)
    pilih=input("Anda ingin menghitung lagi (y/n): ")
'''

# Fungsi dengan argument string
'''
def programUtama():
    data =  input("Tuliskan kalimat: ")
    jumlah = jumlah_karakter(data)
    print('\nJumlah karakter adalah: ', jumlah)

def jumlah_karakter(string):
    hitung = 0
    indeks = 0
    while (string[indeks]!= '.' and indeks<(len(string)-1)):
        hitung+=1
        indeks+=1
    return hitung+1

programUtama()      # Panggil fungsi utama (main)
'''

# Fungsi dengan argument list/Tuple
'''
def tampilkan_Tuple(tuple):
    for t in range(len(tuple)):
        print(t+1,'.',tuple[t])

def tampilkan_List(list):
    for u in list:
        print(u)

def program_utama():
    list =[1,2,3,4,5]
    tuple=('jogja','solo','klaten','sukoharjo','wonogiri')

    print("Nama-nama kota:")
    tampilkan_Tuple(tuple)
    print('-----------------------')
    print("Ini adalah data list:")
    tampilkan_List(list)

program_utama()         # Panggil program utama
'''

# Fungsi argument formal - argument posisional
'''
def fungsi1(nama):
    print("Assalamu'alaikum", nama)

def fungsi2(nama1,nama2):
    print("Assalamu'alaikum",nama1,"dan",nama2)

fungsi1('Taufiq')           # Memanggil fungsi1
fungsi2('Boby','Budi')      # Memanggil fungsi2

fungsi2('Razak')            # Memanggil fungsi2, namun kurang jumlah argument-nya
'''

# Fungsi argument formal - argument default
'''
def tampilkan(t = 70):  # Fungsi 'tampilkan' dengan argument default
    print(t)

tampilkan()        # Memanggil fungsi 'tampilkan' tanpa melewatkan argument (default)
tampilkan(277)     # Memanggil fungsi 'tampilkan' dengan melewatkan argument (277)
'''

# Fungsi dengan argument berdasarkan panjang variabel - Non-keyword argument (Tuple)
'''
def data_view(a,b,*c):
    print("Formal argument A: ", a)
    print("Formal argument B: ", b)
    for t in c:
        print("Non-keyword argument : ", t)

def utama():
    data_view(100,80,60,'Batam',355,'Jogja')  # Memanggil 6 data

utama()     # Memanggil fungsi utama
'''

# Fungsi dengan argument berdasarkan panjang variabel - Keyword argument (Dictionary)
'''
def data_dict(u,v,**w):
    print("Formal argument U: ", u)
    print("Formal argument V: ", v)
    for t in w.keys():
        print("Keyword argument ",t," : ",w[t])

def utama():
    data_dict(u='Durian',v='777',R=357,S=425,T=757)

utama()     #
