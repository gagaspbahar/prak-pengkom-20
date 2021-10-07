# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 29 November 2020
# Deskripsi: Problem 3 - Matriks Pascal

# Kamus
# int N = kolom dan baris Matriks
# int a[N][N]: Matriks 2 dimensi penampung bilangan pascal

# Algoritma

# Inisialisasi
N = int(input("Masukkan N: "))
a = [[1 for i in range(N)] for j in range(N)]

# Pascal, bilangan ditambah dengan yang diatasnya dan dikirinya
for i in range(N):
    for j in range(N):
        if (i == 0 or j == 0) and j != N-1:
            print(a[i][j], end=" ")
        elif(i == 0 or j == 0):
            print(a[i][j])
        else:
            a[i][j] = a[i-1][j] + a[i][j-1]
            if j != N-1:
                print(a[i][j], end=" ")
            else:
                print(a[i][j])

# # Print kembali matriks baru
# for i in range(N):
#     for j in range(N):
#         if j != N-1:
#             print(a[i][j], end=" ")
#         else:
#             print(a[i][j])