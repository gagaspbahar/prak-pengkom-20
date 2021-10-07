# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 19 Oktober 2020
# Deskripsi: Problem 3 - Penentu Ganjil Genap

# Kamus
# x adalah bilangan yang ingin dicek

#masukan
x = int(input("Masukkan X: "))

#proses dan keluaran
if x > 0:
    if x % 2 == 0:
        print("X adalah bilangan positif genap")
    else:
        print("X adalah bilangan positif ganjil")
elif x == 0:
    print("X adalah bilangan 0")
else:
    print("X adalah bilangan negatif")    