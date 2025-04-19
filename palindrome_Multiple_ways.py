def palindrome1(s):
    n = s[::-1]
    if ( s== n):
        return True
    else:
        return False
def palindrome2(s):
    j = len(s)-1
    for i in range( int(len(s)/2)):
        if ( s[i]== s[j]):
            i+=1
            j-=1
        else:
            return False
        return True
s = input("enter a string: ")
a= ""
for i in s:
    if ((i>="a" and i <="z") or ( i >= "A" and i<= "Z")):
        a = a+ i
    else:
        continue

result = palindrome1(a.lower())
print( result)
result= palindrome2(a.lower())
print( result)