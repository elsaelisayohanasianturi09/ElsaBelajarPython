"""class mobil:
    def __init__(self,inputName, inputWarna, inputPrice):
        self.name =  inputName
        self.warna = inputWarna
        self.price = inputPrice

mobil1 = mobil("Toyota", "Black", 62000000 )
mobil2 = mobil("Sport", "Yellow", 90000000 )

print(mobil1.__dict__)
print(mobil2.__dict__)


class TeknikInformatika :
    def __init__(self, inputName, inputAge, inputAsal):
        self.name =inputName
        self.age = inputAge
        self.asal = inputAsal

mahasiswa1 = TeknikInformatika("Elsa", 20, "Sumatera Utara")
mahasiswa2 = TeknikInformatika("Nydia", 18, "Sumatera Utara")
mahasiswa3 = TeknikInformatika("Angga", 19, "Lampung Selatan")


print(mahasiswa1.__dict__)
print(mahasiswa2.__dict__)
print(mahasiswa3.__dict__)"""
# Membuat list kosong
input_list = []

# Meminta pengguna untuk memasukkan input sebanyak yang diinginkan
while True:
    nilai = input("Masukkan nilai (atau ketik 'selesai' untuk mengakhiri): ")

    # Mengecek apakah pengguna ingin mengakhiri
    if nilai.lower() == 'selesai':
        break

    # Menambahkan nilai ke dalam list
    input_list.append(int(nilai))

# Menampilkan list setelah pengguna selesai memasukkan input
print("List setelah input pengguna:", input_list)
