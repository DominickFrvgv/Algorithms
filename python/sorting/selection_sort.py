def selection_sort(arr):
    if len(arr) == 1:
        return f'{arr} list was already sorted'
    for i in range(0, len(arr) - 1): # from zero to second last item (the last item will be already sorted by the end)
        minIndex = i
        for j in range(i+1, len(arr)): # loop through the unsorted part of the list
            if arr[minIndex] > arr[j]: # compare the min item with the unsorted part
                minIndex = j # update the smallest

        arr[i], arr[minIndex] = arr[minIndex], arr[i] # swap
    return arr

# tests
list1=[123, 5, 4, 634, 6, 31]
list2=[]
list3=[1, 5, 4, 534, 63, 431]
list4=[3]
list5=[1,2,3,4,5,9,8]
print(selection_sort(list1))
print(selection_sort(list2))
print(selection_sort(list3))
print(selection_sort(list4))
print(selection_sort(list5))