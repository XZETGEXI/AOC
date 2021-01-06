from collections import namedtuple
import itertools as it
import time

# CONS

STEPS = 6
SIZE = 15

# UTILITIES

def read():
    matrix = []
    with open("input.txt") as f:
        data = [datum.strip() for datum in f.readlines()]
    data.reverse()
    x, y = len(data[0]), len(data)
    for i in range(x):
        for j in range(y):
            if data[i][j] == ".":
                matrix.append(Point(i, j, 0, 0, False))
            else:
                matrix.append(Point(i, j, 0, 0, True))
    return matrix

def logger(verbose = True):
    def log(*arg):
        if verbose:
            print(*arg)
    return log

# CLASSES

class Point(namedtuple("Point", ["x", "y", "z", "w", "active"], defaults = (0,0,0,0,False))):
    def __add__(self, p):
        return self.x + p.x, self.y + p.y, self.z + p.z, self.w + p.w
    def border(self):
        return max(self.x, 0), max(self.y, 0), max(self.z, 0)
    def isactive(self):
        return self.active
    def activate(self):
        return self._replace(active = True)
    def desactivate(self):
        return self._replace(active = False)

# FUNCTIONS

def count_actives(matrix):
    score = 0
    for i in matrix:
        score += i.isactive()
    return score

def adjacent(point):
    adjacent = set()
    facteurs = it.product((-1,0,1), repeat = 4)
    for i in facteurs:
        if i == (0,0,0,0):
            continue
        else:
            neighbour = point + Point(*i)
            neighbour = Point(*neighbour)
            #neighbour = neighbour.border()
            adjacent.add(neighbour)
    return adjacent

def adjacent_score(point, matrix):
    adjacents = adjacent(point)
    score = 0
    for i in adjacents:
        if Point(i.x, i.y, i.z, i.w, False) in matrix:
            pass
        elif Point(i.x, i.y, i.z, i.w, True) in matrix:
            score += 1
    return score

def change(test, matrix):
    score = adjacent_score(test, matrix)
    if test.active:
        if score < 2 or score > 3:
            test = test.desactivate()
    else:
        if score == 3:
            test = test.activate()
    return test

def step(matrix):
    new_state = set()
    for i in matrix:
        temp = change(i, matrix)
        new_state.add(temp)
    return new_state

def merger(matrix, to_merge):
    result = set()
    for i in matrix:
        if Point(i.x, i.y, i.z, i.w, True) in to_merge:
            i = i.activate()
            result.add(i)
        else:
            result.add(i)
    return result

def new_matrix(n):
    new_matrix = set()
    for x, y, z, w in it.product(range(-n, n), repeat = 4):
        new_matrix.add(Point(x, y, z, w))
    return new_matrix

# MAIN

def main2(data):
    matrix = new_matrix(SIZE)
    new_state = merger(matrix, data)
    for i in range(STEPS):
        log(f"Step {i}")
        new_state = step(new_state)
    return count_actives(new_state)

if __name__ == "__main__":
    log = logger()
    start = time.time()
    data = read()
    print("Gold :", main2(data))
    end = time.time()
    print("Fini en ", (end - start), " secondes")