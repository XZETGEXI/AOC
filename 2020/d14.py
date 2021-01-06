import re
import itertools as it

BITS = 36

file = "input"

# Utilities

def read():
    with open(f"{file}.txt", "r") as f:
        data = f.read().splitlines()
    return data

def parser(s, mode = "mem"):
    if mode == "mask":
        re_mask = re.compile(r"^mask = (\w+)$")
        match = re_mask.search(s)
        if match:
            return match.groups(s)[0]
    else:
        re_mem = re.compile(r"^mem\[(\d+)\] = (\d+)$")
        match = re_mem.fullmatch(s)
        if match:
            return match.groups(s)

def bin_format(value):
    temp_bin = bin(value)[2:]
    nb_char = len(temp_bin)
    nb_char = BITS - nb_char
    missing = "0"*nb_char
    temp_bin = missing + temp_bin
    return temp_bin

# Part I

def mask_xor(value, mask):
    temp_bin = bin_format(value)
    for n, i in enumerate(mask):
        if i == "1":
            temp_bin = temp_bin[:n] + "1" + temp_bin[n+1:]
        if i == "0":
            temp_bin = temp_bin[:n] + "0" + temp_bin[n+1:]
    result = int(temp_bin, 2)
    return result

def main(data):
    d = {}
    for i in data:
        if "mask" in i:
            mask = parser(i, mode = "mask")
        else:
            mem, value = parser(i)
            mem = int(mem)
            value = int(value)
            value = mask_xor(value, mask)
            d[mem] = value
    return d

# Part II

# Utilities

def binary_lst_maker(n):
    temp = {*it.product(("0","1"), repeat = n)}
    return temp

def MAD(mem, mask):
    temp_bin = bin_format(mem)
    for n, i in enumerate(mask):
        if i == "1":
            temp_bin = temp_bin[:n] + "1" + temp_bin[n+1:]
        elif i == "0":
            pass
            #temp_bin = temp_bin[:n] + "0" + temp_bin[n+1:]
        elif i == "X":
            temp_bin = temp_bin[:n] + "X" + temp_bin[n+1:]
    int_values_lst = MAD_format_X(temp_bin)
    return int_values_lst

def MAD_format_X(temp_bin):
    result = []
    temp_lst = fuck_you(temp_bin)
    print(temp_lst, "découpage")
    n = len([a for a in temp_lst if not a])
    binary_lst = binary_lst_maker(n)
    while binary_lst:
        current = binary_lst.pop()
        print(current, "current")
        temp_str = ""
        init = 0
        for i in temp_lst:
            if i:
                temp_str += i
            else:
                temp_str += current[init]
                init += 1
        print(temp_str, "combination")
        temp_int = int(temp_str, 2)
        result.append(temp_int)
    return result
            
def fuck_you(s):
    pattern = re.compile(r"([^X]+|X)")
    result = [*pattern.findall(s)]
    temp_lst = []
    for i in result:
        if i == "X":
            temp_lst.append("")
        else:
            temp_lst.append(i)
    return temp_lst
    
def main2(data):
    d = {}
    for i in data:
        if "mask" in i:
            mask = parser(i, mode = "mask")
            print(mask, "last mask")
        else:
            mem, value = parser(i)
            mem = int(mem)
            print(mem, "last mem")
            value = int(value)
            print(value, "last value")
            mem_list = MAD(mem, mask)
            print(mem_list, "last mem_list")
            for j in mem_list:
                d[j] = value
    return d

# Main

if __name__ == "__main__":
    data = read()
    d = main(data)
    print("p1 :", sum(d.values()))
    d = main2(data)
    print("p2 :", sum(d.values()))