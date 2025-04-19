num = int(input( "Enter the decimal integer: "))
rem=0
count=""
print (num, type(num))
while ( num!=0):
    rem=(num%2)
    #print(rem)
    num= int(num/2)
    count= str(rem)+count
print(int(count))