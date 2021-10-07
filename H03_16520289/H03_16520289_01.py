# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 15 November 2020
# Deskripsi: Problem 1 - Penulisan Terbalik

# Kamus
# int n = panjang array
# int ar[] = array penampung angka

#Algoritma
#Input
n = int(input("Masukkan N: "))

#Inisialisasi array dan memasukkan angka ke array
ar = [0 for i in range(n)]
for i in range(n):
    ar[i] = int(input())

#Pembalikkan array
print("Hasil dibalik: ")
for i in range(n-1,-1,-1):
    print(ar[i])
    