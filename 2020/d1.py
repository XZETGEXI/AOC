TARGET = 2020

def check(LST, TARGET):
    for i in LST:
        if TARGET - i in LST:
            return (i, TARGET - i)
        else:
            return 0

with open("input.txt", "r") as f:
    LST = list(map(int, f.readlines()))
    
for i in LST:
    for j in LST:
        for k in LST:
            if (i+j+k) == 2020:
                print(i*j*k)
