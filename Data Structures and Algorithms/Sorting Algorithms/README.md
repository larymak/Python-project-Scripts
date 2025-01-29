# Cycle Sort Algorithm

## Overview
Cycle Sort is a comparison-based sorting algorithm that is efficient when minimizing memory writes is important. It is an in-place sorting algorithm that rearranges the elements by identifying cycles in the permutation of elements.

## Algorithm Explanation
The algorithm works by:
1. Identifying the correct position of each element in the array.
2. Placing the element in its correct position and replacing the element already there in the cycle.
3. Repeating the process for the remaining unsorted elements.

## Complexity
- **Time Complexity**:
  - Best, Worst, and Average Case: O(n²) (due to nested cycles).
- **Space Complexity**: O(1) (in-place sorting).

## Usage Example
```python
from Cycle_Sort import cycle_sort

arr = [4, 5, 3, 2, 1]
print("Original array:", arr)
writes = cycle_sort(arr)
print("Sorted array:", arr)
print("Number of writes performed:", writes)
```
# Pigeonhole Sort Algorithm

## Overview
Pigeonhole Sort is a sorting algorithm that works well for sorting lists where the range of values (i.e., the difference between the maximum and minimum values) is not significantly larger than the number of elements in the list. It is a non-comparison-based sorting algorithm.

The algorithm works by placing each element into its corresponding "pigeonhole" (a slot or bucket) and then iterating through the pigeonholes in order to reconstruct the sorted list.

## Complexity
- **Time Complexity**:
  - The time complexity of Pigeonhole Sort is O(n + range), where n is the number of elements in the list and range is the difference between the maximum and minimum values.

  - This makes it efficient for lists with a small range of values.
- **Space Complexity**: The space complexity is O(range), as it requires additional space for the holes list.
- **Limitations**: Pigeonhole Sort is not suitable for lists with a large range of values, as it would require a lot of memory for the holes list.

## Usage Example
```python
from PigeonHole_Sort import pigeonhole_sort

arr = [4, 5, 3, 2, 1]
print("Original array:", arr)
writes = pigeonhole_sort(arr)
print("Sorted array:", arr)
