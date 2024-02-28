Buah1 = ('apel', 'jeruk', 'nanas', 'pisang')
Buah2 = ('apel', 'anggur', 'nanas', 'mangga')

print(f"Tuple buah setelah digabungkan, dihapus duplikat dan diurutkan yaitu : {tuple(sorted(set(Buah1 + Buah2)))}")