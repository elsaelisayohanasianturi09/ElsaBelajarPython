set1 = {"apel", "jeruk", "nanas", "pisang"}
set2 = {"apel", "anggur", "nanas", "mangga"}

buahdiKeduaSetDenganA = set()

for buah in set.intersection(set2) :
    if "a" in buah :
        buahdiKeduaSetDenganA.add(buah)

print(f"Buah yang ada di kedua set mengandung huruf 'a', {buahdiKeduaSetDenganA}")