import random
import math

def symuluj_bladzacych(liczba_osob, liczba_krokow, dystans_min):
    osoby_poza_zakresem = 0

    for _ in range(liczba_osob):
        x = 0
        y = 0
        for _ in range(liczba_krokow):
            dx = random.choice([-1, 1])
            dy = random.choice([-1, 1])
            kierunek = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            x += kierunek[0]
            y += kierunek[1]
        odleglosc = math.sqrt(x ** 2 + y ** 2)
        if odleglosc > dystans_min:
            osoby_poza_zakresem += 1
    procent_poza_zakresem = (osoby_poza_zakresem / liczba_osob) * 100

    return procent_poza_zakresem

LICZBA_OSOB = 1000
LICZBA_KROKOW = 100
MIN_DYSTANS = 20

procent_daleko = symuluj_bladzacych(LICZBA_OSOB, LICZBA_KROKOW, MIN_DYSTANS)

print(f"Liczba symulacji: {LICZBA_OSOB}")
print(f"Liczba kroków: {LICZBA_KROKOW}")
print(f"Minimalna odległość od baru: {MIN_DYSTANS} m")
print(f"Procent osób dalej niż {MIN_DYSTANS} m: {procent_daleko:.2f}%")