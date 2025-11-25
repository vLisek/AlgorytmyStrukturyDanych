import collections

def zaplanuj_dostawy(paczki, pojemnosc):
    paczki_sorted = sorted(paczki, key=lambda x: (x[2], -x[3]))

    max_deadline = max(p[2] for p in paczki)
    harmonogram = collections.defaultdict(list)
    zajetosc_dzienna = collections.defaultdict(int)

    for nazwa, rozmiar, deadline, wartosc in paczki_sorted:

        for dzien in range(1, deadline + 1):

            if zajetosc_dzienna[dzien] + rozmiar <= pojemnosc:
                harmonogram[dzien].append(nazwa)
                zajetosc_dzienna[dzien] += rozmiar
                break

    return dict(harmonogram)

paczki = [
    ("Paczka A", 5, 3, 100),
    ("Paczka B", 3, 2, 80),
    ("Paczka C", 4, 4, 120),
    ("Paczka D", 2, 2, 60),
]
pojemnosc_auta = 10

plan_dostaw = zaplanuj_dostawy(paczki, pojemnosc_auta)

total_value = 0
paczki_map = {p[0]: p[3] for p in paczki}

for day_list in plan_dostaw.values():
    for item_name in day_list:
        total_value += paczki_map[item_name]

print(f"Pojemność auta: {pojemnosc_auta}")
print("Harmonogram dostaw:")
print(plan_dostaw)
print(f"Maksymalna uzyskana wartość: {total_value}")