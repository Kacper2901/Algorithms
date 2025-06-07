def even_greater_than_odd(numbers):
    """     Rule:
            arr[i] >= arr[i - 1], if i is even, ∀ 1 <= i < n
            arr[i] <= arr[i - 1], if i is odd, ∀ 1 <= i < n

    Args:
        numbers (list of int): list of integers
    """

    for i in range(len(numbers) - 1):
        if i % 2 == 0 and numbers[i] < numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        elif i % 2 == 1 and numbers[i] > numbers[i+1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    return numbers



if __name__ == "__main__":

    print(even_greater_than_odd([1,2,3,4,5,6,7,8]))
    print(even_greater_than_odd([1]))
    print(even_greater_than_odd([8,7,6,5,4,3,2,1]))
    print(even_greater_than_odd([9,99,7,32,4,5,7]))