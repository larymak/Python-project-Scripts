def cycleSort(array):
  writes = 0 # keeps track of the number of writes or swaps made during the sorting process
   
  # Loop through the array to find cycles to rotate.
  for cycleStart in range(0, len(array) - 1):
    item = array[cycleStart]
     
    # Find where to put the item.
    position = cycleStart
    for i in range(cycleStart + 1, len(array)):
      if array[i] < item:
        position += 1
     
    # If the item is already there, this is not a cycle.
    if position == cycleStart:
      continue
     
    # Otherwise, put the item there or right after any duplicates.
    while item == array[position]:
      position += 1
    array[position], item = item, array[position]
    writes += 1
     
    # Rotate the rest of the cycle.
    while position != cycleStart:
       
      # Find where to put the item.
      position = cycleStart
      for i in range(cycleStart + 1, len(array)):
        if array[i] < item:
          position += 1
       
      # Put the item there or right after any duplicates.
      while item == array[position]:
        position += 1
      array[position], item = item, array[position]
      writes += 1
   
  return writes
   
   
   
arr = [1, 8, 3, 9, 10, 10, 2, 4 ]
n = len(arr) 
cycleSort(arr)
 
print("After sort : ")
for i in range(0, n) : 
    print(arr[i], end = ' ')
