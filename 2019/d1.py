from math import floor
from collections import defaultdict

with open("input.txt") as f:
    data = map(int, [datum.strip() for datum in f.readlines()])

f_r = {}

for n, i in enumerate(data):
    value = floor(i / 3) - 2
    f_r[n] = value

print(sum(f_r.values()))

d = defaultdict(int)

with open("input.txt") as f:
    data = map(int, [datum.strip() for datum in f.readlines()])

for n, i in enumerate(data):
    value = i
    while value > 0:
        value = floor(value / 3) - 2
        d[n] += value
    d[n] -= value
 
print(sum(d.values()))
