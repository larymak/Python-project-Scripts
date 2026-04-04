from typing import List

def cycle_sort(nums: List[int]) -> int:

    writes = 0

    for cycle_start in range(len(nums) - 1):
        current = nums[cycle_start]

        # Find the target position for the current item.
        target_position = cycle_start
        for i in range(cycle_start + 1, len(nums)):
            if nums[i] < current:
                target_position += 1

        # Skip if the item is already in the correct position.
        if target_position == cycle_start:
            continue

        # Handle duplicates by finding the next available position.
        while current == nums[target_position]:
            target_position += 1

        nums[target_position], current = current, nums[target_position]
        writes += 1

        # Rotate the rest of the cycle.
        while target_position != cycle_start:
            target_position = cycle_start
            for i in range(cycle_start + 1, len(nums)):
                if nums[i] < current:
                    target_position += 1

            while current == nums[target_position]:
                target_position += 1

            nums[target_position], current = current, nums[target_position]
            writes += 1

    return writes


if __name__ == "__main__":
    arr = [1, 8, 3, 9, 10, 10, 2, 4]
    print("Before sort:", arr)

    writes = cycle_sort(arr)

    print("After sort:", arr)
    print(f"Number of writes: {writes}")
