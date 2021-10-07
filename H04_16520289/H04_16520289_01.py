# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 29 November 2020
# Deskripsi: Problem 1 - Fungsi Kuadrat

#Kamus
# func f(x) = Fungsi kuadrat
# int a = awal
# int b = akhir

#Algoritma
def f(x):                               #Fungsi f(x)
    return x*x - 2*x + 5

#Inisialisasi nilai
a = int(input("Masukkan A: "))
b = int(input("Masukkan B: "))

#Keluaran
for i in range(a, b+1):
    print("f({}) = {}".format(i, f(i)))