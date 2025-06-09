def rotate(numbers, step):
    """Rearranging the elements in an array by given amount of steps. 

        Time complexity: o(n)
        Space complexity: O(n)

    Args:
        numbers (list of int): Input list to be rearranged.
        step (int): Number of positions to shift (can be negative).

    Returns:
        list of int: Rotated list
    """
    length = len(numbers)
    results = [None]*length
    for i in range(length):
        new_index = (i + step) % length # Use modulo to wrap around if the index exceeds the list length
        results[new_index] = numbers[i]

    return results


def reverse_slice(numbers, left, right):
    """Reverse part of the list

    Args:
        numbers (list of int): List to reverse slice.
        left (int): Left index of part to reverse.
        right (int): Right index of part to reverse.

    Returns:
        list of int: List with reversed slice.
    """
    counter = 0
    mid = left + (right - left) // 2 
    for i in range(left, mid + 1):
        numbers[i], numbers[right - counter] = numbers[right - counter], numbers[i] # Swap of i and (right - i) elements
        counter += 1
    

def rotate_2(numbers, step):
    """The same effect, but Space Complexity is O(1), because we return the list from input.

    Args:
        numbers (list of int): Input list to be rearranged.
        step (int): Number of positions to shift (can be negative).

    Returns:
        list of int: Rotated list.
    """
    step = step % len(numbers)

    reverse_slice(numbers, 0, len(numbers) - 1) # Reverse whole list
    reverse_slice(numbers, 0, step - 1) # reverse first part
    reverse_slice(numbers, step, len(numbers) - 1) # reverse the rest

    return numbers




if __name__ == "__main__":
    
    array = [1,2,3,4,5,6,7,8,9]

    print(rotate(array, 1))
    print(rotate(array, 20))
    print(rotate(array, -1))


    print()
    print(rotate_2(list(array), 1))
    print(rotate_2(list(array), 2))
    print(rotate_2(array, -1))
    