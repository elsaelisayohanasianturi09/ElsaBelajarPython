print("Pemanggilan Fungsi")
print()
#Deklarasi fungsi

def f(x) :
    return x + 5

#Pemangilan fungsi
z = f(8)
print(f"Nilai nya adalah {z}")

print()
print("Menghitung Luas Segitia \n ")
def menghitung_luas_segitiga (alas, tinggi):
    luas_segitiga = 0.5 * alas * tinggi
    return luas_segitiga
y : int = menghitung_luas_segitiga(2 , 5)
print(f"Luas segitiga adalah {y}")
print()

def greeting(nama, ucapan, /) :
    return f"Halo {nama}.{ucapan}"
print(greeting("Elsa", "Selamat Ulang Tahun yaa"))

print()
print("CONTOH PROSEDUR")

#Deklarasi prosedur
def eatSomething (food) :
    print(f"Saya sedang makan {food}.")

#Pemanggilan Prosedur

eatSomething("Pecel Lele")

print()
def bayarMakan(jumlah : int, hargaPerPorsi : int = 10000) -> int :
    totalHarga : int = jumlah * hargaPerPorsi
    return totalHarga
belanjaHariIni : int = bayarMakan(4)
print(belanjaHariIni)

print()
landArea : float = float(input("Masukan luas : "))
width : float = float(input("Masukan panjang : "))
length : float = float(input("Masukan lebar : "))
def checkArea (landArea : float, width : float, length : float) -> bool:
  buildingArea = width * length
  if buildingArea > landArea:
    return False
  else:
    return True
check: bool = checkArea(landArea, width, length)
if check == False:
    print("Rumah tidak dapat dibangun berdasarkan ketiga nilai tersebut.")
else:
    print("Rumah dapat dibangun berdasarkan ketiga nilai tersebut.")

print()
print("Dictionary")
keluargaFajar = {
    "bapak": {
        "nama": "Bapak Fajar",
        "pekerjaan": "arsitek dan mandor"
    },
    "ibu": {
        "nama": "Ibu Fika",
        "pekerjaan": "ibu rumah tangga dan usaha katering"
    },
    "anak": {
        "nama": "Bima",
        "pekerjaan": "pelajar dan guru les"
    }
}

for anggotaKeluarga, data in keluargaFajar.items():
    print(anggotaKeluarga)
    for kategori, nilai in data.items():
        print(f"{kategori}: {nilai}")
    print()
print()
print()
print("Mencacah dalam set")
set1 = (1, 2, 3)
set2 = (4, 5, 6)
set3 = {set1, set2}

# Mencacah elemen set dalam set
for setItem in set3:
    for value in setItem:
        print(value, end=" ")
    print()