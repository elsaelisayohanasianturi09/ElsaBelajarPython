print("Heloo my friend")
#ini adalah komen guyss


"""Ini adalah komen multi line
ingat yaa elsa """
elsa = 100
print(elsa)

#kita bisa compile python ke yang namanya bytecode

"""
TODO:
 1. Buatlah variabel chocolateBarPrice bertipe data integer yang bernilai 3500.
 2. Tambahkan perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel chocolateBarCount.
 3. Gunakan ekspresi yang tepat untuk menghitung total harga snack dan simpan pada variabel chocolateBarTotalPrice bertipe data integer.
 4. Tampilkan hasil perhitungan pada console dengan teks "Harga yang harus dibayar adalah {chocolateBarTotalPrice} rupiah."
"""

# Tulis kode Anda di bawah ini
chocolateBarPrice : int = 3500
chocolateBarCount : int = int(input("Masukkan jumlah yang akan dibeli : "))
chocolateBarTotalPrice : int = chocolateBarPrice * chocolateBarCount
print(f"Harga yang harus dibayar adalah {chocolateBarTotalPrice} rupiah.") 

print()
for i in range(5) :
    print(f"Ini mencetak ke {i}")
print()
print("Mencetak list/tuple")

for i in[0, "Elsa", 5.7, True] :
    print(f"Ini mencetak {i}")
print()
for i in("ELSA") :
    print(f"Ini mencetak {i}")

print()
print("Penggunaan while")

first = 0
while first < 10 :
    print(f"Ini mencetak ke : {first}")
    first = first + 1

print()
print("Penggunaan Do While dalam python")

iterateNumber = 0
iterateValue = True
while iterateValue:
    print(f"Perintah ini mencetak angka {iterateNumber}")
    iterateNumber = iterateNumber + 1
    if iterateNumber >= 5:
        iterateValue = False 
print()

for i in range (1,6):
    for j in range (i):
        print("*", end = ' ')
    print("")


print()
print("Perulangan")

for i in range(1,5) :
    print(f"Ini adalah lantai ke {i}")
    if i == 2 : 
        print(f"Berhenti di lantai ke {i}")
        break 
    print(f"Melewati lantai ke {i}")

print()
print()
for i in range(1, 5):
    print(f"Ini adalah lantai {i}")
    
    if i != 3:
        print(f"Melewati lantai {i}")
        continue

    print("Berhenti di lantai 3")
    break

print()
print()
#Menghitung total
total = 0
for value in [2, 4, 6, 8] :
    total = total + value
    print(f"Total saat ini adalah : {total}")
print(f"Total akhir adalah : {total}")

print()
print("Kuis Dicoding")
"""
TODO:
 1. Buatlah variabel a bertipe data integer yang bernilai 1 untuk menyimpan nilai suku pertama.
 2. Buatlah variabel b bertipe data integer yang bernilai 2 untuk menyimpan nilai beda antar suku.
 3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n sebagai nilai suku yang ingin diketahui.
 4. Lakukan perulangan mulai dari 1 hingga n+1 dengan
    4.1. state i;
    4.2. menghitung suku ke-n berdasarkan state i dan simpan pada variabel Un; dan
    4.3. mencetak setiap variabel Un menggunakan perintah print dan parameter end.
 5. Lakukan pemberhentian mencetak teks dengan perintah print tanpa isi.
"""

# Tulis kode Anda di bawah ini
a : int = 1
b : int = 2
n : int = int(input("Masukkan suku keberapa yang ingin diketahui : "))
for i in range(1, n + 1) :
  Un : int = a + (i-1) * b
  print(Un, end=' ')
print("\n")

print()
print()
print("Hallo David ")

