board = [
    ['T', 'A', 'K', 'O'],
    ['R', 'A', 'M', 'A'],
    ['S', 'O', 'L', 'E'],
    ['M', 'A', 'T', 'A']
]

dictionary = ["TAK", "RAMA", "SALA", "TAMA", "MATA", "MA", "ALE", "SOM", "TAM", "MAL", "KOT", "KORA", "SOLA"]

prefixes = set()
for word in dictionary:
    for i in range(1, len(word) + 1):
        prefixes.add(word[:i])

found_words = set()
ROWS, COLS = len(board), len(board[0])

def backtrack(r, c, visited, current):
    if current not in prefixes:
        return

    if current in dictionary:
        found_words.add(current)

    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
            backtrack(nr, nc, visited | {(nr, nc)}, current + board[nr][nc])

for r in range(ROWS):
    for c in range(COLS):
        backtrack(r, c, {(r, c)}, board[r][c])

print("Znalezione słowa:")
for w in sorted(found_words):
    print(" ", w)
print(f"\nŁącznie znaleziono: {len(found_words)} słów.")
