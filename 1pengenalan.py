#1 Variabel dan Tipe Data
# a. Buat 3 variabel bertipe data: int, float, str, dan list.
# b. Tampilkan tipe datanya dengan fungsi type().

strign = "halo"
intreger = 2
gloat = 12.0
lits = ["ayam","sate"]

print(type(gloat))
print(type(lits))
print(type(intreger))
print(type(strign))

#2 List dan Manipulasi
# a. Buat list belanja (beras, minyak, dan telur).
# b. Kemudian tambahkan item gula dan kopi menggunakan fungsi.
# c. Tampilkan semua item dengan perulangan.

keranjang = ["beras", "minyak", "telur"]

def tambah_item(list_keranjang, item):
    list_keranjang.append(item)

tambah_item(keranjang, "gula")
tambah_item(keranjang, "kopi")

for item in keranjang:
    print(item)

#3 Dictionary
# a. Buat dictionary harga belanjaan:
#  i. beras: 12.000
#  ii. minyak: 17.000
#  iii. telur: 24.000
#  iv. gula:15.000
#  v. kopi:20.000
# b. Hitung dan tampilkan total harga semua belanjaan.

belanjaan = {"beras":12000, 
              "minyak":17000,
              "telur":24000,
              "gula":15000,
              "kopi":20000}

list_harga = [belanjaan[x] for x in belanjaan]
list_harga

total = sum(list_harga)
total

print(total)

#4 Fungsi
# a. Buat fungsi untuk menghitung luas lingkaran yang mengembalikan nilai luas dan keliling.

import math

jari = float(input("Jari-Jari Lingkaran: "))

def luasling(jari):
    luas = math.pi*jari**2
    keliling = 2*math.pi*jari
    
    return luas, keliling

luas, keliling = luasling(jari)

print("Luas Lingkaran: ", luas)
print("Keliling Lingkaran: ", keliling)

#5 Percabangan
# a. Minta pengguna memasukkan usia, tampilkan:
#  i. “Anak” jika usia 0-13
#  ii. “Remaja” jika usia 14-24
#  iii. “Dewasa” jika usia 25-49
#  iv. “Lansia” jika usia >50

usia = int(input("Masukkan usia Anda: "))

if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia >= 50:
    print("Lansia")
else:
    print("Belum lahir")
