from pprint import pprint
import itertools as it

# with open("d3.txt") as f:
#     data  [datum.strip() for datum in f.readlines()]

# data  [datum.split() for datum in data]
# data  [map(int, datum) for datum in data]
# data  [[*datum] for datum in data] 312051

# print(data)
BIGVALUE = 312051

d_coo_values = {}
d_rose_func = {"E": lambda x,y: (x + 1, y),
"N": lambda x,y: (x, y + 1),
"W": lambda x,y: (x - 1, y),
"S": lambda x,y: (x, y - 1),
}

value = 1
value_coords = (0,0)
times = 1
turn = 0
flag = False

d_coo_values[value_coords] = value

def cha(v, v_c):
    score = 0
    for i,j in it.product((-1,0,1), repeat = 2):
        if i == 0 and j == 0:
            pass
        try:
            score += d_coo_values[(v_c[0] + i, v_c[1] + j)]
        except:
            pass

    return score

for rose in it.cycle(d_rose_func):
    
    if turn == 2:
        turn = 0
        times += 1
    for i in range(times):
        value_coords = d_rose_func[rose](*value_coords)
        value = cha(value, value_coords)
        
        d_coo_values[value_coords] = value
        if value >= BIGVALUE:
            flag = True
            break
    
    if flag:
        break
    
    turn += 1

print(value)

# for k,v in d_coo_values.items():
#     if v == BIGVALUE:
#         print(k)
        
print(151 + 279)