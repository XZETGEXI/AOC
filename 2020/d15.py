from collections import defaultdict

input = [18,11,9,0,5,1]

# Utilities

def logger(verbose = True):
    def log(*arg):
        if verbose:
            print(*arg)
    return log

# Main
        
STEPS1 = 2020

def main(data, STEPS):
    indexes = {n+1: i for n,i in enumerate(data)}
    init = 1
    while init < STEPS:
        log(indexes, "dict is")
        log(init, "init is")
        log("Trying...")
        if init in indexes.keys():
            log("Found", indexes[init])
            init += 1
        else:
            log("Catched")
            temp = indexes[init - 1]
            log(temp, "temp is")
            if temp in [*indexes.values()][:-1]:
                log("Found", temp)
                temp_lst = [*indexes.values()][:-1]
                temp_lst.reverse()
                log(temp_lst, "temp list is")
                temp_key = temp_lst.index(temp)
                temp_key = init - 2 - temp_key
                log("Hum", temp_key, type(temp_key))
                value = init - temp_key - 1
            else:
                log("Fouck")
                value = 0
            indexes[init] = value
            log("Value is", value)
            init += 1
    return indexes

# Main 2

STEPS2 = 30000000

def main2(data, STEPS):
    d_map = {}
    d = {}
    for n, i in enumerate(data):
        d[n] = i
    init = len(input)
    while init < 2*STEPS:
        number = d[init - 1]
        try:
            d[init] = init - d_map[number] - 1
            d_map[init] = init
        except:
            d[init] = 0
            d_map[0] = init
        init += 1
    return [c for c in d.items() if c[0] == STEPS]
    
    

if __name__ == "__main__":
    log = logger(False)
    #assert main([0,3,6], STEPS1) == 436
    #assert main([1,3,2], STEPS1) == 1
    #assert main([2,1,3], STEPS1) == 10
    #assert main([1,2,3], STEPS1) == 27
    #assert main([2,3,1], STEPS1) == 78
    #assert main([3,2,1], STEPS1) == 438
    #assert main([3,1,2], STEPS1) == 1836
    #print("Silver :", main(input, STEPS1))
    # d = main(input, STEPS1)
    #assert main([0,3,6], STEPS2) == 175594
    #assert main([1,3,2], STEPS2) == 2578
    #assert main([2,1,3], STEPS2) == 3544142
    #assert main([1,2,3], STEPS2) == 261214
    #assert main([2,3,1], STEPS2) == 6895259
    #assert main([3,2,1], STEPS2) == 18
    #assert main([3,1,2], STEPS2) == 362
    d = main2(input, STEPS2)
    print(d)
    #print("Gold :", main(input, STEPS2))
    print("OK")
    
