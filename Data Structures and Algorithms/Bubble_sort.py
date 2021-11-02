
def BubbleSort(array):

    # Loop to access each array element
    for i in range(len(array)):
        for j in range(0,len(array)-1-i):
            # Replace > with < for descending order
            if array[j] > array[j+1]:

                # Swapping elements if elements are not in the intended order
                temp = array[j] 
                array[j] = array[j+1]
                array[j+1] = temp
    return array


# Driver code
if __name__ == '__main__':
    Array = [-1,9,21,34,1,5,6,8,10,23,25,27,31]
    print("Array before sorting: ", Array)
    print("Array after sorting: ", BubbleSort(Array))