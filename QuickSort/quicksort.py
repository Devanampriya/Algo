"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if(len(array)==1):
        return array
### PARTITIONING STARTS
    p = 0
    i = p+1
    j = p+1
    while(j < len(array)):
        if(array[j] <= array[p]):
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            i = i + 1
        j = j + 1
    tmp = array[i-1]
    array[i-1] = array[p]
    array[p] = tmp
### PARTITIONING ENDS
    quicksort(array[:i-1])
    quicksort(array[i+1:])
    return array
    
#test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test = [33,1,50,40,2,4]

print(quicksort(test))