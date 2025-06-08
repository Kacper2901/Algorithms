# best for sorted arrays O(logn)


def binary_search_rec(arr, target, left, right):
    """Binary search on sorted list

    Args:
        arr (list of int): list of sorted elements
        target (int):The value to search for
        left (int): The first index of the search range
        right (int): The last index of the search range

    Returns:
        int: The index of target value if found; -1 if not found
    """

    if right >= left:
        mid = left + (right - left) // 2 # avoiding integer overflow

        if arr[mid] == target:
            return mid
        else:
            if target > arr[mid]:
                return binary_search_rec(arr, target, mid + 1, right)
            else:
                return binary_search_rec(arr, target, left, mid - 1)
    else:
        return -1
    

# same time complexity but better space complexity [O(1) instead of O(logn)]
def binary_search_it(array, target, left, right):    
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        else:
            if target > array[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
        

if __name__ == "__main__":
    array = [1,2,4,5,6,7,8,12,45,166]

    print(binary_search_rec(array, 2, 0, len(array)-1))
    print(binary_search_rec(array, 12, 0, len(array)-1))
    print(binary_search_rec(array, 1111, 0, len(array)-1))

    print(binary_search_it(array, 2, 0, len(array)-1))
    print(binary_search_it(array, 12, 0, len(array)-1))
    print(binary_search_it(array, 1111, 0, len(array)-1))
