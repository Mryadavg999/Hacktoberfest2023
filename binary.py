def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index (integer division)

        if arr[mid] == target:
            return mid  # Found the target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

# Example usage:
sorted_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 10
result = binary_search(sorted_list, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")
