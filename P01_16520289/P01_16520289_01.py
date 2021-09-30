# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 21 Oktober 2020
# Deskripsi: Problem 1 - Menghitung Indeks Kuliah

#Kamus
#nilai (int) = nilai yang ingin dicek indeksnya
#indeks (str) = indeks dari nilai

#prompt untuk masukan
nilai = int(input("Masukkan nilai akhir Tuan Mor: "))

#percabangan untuk menentukan indeks
if nilai >= 80:
    indeks = "A"    #bila diatas atau sama dengan 80 maka A
elif nilai >= 75:
    indeks = "AB"   #bila diatas atau sama dengan 75 namun lebih kecil dari 80 maka AB
elif nilai >= 70:
    indeks = "B"    #bila diatas atau sama dengan 70 namun lebih kecil dari 75 maka B
elif nilai >= 60:
    indeks = "BC"   #bila diatas atau sama dengan 60 namun lebih kecil dari 70 maka BC
elif nilai >= 50:
    indeks = "C"    #bila diatas atau sama dengan 50 namun lebih kecil dari 60 maka C
elif nilai >= 40:
    indeks = "D"    #bila diatas atau sama dengan 40 namun lebih kecil dari 50 maka D
else:
    indeks = "E"    #bila lebih kecil dari 40 maka E

#keluaran indeks
print("Tuan Mor mendapatkan indeks", indeks + ".")