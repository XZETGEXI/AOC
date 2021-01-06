from pprint import pprint
import copy
import re
from collections import defaultdict

def logger(verbose = True):
    def log(*arg):
        if verbose:
            print(*arg)
    return log

def read():
    with open("example.txt") as f:
        rules, messages = f.read().split("\n\n")
    return rules, messages
        
def parser(data, mode = "rules"):
    if mode == "rules":
        d = {}
        data = data.split("\n")
        for datum in data:
            result_lst = []
            datum = datum.split(" ")
            rule_id = int(datum.pop(0).rstrip(":"))
            try:
                index = datum.index("|")
                left = datum[:index]
                result_lst.append(left)
                right = datum[index + 1:]
                result_lst.append(right)
            except ValueError:
                for i in datum:
                    if i == "\"a\"" or i == "\"b\"":
                        result_lst.append(i.strip("\"\""))
                    else:
                        result_lst.append(int(i))
            d[rule_id] = result_lst
        return d
    elif mode == "messages":
        data = data.split("\n")[:-1]
        return data
    else:
        log("Wrong mode")



def rule_descent(rules_dict, d, i = 0, n = 0):
    log(f"Enteriiiiiiing {i} level {n}".center(100))
    log("d is ", d)
    try:
        log("Rules:", rules_dict[i])
        l = len(rules_dict[i])
        if l == 1:
            value = rules_dict[i][0]
            log("value is", value)
            if value == "a":
                try:
                    d[n] = d[n] + "a"
                except:
                    d[n].append("a")
                log("Appending a on floor ", n)
                return n
            elif value == "b":
                try:
                    d[n] = d[n] + "b"
                except:
                    d[n].append("b")
                log("Appending b on floor ", n)
                return n
            else:
                n = rule_descent(rules_dict, d, i = i , n = n)
        else:
            raise TypeError
    except TypeError:
        log("list detected", rules_dict[i])
        for j in rules_dict[i]:
            log("Checking", "->", j)
            if isinstance(j, list):
                if d[n]:
                    d[n].append("|")
                else:
                    d[n] = []
                log("Opening list on floor", n)
                for k in j:
                    log(j, "in that list testing", k)
                    k = int(k)
                    result = rule_descent(rules_dict, d, i = k, n = n)
            else:
                log("No Deeper")
                result = rule_descent(rules_dict, d, i = j, n = n)
            if result:
                n = result
            n += 1
            
                

        
    
def nawak():
    first_val = list(rules_dict[i])
    log("i is", i, "then", first_val, "checking", first_val[0])
    if isinstance(first_val[0], list):
        mode = 2
    else:
        mode = 1
    if mode == 1:
        if first_val[0] == "a":
            return "a"
        elif first_val[0] == "b":
            return "b"
        else:
            return rule_descent(rules_dict, first_val[0])
    elif mode == 2:
        collector = []
        middle = 1
        for j in first_val:
            log(j, "j")
            for k in j:
                temp = rule_descent(rules_dict, int(k))
                collector.append(temp)
            if middle:
                collector.append("_")
                middle -= 1
        return collector
 
def stringify_list(lst_in):
    s = ""
    lst = list(lst_in)
    while lst:
        s += str(lst.pop(0))
    return s

def find(e):
    t = 0
    for i in range(len(e)):
        t += int(e[i] == "[")
        t -= int(e[i] == "]")
        if t == - 1:
            return i
            
def seek(e):
    while True:
        try:
            pattern = re.search("\[", e)
            ps = pattern.span(0)[0]
            pe = find(e[ps+1:]) + ps + 2
            e = e[:ps] + merge(e[ps+1:pe-1]) + e[pe:]
        except:
            break
    return e

def merge(e):
    result = ""
    e = eval(e)
    print(e)
    for n, i in enumerate(e):
        print(i)
        if i == "_":
            print("hre")
            for j in e[n+1:]:
                result += str(j)
            break
        else:
            result += str(i)
    return result
        
def main():
    rules, messages = read()
    rules_dict = parser(rules, mode = "rules")
    msg_lst = parser(messages, mode = "messages")
    print("Rules :")
    pprint(rules_dict)
    print("Messages :", msg_lst)
    
    print("startin'")
    d = {i: "" for i in range(9)}
    result = rule_descent(rules_dict, d)
    print(result)
    print("\n")
    print(d)
    
log = logger(True)

main()



