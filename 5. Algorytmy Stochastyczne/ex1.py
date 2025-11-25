import random


def estymuj_podzielne_przez_7(zakres_max, liczba_probek):
    trafienia = 0

    for _ in range(liczba_probek):
        losowa_liczba = random.randint(1, zakres_max)

        if losowa_liczba % 7 == 0:
            trafienia += 1

    proporcja_estymowana = trafienia / liczba_probek

    estymowana_liczba = proporcja_estymowana * zakres_max

    return estymowana_liczba


zakres_max = 100
liczba_probek = 100000

estymacja = estymuj_podzielne_przez_7(zakres_max, liczba_probek)

print(f"Liczba próbek (N): {liczba_probek}")
print(f"Estymowana liczba podzielnych przez 7: {estymacja:.2f}")

print(f"Dokładna liczba (100 // 7): {100 // 7}")