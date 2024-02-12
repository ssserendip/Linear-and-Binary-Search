def binary(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

array = [1,2,3,4,5,6,7]
target = 5
index = binary(array, target)

if index != -1:
    print(target, "was found at index" , index)
else:
    print(target, "was not found")