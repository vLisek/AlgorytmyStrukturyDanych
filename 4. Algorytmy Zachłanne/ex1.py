import heapq

def min_sal(wyklady):
    wyklady_sorted = sorted(wyklady, key=lambda x: x[1])

    zajete_sale = []
    wolne_numery = []
    przydzial = {}
    max_room_id = 0

    for nazwa, start, koniec in wyklady_sorted:
        while zajete_sale and zajete_sale[0][0] <= start:
            _, room_id = heapq.heappop(zajete_sale)
            heapq.heappush(wolne_numery, room_id)

        if wolne_numery:
            room_id = heapq.heappop(wolne_numery)
        else:
            max_room_id += 1
            room_id = max_room_id

        heapq.heappush(zajete_sale, (koniec, room_id))
        przydzial[nazwa] = room_id

    return max_room_id, przydzial

wyklady_1 = [
    ("Wykład A", 9, 10),
    ("Wykład B", 9, 11),
    ("Wykład C", 10, 12),
    ("Wykład D", 11, 13),
]
print(f"Test 1: {min_sal(wyklady_1)}")

wyklady_2 = [
    ("A", 1, 5),
    ("B", 2, 4),
    ("C", 3, 4)
]
print(f"Test 2: {min_sal(wyklady_2)}")

wyklady_3 = [
    ("A", 1, 2),
    ("B", 2, 3),
    ("C", 3, 4)
]
print(f"Test 3: {min_sal(wyklady_3)}")