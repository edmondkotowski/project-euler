# used for memoization of fibonacci sequence
FIB_LOOKUP = {}


def fibonacci(n):
    if n == 1 or n == 2:
        FIB_LOOKUP[n] = 1
        return 1

    if n in FIB_LOOKUP:
        return FIB_LOOKUP[n]

    FIB_LOOKUP[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return FIB_LOOKUP[n]