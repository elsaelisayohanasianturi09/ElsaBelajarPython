print("Pencarian Data secara Linier")
print()
numbers : int = [2,34,56,33,24,56,34,26,56]
nilaiYangAkandiCari = 24

i = 0
while i < len(numbers) and numbers[i] != nilaiYangAkandiCari :
    i =  i + 1

if numbers[i] == nilaiYangAkandiCari :
    print(f"Nilai {nilaiYangAkandiCari} ditemukan pada indeks ke- {i}")
else :
    print(f"Angka tidak ditemukan pada kumpulan data")

print()
print("Cara mencari nilai yang tidak ada didalam sekumpulan data tersebut")

def pencarianLinier (data : list, target : any)-> int :
    i = 0
    while i < len(numbers) :
        if numbers[i] == nilaiYangAkandiCari :
            return i
        i = i + 1
    return -1 #Mengembalikan nilai -1 jika data tidak ditemukan dalam sekumpulan array

numbers : int = [2, 354, 56, 35, 37, 99, 60]
nilaiYangAkandiCari = 100
output = pencarianLinier(numbers, nilaiYangAkandiCari)
if output != -1 :
    print(f"Angka {nilaiYangAkandiCari} ditemukan dalam indeks ke {i}")
else :
    print("Angka tidak ditemukan dalam sekumpulan data")
print()
print("Metode yang lain")
numbers = [23,99,55,49,89,72,9,13,42,62]
number_what_we_looking_for = 42

i = 0

last = numbers.pop()
numbers.append(number_what_we_looking_for)

while numbers[i] != number_what_we_looking_for:
    i = i + 1

numbers[-1] = last

if i < len(numbers) - 1 or numbers[-1] == number_what_we_looking_for:
    print(f"Angka {number_what_we_looking_for} ditemukan pada indeks ke-{i}.")
else:
    print("Angka tidak ditemukan dalam kumpulan data.")
print()
print("Mencari data dengan metode sorted list")
numbers = [23,99,55,49,89,72,9,13,42,62]
number_what_we_looking_for = 42

numbers = sorted(numbers)

i = 0

last = numbers.pop()
numbers.append(number_what_we_looking_for)

print()
print("Metode pencarian data dengan binary serach")
numbers = [23,99,55,49,89,72,9,13,42,62]
number_what_we_looking_for = 42

numbers = sorted(numbers)

low = 0
high = len(numbers) - 1

found = False
mid = 0

while low <= high and not found:
    mid = (low + high) // 2
    mid_value = numbers[mid]

    if mid_value == number_what_we_looking_for:
        found = True
    elif mid_value < number_what_we_looking_for:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print(f"Angka {number_what_we_looking_for} ditemukan pada indeks ke-{mid}.")
else:
    print("Angka tidak ditemukan dalam kumpulan data.")

print()
print()
print("sorting")
def counting_sort(numbers: list) -> list:
    max_value = max(numbers)  # Menentukan nilai maksimum dalam data
    min_value = min(numbers)  # Menentukan nilai minimum dalam data
    range_values = max_value - min_value + 1  # Mencari rentang nilai data
    # Membuat list kosong untuk menyimpan frekuensi kemunculan setiap nilai
    count = [0] * range_values
    # Menghitung frekuensi kemunculan setiap nilai dalam data
    for num in numbers:
        count[num - min_value] += 1
    # Mengakumulasi jumlah dalam count list
    for i in range(1, range_values):
        count[i] += count[i - 1]
    # Membuat list kosong baru untuk menyimpan data yang sudah diurutkan
    sorted_numbers = [0] * len(numbers)
    # Mengatur data yang akan diurutkan berdasarkan count list
    for num in numbers:
        index = count[num - min_value] - 1
        sorted_numbers[index] = num
        count[num - min_value] -= 1
    return sorted_numbers
 
# main program
numbers = [1,3,2,5,1,6,1,3,2,1]
 
sorted_data_counting_sort = counting_sort(numbers)
print("Data sebelum diurutkan:", numbers)
print("Data setelah diurutkan:", sorted_data_counting_sort)

print()
print()
print("REKURSIF")

def rekursif(n : int) -> int :
    if n == 0 :
        return 0 
    elif n == 1 :
        return 1
    else :
        return rekursif(n-1) + rekursif(n-2) 
n = 14
output : int = rekursif(n)
print(f"Hasil dari Fibonacci {n} adalah {output}")