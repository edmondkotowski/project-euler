# Number letter counts

LOOKUP = {'1': 'one',
          '2': 'two',
          '3': 'three',
          '4': 'four',
          '5': 'five',
          '6': 'six',
          '7': 'seven',
          '8': 'eight',
          '9': 'nine',
          '10': 'ten',
          '11': 'eleven',
          '12': 'twelve',
          '13': 'thirteen',
          '14': 'fourteen',
          '15': 'fifteen',
          '16': 'sixteen',
          '17': 'seventeen',
          '18': 'eighteen',
          '19': 'nineteen',
          '20': 'twenty',
          '30': 'thirty',
          '40': 'forty',
          '50': 'fifty',
          '60': 'sixty',
          '70': 'seventy',
          '80': 'eighty',
          '90': 'ninety',
          '1000': 'one thousand'}


def convert_num_to_english(n):
    value = str(n)
    if value in LOOKUP:
        return LOOKUP[value]

    if len(value) == 2:
        return "{}-{}".format(LOOKUP[value[0] + "0"], LOOKUP[value[1]])

    if len(value) == 3:
        if value[1] == '0':
            if value[2] == '0':
                return "{} hundred".format(
                    LOOKUP[value[0]])
            else:
                return "{} hundred and {}".format(
                    LOOKUP[value[0]], LOOKUP[value[2]])
        elif value[1] == '1':
            return "{} hundred and {}".format(
                LOOKUP[value[0]], LOOKUP[value[1] + value[2]])
        elif value[2] == '0':
            return "{} hundred and {}".format(
                LOOKUP[value[0]], LOOKUP[value[1] + "0"])

        return "{} hundred and {}-{}".format(
            LOOKUP[value[0]], LOOKUP[value[1] + "0"], LOOKUP[value[2]])


def number_letter_counts():
    sum_of_letter_counts = 0
    for i in range(1, 1001):
        english_number = convert_num_to_english(i)
        english_number = english_number.replace(" ", "")
        english_number = english_number.replace("-", "")
        sum_of_letter_counts += len(english_number)

    return sum_of_letter_counts

print number_letter_counts()