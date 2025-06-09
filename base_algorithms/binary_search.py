def binary_search(numbers, target, left, right):
    """Binary search on sorted list.

    Args:
        numbers (list of int): List of sorted elements.
        target (int): The value to search for.
        left (int): The first index of the search range.
        right (int): The last index of the search range.

    Returns:
        int: The index of target value if found; -1 if not found.
    """
    while left <= right:
        mid = left + (right - left) // 2 # Avoid overflow
        
        if numbers[mid] == target:
            return mid
        else:
            if target > numbers[mid]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


if __name__ == "__main__":
    print(binary_search([1,2,3,4,5,6,7,8,9], 2, 0,8))
    print(binary_search([1,2,3,4,5,6,7,8,9], 12, 0,8))
    print(binary_search([1,2,3,4,5,6,7,8,9], 7, 0,8))