def distinct(numbers):
    """
    Remove duplicates from Sorted Array
    Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements 
    appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

    Args:
        numbers (list of int): list of integers
    """
    prev = None
    result = []

    # If previous value doesnt equal to current value, then it hasn't appeared yet.
    for i in range(len(numbers)):
        if numbers[i] != prev:
            result.append(numbers[i])
        prev = numbers[i]

    return result



if __name__ == "__main__":

    print(distinct([1,1,2,2,4,5,5,5,6]))
        