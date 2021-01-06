import os
from pprint import pprint
from collections import defaultdict
import time
from functools import lru_cache
import timeit


w, h = os.get_terminal_size()

def read():
    with open("input.txt") as f:
        data = f.readlines()
        data = [datum.strip() for datum in data]
        data = [datum.split(")") for datum in data]
        data = {datum[1]:datum[0] for datum in data}
    return data

def logger(verbose = True):
    def log(*arg):
        if verbose:
            print("-"*w, *arg)
    return log

@lru_cache()
def regression(orb, stop = "COM"):
    if data[orb] == stop:
        return 1
    else:
        return 1 + regression(data[orb], stop)
    
  
log = logger(True)
data = read()

def main():
    result = 0
    for i in data:
        result += regression(i)
    print("silver",result)

def path(orb):
    path = {}
    index = 0
    while orb != "COM":
        path[data[orb]] = index
        orb = data[orb]
        index += 1
    return path

def first_inter(orb1, orb2):
    result = {}
    d1 = path(orb1)
    d2 = path(orb2)
    for i in d1:
        if i in d2:
            result[d1[i] + d2[i]] = i
    return result[min(result)]

def main2():
    node = first_inter("SAN", "YOU")
    v1 = regression("SAN", stop = node)
    v2 = regression("YOU", stop = node)
    return abs(v2 + v1) - 2

print(main2())