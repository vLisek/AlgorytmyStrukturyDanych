costs = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

best = float('inf')
best_assign = []

def solve(person, used, cost, assign):
    global best, best_assign
    if person == len(costs):
        if cost < best:
            best, best_assign = cost, assign[:]
        return
    if cost >= best:
        return
    for task in range(len(costs[0])):
        if task not in used:
            solve(person + 1, used | {task}, cost + costs[person][task], assign + [task])

solve(0, set(), 0, [])
print("Najlepszy przydział:", best_assign)
print("Minimalny koszt:", best)
