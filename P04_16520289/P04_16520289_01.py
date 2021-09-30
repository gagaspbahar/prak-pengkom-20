# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 2 Desember 2020
# Deskripsi: Problem 1 - Ratu dan Benteng

# Kamus
# def cek = pengecek ratu aman atau tidak
# int n = baris dan kolom matriks
# int a[n][n] = matriks catur

# Algoritma

def cek():                                          # Cek apakah ratu aman
    for i in range(n):
        if (a[ratu[0]][i] == 'B'):                  # Sesuai kolom
            return 0
    for j in range(n):
        if(a[j][ratu[1]] == 'B'):                   # Sesuai baris
            return 0
    return 1

# Masukan
n = int(input("Masukkan nilai N: "))
a = [["" for i in range(n)] for i in range(n)]
print("Masukkan matriks: ")
for i in range(n):
    a[i] = input()
    for j in range(n):
        if a[i][j] == 'R':                          #Bila ditemukan ratu, simpan koordinat ratu.
            ratu = [i,j]

# Keluaran
if cek():
    print("Ratu aman dari serangan benteng.")
else:
    print("Ratu tidak aman dari serangan benteng.")