# String

# Penugasan String pada Variabel
'''
a = "Kawan Hafizh"
print(a)
b = a
print(b)
c = 'Hallo apa kabar '
print(c)
gabungan_string = c + a
print(gabungan_string)
'''

# Mengakses Anggota String
'''
a = 'Sahabat Robonesia'
print(a[3])     # Akses karakter index ke-3
print(a[:3])    # Akses karakter sebelum index ke-3
print(a[3:])    # Akses karakter index ke-3 dan setelahnya
'''

# Menambah String
'''
kata = "Kami Cinta Indonesia"
print(kata)
kata = kata[:11] + "Tanah Air" + kata[10:]
print(kata)
'''

# Menghapus String (1)
'''
kata = "Kami Cinta Indonesia"
print(kata)
kata = ""          # Menghapus string dalam variabel 'kata'
print(kata)        # Data string tidak tertampil, karena sudah terhapus
'''

# Menghapus String (2)
'''
kata = "Kami Cinta Tanah Air Indonesia"
kata = kata[:11] + "" + kata[21:]
print(kata)
'''

# Penggunaan fungsi upper()& lower()
'''
sapaan = "Haloo, Kawan Hafizh"
up = sapaan.upper()		# Mengubah menjadi huruf besar
lo = sapaan.lower()		# Mengubah menjadi huruf kecil
print(sapaan)
print(up)
print(lo)
'''

# Penggunaan Fungsi len()
'''
sapaan = "Haloo, Kawan Hafizh di mana pun Anda berada!"
t = len(sapaan)
print(sapaan)
print("Panjang string adalah: ", t)
'''

# Penggunaan Fungsi rjust(),ljust(),center()
'''
sapaan = "Haloo, Kawan Hafizh di mana pun Anda berada!"
print (sapaan.center(50))   # Rata tengah
print (sapaan.rjust(80))    # Rata kanan
print (sapaan.ljust(70))    # Rata kiri
'''

# Penggunaan Fungsi join()
'''
kata1 = "Hallo"; kata2 = "Sahabat"; kata3 = "Hafizh!"
C = ['Hallo','Kawan','Hafizh!']        # List C
print ("List C:", C)
print ("Kalimat penjumlahan kata:", kata1+kata2+kata3)       # Menggabung string dengan tanda +
print ("Kalimat dari list: " + "".join(C))                   # Menggabung string dengan fungsi join()
'''

# Penggunaan Fungsi index()
'''
kata = "Hai, Kawan Hafizh!"
print ("No. Indeks huruf i: ", kata.index('i'))
print ("No. Indeks huruf Sa: ", kata.index('Sa'))
print ("No. Indeks huruf Ro: ", kata.index('Ro'))
'''

# Penggunaan Fungsi replace()
'''
kalimat1 = "Haloo, nama saya Kirito"
kalimat2 = kalimat1.replace('Kirito','Suyadhi')
print (kalimat1)
print (kalimat2)
'''

# Menampilkan String Terformat
'''
string1 = "satu"
string2 = "dua"
string3 = "tiga"
string4 = "empat"
print ("%s %s %s %s" %(string1,string2,string3,string4))
print ("Motor saya beroda %s" %(string2))
print ("Motor mempunyai %s roda, sedangkan Mobil mempunyai %s roda" %(string2,string4))
'''
