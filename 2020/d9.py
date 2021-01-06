import itertools as it

WINDOW_SIZE = 25

with open("input.txt", "r") as f:
    data = [int(i.strip()) for i in f.readlines()]

def p1():
    """ Solves the first part"""
    flag = False
    for i in range(len(data)):
        if not flag:
            to_check = int(data[i + WINDOW_SIZE])
            window = list(data[i : i+WINDOW_SIZE])
            # quick check
            _min = calcul_min(window)
            _max = calcul_max(window)
            if to_check < _min or to_check > _max:
                flag = True
                print("BUSTED (EASY!)")
            # tedious check if quick check fails
            else:
                answer = tedious_check(window, to_check, 2)
                if not answer:
                    flag = True
                    print("BUSTED")
    print("Found !") # since we know there's a solution
    print(to_check)
 
def calcul_min(l: list) -> int:
    """ returns the sum of the 2 lowest elements of l """
    _l = list(l)
    min1 = min(_l)
    _l.remove(min1)
    min2 = min(_l)
    return min1 + min2

def calcul_max(l: list) -> int:
    """ returns the sum of the 2 highest elements of l """
    _l = list(l)
    max1 = max(_l)
    _l.remove(max1)
    max2 = max(_l)
    return max1 + max2

def tedious_check(l, n, X):
    """ check if sum of X elements of l gives n """
    combinations = it.combinations(l, X)
    combinations = map(lambda x: sum(x), combinations)
    flag = False
    answer = False
    while not flag:
        try:
            i = next(combinations)
            if i == n:
                answer = True
                flag = True
        except:
            flag = True
    return answer

def p2():
    """ solves part 2 """
    to_find = 85848519
    for i in range(2, len(data)):
        WINDOW_SIZE = i
        for j in range(0, len(data) - WINDOW_SIZE):
            l = list(data[j: j + WINDOW_SIZE])
            answer = tedious_check(l, to_find, len(l))
            if answer:
                return l
        
        
euh = p2()
print(min(euh) + max(euh))