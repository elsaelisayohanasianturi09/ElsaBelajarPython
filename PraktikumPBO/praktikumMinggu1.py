"""buah = ['Semangka', 'Melon', 'Anggur', 'Jeruk']
for buahan in buah :
    print(buahan)

score = []
for i in range (3) :
    x = int(input("Masukkan Score : "))
    score.append(x)

average = sum(score)/ len(score)
print(f"Rata-rata : {average}")

#Tipe Data Dictionary

mahasiswa = [{'Nama' : 'Elsa', 'NIM' : 122140135}, {'Nama' : 'Dwi Arthur', 'NIM' : 122140144}]

#Search of name

Nama = input("Name : ")
for person in mahasiswa :
    if person['Nama'] == Nama :
        print(f"{person['Nama']} : {person['NIM']}")
        break
else :
    print("Data tidak ditemukan")"""

def print_triangle(height):
    for i in range(1, height + 1):
        for j in range(i):
            print("*", end=" ")
        print()


height = int(input("Enter the height of the triangle: "))


print_triangle(height)



