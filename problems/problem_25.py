FIB_LOOKUP = {}


def fibonacci(n):
    if n == 1 or n == 2:
        FIB_LOOKUP[n] = 1
        return 1

    if n in FIB_LOOKUP:
        return FIB_LOOKUP[n]

    FIB_LOOKUP[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return FIB_LOOKUP[n]


def calc_1000_digit_fibonacci_number():
    n = 1
    while True:
        if len(str(fibonacci(n))) == 1000:
            break
        n += 1

    return n

print calc_1000_digit_fibonacci_number()