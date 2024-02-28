usia = {'Budi' : 30, 'Andi' : 25, 'Cindy' : 20}

inputAnggota = input("Masukkan nama anggota keluarga : ")
if inputAnggota in usia:
    usiaAnggota = usia[inputAnggota]
    print(f"Usia {inputAnggota} adalah {usiaAnggota}")
else:
    print(f"{inputAnggota} tidak ditemukan di dalam kamus ")
