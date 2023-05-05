def counting_sort(list):
    """
    sorts a list of nonnegative integers in ascending order
    
    takes O(n + k) time where
    k is the maximum value in the list
    n is the length of the list
    """

    k = max(list)
    n = len(list)
    count = [0] * (k+1)
    new_lst = [0] * n

    # Counting Sort algorithm
    for i in range(n):
        count[list[i]] += 1

    for i in range(1, k+1):
        count[i] += count[i-1]

    for i in range(n):
        new_lst[count[list[i]]-1] = list[i]
        count[list[i]] -= 1

    # Copy elements back into original list
    for i in range(n):
        list[i] = new_lst[i]

    return list

# Test Case
def verify(list):
    list_copy = list[:]
    list_copy.sort()
    return list == list_copy

test_list = [1, 3, 1, 4, 10, 6, 3, 4, 5, 8, 3, 4, 8]
sorted = counting_sort(test_list)
print(sorted)
print(verify(sorted))