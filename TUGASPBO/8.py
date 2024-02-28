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
    print(f"Tidak ada anggota Budi yang memenuhi kriteria usia diatas 20 tahun")