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
