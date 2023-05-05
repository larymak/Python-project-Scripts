import sys
# from load import load_strings

# names = load_strings(sys.argv[1])

search_names = ["habib", "adam", "nasir", "jelilat"]


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


sorted_names = quicksort(search_names)
for n in sorted_names:
    print(n)
