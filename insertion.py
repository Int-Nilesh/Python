def insertion_sort ( arr):
    for i in range( 1, len(arr)):
        key= arr[i]
        j = i
        while j>0:
            if (arr[j-1]>key):
                arr[j]= arr[j-1]
                j -=1
            else:
                arr[j]=key
                break
        if (arr[0]>key):
            arr[0]= key
    return arr
print("ENter the elements if array")
arr= list(int(input().split()))
sortedarr= insertion_sort(arr)
print(sortedarr)


