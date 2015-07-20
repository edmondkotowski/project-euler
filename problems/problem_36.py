# Double-base palindromes


def decimal_to_binary(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n /= 2

    output = []
    while len(binary) != 0:
        output.append(str(binary.pop()))

    return "".join(output)


def is_palindrome(product):
    product = str(product)
    reverse = product[::-1]
    return product == reverse


def sum_of_double_base_palindromes():
    return sum([x for x in range(1, 1000000)
                if is_palindrome(x) and is_palindrome(decimal_to_binary(x))])

print sum_of_double_base_palindromes()