import sys
# from load import load_numbers

# numbers = load_numbers(sys.argv[1])


def merge_sort(values):
    if len(values) <= 1:
        return values
    middle_index = len(values) // 2
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    # print("%15s %-15s" % (left_values, right_values))
    sorted_values = []
    left_index = 0
    right_index = 0

    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1

    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values


# print([5, 8, 1, 4, 7, 9, 6, 3, 2])
sorted_numbers = merge_sort([5, 8, 1, 4, 7, 9, 6, 3, 2])
print(sorted_numbers)
