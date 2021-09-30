# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 2 Desember 2020
# Deskripsi: Problem 3 - Simetri Lipat dan Simetri Putar

# Kamus
# cekLipatVertikal = cek sb.vertikal
# cekLipatHorizontal = cek sb. horizontal
# cekDiagonalAtas = cek lipat diagonal yang arahnya keatas
# cekDiagonalBawah = cek lipat diagonal yang arahnya kebawah
# putarMatriks1, 2, 3 = cek sb. putar 90, 180, 270 derajat
# int n = baris matriks
# int m = kolom matriks
# int a = matriks
# int sLipat = jumlah simetri lipat
# int sPutar = jumlah simetri putar

#Kamus untuk para fungsi:
# bool flag = bool untuk mengecek sudah terlihat salah atau belum, lalu return 1 bila tidak ada kesalahan, 0 bila ada kesalahan.
# Algoritma

def cekLipatVertikal(n,m):              # Cek lipat Vertikal
    flag = True
    for i in range(n):
        for j in range(m):
            if a[i][j] != a[i][m-1-j]:
                flag = False
    if(flag):
        return 1
    else:
        return 0

def cekLipatHorizontal(n,m):            # Cek lipat Horizontal
    flag = True
    for i in range(n):
        for j in range(m):
            if a[i][j] != a[n-1-i][j]:
                flag = False
    if(flag):
        return 1
    else:
        return 0

def cekLipatDiagonalAtas(n):            # Cek diagonal atas
    flag = True
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[n-1-j][n-1-i]:
                flag = False
    if(flag):
        return 1
    else:
        return 0

def cekLipatDiagonalBawah(n):           # Cek diagonal bawah
    flag = True
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                flag = False
    if(flag):
        return 1
    else:
        return 0

def putarMatriks1(n):                   # Cek putar 90
    flag = True
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[n-j-1][i]:
                flag = False
    if(flag):
        return 1
    else:
        return 0

def putarMatriks2(n,m):                 # Cek putar 180
    flag = True
    for i in range(n):
        for j in range(m):
            if a[i][j] != a[n-i-1][m-j-1]:
                flag = False
    if(flag):
        return 1
    else:
        return 0

def putarMatriks3(n):                   # Cek putar 270
    flag = True
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][n-i-1]:
                flag = False
    if(flag):
        return 1
    else:
        return 0

#Inisialisasi
n = int(input("Masukkan N: "))
m = int(input("Masukkan M: "))
a = [[0 for i in range(m)] for i in range(n)]
sLipat = 0
sPutar = 0

#Masukan array
for i in range(n):
    for j in range(m):
        a[i][j] = int(input("Masukkan elemen baris {} kolom {}: ".format(i+1,j+1)))

#Penghitungan sLipat dan sPutar dengan pemanggilan fungsi
if(n == m):
    sLipat += cekLipatDiagonalBawah(n) + cekLipatDiagonalAtas(n)
    sPutar += putarMatriks1(n) + putarMatriks3(n)
sLipat += cekLipatHorizontal(n,m) + cekLipatVertikal(n,m)
sPutar += putarMatriks2(n,m) + 1                                    #sPutar selalu minimal 1, saat diputar 360 derajat

# Keluaran
print("Simetri lipat:", sLipat)
print("Simetri putar:", sPutar)
# Note from class:
# [NOMOR 3]
# jadi maksudnya simetri lipat itu -> ngecek tengah vertikal, tengah horizontal, 2 diagonalnya (4 berarti maxnya).
# simetri putar -> diputer 90 derajat, max 4 juga (360 derajat)