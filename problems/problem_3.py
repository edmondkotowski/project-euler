# Largest prime factor

from math import sqrt


def get_prime_factors(n):
    prime_factors = set()
    for i in range(2, int(sqrt(n))):
        power = 0
        while n % i == 0:
            n /= i
            power += 1
            prime_factors.add(i)

    return prime_factors

print max(get_prime_factors(600851475143))
