def radix_sort(arr):
    if len(arr) == 0:
        return arr

    max_number = max(arr)
    position = 1 # get postition of the digit

    while max_number >= position : # check if the there are more digits to go through
        buckets = [[] for i in range(10)] # list of 10 buckets
        for element in arr: 

            index = (element//position) % 10 # getting the last digit of each number
            buckets[index].append(element) # apend element to the correct bucket

        arr = [] # empty the array

        for bucket in buckets:
            arr+=bucket # add the numbers sorted in the buckets into the array

        position *= 10 # increment to get the next digit

    return arr


# test
lista = [135, 54, 66, 156, 560, 345]
lista2 = [2]
lista3 = [5,4,11,6,79,1547,9,25,35,25]
lista4 = []
print(radix_sort(lista))
print(radix_sort(lista2))
print(radix_sort(lista3))
print(radix_sort(lista4))
