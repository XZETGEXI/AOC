import time
from anytree import Node, RenderTree
from anytree.importer import DictImporter
import itertools as it
import numpy as np
from functools import lru_cache
from collections import defaultdict

LOW_ADAPT = 3
JOLT_START = 0
HIGH_ADAPT = 3

with open("input.txt", "r") as f:
    data = [int(datum) for datum in f.readlines()]

data.append(JOLT_START)

data = sorted(data)
    
def get_max_jolt(data):
    return max(data)

def get_next_adapt(current, data):
    if current + 1 in data:
        return 1
    if current + 2 in data:
        return 2
    if current + 3 in data:
        return 3
    else:
        return 0
    
jolt_diff = {1: 0, 2: 0, 3: 0}

def main1(data):
    current = JOLT_START
    goal = get_max_jolt(data)
    while data and current != goal:
        next_adapt = get_next_adapt(current, data)
        jolt_diff[next_adapt] += 1
        data.remove(current)
        current += next_adapt
    jolt_diff[HIGH_ADAPT] += 1
    print(jolt_diff)

STEP = 3

def create_tree(data):
    tree = {}
    for i in data:
        tree[i] = []
        for j in range(1,4):
            if i + j in data:
                tree[i].append(i+j)
    return tree

tree = create_tree(data)

def main2(data):
    goal = get_max_jolt(data)
    score = 0
    lst_depart = hm_roads(goal)
    score += len(lst_depart)
    while any(lst_depart):
        current = lst_depart.pop()
        print(lst_depart)
        call = hm_roads(current)
        if call:
            score += max(len(call) - 1, 0)
            for i in call:
                lst_depart.append(i)
    print("score :", score)
 
@lru_cache(maxsize = 100000)
def hm_roads(indice):
    branches = []
    for i in tree:
        if indice in tree[i]:
            branches.append(i)
    return branches
    
def laplace(tree):
    #matrix creation
    matrice = {}
    maximum = get_max_jolt(data)
    for i in tree:
        for j in tree:
            name = f"L{i}C{j}"
            if i == j:
                matrice[name] = len(tree[i])
            elif is_related(i,j,tree):
                matrice[name] = -1
            else:
                matrice[name] = 0
    size = len(tree)
    a = np.array([matrice[i] for i in matrice])
    a = np.reshape(a, (size, size))
    print(a)
    #det
    det = np.linalg.det(a)
    print(det)
    print(len(matrice))

def is_related(i, j, tree):
    if j in tree[i] or i in tree[j]:
        return True
    else:
        return False

tree = create_tree(data)

def parcours(jolt):
    #cache
    memo_dict = {}
    if jolt in memo_dict:
        return memo_dict[jolt]
    #tic
    if jolt == maximum:
        value = 1
        return value
    if jolt == maximum - 1:
        value = 1
        return value
    if jolt == maximum - 2:
        value = 3
        return value
    else:
        value = parcours(jolt + 1) + parcours(jolt + 2) + parcours(jolt + 3)
    #tac
    memo_dict[jolt] = value
    return value
    
def tamere():
    score = 0
    memo_dict = {}
    while s:
        current_score = 0
        current = s.pop()
        if current in memo_dict:
            score_current += memo_dict[current]
        else:
            for i in tree:
                if indice in tree[i]:
                    s.add(i)
            score_current = len(branches)
            memo_dict[current] = score_current
        score += score_current
        print("score", score)
    return score

def p2(data):
    d = defaultdict(int)
    maximum = get_max_jolt(data)
    d[0] = 1
    for x in data:
        d[x] += d[x-1] + d[x-2] + d[x-3]
    print([(i, d[i]) for i in d])
    
#main2(data)
p2(data)
    
###
# Apparement main2 aurait pu marcher
# si je casse l'input
# des que je trouve deux nombres qui sautent de trois
# xxxx 4 7 xxxxx -> xxxx 4 // 7 xxxxx
#
#
#
# pour laplace
# L[i][j] = len(tree[i])*(i==j) - (j in tree[i])
#
# and for a tree a defaultdict