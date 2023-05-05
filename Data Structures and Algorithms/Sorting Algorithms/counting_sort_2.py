def counting_sort(list, digit):
    """
    sorts a list of nonnegative integers in ascending order
    unstable version used as a helper for radix sort

    takes O(n + k) time where
    k is the maximum value in the list
    n is the length of the list
    """
    n = len(list)
    count = [0] * 10
    new_list = [0] * n

    for i in range(n) :
        index = int((list[i]/digit)%10)
        count[index] += 1

    for i in range(1, 10):
        count[i] = count[i] + count[i-1]

    for i in range (n-1, -1, -1):
        index = int((list[i]/digit)%10)
        new_list[count[index]-1] = list[i]
        count[index] -= 1

    for i in range(n):
        list[i] = new_list[i]

    return list

# Test Case
def verify(list):
    list_copy = list[:]
    list_copy.sort()
    return list == list_copy

def main():
    test_list = [1, 3, 1, 4, 9, 6, 3, 4, 5, 8, 3, 4, 8]
    sorted = counting_sort(test_list, 1)
    print(sorted)
    print(verify(sorted))

if __name__ == "__main__":
    main()