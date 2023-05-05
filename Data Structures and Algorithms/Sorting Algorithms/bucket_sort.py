import random
 
def bucketSort(array):
    largest = max(array)
    length = len(array)
    size = largest/length
 
    # Create Buckets
    buckets = [[] for i in range(length)]
 
    # Bucket Sorting   
    for i in range(length):
        index = int(array[i]/size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])
 
    # Sorting Individual Buckets  
    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])
 
 
    # Flattening the Array
    result = []
    for i in range(length):
        result = result + buckets[i]
             
    return result
