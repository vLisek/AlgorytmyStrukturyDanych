import random

def estimate_integral(n_samples):
    trafienia = 0

    for _ in range(n_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        wartosc_funkcji = x ** 2
        if y <= wartosc_funkcji:
            trafienia += 1
    integral_estimate = trafienia / n_samples
    return integral_estimate

N = 1000000
estymacja = estimate_integral(N)

print(f"Liczba próbek (N): {N}")
print(f"Estymowane pole pod krzywą: {estymacja:.4f}")
print(f"Prawidłowa wartość: {1 / 3:.4f}")