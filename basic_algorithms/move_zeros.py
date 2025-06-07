def move_zeros(numbers):
    """ Moves all zeros to the end of the list. O(n)
    
        Counts non-zero elements. When a zero is encountered,
        it swaps the current number with numbers[count],
        so the zero is pushed towrad the end.

    Args:
        numbers (list of int): list of integers
    """

    counter = 0

    for i in range(len(numbers)):
        if numbers[i] != 0: # if zero then nothing changes, because we want index where to put next non-zero
            numbers[i], numbers[counter] = numbers[counter], numbers[i]
            counter += 1

    return numbers




if __name__ == "__main__":
    
    print(move_zeros([0, 0, 0]))     
    print(move_zeros([1, 2, 3]))        
    print(move_zeros([]))               
    print(move_zeros([0, 1, 0, 2, 0]))   
