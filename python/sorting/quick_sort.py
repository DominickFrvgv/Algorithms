def quick_sort(arr):
    quick_sort2(arr, 0, len(arr)-1)

def quick_sort2(arr, start, end):
    if start < end: # check if start and end overlap 
        p = partition(arr, start, end)
        quick_sort2(arr, start, p-1) # sort the left side
        quick_sort2(arr, p+1, end) # sort the right side

def partition(arr, start, end):
    pivot = arr[end] # pivot at the end
    i = start # 
    for j in range(start, end): # iterate the list
        if arr[j] <= pivot: # compare the current element with the pivot
            arr[j], arr[i] = arr[i], arr[j] # swap the two
            i += 1 # move the iteration
    arr[i], arr[end] = arr[end], arr[i] # put the pivot at place
    return i # pivot


# test
alist = [12,6,78,4,7,47,84,15]
alist2 = [12,6,78,4,4,4,4,7,47,84,15]
quick_sort(alist)
quick_sort(alist2)
print(alist)
print(alist2)