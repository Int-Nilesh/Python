import random

with open ("vectors.csv", "w") as f:
    for i in range (100):
        f.write(str(random.randint(0, 15)) +","+str(random.randint(0, 15)) +","+str(random.randint(0, 3))+"\n")
