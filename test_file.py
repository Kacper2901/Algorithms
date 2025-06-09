def minimum_incretment(numbers, k):
    length = len(numbers)
    max_val = float("-inf")

    for i in range(length):
        if numbers[i] > max_val:
            max_val = numbers[i]
        
    incremets_count = 0

    for i in range(length):
        if max_val % k != numbers[i] % k:
            return -1
        incremets_count += (max_val - numbers[i]) // k
    
    return incremets_count


def reverse_slice(numbers, left, right):
    mid = left + (right - left) // 2
    counter = 0

    for i in range(left, mid + 1):
        numbers[i], numbers[right - counter] = numbers[right - counter], numbers[i]
        counter += 1

def rotations(numbers, step):
    length = len(numbers)
    reverse_slice(numbers, 0, length -1)
    reverse_slice(numbers, 0, step - 1)
    reverse_slice(numbers, step, length - 1)

    return numbers

def selection_sort(numbers):
    length = len(numbers)

    for i in range(length):
        min_val = float("+inf")
        index = i

        for j in range(i,length):
            if numbers[j] < min_val:
                min_val = numbers[j]
                index = j

        numbers[i], numbers[index] = numbers[index], numbers[i]
    
    return numbers

if __name__ == "__main__":
    
    print(minimum_incretment([4,7,10,16],3))
    print(minimum_incretment([4,7,10,20,16], 3))

    print()

    print(rotations([1,2,3,4,5,6,7,8,9], 3))

    print()

    print(selection_sort([2,56,34,87,12,45,896,3,234,2]))