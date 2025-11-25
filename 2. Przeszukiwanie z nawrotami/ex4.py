N = 3
target_sum = 15
numbers = list(range(1, 10))

solutions = []

def is_valid(partial):
    for i in range(N):
        row = [partial[j] for j in range(i*N, min((i+1)*N, len(partial)))]
        if len(row) == N and sum(row) != target_sum:
            return False
        if sum(row) > target_sum:
            return False

    for c in range(N):
        col = [partial[r*N + c] for r in range(N) if r*N + c < len(partial)]
        if len(col) == N and sum(col) != target_sum:
            return False
        if sum(col) > target_sum:
            return False

    diag1 = [partial[i*N + i] for i in range(N) if i*N + i < len(partial)]
    diag2 = [partial[i*N + (N - 1 - i)] for i in range(N) if i*N + (N - 1 - i) < len(partial)]
    for d in [diag1, diag2]:
        if len(d) == N and sum(d) != target_sum:
            return False
        if sum(d) > target_sum:
            return False

    return True


def backtrack(partial, remaining):
    if len(partial) == N*N:
        if is_valid(partial):
            solutions.append(partial[:])
        return

    for num in remaining:
        if not is_valid(partial + [num]):
            continue
        backtrack(partial + [num], [x for x in remaining if x != num])


backtrack([], numbers)

print(f"Znaleziono {len(solutions)} rozwiązań:")
for sol in solutions:
    for i in range(0, 9, 3):
        print(sol[i:i+3])
    print("-" * 10)
