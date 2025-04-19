def insertion(arr):
    for i in range ( 1, len(arr)):
        key = arr[i]
        j = i
        while j>0 :
            if (arr[j-1]> key):
                arr[j]= arr[j-1]
                j-=1
            else:
                arr[j]=key
                break
        if arr[0]>key:
            arr[0]= key
    return arr
arr= (input("Enter Elements of Array: ")).split()
for i in range(len(arr)):
    arr[i]= int(arr[i])
target_sum = int(input("Enter target sum"))
arr = insertion(arr)
i = 0
j = len(arr)-1
while (j>i):
    sum = arr[i]+arr[j]
    if ( sum > target_sum):
        j-=1
    elif ( sum < target_sum):
        i=i+1
    elif ( sum == target_sum):
        print([arr[i],arr[j]])
        i+=1
        j-=1
    else:
        print("no match found")



