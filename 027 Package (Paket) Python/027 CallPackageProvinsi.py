# Program Aplikasi Pemanggilan Package
from package_provinsi.Jawa_Barat import Bandung,Bogor,Depok
from package_provinsi.Jawa_Tengah import Semarang,Wonogiri
from package_provinsi.Jawa_Timur import Surabaya,Kediri

print(Bandung.__doc__)
Bandung.tampil()
Bandung.run()

print(Wonogiri.__doc__)
Wonogiri.tampil()
Wonogiri.run()

print(Surabaya.__doc__)
Surabaya.tampil()
Surabaya.run()
