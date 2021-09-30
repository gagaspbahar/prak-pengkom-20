# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 4 November 2020
# Deskripsi: Problem 3 - Bilangan Cantik

#Kamus
#int x = input bilangan pembagi (asumsi relatif prima dengan 10)
#int i = bilangan cantik
#int pw = pangkat dari 10
#int pw1 = beda setiap suku saat 10*pw, misal 1 lalu 11 lalu 111
#int ans = jawaban yang akan di output
#bool divided = kondisi apakah sudah menemukan bilangan yang habis dibagi x atau belum
#int j = counter

#Inisialisasi variabel
x = int(input("Masukkan X: "))
i = 1
pw = 0
pw1 = 1
ans = 0
divided = False

#Algoritma
while (divided == False):                                       #ketika belum terbagi
    for j in range(9):                                          #ulangi 9 kali
        if (i % x == 0):                                        #pengecekan i % x
            ans = i
            divided = True
        else:                                                   #tambahkan i dengan pw1
            i += pw1
    i += 1                                                      #karena loop berakhir dengan angka belakang 0, untuk ke angka cantik harus ditambah 1
    pw += 1                                                     #pangkat dari 10 ditambah 1
    pw1 += 10**pw                                               #beda suku ditambah 10**pw

print("Bilangan cantik terkecil yang habis dibagi", x, "ialah", ans)