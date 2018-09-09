def quicksort(array,low=0,high=-1):
    if(high - low <= 0):
        return array
    pivotindex = partition(array,low,high)
    quicksort(array,0,pivotindex-1)
    quicksort(array,pivotindex+1,high)
    return array

def partition(array,low,high):
    pivot = array[high]
    pivotindex = high
    while(low < pivotindex):
        if(array[low] > pivot):
            tmp = array[low]
            array[low] = array[pivotindex-1]
            array[pivotindex-1] = array[pivotindex]
            array[pivotindex] = tmp
            pivotindex = pivotindex-1
        else:
            low = low + 1
    return pivotindex

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test,0,len(test)-1))

