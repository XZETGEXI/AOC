def read():
    with open("input.txt", "r") as f:
        return [i.strip().split() for i in f.readlines()]

# part 1
def loop(d, ending):
    _dict = d
    ACCU = 0
    pointer = 0
    visited = set()
    command = 0
    value = 0
    flag = True
    while flag:
        command = _dict[pointer][0]
        value = _dict[pointer][1]
        if pointer in visited:
            ACCU = -1
            flag = False
            continue
        else:
            visited.add(pointer)
        if command == "nop":
            pointer += 1
        if command == "acc":
            ACCU += int(value)
            pointer += 1
        if command == "jmp":
            pointer += int(value)
        if ending in visited:
            flag = False
    return ACCU

# change key n to (jmp if nop / nop if jmp)
def change_dict(d_zero, n, p):
    d_copy = d_zero.copy()
    if p == "jmp":
        d_copy[n][0] = "nop"
    if p == "nop":
        d_copy[n][0] = "jmp"
    return d_copy

# create a dict from data with numbered keys
def create_dict(data):
    d = {}
    jmp_lst = set()
    nop_lst = set()
    for (n, i) in enumerate(data):
        d[n] = i
        if i[0] == "jmp":
            jmp_lst.add(n)
        if i[0] == "nop":
            nop_lst.add(n)
    ending = len(d) - 1
    return d, ending, jmp_lst, nop_lst

def main(p):
    value_lst = []
    if p == "jmp":
        # IF I DON'T READ HERE
        data = read()
        d, ending, jmp_lst, nop_lst = create_dict(data)
        while jmp_lst:
            n = jmp_lst.pop()
            # IF I DON'T RE-READ DATA AT EVERY TURN OF THE LOOP
            data = read()
            d = create_dict(data)[0]
            # WHEN I CALL THIS
            d_changed = change_dict(d, n, p)
            # IT CHANGES THE MOTHERF***CKING DATA
            # THE DATA ITSELF
            value_lst.append(loop(d_changed, ending))
    if p == "nop":
        data = read()
        d, ending, jmp_lst, nop_lst = create_dict(data)
        while nop_lst:
            n = nop_lst.pop()
            data = read()
            d = create_dict(data)[0]
            d_changed = change_dict(d, n, p)
            value_lst.append(loop(d_changed, ending))
    return value_lst

print max(main("jmp"))
print max(main("nop"))
