# Statement BREAK-CONTINUE-PASS

# Uncomment untuk blok contoh program yang akan dijalankan!

# Demonstrasi statement BREAK
'''
print("TEBAK ANGKA")
angka = 270
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

# Demonstrasi statement CONTINUE
'''
for nilai in range(2,10):
    if nilai % 2 == 0:
        print("Temukan bilangan genap:", nilai)     # even number
        continue
    print("Temukan bilangan ganjil:", nilai)        # odd number
'''


# Demonstrasi statement PASS
'''
while True:
    pass    # Diam tidak melakukan apa-apa. Menunggu interrupsi keyboard.
'''
