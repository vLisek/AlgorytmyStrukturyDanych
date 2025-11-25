def can_partition(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False

    target = total // 2
    possible = {0}

    for num in arr:
        new_sums = set()
        for s in possible:
            if s + num == target:
                print("Znaleziono podzbiór o sumie:", target)
                return True
            if s + num < target:
                new_sums.add(s + num)
        possible |= new_sums
        print("Po dodaniu", num, "możliwe sumy:", possible)

    return target in possible


arr = [1, 5, 11, 5]
print("Wynik:", can_partition(arr))
