def subarrays(numbers):
    """
    Given an array arr[], the task is to generate all the possible subarrays of the given array.

    Args:
        numbers (list of int): list of integers

    Returns:
        list of (lists of int): list of subarrays
    """
    results = []
    for i in range(len(numbers)):
        temp = []
        for j in range(i, len(numbers)):
            temp.append(numbers[j])
            results.append(list(temp)) # Create a copy of the list, because python adds a pointer not an object itself
            
    return results



if __name__ == "__main__":

    print(subarrays([1, 2, 3, 4]))