from utilities import *
import itertools as it

start = tic()

log = logger()
log("Logger in")

time.sleep(1)

step = toc(start)
time.sleep(1)

data = read()

log("Data read")
step = toc(step)
time.sleep(1)

log("Silver", sum(data))

step = toc(step)
time.sleep(1)

s_r = set()
somme = 0
cycle = it.cycle(data)

while 1:
    n = next(cycle)
    somme += n
    if somme in s_r:
        break
    else:
        s_r.add(somme)

log("Gold", somme)
end = toc(step)
time.sleep(1)

log("Total time")
toc(start)
