"""
#Soal No 1
def jmlhBilangan(n):
    total = 0
    for i in range (1, n+1) :
        if i % 3 == 0 or i % 5 == 0 :
            total += i
    return total

n  = int(input("Masukkan nilai n : "))
hasil = jmlhBilangan(n)
print(f"Jumlah bilangan yang habis dibagi 3 atau 5 dalam rentang 1 - {n} adalah {hasil}")

#Soal nomor 2
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def hitungBilangan(n):
    total = 0

    for num in range(1, n + 1):
        if num % 3 == 0 or num % 5 == 0:
            if not is_prime(num):
                total += 1

    return total

n = int(input("Masukkan nilai n: "))
result = hitungBilangan(n)
print(f"Jumlah bilangan yang habis dibagi 3 atau 5 dan bukan prima dalam rentang 1 hingga {n} adalah: {result}")

#Soal No 3
daftarNilai = []
while True:
    nilai = input("Masukkan nilai yang ingin ditaambah (atau ketik 'stop' untuk mengakhiri): ")
    if nilai.lower() == 'stop4':
        break
    daftarNilai.append(int(nilai))

print(f"Daftar Nilai Setelah Ditambahkan : {daftarNilai}")

#Soal nomor 4
daftarNilai = [80, 75, 90, 85]
print(f"Daftar nilai awal  : {daftarNilai}")

nilaiBaru = int(input("Masukkan nilai baru yang ingin ditambahkan : "))
if nilaiBaru not in daftarNilai :
    daftarNilai.append(nilaiBaru)
else :
    print(f"Nilai {nilaiBaru} sudah ada di dalam daftar nilai")
print(f"Daftar nilai setelah ditambahkan : {daftarNilai}")

#SoalnOMOR 5
set1 = {"apel", "jeruk", "nanas", "pisang"}
set2 = {"apel", "anggur", "nanas", "mangga"}

buahdiKeduaSet = set1.intersection(set2)
print(f"Buah yang ada dikedua set adalah : {buahdiKeduaSet}")

#Soal nomor 6
set1 = {"apel", "jeruk", "nanas", "pisang"}
set2 = {"apel", "anggur", "nanas", "mangga"}

buahdiKeduaSetDenganA = set()

for buah in set.intersection(set2) :
    if "a" in buah :
        buahdiKeduaSetDenganA.add(buah)

print(f"Buah yang ada di kedua set mengandung huruf 'a', {buahdiKeduaSetDenganA}")

#Nomor 7
usia = {'Budi' : 30, 'Andi' : 25, 'Cindy' : 20}

inputAnggota = input("Masukkan nama anggota keluarga : ")
if inputAnggota in usia:
    usiaAnggota = usia[inputAnggota]
    print(f"Usia {inputAnggota} adalah {usiaAnggota}")
else:
    print(f"{inputAnggota} tidak ditemukan di dalam kamus ")


#Nomor 8
kamusUsia = {'Budi' : 30, 'Andi' : 25, 'Cindy' : 20, 'Deni' : 18}
totalUsia = 0
jumlahAnggota = 0
print(f"Usia keluarga Budi : {kamusUsia}")
for nama, usia in kamusUsia.items() :
    if usia > 20:
        totalUsia += usia
        jumlahAnggota += 1
if jumlahAnggota > 0:
    usiaRatarata = totalUsia / jumlahAnggota
    print(f"Usia rata-rata anggota keluarga Budi yang usianya lebih dari 20 tahun adalah {usiaRatarata} tahun.")
else :
    print(f"Tidak ada anggota Budi yang memenuhi kriteria usia diatas 20 tahun")"""

#Nomor 9
buah = ('apel', 'jeruk', 'nanas', 'pisang')
tupleUrut = tuple(sorted(buah))
print(f"Tuple buah setelah diurutkan: {tupleUrut}" )





