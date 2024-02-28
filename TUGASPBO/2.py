def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def hitungBilangan(n):
    total = 0

    for num in range(1, n + 1):
        if num % 3 == 0 or num % 5 == 0:
            if not is_prime(num):
                total += 1

    return total

n = int(input("Masukkan nilai n: "))
result = hitungBilangan(n)
print(f"Jumlah bilangan yang habis dibagi 3 atau 5 dan bukan prima dalam rentang 1 hingga {n} adalah: {result}")