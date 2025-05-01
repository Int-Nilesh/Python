f = open("result.csv", "r") #open the file in read mode, file should be present in the same directory
n = open("Errorlist.csv", "w") #open the file in write mode, if file not present it will create a new file
count = 0

for line in f:
    if "Error" in line: #check if Erro present in line
        n.write(line) # write the line to error.log
        count +=1 #increment the error count

print("No of Error found:  ", count)   
f.close()
n.close()