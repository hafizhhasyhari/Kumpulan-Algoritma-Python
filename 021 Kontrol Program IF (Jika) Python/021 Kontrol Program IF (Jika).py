# Kontrol Program IF

# Uncomment blok program contoh yang akan dijalankan!

# Menghitung jumlah elemen tertetu di dalam suatu list

'''
a_list = [1,3,5,7,1,3,7,5,8,9,6,1]
count = 0
elemen = int(input("Masukkan elemen: "))  # Ketik elemen yang akan dihitung!
for i in range(len(a_list)):
    if elemen==a_list[i]:
        count+=1
print("Jumlah elemen ",elemen, "dalam list adalah: ",count)
'''

# Penggunaan statemen IF 2 kondisi dan Logika or, dan statemen else
'''
print("Pertanyaan Sebelum Mengendarai Mobil")
print('------------------------------------')
sim=input("Apakah Anda punya SIM (y/n): ")
skill=input("Apakah Anda bisa mengendarai mobil (y/n): ")
if sim=="y" or skill=="y":
    print("Silakan kendarai mobil, hati-hati dijalan!")
else:
    print("STOP, Anda dilarang mengendarai mobil!")
'''


# Penggunaan statemen IF 2 kondisi, logika and, dan statemen else
'''
print("Syarat Umur Membuat SIM")
print("------------------------")
umur=int(input("Ketik Umur Kamu: "))
if umur >=17 and umur <=50:
    print("Kamu sudah boleh bikin SIM!")
else:
    print('Kamu belum boleh bikin SIM!')
'''


# Penggunaan struktur if...elif...else...
'''
print("TEBAK ANGKA")
angka = 270             # Angka yang ditebak
print("Clue-nya adalah angka di range 10-300")
tebak=int(input("Coba tebak: "))

while (tebak!=angka):
    if tebak>270:
          print("Terlalu besar")
          tebak=int(input("Coba lagi: "))   # Konversi string to integer
    elif tebak>=260 and tebak<=270:
          print("Sudah mendekati!")
          tebak = int(input("Coba lagi: "))
    elif tebak >90 and tebak <=259:
          print("Masih kurang besar!")
          tebak = int(input("Coba lagi: "))
    elif tebak >=10 and tebak <=90 :
          print("Terlalu kecil")
          tebak = int(input("Coba lagi: "))
    else:
        print("\nNyerah aja deh...!")
        break

print("\nYang benar adalah: ", angka)
'''
