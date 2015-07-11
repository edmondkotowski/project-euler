# Sum of even terms in the fibonacci sequence who values are < 4 million

FIB_LOOKUP = {}

def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    if n - 1 not in FIB_LOOKUP:
        FIB_LOOKUP[n - 1] = fibonacci(n - 1)

    if n - 2 not in FIB_LOOKUP:
        FIB_LOOKUP[n - 2] = fibonacci(n - 2) 

    value = FIB_LOOKUP[n - 1] + FIB_LOOKUP[n - 2]
    if n not in FIB_LOOKUP:
        FIB_LOOKUP[n] = value

    return value

def sum_even_fibonacci_numbers(n):
    fibonacci(n)
    return sum([FIB_LOOKUP[x] for x in range(1, n+1) 
               if FIB_LOOKUP[x] % 2 == 0])


if __name__ == "__main__":
    # 34 generates the the smallest fibonacci term (5702887) whose values 
    # is greater than 4 million
    n = 34
    print "Sum of even fibonacci values < 4 million: {sum}".format(
        sum=sum_even_fibonacci_numbers(n))