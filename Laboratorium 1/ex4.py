def najkrotsza_trasa(macierz):
    najlepszy_koszt = float('inf')
    najlepsza_trasa = None

    for b in (1, 2, 3):
        for c in (1, 2, 3):
            if c == b:
                continue
            for d in (1, 2, 3):
                if d == b or d == c:
                    continue

                obecna_trasa = [0, b, c, d, 0]
                obecny_koszt = (
                    macierz[obecna_trasa[0]][obecna_trasa[1]] +
                    macierz[obecna_trasa[1]][obecna_trasa[2]] +
                    macierz[obecna_trasa[2]][obecna_trasa[3]] +
                    macierz[obecna_trasa[3]][obecna_trasa[4]]
                )

                if obecny_koszt < najlepszy_koszt:
                    najlepszy_koszt = obecny_koszt
                    najlepsza_trasa = obecna_trasa

    return najlepsza_trasa, int(najlepszy_koszt)

macierz_odleglosci = [
    [0, 10, 15, 20],  # A
    [10, 0, 35, 25],  # B
    [15, 35, 0, 30],  # C
    [20, 25, 30, 0]   # D
]

trasa_wynikowa, koszt_wynikowy = najkrotsza_trasa(macierz_odleglosci)

miasta = ["A", "B", "C", "D"]
trasa_literowa = [miasta[i] for i in trasa_wynikowa]

print("Najkrótsza trasa:", " -> ".join(trasa_literowa))
print("Długość trasy:", koszt_wynikowy)
