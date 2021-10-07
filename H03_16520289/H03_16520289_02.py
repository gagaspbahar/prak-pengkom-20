# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 15 November 2020
# Deskripsi: Problem 2 - Anagram

# Kamus
#int arA[] = array A
#int arB[] = array B
#int nA = panjang array A
#int nB = panjang array B
#bool sama  = kondisi kesamaan dua tabel frekuensi

#Inisialisasi
arA = [0 for i in range(1001)]
arB = [0 for i in range(1001)]
sama = True

#input kedua array
nA = int(input("Masukkan banyaknya elemen A: "))
for i in range(nA):
    a = int(input("Masukkan elemen A ke-" + str(i+1) + ": "))
    arA[a] += 1

nB = int(input("Masukkan banyaknya elemen B: "))
for i in range(nB):
    a = int(input("Masukkan elemen B ke-" + str(i+1) + ": "))
    arB[a] += 1

#Penyamaan kedua tabel frekuensi
if arA != arB:
    sama = False

#Keluaran
if sama:
    print("B adalah anagram dari A")
else:
    print("B bukan anagram dari A")