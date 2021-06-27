import random

def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr)- i): # the last item in the list will be already sorted
            if arr[j] > arr[j+1]: # compare item with item in the right
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap

    return arr

# test
for _ in range(4):
    my_list = random.sample(range(1, 9), 6)
    print(f'random list: {my_list}')
    print(f'sorted list:{bubble_sort(my_list)}')
    print('-----')