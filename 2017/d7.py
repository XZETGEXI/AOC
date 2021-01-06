from collections import defaultdict
from pprint import pprint
import re

with open("d7.txt") as f:
    data = [datum.strip() for datum in f.readlines()]
    data = [datum.split(" -> ") for datum in data]
    

d_what_inwhat = {}
d_name_weight = {}

for datum in data:
    if len(datum) == 2:
        for subdatum in datum[1].strip().split(","):
            d_what_inwhat[subdatum.strip()] = datum[0].strip().split()[0]
             
    
    name, weight = datum[0].split()
    weight = re.search(r"\d+", weight)[0]
    weight = int(weight)
    d_name_weight[name] = weight

def rec(data):
    result = []
    for datum in data:
        check = datum[0].split()[0]
        if not check in d_what_inwhat:
            result.append(check)
    return result

print("silver", rec(data))

d_inwhat_what = defaultdict(list)

for k, v in d_what_inwhat.items():
    d_inwhat_what[v].append(k)




        
d_name_realweight = {}

for name in d_name_weight:
    s = [name]
    score = 0

    while s:
        tic = s.pop()
        score += d_name_weight[tic]
        for i in d_inwhat_what[tic]:
            s.append(i)
    d_name_realweight[name] = score
    
for k, v in d_inwhat_what.items():
    check = {}
    
    for name in v:
        check[d_name_realweight[name]] = name
    if len(check) > 1:
        print(check, 'name', k, "v", v)
        
print(d_inwhat_what["eionkb"])

print(d_name_weight["eionkb"])

print(d_name_realweight["hxmcaoy"])

print(d_name_realweight["sybpg"])

print(d_name_realweight["jfhqrla"])