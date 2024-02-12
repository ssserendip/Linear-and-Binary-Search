def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
array = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G']
target = 'E'

index = linear(array, target)

if index != -1:
    print(target, "was found at index" , index)
else:
    print(target, "was not found")
