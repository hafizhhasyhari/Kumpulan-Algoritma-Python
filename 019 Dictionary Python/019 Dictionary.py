# Dictionary

# Uncomment untuk menjalankan blok program contoh!

'''
# Membuat Dictionary
A = {1:"Bayam",2:"Sawi",3:"Kangkung"}
B = {'satu':"Batam",'dua':"Jogja",'tiga':"wonogiri"}
print("Dictionary A = ", A)
print("Dictionary B = ", B)
'''

'''
# 1. Mengakses Elemen Dictionary
C = {'satu':"Batam",'dua':"Jogja",'tiga':"Wonogiri"}
print("Dictionary C = ", C)
print("Elemen dictionary ke-1: ", C['satu'])    # Mengakses elemen ke-1
print("Elemen dictionary ke-2: ", C['dua'])     # Mengakses elemen ke-2
print("Elemen dictionary ke-3: ", C['tiga'])    # Mengakses elemen ke-2
'''

'''
# 2. Menambah Elemen Dictionary
D = {'satu':"Jawa",'dua':"Sumatera",'tiga':"Kalimantan"}
print("Dictionary D = ", D)
D['empat']="Sulawesi"       # Menambah Elemen Dictionary ke-4
print("Dictionary D update = ", D)
'''

'''
# 3. Mengubah Elemen Dictionary
E = {'satu': 'Jawa', 'dua': 'Sumatera', 'tiga': 'Kalimantan', 'empat': 'Sulawesi'}
print("Dictionary E = ", E)
E['tiga']="Papua"           # Mengubah Elemen Dictionary ke-4
print("Dictionary E edit = ", E)
'''

'''
# 4. Menghapus Elemen Dictionary
buah = {1:"Pepaya",2:"Durian",3:"Peer",4:"Appel",5:"Jeruk"}
print("Dictionary buah: ", buah)
del buah[2]                             # Menghapus Elemen Dictionary ke-2
print("Dictionary buah-edit1: ", buah)
buah.pop(5)                             # Menghapus Elemen Dictionary ke-5
print("Dictionary buah-edit2: ", buah)
'''

'''
# 5. Menghapus Seluruh Elemen Dictionary
material = {1:"batu",2:"bata",3:"pasir",4:"semen",5:"ubin"}
print("Dictionary material: ", material)
material.clear()
print("Dictionary material - edit: ", material)
'''

'''
# 6. Operasi Keanggotaan (Membership)
komponen = {1:"R",2:"C",3:"L",4:"D",5:"LED",6:"BJT",7:"FET",8:"MOSFET"}
print("Data Komponen: ", komponen)
print("Apakah 5 anggota komponen? : ", 5 in komponen)
print("Apakah 7 anggota komponen? : ", 7 in komponen)
print("Apakah 9 anggota komponen? : ", 9 in komponen)
print("Apakah 8 bukan anggota komponen? : ", 8 not in komponen)
'''

'''
# Fungsi-Fungsi Pada Dictionary
electronics1 = {1:"R",2:"C",3:"L",4:"D",5:"LED",6:"BJT",7:"FET"}
print("Panjang electronics1: ", len(electronics1))  # Menampilkan panjang "electronics1"
print("All element: ", electronics1.items())         # Menampilkan seluruh elemen
print("All keys: ", electronics1.keys())            # Menampilkan seluruh kunci
print("All values: ", electronics1.values())        # Menampilkan seluruh nilai
print("Get values: ", electronics1.get(7))          # Mendapatkan nilai elemen kunci-7
print("Hapus elemen ke-5: ", electronics1.pop(5))   # Menghapus elemen ke-5

electronics2 = {8:"MOSFET",9:"IC"}
print("Panjang electronics2: ", len(electronics2))  # Menampilkan panjang "electronics2"
# print("Bandingkan: ", cmp(electronics1,electronics2))  # Bandingkan "electronics1" vs. "electronics2"
# print("Menambah elemen: ", electronics1.update(electronics2))     # Menambah elemen
# print("Search a key: ", electronics1.has_key(6))  # Mencari kunci(6)
'''
