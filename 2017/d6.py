from pprint import pprint
import copy

with open("d7.txt") as f:
    data = f.read()
    
data = data.split()

d_no_blocks = {}

for n, i in enumerate(data):
    d_no_blocks[n] = int(i)

# d_no_blocks = {0: 0, 1: 2, 2: 7, 3: 0}

checker = {}
steps = 0

def reverse(d):
    new_d = {v: k for k,v in d.items()}
    return new_d

def changer(d):
    new_d = copy.deepcopy(d)
    nb_cells = len(d)
    max_val = max(new_d.values())
    for k in new_d:
        if new_d[k] == max_val:
            max_key = k
            break
    max_key_memo = max_key
    for i in range(max_val):
        max_key = (max_key + 1) % nb_cells
        new_d[max_key] += 1
    new_d[max_key_memo] -= max_val
    return new_d

while True:
    steps += 1
    d_no_blocks = changer(d_no_blocks)
    d_to_s = str(d_no_blocks)
    if d_to_s in checker:
        print("gold", steps - checker[d_to_s])
        break
    else:
        checker[d_to_s] = steps

print("silver", steps)