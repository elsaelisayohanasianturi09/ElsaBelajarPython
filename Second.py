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
