# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 4 November 2020
# Deskripsi: Problem 2 - Konversi basis K ke basis 10

#Kamus
#int sm = jumlah bilangan dalam basis 10
#int n = jumlah digit
#int k = basis awal
#int i = counter

#Inisialisasi variabel
sm = 0
n = int(input("Masukkan nilai N: "))
k = int(input("Masukkan nilai K: "))

#Algoritma
for i in range(n-1,-1,-1):                                                          #Loop dari n-1 sampai 0
    digit = int(input("Masukkan digit ke " + str(n-i) + ": "))                      #Input digit
    sm += k**i * digit                                                              #Kalikan basis dengan nilai digit ke-berapa lalu tambahkan ke sm

#Output
print("Bilangan dalam basis 10 adalah", sm)
