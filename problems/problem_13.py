# Large sum
# Return first ten digits of sum of 100 50 digit numbers


def get_large_num():
    with open('files/large_num.txt', 'r') as f:
        return f.read().replace("\n", "")


def calc_large_sum():
    large_num = get_large_num()
    sum = 0
    batch_size = 50
    i = 0

    while i < len(large_num):
        number = int(large_num[i:i+batch_size])
        i += batch_size
        sum += number

    return str(sum)[0:10]

print calc_large_sum()