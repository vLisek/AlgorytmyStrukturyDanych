import random
import string

target = "PYTHON"
dlugosc_hasla = len(target)
mozliwe_znaki = string.ascii_uppercase
ROZMIAR_POPULACJI = 100
WSPOLCZYNNIK_MUTACJI = 0.05
MAX_GENERACJI = 1000

def oblicz_fitness(osobnik):
    fitness = 0
    for i in range(dlugosc_hasla):
        if osobnik[i] == target[i]:
            fitness += 1
    return fitness

def stworz_losowego_osobnika():
    return ''.join(random.choice(mozliwe_znaki) for _ in range(dlugosc_hasla))


def selekcja_turniejowa(populacja, fitnessy, rozmiar_turnieju=5):
    zwyciezca = random.choice(populacja)
    for _ in range(rozmiar_turnieju - 1):
        kandydat = random.choice(populacja)
        if fitnessy[kandydat] > fitnessy[zwyciezca]:
            zwyciezca = kandydat
    return zwyciezca


def krzyzowanie(rodzic1, rodzic2):
    punkt_przeciecia = random.randint(1, dlugosc_hasla - 1)
    potomek1 = rodzic1[:punkt_przeciecia] + rodzic2[punkt_przeciecia:]
    potomek2 = rodzic2[:punkt_przeciecia] + rodzic1[punkt_przeciecia:]
    return potomek1, potomek2


def mutacja(osobnik, wspolczynnik_mutacji):
    osobnik_lista = list(osobnik)
    for i in range(dlugosc_hasla):
        if random.random() < wspolczynnik_mutacji:
            osobnik_lista[i] = random.choice(mozliwe_znaki)
    return "".join(osobnik_lista)


def algorytm_genetyczny():
    populacja = [stworz_losowego_osobnika() for _ in range(ROZMIAR_POPULACJI)]

    for generacja in range(MAX_GENERACJI):

        fitnessy = {osobnik: oblicz_fitness(osobnik) for osobnik in populacja}
        najlepszy_osobnik = max(populacja, key=lambda x: fitnessy[x])
        najlepszy_fitness = fitnessy[najlepszy_osobnik]

        if generacja % 50 == 0 or najlepszy_fitness == dlugosc_hasla:
            print(f"Generacja {generacja}: Najlepszy osobnik = {najlepszy_osobnik} (Fitness: {najlepszy_fitness})")

        if najlepszy_fitness == dlugosc_hasla:
            return najlepszy_osobnik, generacja

        nowa_populacja = []

        while len(nowa_populacja) < ROZMIAR_POPULACJI:
            rodzic1 = selekcja_turniejowa(populacja, fitnessy)
            rodzic2 = selekcja_turniejowa(populacja, fitnessy)

            potomek1, potomek2 = krzyzowanie(rodzic1, rodzic2)

            nowa_populacja.append(mutacja(potomek1, WSPOLCZYNNIK_MUTACJI))
            if len(nowa_populacja) < ROZMIAR_POPULACJI:
                nowa_populacja.append(mutacja(potomek2, WSPOLCZYNNIK_MUTACJI))

        populacja = nowa_populacja

    return "Nie znaleziono w maksymalnej liczbie generacji.", MAX_GENERACJI


wynik, generacja = algorytm_genetyczny()

print("\n--- WYNIK KOŃCOWY ---")
print(f"Hasło docelowe: {target}")
print(f"Znalezione hasło: {wynik}")
print(f"Znalezione w generacji: {generacja}")