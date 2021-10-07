# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 1 November 2020
# Deskripsi: Problem 1 - Mencetak bilangan 1 sampai N

#Kamus
# int n = 

n = int(input("Masukkan N: "))

if(n > 1):                          #bila n positif
    for i in range(1,n+1):          #loop dari 1 sampai n
        if (i == n):                #bila i = n, jangan print spasi
            print(i)
        else:
            print(i, end=" ")       #print spasi bila i bukan n
else:                               #bila n negatif
    for i in range(n-1, 1):         #loop dari n sampai 0
        if (i == 1):                #bila i = 1, jangan print spasi
            print(n-i)              #print n-i agar dapat nilai negatifnya
        else:
            print(n-i, end=" ")     #print spasi bila i bukan 1
