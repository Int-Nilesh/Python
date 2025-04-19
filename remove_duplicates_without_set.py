def insertion(arr):
    for i in range( 1, len(arr)):
        key = arr[i]
        j = i
        while j>0:
            if ( arr[j -1]>key):
                arr[j]= arr[j-1]
                j-=1
            else:
                arr[j]= key
                break
        if (arr[0]>key):
            arr[0]= key
    return arr

arr= (input(" ENter elemets of array: ")).split()
for i in range(len(arr)):
    arr[i]= int(arr[i])
sorted = insertion(arr)
i= 0
j = i + 1
while j < len(sorted):
    if ( sorted[j]== sorted[i]):
        sorted.pop(j)
    else:
        i+=1
        j+=1
print( sorted)
