# Sum of even terms in the fibonacci sequence who values are < 4 million

from utilities.fibonacci import *

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
