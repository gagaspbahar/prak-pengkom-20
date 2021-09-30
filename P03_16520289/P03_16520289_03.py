# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 18 November 2020
# Deskripsi: Problem 3 - Kemunculan 'tuan' pada Subsequence

# # Kamus
# int n = panjang string
# string s = string yang ingin dicek
# int muncul = jumlah kemunculan

# Inisialisasi nilai panjang, string, dan jumlah kemunculan
n = int(input("Masukkan nilai N: "))
s = input("Masukkan string: ")
muncul = 0

# Cek apakah panjang string yang di input dan panjang yang diberikan sama
if n != len(s):
    print("Panjang string dan string yang di input tidak sama.")
else:
    for i in range(n-3):                                                            #sampai n-3, karena t uan -> butuh 3 huruf lagi
        if s[i] == 't':                                                             #bila ketemu huruf t
            for j in range(i+1, n-2):                                               #cek selanjutnya sampai n-2 -> tu an -> butuh 2 huruf lagi
                if s[j] == 'u':                                                     
                    for k in range(j+1, n-1):                                       #ulangi proses dengan a, n
                        if s[k] == 'a':                                             
                            for l in range(k+1,n):
                                if s[l] == 'n':                                     #apabila ketemu subsequence yang memenuhi
                                    muncul += 1                                     #tambahkan satu ke variabel muncul

# Keluaran
print("Ada", muncul, "buah kemunculan.")
