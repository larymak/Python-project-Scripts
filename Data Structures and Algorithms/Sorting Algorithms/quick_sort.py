import sys
# from load import load_numbers

# numbers = load_numbers(sys.argv[1])


def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    # print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


# print([5, 8, 1, 4, 7, 9, 6, 3, 2])
sorted_numbers = quicksort([5, 8, 1, 4, 7, 9, 6, 3, 2])
print(sorted_numbers)
