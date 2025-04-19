def insertionSort( arr):
    for i in range( 1, len(arr)):
        key= arr[i]
        j=i
        while j>0:
            if ( arr[j-1]> key):
                arr[j]= arr[j-1]
                j-=1
            else:
                arr[j]= key
                j-=1
                break
        if (arr[0]> key):
            arr[0]= key
        return arr
arr = (input("enter the elements of array: ").split())
for i in range(len(arr)):
    arr[i]= int(arr[i])    
sortedArr= insertionSort(arr)
print(sortedArr)
