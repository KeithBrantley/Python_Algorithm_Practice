# Selection Sort Algorithm

def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)
# declare a default for the min value
    for i in indexing_length:
        min_value = i
# if value at j index is < current min value, replace the min value
        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j
# if the min value is lower then default switch the value
        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
# return the list
    return list_a

print(selection_sort([9,7,8,4,6,5,1,3,2]))