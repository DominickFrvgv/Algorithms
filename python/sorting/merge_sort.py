def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    if (end - start > 1): # if there's more than one item in the list
        middle = (start + end) // 2 # break the list in half
        merge_sort(arr, start, middle) # merge from the start to the middle 
        merge_sort(arr, middle, end) # merge from the middle + 1 to the end
        merge(arr, start, middle, end) # merge the two lists

def merge(arr, start, middle, end):
    left = arr[start:middle] # copy the left list
    right = arr[middle:end] # copy the right list

    left.append(999999999) # reach the end of the list
    right.append(999999999)

    i = j = 0 
    for k in range(start, end): # run through the len of the original list
        if i >= len(left): 
            arr[k] = right[j] # copy the item to the original list
            j += 1 # increment the right index
        if j >= len(right):
            arr[k] = left[i] # copy the item to the original list
            i += 1 # increment the left index
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


import random 

for _ in range(4):
    my_list = random.sample(range(1, 9), 6)
    print(f'random list: {my_list}')
    merge_sort(my_list)
    print(f'sorted list:{my_list}')
    print('-----')