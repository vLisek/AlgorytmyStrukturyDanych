def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
            print("Użyto monety:", coin, "| Pozostało:", amount)

    if amount == 0:
        print("Minimalna liczba monet:", count)
        return count
    else:
        print("Nie da się wydać tej kwoty.")
        return -1


coins = [1, 5, 10, 25]
amount = 30
coin_change(coins, amount)
