def selection_sort(numbers):
    """Sorting algotithm with Time Complexity: O(n^2)
       and Space Complexity: O(1).

    Args:
        numbers (List of Int): List to be sorted.

    Returns:
        List of Int: Sorted List.
    """
    length = len(numbers)

    for i in range(length):
        minimum = float("+inf")
        index = i
        # Searh for minimum value in unsorted part of the list
        for j in range(i, length):
            if numbers[j] < minimum: 
                minimum = numbers[j]
                index = j

        # Swap current number with found minimum
        numbers[i], numbers[index] = numbers[index], numbers[i]
    
    return numbers



if __name__ == "__main__":

    print(selection_sort([5,3,7,8,3,5]))
    print(selection_sort([5,3,7,8,3,23,1,765,3,5]))
    print(selection_sort([5,3,7,8,3,23,1,765,3,5]))
    print(selection_sort([]))