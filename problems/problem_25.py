from utilities.fibonacci import fibonacci


def calc_1000_digit_fibonacci_number():
    n = 1
    while True:
        if len(str(fibonacci(n))) == 1000:
            break
        n += 1

    return n

print calc_1000_digit_fibonacci_number()