# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 21 Oktober 2020
# Deskripsi: Problem 3 - Keadaan Dua Garis (Gradien)

#kamus
# persamaan garis = ax + by = c
#a1 (int) = nilai a pertama
#b1 (int) = nilai b pertama
#c1 (int) = nilai c pertama
#a2 (int) = nilai a kedua
#b2 (int) = nilai b kedua
#c2 (int) = nilai c kedua
#m1 (int) = gradien 1
#m2 (int) = gradien 2
#d1 (int) = Hasil kali kedua gradien

#masukan
a1 = int(input("Masukkan a1: "))
b1 = int(input("Masukkan b1: "))
c1 = int(input("Masukkan c1: "))
a2 = int(input("Masukkan a2: "))
b2 = int(input("Masukkan b2: "))
c2 = int(input("Masukkan c2: "))

#Apabila ada nilai b yang 0, jangan dibagi dulu.
if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
    print("Angka yang diinput bukanlah sebuah garis.")          #bila kedua a dan b salah satu garis sama dengan 0, maka bukanlah sebuah garis.
elif b1 == 0 and b2 == 0:
    print("Kedua garis sejajar.")                               #apabila kedua garis b = 0 maka sejajar, seperti garis x = 2 dan x = 1.
elif b1 == 0 and a2 == 0:
    print("Kedua garis tegak lurus.")                           #apabila b1 = 0 dan a2 = 0 maka akan tegak lurus, seperti garis y = 2 dan x = 1
elif a1 == 0 and b2 == 0:
    print("Kedua garis tegak lurus.")                           #apabila b2 = 0 dan a1 = 0 maka akan tegak lurus, seperti garis y = 2 dan x = 1
elif b1 == 0 or b2 == 0:
    print("Kedua garis tidak sejajar dan tidak tegak lurus.")   #apabila nilai b ada yang 0 dan a tidak ada yang 0

#Apabila kedua nilai b aman:
else:
    m1 = -a1/b1
    m2 = -a2/b2
    d1 = (-a1 * -a2)/(b1 * b2)
    if(m1 == m2):
        print("Kedua garis sejajar.")                               #apabila kedua gradien sama maka sejajar
    elif (d1 == -1):
        print("Kedua garis tegak lurus.")                           #apabila hasil kali kedua gradien = -1 maka tegak lurus
    else:
        print("Kedua garis tidak sejajar dan tidak tegak lurus.")   #apabila tidak keduanya