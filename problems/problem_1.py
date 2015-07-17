# Sum of multiples of 3 or 5 below 1000


def sum_of_multiples():
    return sum([x for x in range(0, 1000) if x % 3 == 0 or x % 5 == 0])

if __name__ == "__main__":
    print "Sum of multiple of 3 or 5 below 1000: {sum}".format(
        sum=sum_of_multiples())