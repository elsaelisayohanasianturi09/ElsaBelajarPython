print("Ini percobaan kedua gaes")

#Latihan dulu yaa

numbers = [1,2,3]
print(numbers)

#menambahkan angka pada indeks ke 4
numbers.insert(4,6)
print(numbers)

#mengubah angka pada indeks ke 4
numbers[3] = 4
print(numbers)

#menghapus indeks 1 
numbers.pop(1)
print(numbers)

print()
print()

myList= [1, "Car", 4.7, ["Cat", "Dog"]]
print (myList[0])
print (myList[1])
print (myList[2])
print (myList[3])

print("Menampilkan Sub Unit")
print (myList[3][0])
print (myList[3][1])

print()
print()

print("Operasi Himpunan")
a = {1, 2, 3}
b = {2, 3, 4}

print("Operasi gabungan")
print(a.union(b))

print("Operasi Irisan")
print(a.intersection(b))

print("Operasi perbedaan")
print(a.symmetric_difference(b))


print()
print()

print("Latihan Dicoding")

# Membuat variabel startTime untuk waktu kedatangan
startTime : dict[str, int] = {
    "HH": 9,
    "mm": 23,
    "ss": 57
}

# Membuat variabel endTime untuk waktu kepulangan
endTime : dict[str, int]= {
    "HH": 15,
    "mm": 25,
    "ss": 43
}

# Menampilkan waktu kedatangan dan kepulangan dalam format yang lebih mudah dibaca
print("Waktu Kedatangan:")
print(f"{startTime['HH']}:{startTime['mm']}:{startTime['ss']}")

print("Waktu Kepulangan:")
print(f"{endTime['HH']}:{endTime['mm']}:{endTime['ss']}")

print()
print()

print("Percobaan untuk input dan output padda python")

hargaMakan = int(input("Berapa harga mie ayam per porsi? \n"))
jumlahMakanan = int(input("Berapa porsi makanan yang Anda beli? \n"))

totalMakanan = jumlahMakanan * hargaMakan

print(f"Harga makan per porsi {hargaMakan}, totalnya adalah \n{totalMakanan}")

print()
print()

barang = "Laptop"

print("Elsa punya ", barang)
 
print()
print()
activity = "belajar python"
located = "di kamar"
money = 20000

print(f"Elsa sedang {activity} {located} seharga Rp{money : ,}")
print()
print("Elsa sedang {} {} seharga Rp {:,}".format(activity, located, money))

chocolateBarStock : int = 50
chocolateBarCount = int(input("Masukkan jumlah yang akan dibeli : "))
newChocolateBarStock = chocolateBarStock - chocolateBarCount
print(f"Stok saat ini adalah {newChocolateBarStock} buah")

print()
print()
print("Blok  Program")
isReady = True
if isReady :
    print("Memasak Sup")
print("Aksi telah berakhir")

print()
print()
print("Kondisi If else")

malam = True
if malam :
    print("Waktunya tidur")
else :
    print("Lanjut belajar")

 

print()
print()

temperature: float = float(input('masukan jumlah '))

if temperature > 100:

  print("Air berubah menjadi gas.")

elif 0 <= temperature <= 100:

  print("Air tetap berupa cairan.")

else :

   print("Air berubah menjadi padat.")

print()
print()

"""
TODO:
 1. Buatlah variabel isSick bertipe data boolean yang bernilai False untuk menyimpan status sakit.
 2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel temperature.
 3. Ada pengecekan variabel temperature sesuai dengan kebutuhan.
    3.1. Jika temperature 38 ke atas akan mencetak teks "Anda mengalami sakit demam." dan ubahlah status isSick menjadi True.
    3.2. Jika temperature di antara 35 dan 38 akan mencetak teks "Suhu tubuh Anda normal."
    3.3. Jika temperature kurang dari atau sama dengan 35 akan mencetak teks "Anda terjangkit sakit hipotermia." dan ubahlah status isSick menjadi True.
 4. Ada pemberian saran apabila sedang mengalami sakit.
    4.1. Gunakan variabel isSick untuk memeriksa sedang sakit atau tidak.
    4.2. Jika mengalami sakit, program akan mencetak teks "Anda disarankan istirahat atau kunjungi dokter secepatnya."
"""

# Tulis kode Anda di bawah ini
isSick : bool = True
temperatue : float =float(input("Masukkan suhu tubuh Anda : "))
if temperature > 38 :
  print("Anda mengalami sakit demam.")
  isSick = True
elif 35 < temperature < 38 :
  print("Suhu tubuh Anda normal.")
else :
  print("Anda disarankan istirahat atau kunjungi dokter secepatnya.")
  isSick = True
if isSick :
  print("Anda disarankan istirahat atau kunjungi dokter secepatnya.")

    