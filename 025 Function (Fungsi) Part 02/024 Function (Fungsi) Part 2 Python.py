# Fungsi - Part 2
# Uncomment blok program yang akan dijalankan!

# Melewatkan fungsi sebagai argument
'''
def plus():
    hasil=17+7
    return hasil

def minus():
    hasil=27-8
    return hasil

def tampilkan(a,b):
    print("Hasil penjumlahan adalah: ",plus())
    print("Hasil pengurangan adalah: ",minus())

def program_utama():
    tampilkan(plus,minus)

program_utama()
'''


# Melewatkan fungsi sebagai nilai balik
'''
def Data():
    print("Selamat belajar Python!")

def Nilai(fungsi):
    print("Fungsi sebagai nilai balik")
    return fungsi

T = Nilai(Data)
T()                         # Menampilkan nilai balik fungsi Data()
'''

# Fungsi Bersarang (Nested)
'''
def fungsi_A():                                 # Deklarasi fungsi_A
    def fungsi_B():                             # Deklarasi fungsi_B
        print("Hi ... saya fungsi_B")
        print("Fungsi A memanggil Fungsi_B")
    fungsi_B()                                  # Memanggil fungsi_B

fungsi_A()                                      # Memanggil fungsi_A
'''

# Bentuk Lain Fungsi Bersarang (Nested) - Decorator
'''
def myDecorator(t):
       def F_bersarang(a):                  # Fungsi bersarang/Nested
           print("Assalamu'alaikum")
           return t(a)                      # Mengembalikan alamat fungsi
       return F_bersarang

@myDecorator            
def hello(b):
    print(b)                                # hello=myDecorator(hello)

hello("Sahabat Robonesia")
'''

# Contoh overloading fungsi
'''
def salam():
    print("Assalamu'alaikum, saya Robonesia")

def salam(t):
    print("Assalamu'alaikum, saya adalah", t)

salam()
salam("Robonesia")
'''

# Fungsi rekursi
'''
def display(t):
    if t>0:
        print("Belajar fungsi Rekursi")
        display(t-1)		# Fungsi memanggil diri sendiri (Rekursi)

def main():
    display(3)			# Memanggil fungsi rekursif dengan berbatas

main()              # Panggil fungsi utama
'''

# Kesalahan penggunaan Fungsi rekursi
'''
def display():
        print("Belajar fungsi Rekursi")
        display()		# Fungsi rekursif yang salah

def main():
    display()			# Memanggil fungsi rekursif tanpa batas

main()              # Panggil fungsi utama
'''

# Fungsi rekursi & Faktorial
'''
def Faktorial(t):               # Fungsi faktorial
    if t==0:
        return 1
    else:
        return t*Faktorial(t-1)     # Rekursi fungsi faktorial

def main():
    t = int(input("Masukkan nilai faktorial yang dicari: "))
    print("Faktorial dari",t,"adalah", Faktorial(t))

main()
'''

# Fungsi rekursi & Deret Fibonacci
'''
def Fibonacci(t):               # Fungsi deret fibonacci
    if t==0:
        return 0
    elif t==1:
        return 1
    else:
        return Fibonacci(t-1)+Fibonacci(t-2)     # Rekursi fungsi deret fibonacci

def main():
    print("20 angka pertama deret Fibonacci:")
    for t in range(0,20):
        print(Fibonacci(t))

main()
'''

# Fungsi Rekursi & Greatest Common Divisor (GCD)
'''
def GCD(t,q):
    if t % q==0:
        return q
    else:
        return GCD(q,t%q)       # Fungsi rekursi GCD

def main():
    pilihan="y"
    while(pilihan=='y' or pilihan=='Y'):
        t=int (input("Masukkan bilangan pertama: "))
        q=int (input("Masukkan bilangan kedua: "))
        print ("GCD dari ",t," dan ",q," adalah ",GCD(t,q))
        pilihan=input("Cari GCD lagi? (y/n): ")

main()		# Panggil fungsi utama
'''
