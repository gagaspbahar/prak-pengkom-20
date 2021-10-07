# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 15 November 2020
# Deskripsi: Problem 3 - Palindrome Checker

#Kamus
# int n = panjang string
# string s = string yang diinput
# bool isPalindrome = kondisi palindrom atau bukan

#inisialisasi nilai
n = int(input("Masukkan panjang string: "))
s = input("Masukkan string: ")
isPalindrome = True

#Algoritma pengecekan palindrom, dari 0 sampai n//2
for i in range(n//2):
    if s[i] != s[n-i-1]:
        isPalindrome = False

#Keluaran
if isPalindrome:
    print(s + " adalah palindrom")
else:
    print(s + " bukan palindrom")