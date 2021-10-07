# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 1 November 2020
# Deskripsi: Problem 2 - Menuliskan bilangan 10^x terkecil yang lebih dari N

#Kamus
# int n = bilangan yang ingin di cek
# int i = counter

n = int(input("Masukkan N: "))      #input n
i = 1                               #inisialisasi i

while(n>i):                         #saat n > i, i x 10
    i *= 10

print(i)                            #print kelipatan terkecil dari 10 yang memenuhi