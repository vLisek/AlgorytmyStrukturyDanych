def znajdz_trojke(lista, target):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lista[i] + lista[j] + lista[k] == target:
                    return i, j, k
    return None

print(znajdz_trojke([1, 5, 2, 8, 4], 11))
print(znajdz_trojke([1, 2, 3, 4], 20))

# Złożoność obliczeniowa czasowa: O(n^3)
# Złożoność obliczeniowa pamięciowa: O(1)

# Dla czwórki liczb:
# Złożoność obliczeniowa czasowa: O(n^4)
# Złożoność obliczeniowa pamięciowa: O(1)
