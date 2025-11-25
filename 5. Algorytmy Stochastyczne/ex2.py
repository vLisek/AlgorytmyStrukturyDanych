import random
import math

def cena_laptopa(sklep_nr):
    random.seed(sklep_nr)
    return 2000 + random.randint(-500, 500) + abs(sklep_nr - 42) * 5


def simulated_annealing(max_sklep_nr, T_poczatkowa, wspolczynnik_chlodzenia, max_iteracji):
    aktualny_sklep = random.randint(0, max_sklep_nr)
    aktualna_cena = cena_laptopa(aktualny_sklep)

    najlepszy_sklep = aktualny_sklep
    najlepsza_cena = aktualna_cena

    T = T_poczatkowa

    for i in range(max_iteracji):
        if T < 1e-8:
            break

        sasiad_sklep = aktualny_sklep + random.randint(-2, 2)

        sasiad_sklep = max(0, min(max_sklep_nr, sasiad_sklep))

        cena_sasiada = cena_laptopa(sasiad_sklep)

        delta_E = cena_sasiada - aktualna_cena

        if delta_E < 0:
            aktualny_sklep = sasiad_sklep
            aktualna_cena = cena_sasiada

            if aktualna_cena < najlepsza_cena:
                najlepsza_cena = aktualna_cena
                najlepszy_sklep = aktualny_sklep

        else:
            P = math.exp(-delta_E / T)
            if random.random() < P:
                aktualny_sklep = sasiad_sklep
                aktualna_cena = cena_sasiada

        T *= wspolczynnik_chlodzenia

    return najlepszy_sklep, najlepsza_cena

max_sklep_nr = 100
T_poczatkowa = 1000.0
wspolczynnik_chlodzenia = 0.995
max_iteracji = 10000

najtanszy_sklep, min_cena = simulated_annealing(
    max_sklep_nr,
    T_poczatkowa,
    wspolczynnik_chlodzenia,
    max_iteracji
)

print(f"Estymowany najtańszy sklep: {najtanszy_sklep}")
print(f"Najniższa znaleziona cena: {min_cena}")