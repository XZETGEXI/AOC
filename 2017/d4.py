from pprint import pprint
import itertools as it
from collections import Counter


with open("d4.txt") as f:
    data = [datum.strip() for datum in f.readlines()]

data = [datum.split() for datum in data]

score = 0

for datum in data:
    if len(datum) == len(set(datum)):
        score += 1

print("silver", score)

d = Counter()

score = 0

for datum in data:
    l = [Counter(s) for s in datum]
    m = [*filter(lambda x: l.count(x) > 1, l)]
    if not m:
        score += 1

print("gold", score)
