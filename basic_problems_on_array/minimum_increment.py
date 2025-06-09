def minimum_increment(numbers, k):
    """Finds the number of operations needed to make all elements of array equal.

    Args:
        numbers (List of int): List of integers 
        k (int): Increment value

    Returns:
        Int: how many increments has been done; -1 if it's not possible
    """
    length = len(numbers)
    max = float("-inf")
    for i in range(length):
        if numbers[i] > max: 
            max = numbers[i] # Search for max, to equal other numbers

    result = 0
    mod = max % k
    for i in range(length):
        if numbers[i] % k != mod: # Modulo has to be equal because we can only add k (no more no less)
            return -1
        result += (max - numbers[i]) // k # How much do we need to get max, end then how many incremets it will be
    
    return result



if __name__ == "__main__":

    print(minimum_increment([4, 7, 19, 16], 3))
    print(minimum_increment([4, 7, 19, 16], 3))
    print(minimum_increment([4, 7, 19, 16], 3))