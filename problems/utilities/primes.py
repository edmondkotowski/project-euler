from math import sqrt


# return list of primes numbers using sieve of eratosthenes
def primes(n):
    values = [True] * n

    for i in range(2, int(sqrt(n) + 1)):
        if values[i]:
            j = i**2
            count = 1
            while j < n:
                values[j] = False
                j = i**2 + count * i
                count += 1

    return [x for x in range(2, len(values)) if values[x]]