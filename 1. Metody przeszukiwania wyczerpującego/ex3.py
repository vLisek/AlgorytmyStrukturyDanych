def znajdz_podzbior_sumy(liczby, target):
    n = len(liczby)

    for maska in range(1, 2**n):
        podzbior = []
        suma = 0
        for i in range(n):
            if maska & (1 << i):
                podzbior.append(liczby[i])
                suma += liczby[i]
        if suma == target:
            return podzbior
    return []

print(znajdz_podzbior_sumy([2, 5, 8, 3], 10))

# Złożoność obliczeniowa czasowa: O(n * 2^n)
# Złożoność obliczeniowa pamięciowa: O(n)

