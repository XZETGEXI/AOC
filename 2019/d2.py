import random
import itertools as it

def read():
    with open("input.txt") as f:
        data = f.read().strip()
        data = data.split(",")
        data = [int(i) for i in data]
    return data

GOAL = 19690720

def main(data):
    #data[1] = 12
    #data[2] = 2
    for n, i in enumerate(data):
        if i == "99":
            break
        if not n % 4:
            try:
                if i == 1:
                    data[data[n+3]] = opcode1(data[data[n+1]],data[data[n+2]])
                elif i == 2:
                    data[data[n+3]] = opcode2(data[data[n+1]],data[data[n+2]])
            except:
                continue
    return data
            
def opcode1(a,b):
    r = a+b
    return r

def opcode2(a,b):
    r = a*b
    return r

def main2(data):
    var = it.product(range(150), repeat = 2)
    mix = set(var)
    tries = 0
    while data[0] != GOAL:
        data = read()
        #t = mix.pop()
        #data[1] = t[0]
        #data[2] = t[1]
        data[1] = random.randint(0,150)
        data[2] = random.randint(0,150)
        data = main(data)
        tries += 1
    return data[1], data[2], tries

data = read()
print(main2(data), 150*150)