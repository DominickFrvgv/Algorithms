# with while loop
def insertion_sort_while(arr):
    for i in range(1, len(arr)):
        j = i-1
        while arr[j] > arr[j+1] and j >= 0: # check if element on the left is bigger 
            arr[j], arr[j+1] = arr[j+1], arr[j] # swap elements
            j -= 1 # decrement j

my_list = [5,6,367,8,4,2,69,8]
my_list2 = [5,6,367,8,5,4,2,69,8]
insertion_sort_while(my_list2)
print(my_list)
print(my_list2)

