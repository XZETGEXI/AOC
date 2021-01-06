from collections import deque
import copy
import time
import os

def read():
    with open("input.txt") as f:
        data = [datum.strip() for datum in f.readlines()]
    return data

def make_queue(example):
    q_open = deque()
    q_close = deque()
    for n, i in enumerate(example):
        if i == "(":
            q_open.append(n)
        if i == ")":
            q_close.append(n)
    return q_open, q_close
            
def change(example, q_open, q_close):
    o = q_open.pop()
    while True:
        try:
            c_expr_lst = q_close.pop()
            if c_expr_lst > o:
                c = c_expr_lst
        except:
            break
    expr_lst = example[o+1:c].split(" ")
    result = resolve(expr_lst)
    return example[:o] + str(result) + example[c+1:]

def resolve(expr_lst):
    if len(expr_lst) == 1:
        return expr_lst[0]
    else:
        new_expr_lst = []
        if expr_lst[1] == "+":
            result = int(expr_lst[0]) + int(expr_lst[2])
            new_expr_lst.append(result)
        else:
            result = int(expr_lst[0]) * int(expr_lst[2])
            new_expr_lst.append(result)
        rest = expr_lst[3:]
        for i in rest:
            new_expr_lst.append(i)
        return resolve(new_expr_lst)
  
def calculate1(line):
    temp = line
    while True:
        try:
            q_open, q_close = make_queue(temp)
            temp = change(temp, q_open, q_close)
        except:
            break
    return resolve(temp.split(" "))

def main1():
    data = read()
    score = 0
    for i in data:
        score += calculate1(i)
    return score

def calculate2(line):
    temp = line
    while True:
        try:
            q_open, q_close = make_queue(temp)
            temp = change2(temp, q_open, q_close)
        except:
            break
    return resolve2(temp.split(" "))

def change2(example, q_open, q_close):
    o = q_open.pop()
    while True:
        try:
            c_expr_lst = q_close.pop()
            if c_expr_lst > o:
                c = c_expr_lst
        except:
            break
    expr_lst = example[o+1:c].split(" ")
    result = resolve2(expr_lst)
    return example[:o] + str(result) + example[c+1:]

def resolve2(expr_lst):
    value = 1
    lst_copy = list(expr_lst)
    while True:
        try:
            index = lst_copy.index("+")
            before = int(lst_copy[index - 1])
            after = int(lst_copy[index + 1])
            temp = before + after
            if index >= (len(lst_copy) - 2):
                bool_end = 0
            else:
                bool_end = 1
            lst_copy = lst_copy[:index - 1] + [temp] + lst_copy[index + 2:]*bool_end
        except:
            break
    filtered = filter(lambda x: x != "*", lst_copy)
    for i in filtered:
        try:
            value *= int(i)
        except:
            pass
    return int(value)

def main2():
    data = read()
    score = 0
    for i in data:
        score += calculate2(i)
    return score

w = os.get_terminal_size()[0]
start = time.time()
Silver = main1()
step = time.time()
print(f"Silver : {Silver}".center(w))
print(f"Time : {(step - start) * 1000 // 1} ms".center(w))
Gold = main2()
end = time.time()
print(f"Gold : {Gold}".center(w))
print(f"Time : {(end - step) * 1000 // 1} ms".center(w))