# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 4 November 2020
# Deskripsi: Problem 1 - Permainan Gunting Kertas Batu

#Kamus
#int n = jumlah ronde
#int m = input dari Mor
#int v = input dari Vin
#int countm = jumlah kemenangan Mor
#int countv = jumlah kemenangan Vin

#Inisialisasi Variabel
n = int(input("Masukkan jumlah ronde: "))
countv = 0
countm = 0

#Algoritma
for i in range(n):
    m = input("Masukkan gerakan Tuan Mor ke " + str(i+1) + ": ")                                #input
    v = input("Masukkan gerakan Tuan Vin ke " + str(i+1) + ": ")
    if (m == "R"):                                                                              #kasus bila tuan mor = R
        if (v == "S"):
            countm += 1
        elif(v == "P"):
            countv += 1
    if (m == "S"):                                                                              #kasus bila tuan mor = S
        if (v == "P"):
            countm += 1
        elif(v == "R"):
            countv += 1
    if (m == "P"):                                                                              #kasus bila tuan mor = P
        if (v == "R"):
            countm += 1
        elif(v == "S"):
            countv += 1

#Output
if (countm > countv):                                                                           #Kasus bila Mor menang
    print("Pemenangnya adalah Tuan Mor.")
elif (countv > countm):                                                                         #Kasus bila Vin menang
    print("Pemenangnya adalah Tuan Vin.")
else:                                                                                           #Bila seri
    print("Permainan berakhir seri.")
