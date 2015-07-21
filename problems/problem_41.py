# Circular primes

from utilities.primes import primes


def is_pan_digital(n):
    n = str(n)
    if '0' in n or len(n) != len(set(n)):
        return False

    sum_of_n = sum([int(i) for i in n])
    max_value = max([int(i) for i in n])
    sum_max = (max_value * (max_value + 1)) / 2
    return sum_of_n - sum_max == 0


def get_largest_pan_digital_prime():
    prime_nums = primes(10000000)
    return max([x for x in prime_nums if is_pan_digital(x)])

print get_largest_pan_digital_prime()

