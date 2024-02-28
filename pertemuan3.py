"""fruits = ["Anggur", "Cherry", "Salak"]
newFruits = ["Mangga", "Jeruk", "Pisang", "Manggis"]
fruits.extend(newFruits)
print(fruits)
#Mengurutkan sesuai abjad
fruits.sort()
print(fruits)
#Menghapus Objek
fruits.remove("Cherry")
print(fruits)

students = ['Ari', 'Budi', 'Cindy', 'Diana', 'Erik', 'Felix']

# fungsi 
def bagi_list(list):
  list_ganjil = []
  list_genap = []
  
  for index, item in enumerate(list):
    if (index+1) % 2 == 0:
      list_genap.append(item)
    else:
      list_ganjil.append(item)
  
  return list_ganjil, list_genap


ganjil, genap = bagi_list(students)
print(f"Kelompok ganjil = {ganjil} ")
print(f"Kelompok genap = {genap} ")

siswa = ['Ari', 'Budi', 'Cindy', 'Diana', 'Erik', 'Felix']

print(siswa[1])
print(siswa[-3])
print(siswa[2:4])

del siswa[0]
print(siswa)
siswa.clear()
print(siswa)

alphabets =['a', 'b', 'c', 'd']
tupleAlphabets = tuple(alphabets)
print(tupleAlphabets)

alphabets = 'abcdefgh'
tuple_alphabets2 = tuple(alphabets)
print(tuple_alphabets2)"""

#Tipe Data Set
#Cara membuat set kosong 
ini_setkosong = set()
newSet = {1, 3, 4, 6, 7, 7, 8, 4, 3, 6, 5}
print(newSet)
print(len(newSet))

