
def selectionSort(Array, size):
    
    for i in range(size):
        min_indx = i

        for j in range(i+1, size):

            # To sort in descending order, change > to < in this line
            # Select the minimum element in each loop
            if Array[j] < Array[min_indx]:
                min_indx = j
        
        # Put minimum eement at the correct position
        (Array[i], Array[min_indx]) = (Array[min_indx], Array[i])
    return Array

if __name__ == "__main__":
    Array = [-2, -3, -1, 11, 9, 12, 4, -5, -12, 6, 19, 20]
    size = len(Array)
    print("Array before sorting: ", Array)
    Array = selectionSort(Array, size)
    print("Array after sorting: ", Array)