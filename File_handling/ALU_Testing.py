#this script will read testcases and parse values and send it to ALU and save result in file
import random

def gen_testcases():
    with open("TestVectors.csv","w") as f:
        for i in range(100):
            a = random.randint(0,15)
            b = random.randint(0,15)
            op = random.randint(0,4) #added till 4 to induce error in ALU operation
            f.write(f"{a},{b},{op}\n")


def update_result():
    with open("TestVectors.csv", "r") as f, open("result.csv", "w") as n:
        n.write("A,B,C,Result\n")
        for line in f:
            a, b, op = map(int, line.strip().split(",")) # map will apply "int" function on every(all) value of "i" 
                                                         # and then those values will get unpacked and get assign to a,b,op
            result = alu(a,b,op)
            n.write(f"{a},{b},{op},{result}\n")

def check_error():
    count = 0
    with open("result.csv","r") as f, open("Errorlist.csv","w") as n:
        for line in f:
            if "Error" in line:
                n.write(line)
                count += 1
    print("Total erros: ", count)

def alu (a,b,op):
    match (op):
        case 0: return (a+b)
        case 1: return (a-b)
        case 2: return (a & b)
        case 3: return (a | b)
        case _: return "Error"
        

def main():
    gen_testcases()
    update_result()
    check_error()
    

if __name__ == "__main__":
    main()
        





