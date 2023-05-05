from counting_sort_2 import counting_sort, verify

def radix_sort(list):
    """
    sorts a list of integers in ascending order in a particular base
    
    takes O(d(n + k)) where:
    d is the number of digits of the maximum element
    k is the maximum value in the list
    n is the length of the list
    """

    max_val = max(list)
    digit = 1

    while digit < max_val:
        counting_sort(list, digit)
        digit *= 10

    return list

# Test Case
test_list = [54, 897, 434, 4, 8, 209, 33, 578, 443, 930, 564, 25, 347, 6, 1]
sorted = radix_sort(test_list)
print(sorted)
print(verify(sorted))
    