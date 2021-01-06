import time

WINDOW_SIZE = 25

with open("bigboy.txt", "r") as f:
    data = [int(i.strip()) for i in f.readlines()]

def p1():
    """ Solves the first part"""
    flag = False
    for i in range(len(data)):
        if not flag:
            to_check = int(data[i + WINDOW_SIZE])
            window = list(data[i : i+WINDOW_SIZE])
            _min = two_min(window)
            _max = two_max(window)
            if to_check < _min or to_check > _max:
                flag = True
                print("Found !")
    print(to_check)

def two_min(l: list) -> int:
    _l = list(l)
    min1 = min(_l)
    _l.remove(min1)
    min2 = min(_l)
    return min1 + min2

def two_max(l: list) -> int:
    _l = list(l)
    max1 = max(_l)
    _l.remove(max1)
    max2 = max(_l)
    return max1 + max2

start = time.time()
p1()
end = time.time()
print("Time", (end - start) * 1000)