import heapq

def lacz_pliki(rozmiary):
    heap = list(rozmiary)
    heapq.heapify(heap)

    koszt_calkowity = 0
    historia_laczen = []

    while len(heap) > 1:
        plik1 = heapq.heappop(heap)
        plik2 = heapq.heappop(heap)

        koszt_operacji = plik1 + plik2
        koszt_calkowity += koszt_operacji
        historia_laczen.append((plik1, plik2))

        heapq.heappush(heap, koszt_operacji)

    return koszt_calkowity, historia_laczen

pliki = [20, 30, 10, 5]
min_koszt, kroki = lacz_pliki(pliki)

print(f"Minimalny koszt: {min_koszt}")
print("Kolejność łączeń:")
for p1, p2 in kroki:
    print(f"Połączono {p1} i {p2} (koszt {p1 + p2})")