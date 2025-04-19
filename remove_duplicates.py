
# Remove dupicates from arr
def insertionSort( arr):
    for i in range(1, len(arr)):
        key= arr[i]
        j = i
        while j>0:
            if [arr[j-1]>key]:
                arr[j]= arr[j-1]
                j -= 1
            else:
                arr[j]= key
                break
        if (arr[0]>key):
            arr[0]= key 
    print (arr)
    return arr

a = input( " ENter eements of arr: ").split()
for i in range (len(a)):
    a[i]= int(a[i])
unique = set()
for i in a:
    unique.add(i)
a= list(unique)
print(unique)
print(a)





