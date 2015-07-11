from math import pow

# Sum square difference

def sum_square_difference(n):
    sum_of_squares = sum(int(pow(x, 2)) for x in range(1, n+1))
    sqaure_of_sum = sum(x for x in range(1, n+1))**2
    return sqaure_of_sum - sum_of_squares

if __name__ == "__main__":
    print sum_square_difference(100)

