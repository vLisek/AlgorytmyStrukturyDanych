def wydaj_reszte_zachlannie(kwota, monety):
    monety = sorted(monety, reverse=True)
    liczba_monet = 0
    for m in monety:
        while kwota >= m:
            kwota -= m
            liczba_monet += 1
    return liczba_monet

def wydaj_reszte_bruteforce(kwota, monety):
    if kwota == 0:
        return 0
    if kwota < 0:
        return float('inf')

    min_monet = float('inf')
    for m in monety:
        wynik = wydaj_reszte_bruteforce(kwota - m, monety)
        min_monet = min(min_monet, wynik + 1)

    return min_monet

def czy_system_kanoniczny(monety, max_kwota):
    for i in range(1, max_kwota + 1):
        zachlanny = wydaj_reszte_zachlannie(i, monety)
        optymalny = wydaj_reszte_bruteforce(i, monety)

        if zachlanny > optymalny:
            return False, i
    return True, None

monety = [1, 5, 2]
kwota = 6

wynik_zachlanny = wydaj_reszte_zachlannie(kwota, monety)
wynik_bruteforce = wydaj_reszte_bruteforce(kwota, monety)

print(f"Kwota: {kwota}")
print(f"Zachłannie: {wynik_zachlanny}")
print(f"Brute Force: {wynik_bruteforce}")

if wynik_zachlanny > wynik_bruteforce:
    print("Zachłanny dał gorszy wynik.")

is_kanoniczny, kontrprzyklad = czy_system_kanoniczny(monety, 20)
print(f"Czy kanoniczny: {is_kanoniczny}")
if kontrprzyklad:
    print(f"Błąd dla kwoty: {kontrprzyklad}")