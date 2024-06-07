def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # gap size

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Perform insertion sort for the elements separated by the gap
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2 

    return arr

print(shell_sort([5, 8, 1, 4, 7, 9, 6, 3, 2]))
