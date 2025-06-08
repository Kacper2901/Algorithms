#best for unsorted arrays O(n)

def linear_search(arr,x):
    length = len(arr)
    for i in range(0,length):
        if x == arr[i]:
            return i
    return -1

array = [1,2,3,4,5,9,8,7]
print(linear_search(array,8))