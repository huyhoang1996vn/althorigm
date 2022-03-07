lst = [4,2,1,3]

for index in range(len(lst)-1):
    for index_next in range(index+1, len(lst)):
        print(lst[index], " vs ", lst[index_next])
        if lst[index] > lst[index_next]:
            lst[index], lst[index_next] = lst[index_next], lst[index]
        print("===total ", lst)


print("=== lst ", lst)



def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            print(arr[j], " vs ", arr[j+1])
            # traverse the array from 0 to n-i-1
            
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print("===bubbleSort total ", arr)
 
# Driver code to test above
arr = [4,2,1,3]
 
bubbleSort(arr)