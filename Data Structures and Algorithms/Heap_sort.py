
def Heapify(Array, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and Array[l] > Array[largest]:
        largest = l

    if r < n and Array[r] > Array[largest]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        Array[i], Array[largest] = Array[largest], Array[i]
        Heapify(Array, n, largest)
    

def HeapSort(Array):
    n = len(Array)

    # Build a max heap
    for i in range(n//2, -1, -1):
        Heapify(Array, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        # Swap
        Array[i], Array[0] = Array[0], Array[i]

        # Heapify root element
        Heapify(Array, i, 0)


if __name__ == "__main__":
    Array = [-2, -3, -1, 11, 9, 12, 4, -5, -12, 6, 19, 20]
    HeapSort(Array)
    n = len(Array)
    print("Sorted array is")
    for i in range(n):
        print("%d " % Array[i], end='')
  