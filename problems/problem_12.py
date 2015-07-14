# Highly divisible triangular number
from math import sqrt


def calc_triangular_numbers(n):
    return (n * (n + 1))/2


def get_factor_count(num):
    num_factors = 1
    n = num
    for i in range(2, int(sqrt(n))):
        power = 0
        while num % i == 0:
            num /= i
            power += 1
        num_factors *= (power + 1)

    if num > 1:
        num_factors *= 2

    return num_factors


def get_triangle_number_with_over_n_divisors(n):
    factor_amount = 0
    triangle = 1
    tri_num = 0
    while factor_amount < n:
        tri_num = calc_triangular_numbers(triangle)
        factor_amount = get_factor_count(tri_num)
        triangle += 1

    return tri_num