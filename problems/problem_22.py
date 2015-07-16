# Names scores
# Total names scores from names.txt

def get_names():
    f = open('files/names.txt', 'r')
    names = f.read()
    return sorted(names.split(','))


def names_scores():
    total_name_score = 0
    count = 1
    names = get_names()
    for name in names:
        name = name.replace('"', "")
        name_sum = 0
        for char in name:
            name_sum += ord(char) - ord('A') + 1

        total_name_score += count * name_sum
        count += 1

    return total_name_score

print names_scores()