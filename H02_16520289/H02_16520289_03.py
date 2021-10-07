# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 1 November 2020
# Deskripsi: Problem 3 - Prime Checker

# Kamus
# int x = bilangan yang ingin di cek keprimaannya
# bool prime = kondisi prima atau bukan
# int i = counter


x = int(input("Masukkan X: "))          #masukkan nilai x
prime = True                            #diawali dengan true
i = 2                                   #nilai prima pertama adalah 2

if (x < 2):
    print(x, "bukan bilangan prima")    #bila lebih kecil dari 2 bukanlah prima
else:
    while (prime and i * i <= x):       #cek sampai sqrt x
        if (x % i == 0):                
            prime = False               #bila ada pembagi = bukan prima
            print(x, "bukan bilangan prima")
        else:
            i += 1
    if (prime):
        print(x, "adalah bilangan prima")