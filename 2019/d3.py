from pprint import pprint

BOATS = [1, 2]

def read():
    with open("input.txt") as f:
        data = [datum.strip() for datum in f.readlines()]
        wire1, wire2 = data
        d = {}
        for i in BOATS:
            d[i] = [wire1, wire2][i - 1].split(",")
            d[i] = [(datum[0], int(datum[1:])) for datum in d[i]]
        return d

def path(instructions):
    """ returns every tile visited """
    set_path = {}
    init = 0
    start = [0,0]
    for i in instructions:
        if i[0] == "U":
            for j in range(i[1]):
                start[1] += 1
                init += 1
                set_path[tuple(start)] = init
        elif i[0] == "D":
            for j in range(i[1]):
                start[1] -= 1
                init += 1
                set_path[tuple(start)] = init
        elif i[0] == "L":
            for j in range(i[1]):
                start[0] -= 1
                init += 1
                set_path[tuple(start)] = init
        elif i[0] == "R":
            for j in range(i[1]):
                start[0] += 1
                init += 1
                set_path[tuple(start)] = init
    return set_path

def find_low_inter(dict1, dict2):
    """ find the lowest intersection (Manhattan distance) """
    set1 = {*dict1.keys()}
    set2 = {*dict2.keys()}
    inter = set1.intersection(set2)
    latencies = {}
    for i in inter:
        latencies[dict1[i] + dict2[i]] = i
    return min(latencies)
    

def main():
    data = read()
    sets = []
    for i in data:
        instructions = data[i]
        sets.append(path(instructions))
    print(find_low_inter(*sets))
    
main()