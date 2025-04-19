# given a arr find all the pairs of  elements whos sum = target

def insertionSort ( arr):
    for i in range( 1, len( arr)):
        key = arr[i]
        j = i
        while j>0:
            if (arr[j-1]>key):
                arr[j]= arr[j-1]
                j -=1
            else:
                arr[j]= key
                break
        if (arr[0]>key):
            arr[0]= key
    return arr

target = int( input(" enther the target: "))
a = input(" Enter the elements pf array space seperated: ").split()
for i in range(len(a)):
    a[i]= int(a[i])

a= insertionSort(a)
j= len(a)-1
for i in range(len(a)):
    if j>i:
        if(a[i]+ a[j]== target):
            print(a[i],a[j])
            i +=1
            j-=1
        elif (a[j]+a[i]> target):
            j-=1
        else:
            i +=1
    


    


