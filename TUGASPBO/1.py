def jmlhBilangan(n):
    total = 0
    for i in range (1, n) :
        if i % 3 == 0 or i % 5 == 0 :
            total += i
    return total

n  = int(input("Masukkan nilai n : "))
hasil = jmlhBilangan(n)
print(f"Jumlah bilangan yang habis dibagi 3 atau 5 dalam rentang 1 - {n} adalah {hasil}")