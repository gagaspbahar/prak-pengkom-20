# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 29 November 2020
# Deskripsi: Problem 2 - Matriks NxM

# Kamus
# int N = baris matriks
# int M = kolom matriks
# int a[N][M] = matriks NxM
# int count = jumlah bilangan positif

# Algoritma
# Inisialisasi
N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))
a = [[0 for i in range(M+1)] for j in range(N+1)]
count = 0

# Input matriks dan penghitungan bilangan positif
for i in range(1, N+1):
    for j in range(1, M+1):
        a[i][j] = int(input("Masukkan nilai A[{}][{}]: ".format(i, j)))
        if a[i][j] > 0:
            count += 1

# Keluaran jumlah bilangan positif
print("Ada {} bilangan positif di matriks.".format(count))

# Print matriks
for i in range(1, N+1):
    for j in range(1, M+1):
        if j != M:
            print(a[i][j], end=" ")
        else:
            print(a[i][j]) 



