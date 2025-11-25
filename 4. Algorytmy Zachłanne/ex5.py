def zaplanuj_z_przerwami(zadania, min_przerwa, max_h):
    przerwa_h = min_przerwa / 60.0

    zadania_przetworzone = []
    for nazwa, sh, eh in zadania:
        zadania_przetworzone.append((nazwa, sh, eh, eh + przerwa_h))

    zadania_przetworzone.sort(key=lambda x: x[3])

    wybrane_zadania = []
    ostatni_koniec = 0.0
    calkowity_czas = 0.0

    for nazwa, start_h, end_h, _ in zadania_przetworzone:

        if start_h >= ostatni_koniec + przerwa_h:

            czas_zadania = end_h - start_h

            czas_przerwy = przerwa_h if ostatni_koniec > 0 else 0.0

            nowy_calkowity_czas = calkowity_czas + czas_przerwy + czas_zadania

            if nowy_calkowity_czas <= max_h:
                wybrane_zadania.append(nazwa)
                ostatni_koniec = end_h
                calkowity_czas = nowy_calkowity_czas

    return wybrane_zadania, calkowity_czas

zadania = [
    ("Meeting", 9, 10),
    ("Coding", 10, 12),
    ("Lunch", 12, 13),
    ("Review", 13, 14),
]
min_przerwa = 30
max_godzin_dziennie = 8

wybrane, czas = zaplanuj_z_przerwami(zadania, min_przerwa, max_godzin_dziennie)

print(wybrane)
print(f"Całkowity czas (z przerwami): {czas} h")