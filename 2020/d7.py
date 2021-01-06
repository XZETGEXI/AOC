import re
from treelib import Node, Tree

def read():
    with open("input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

data = read()

# fun
#parse
def parse(s: str):
    reg = re.findall(r"\D+bag", s)
    return set(i.rstrip("bag").rstrip().lstrip() for i in reg)

def partita(s: str):
    [index, part] = [s.partition("contain").index("contain"), s.partition("contain")]
    (left, right) = ([parse(i) for i in part[:index]][0], [parse(i) for i in part[index+1:]][0])
    return left, right

##tree
def check(g):
    tree = Tree()
    tree.create_node("Root", "root")
    flag = True
    while flag:
        try:
            temp = next(g)
            tree = check_tree(temp, tree)
        except StopIteration:
            flag = False
    #tree.show()
    return(tree)

def check_tree(temp, tree):
    dad = temp[0].pop()
    ID = "{}".format(dad)
    all_tree = [*tree.expand_tree()]
    if ID in all_tree:
        print("???")
    else:
        tree.create_node(dad, ID, parent="root")
    for i in list(temp[1]):
        ID_F = "{}/{}".format(dad, i)
        tree.create_node(i, ID_F, parent = ID)
    return tree

##score
def score(tree):
    score = 0
    all_tree = [*tree.expand_tree()]
    return 0

##main
generator = (partita(s) for s in data)

tree = check(generator)

def score2(l):
    names = []
    if l:
        for s in l:
            for i in tree.all_nodes():
                if s in i.identifier:
                    names.append(str(i.identifier))
    if names:
        return names
    else:
        return -1

def score3(fils = ["/shiny gold"]):
    score = 0
    temp = score2(fils)
    score += len(temp)
    for i in temp:
        i = "/" + i.partition("/")[0]
        fils.append(i)
    return fils
        
test = score2(["/shiny gold"])
print(test)
print("//////////////////////////")

def score4():
    ref = score3()
    flag = True
    st = set()
    while flag:
        lon = len(st)
        for i in score3(fils = ref):
            st.add(i)
        ref = list(st)
        if len(st) == lon:
            flag = False
    return st
    
print(len(score4()))
#print(score2(score2(["/shiny gold"])))
