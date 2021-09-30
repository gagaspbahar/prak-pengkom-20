# NIM/Nama : 16520289/Gagas Praharsa Bahar
# Tanggal  : 18 November 2020
# Deskripsi: Problem 1 - Diskon Terbesar

# # Kamus
# int n = banyak barang
# int harga[n] = harga awal barang, kemudian akan diubah menjadi harga setelah diskon
# int diskon[n] = besaran diskon dalam persen untuk tiap barang
# int besardiskon[n] = jumlah diskon dalam rupiah untukn tiap barang
# int mx = indeks dengan diskon terbesar

# Inisialisasi array
n = int(input("Masukkan banyak barang: "))
harga = [0 for i in range(n)]
diskon = [0 for i in range(n)]
besardiskon = [0 for i in range(n)]

# Pemasukan input ke array harga dan array diskon
for i in range(n):
    harga[i] = int(input("Masukkan harga awal barang ke-" + str(i+1) + ": "))
for i in range(n):
    diskon[i] = int(input("Masukkan besar diskon (dalam persen) barang ke-" + str(i+1) + ": "))

# Declare terlebih dahulu diskon maksimum ada di indeks pertama (0)
mx = 0
# Looping untuk mencari diskon terbesar
for i in range(n):
    besardiskon[i] = harga[i]                                       # Awalnya besardiskon sama dengan harga
    harga[i] = harga[i] * (100-diskon[i])/100                       # Buat harga menjadi harga setelah diskon
    besardiskon[i] -= harga[i]                                      # besardiskon = harga - harga setelah diskon
    if besardiskon[i] > besardiskon[mx]:                            # Cari indeks dengan besardiskon terbesar
        mx = i

# Keluaran
print("Barang " + str(mx+1) + " memiliki diskon paling besar yaitu " + str(int(besardiskon[mx])) + ".")