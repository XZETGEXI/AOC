from utilities import *
from collections import Counter

log = logger()

log("Logger in")

start = tic()

data = read()

doubles = 0
triples = 0

for i in data:
    c = Counter(i)
    if 2 in c.values():
        doubles += 1
    if 3 in c.values():
        triples += 1

log("Silver", doubles * triples)

# forgot the "same position" trick
# new_data = [set(datum) for datum in data]
# result = [i - (i ^ j) for i in new_data for j in new_data if len(i ^ j) == 1]

LENGTH = len(data[0])
for i in range(LENGTH):
    new_data = [datum[:i] + datum[i+1:] for datum in data]
    result = [i for i in new_data if new_data.count(i) > 1]
    if result:
        break

log("Gold", result[0])

end = toc(start)
