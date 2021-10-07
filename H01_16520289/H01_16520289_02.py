# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 19 Oktober 2020
# Deskripsi: Problem 2 - Program Kalkulator

# Kamus
# Angka pertama = a
# Angka kedua = b
# Operator = op
# Hasil = hasil

#masukan
a = int(input("Masukkan angka pertama: ")) #Input angka pertama
b = int(input("Masukkan angka kedua: ")) #Input angka kedua
op = input("Masukkan operator: ") #Input tipe operator

#proses
if op == "+":
    hasil = a + b #penjumlahan
elif op == "-":
    hasil = a - b #pengurangan
elif op == "*":
    hasil = a * b #perkalian
elif op == "/":
    hasil = a // b #pembagian dengan pembulatan kebawah
elif op == "%":
    hasil = a % b #sisa pembagian

#keluaran
print(a," ", op," ", b, " = ", hasil)