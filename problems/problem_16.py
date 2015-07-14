# power digit sum


def power_digit_sum(exp):
    return sum([int(x) for x in str(2**exp)])

print power_digit_sum(1000)