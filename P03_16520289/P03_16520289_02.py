# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 18 November 2020
# Deskripsi: Problem 2 - Koordinat Kartesius

# # Kamus
# int koordinat[101] = array koordinat, 1 melambangkan ada garis, 0 melambangkan tidak ada garis
# int N = banyaknya garis yang dibuat
# int L = awal penarikan garis
# int R = akhir penarikan garis
# int Q = banyak pertanyaan
# int x = titik yang ingin diuji

# Inisialisasi array dan N untuk penarikan garis
koordinat = [0 for i in range(101)]
N = int(input("Masukkan N: "))

for i in range(N):
    # Inisialisasi nilai L dan R ke-i
    L = int(input("Masukkan L[" + str(i+1) + "]: "))
    R = int(input("Masukkan R[" + str(i+1) + "]: "))
    # Pastikan R > L, apabila tidak terpenuhi, tukar keduanya
    if L > R:
        L, R = R, L
    for i in range(L, R+1):                                             # Semua titik yang dilewati garis diberi tanda 1 pada array koordinat
        koordinat[i] = 1

# # Pengujian titik
#Inisialisasi jumlah pertanyaan
Q = int(input("Masukkan Q: "))
# Loop sampai Q
for i in range(Q):
    # Inisialisasi nilai X ke-i
    x = int(input("Masukkan X ke " + str(i+1) + ": "))
    if koordinat[x] == 1:                                                   # Bila koordinat x = 1 maka ada di garis
        print("Titik ke " + str(i + 1) + " ada di garis.")
    else:                                                                   # Bila 0 maka tidak ada di garis
        print("Titik ke " + str(i + 1) + " tidak ada di garis.")
