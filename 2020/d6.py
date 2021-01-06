import string
import time

# logger
def logger(verbose = False):
    def log(*arg):
        if verbose:
            print(*arg)
    return log

# time utils
def tic():
    return time.time()

def toc(start, msg=None):
    end = time.time()
    print("Done en {}ms".format(((end - start)*1000) // 1), msg)

# lecture et parsing
def read(filename: str) -> list:
    with open("{}.txt".format(filename), "r") as f:
        data = f.read().strip().split("\n\n")
        data = [i.replace("\n", " ") for i in data]
        return data
    
lettres = string.ascii_lowercase

d = {}
for i in lettres:
    d[i] = 0

def p1(data: list) -> int:
    score = 0
    for i in data:
        d_c = d.copy()
        for j in i:
            if j in lettres:
                try:
                    d_c[j] = 1
                except KeyError:
                    pass
        score += sum(d_c.values())
    return score


def p2(data: list) -> int:
    score = 0
    for i in data:
        if " " in i:
            score += attenzione(i)
        else:
            score += p1(i)
    return score

def attenzione(i: list) -> int:
    i = i.split()
    score_a = 0
    for j in lettres:
        flag = True
        while flag:
            k = 0
            while k < len(i):
                if j in i[k]:
                    k += 1
                else:
                    flag = False
                    k += 1000
            score_a += flag
            flag = False
    return score_a

def p3(data: list) -> int:
    score = 0
    for i in data:
        d_c = d.copy()
        d_c["skips"] = 0
        for j in i:
            if j in lettres:
                try:
                    d_c[j] += 1
                except KeyError:
                    pass
            elif j == " ":
                d_c["skips"] += 1
        log("d_c", d_c)
        for k in d_c.keys():
            if d_c[k] == d_c["skips"] + 1:
                d_c[k] = 1
            else:
                d_c[k] = 0
        log("d_c", d_c)
        score += sum(d_c.values())
        log("score", score)
    return score

start = tic()
log = logger(False)
print("Silver : ", p1(read("test")))
toc(start, "Step 1")
step2 = tic()
print("Gold : ", p2(read("input")))
toc(step2, "Step2")
step3 = tic()
print("Platine : ", p3(read("input")))
toc(step3, "Step3")