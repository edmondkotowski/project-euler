# Largest palindrome product of two 3-digit numbers

def is_palindrome(product):
    product = str(product)
    reverse = product[::-1]
    return product == reverse


def largest_palindrome_product():
    left_value = 999
    max_product = 0
    while left_value > 0:
        right_value = 999
        while right_value > 0:
            product = left_value * right_value
            if is_palindrome(product):
                if product > max_product:
                    max_product = product
            right_value -= 1
        left_value -= 1

    return max_product

if __name__ == "__main__":
    print "Largest palindrome product: {product}".format(
        product=largest_palindrome_product())
