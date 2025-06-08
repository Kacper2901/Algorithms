def second_max(numbers):
    """Finds second greatest number in the list.

    Args:
        numbers (list of int): list of integers
    """

    length = len(numbers)

    if length < 2:
        raise ValueError("List is too small")
    
    max_val = float("-inf")
    sec_max = float("-inf")


    for i in range(0,length):
        if numbers[i] >= max_val:
            sec_max = max_val
            max_val = numbers[i]
        elif numbers[i] > sec_max:
            sec_max = numbers[i]
    
    return sec_max

if __name__ == "__main__":
    
    numbers = [1,2,3,4,5,77,88,33,44]
    print(second_max(numbers))