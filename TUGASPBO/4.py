daftarNilai = [80, 75, 90, 85]
print(f"Daftar nilai awal  : {daftarNilai}")

nilaiBaru = int(input("Masukkan nilai baru yang ingin ditambahkan : "))
if nilaiBaru not in daftarNilai :
    daftarNilai.append(nilaiBaru)
else :
    print(f"Nilai {nilaiBaru} sudah ada di dalam daftar nilai")
print(f"Daftar nilai setelah ditambahkan : {daftarNilai}")