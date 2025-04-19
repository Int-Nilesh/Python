# check palindronme

a = "A man, a plan, a canal: Panama"

j = len(a)-1
flag = False

for i in range(len(a)):
    if j>i:
        if ( not a[i].isalnum()):
            i+=1
        if ( not a[j].isalnum()):
            j-=1
        
        if(a[i].lower() == a[j].lower()):
            flag= True
        else:
            flag= False
            break
        i+=1
        j_=1
    else:
        break
if(flag):
    print("palindrom")
else:
    print(" not palindrom")


