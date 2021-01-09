#!/usr/bin/env python3
from pprint import pprint
from collections import defaultdict

def read():
    with open("d8.txt") as f:
        data = [datum.strip().split() for datum in f.readlines()]
    return data

d_register_value = defaultdict(int)

data = read()

def check_cond(var1, cond, var2):
    return eval(f"{d_register_value[var1]}{cond}{var2}")
    
gold = set()

for datum in data:
    var1, cond, var2 = datum[4:]
    if check_cond(var1, cond, var2):
        var3, cond, var4 = datum[:3]
        if cond == "inc":
            d_register_value[var3] += int(var4)
        if cond == "dec":
            d_register_value[var3] -= int(var4)
    
    for i in d_register_value.values():
        gold.add(i)
            
print("Silver", max(d_register_value.values()))
print("Gold", max(gold))