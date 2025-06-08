def find_leaders(numbers):
    """
    Given an array arr[] of size n, the task is to find all the Leaders in the array.
    An element is a Leader if it is greater than or equal to all the elements to its right side.

    Args:
        numbers (list of int): list of numbers
    """
    suffix_max = [0] * len(numbers)
    curr_max = float("-inf")


    # Store sufix maximum for each index in the new list.
    for i in reversed(range(len(numbers))):
        if numbers[i] > curr_max:
            curr_max = numbers[i]
        suffix_max[i] = curr_max
    

    # If sufix maximum is equal to number[i] then there is no bigger number on the right
    leaders = []
    for i in range(len(numbers)):
        if suffix_max[i] == numbers[i]:
            leaders.append(numbers[i])


    return leaders



if __name__ == "__main__":

    numbers = [19, 17, 4, 3, 5, 2]
    print(find_leaders(numbers))
