import re
import os
import time
import itertools as it
import numpy as np

# logger
def logger(verbose = False):
    def log(*arg):
        if verbose:
            print(*arg)
    return log

# time utils
def tic():
    return time.time()

def toc(start, msg=None):
    end = time.time()
    print("Done en {}s".format((end - start) // 1), msg)

# lecture

with open("input.txt", "r") as f:
    data = [i.rstrip().replace("B","1").replace("L","0").replace("F","0").replace("R","1") for i in f.readlines()]

def calcul_score(x):
    return x[0]*8+x[1]

def score_ticket(a):
    b = a % 8
    c = a // 8
    return c, b
    
def nombre_ticket(i):
    ticket = str(bin(i))[:-3].replace("1","B").replace("0","L")[2:]
    tock = str(bin(i))[-3:].replace("0","F").replace("1","R")
    return (ticket, tock)

prescores = [(int(i[:-3], 2),int(i[-3:], 2)) for i in data]
scores = list(map(calcul_score, prescores))

max_t = max(scores)
min_t = min(scores)

print("max is", max_t)
print("min is", min_t)

with open("input.txt", "r") as f:
    base = [i.rstrip("\n") for i in f.readlines()]

for i in range(min_t,max_t):
    step = nombre_ticket(i)
    if not step[0]+step[1] in base:
        ...
for i in range(min_t,max_t):
    if not i in scores:
        if i - 1 in scores:
            if i + 1 in scores:
                print("ticket", nombre_ticket(i))
                print("score", i)