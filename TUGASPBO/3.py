daftarNilai = []
while True:
    nilai = input("Masukkan nilai yang ingin ditaambah (atau ketik 'stop' untuk mengakhiri): ")
    if nilai.lower() == 'stop':
        break
    daftarNilai.append(int(nilai))

print(f"Daftar Nilai Setelah Ditambahkan : {daftarNilai}")