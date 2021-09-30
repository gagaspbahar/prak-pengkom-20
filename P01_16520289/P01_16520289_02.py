# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 21 Oktober 2020
# Deskripsi: Problem 2 - Pengurai Warna RGB

#Kamus
#Warna (str) = Adalah warna yang ingin diuraikan, huruf pertama harus kapital

#masukan
warna = input("Masukkan sebuah warna: " )

#keluaran1
print("Warna RGB yang menyala:")

#percabangan
if warna == "Black":
    print("")
else:
    if warna == "Red" or warna == "Yellow" or warna == "Magenta" or warna == "White":
        print("- Red")      #apabila warna mengandung Red maka akan print Red
    if warna == "Blue" or warna == "Magenta" or warna == "Cyan" or warna == "White":
        print("- Blue")     #apabila warna mengandung Blue maka akan print Blue
    if warna == "Green" or warna == "Cyan" or warna == "Yellow" or warna == "White":
        print("- Green")    #apabila warna mengandung Green maka akan print Green