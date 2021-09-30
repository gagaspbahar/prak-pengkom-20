# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 2 Desember 2020
# Deskripsi: Problem 2 - Caesar Cipher

# Kamus
# def length(s) = penghitung panjang string
# def caesar(s,n) = translasi string
# string s = input awal pesan
# int n = berapa banyak perubahan

# Algoritma
def length(s):          #Fungsi penghitung panjang string
    # Kamus
    # int count = penghitung
    count = 0
    for i in s:
        count += 1
    return count

def caesar(s,n):                                #Fungsi translasi string
    # Kamus
    # String alph = daftar alfabet
    # String ans = string jawaban
    # int ind = index huruf

    alph = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    for i in range(length(s)):
        for j in range(26):
            if s[i] == alph[j]:
                ind = j+26
                if ind > 25:
                    ind = j+n - 26
                ans += alph[ind]
    return ans

#Input
s = input("Masukkan pesan awal: ")
n = int(input("Masukkan nilai N: "))

#Keluaran
print("Pesan akhir Kaisar adalah " + caesar(s,n))