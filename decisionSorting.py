def sorting ( z, decision):
    #print(z)
    #print( decision)
    if ( decision == "asc"):
        z.sort()
        return z
    elif ( decision== "dec"):
        print("in dec")
        z.sort( reverse= True)
        return z
    else:
        return z
x= input(" ENter the elements of list as speca eseprated: ").split()
x= [int (y) for y in x]
decision = input( "Enter asc for sort in assending order, dec for decending order, none for no sortig: ")
sorted_list= sorting( x, decision)
print( sorted_list)
