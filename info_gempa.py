#memanggil file gempa dan import semua methodfungsi
from gempa import *

# membuat objek gempa dengan argumen
gempa1 = Gempa('Banten', 1.2)
gempa2 = Gempa('Palu', 6.1)
gemppa3 = Gempa('Cianjur', 5.6)
gempa4 = Gempa('Jayapura', 3.3)
gempa5 = Gempa('Garut', 4.0)
# informasi Gempa 
print('info Gempa Mazehh ##')
print()
gempa1.dampak()
gempa2.dampak()
gemppa3.dampak()
gempa4.dampak()
gempa5.dampak()