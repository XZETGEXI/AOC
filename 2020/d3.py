import time
import numpy

## Constantes

## Utilities

def tic(): return time.time()

def toc(tic, msg = None):
    toc = time.time()
    format_time(toc - tic)
    if msg:
        print(str(msg))

def logger(verbose=False):
    def log(*arg):
        if verbose:
            print(*arg)
    return log

def format_time(seconds):
    hours = seconds // (60*60)
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    millis = seconds % 1
    d = {"hours": "","minutes": "","seconds": "","millis": ""}
    if hours > 0:
        d["hours"] = str(int(hours)) + " H \n"
    if minutes > 0:
        d["minutes"] = str(int(minutes)) + " M \n"
    if seconds > 0:
        d["seconds"] = str(int(seconds - millis)) + " S \n"
    if millis > 0:
        d["millis"] = str(int(100*millis)) + " MS"
    print("\nTIME :\n%(hours)s%(minutes)s%(seconds)s%(millis)s" % d)

## Parser

def parse():
    with open("input.txt", "r") as f:
        LST = [i.splitlines()[0] for i in f.readlines()]
        return LST

## fonctions

def dim(LST):
    return len(LST[0]), len(LST)

## main

def main(SLOPE_X, SLOPE_Y):
    pos_x = 0
    pos_y = 0
    trees = 0
    while pos_y < h-1:
        pos_x += SLOPE_X
        pos_x = pos_x % w
        pos_y += SLOPE_Y
        try:
            if data[pos_y][pos_x] == '#':
                trees += 1
        except IndexError:
            pass
        #log("Trees encountered : {0} and pos is x: {1} and y: {2}".format(trees, pos_x, pos_y))
    return trees
    
def main2():
    SLOPES = []
    for i in range(1, w+1):
        SLOPES.append((i,1))
    PROD = []
    REF = []
    for (i,j) in SLOPES:
        SLOPE_X, SLOPE_Y = i, j
        trees = main(SLOPE_X, SLOPE_Y)
        log("Testing Slope {} and {}. Trees: {}".format(i, j, trees))
        PROD.append(trees)
        REF.append([i,j])
    return REF[PROD.index(max(PROD))]

log = logger(True)
log("Initiated")
start = tic()
data = parse()
w, h = dim(data)
value = main2()
print("Result", value)
end = toc(start, "fin main2")