from collections import defaultdict
from utilities import *

log = logger()

log("Logger in")

start = tic()

data = read()

log("Data read")

step = toc(start)


d = defaultdict(int)

for i in data:
    i0, i1 = i[1].split(": ")
    i00 = [*map(int, i0.split(","))]
    i11 = [*map(int, i1.split("x"))]
    for j in range(i00[0], i00[0] + i11[0]):
        for k in range(i00[1], i00[1] + i11[1]):
            d[(j, k)] += 1
    
s = [1 for i in d.values() if i > 1]

log("Silver", sum(s))

step = toc(step)

for i in data:
    flag = True
    i0, i1 = i[1].split(": ")
    i00 = [*map(int, i0.split(","))]
    i11 = [*map(int, i1.split("x"))]
    for j in range(i00[0], i00[0] + i11[0]):
        for k in range(i00[1], i00[1] + i11[1]):
            if d[(j, k)] > 1:
                flag = False
                break
    if flag:
        log("Gold", i[0])
        break

end = toc(step)
