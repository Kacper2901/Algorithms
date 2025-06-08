def linear_max(array):
    """Search for maximum value in the list O(n)

    Args:
        array (list): list of integers
    """

    length = len(array)
    max_val = array[0]

    for i in range(1,length):
        max_val = max(max_val, array[i])
    
    return max_val



if __name__ == "__main__":
    
    arr = [1,2,3,4,5,6,8,199,2,3,4,5]
    print(linear_max(arr))
