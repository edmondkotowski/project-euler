# 10001st prime
from math import sqrt


# get primes numbers
def sieve_of_eratosthenes(n):
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

print "10001st prime number is: {}".format(
    sieve_of_eratosthenes(1000000)[10000])

