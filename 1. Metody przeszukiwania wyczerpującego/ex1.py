def zlam_haslo(prawdziwe_haslo: str) -> int:
    alfabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    proby = 0

    for a in alfabet:
        for b in alfabet:
            for c in alfabet:
                proby += 1
                haslo = a + b + c
                if haslo == prawdziwe_haslo:
                    print(f'Znaleziono hasło "{haslo}" po {proby} próbach.')
                    return proby

    print("Hasło nie należy do przestrzeni przeszukiwania.")
    return proby

zlam_haslo("999")

# Złożoność obliczeniowa czasowa: O(36^3).
# Złożoność obliczeniowa pamięciowa: O(1).
# Maksymalna liczba prób (najgorszy przypadek): 36^3 = 46656.