import random
import sys
# from load import load_numbers

# number = load_numbers(sys.argv[1])
# print(number)


def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def bogo_sort(values):
    attempts = 0

    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values


print(bogo_sort([5, 8, 1, 4, 7, 9, 6, 3, 2]))
