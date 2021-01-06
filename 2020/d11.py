file = "input"

def read():
    with open(f"{file}.txt", "r") as f:
       data = [datum.strip() for datum in f.readlines()]
       return data

def get_cell(t):
    """ Return cell size, 2x2 coordinates """
    x = t[0]
    y = t[1]
    cell_x = [max(x - 1, 0), min(x + 1, w - 1)]
    cell_y = [max(y - 1, 0), min(y + 1, h - 1)]
    return cell_x, cell_y

def data_to_bin(data):
    """ Translates occupied seats to 1, others to 0 """
    data = list(data)
    to_bin = str.maketrans("L.#","001")
    for i in range(len(data)):
        data[i] = "".join(data[i])
    return [datum.translate(to_bin) for datum in data]

def crowded(t, data):
    """ from # coordinate, returns True if it switches """
    Dx, Dy = get_cell(t)
    cell_score = 0
    switch_list = zone_eval(Dx, Dy, data)
    for i in data_to_bin(switch_list):
        for j in i:
            cell_score += int(j)
    cell_score -= 1
    if cell_score >= 4:
        return True
    return False

def free(t, data):
    """ from L coordinate, returns True if it switches """
    Dx, Dy = get_cell(t)
    cell_score = 0
    switch_list = zone_eval(Dx, Dy, data)
    for i in data_to_bin(switch_list):
        for j in i:
            cell_score += int(j)
    if cell_score == 0:
        return True
    return False

def zone_eval(Dx, Dy, data):
    """ gives back the formatted list of adjacent seats """
    switch_list = []
    for i in range(Dy[0], Dy[1] + 1):
        temp = [data[i][j] for j in range(Dx[0], Dx[1] + 1)]
        switch_list.append(temp)
    return switch_list
    
def step(data):
    """ Changes the grid once """
    new_data = []
    for i in range(w):
        new_line = [0]*h
        for j in range(h):
            current = data[j][i]
            if current == ".":
                value = "."
            elif current == "L":
                b = free((i, j), data)
                value = "L"*(1-b) + "#"*b
            else:
                b = crowded((i, j), data)
                value = "#"*(1-b) + "L"*b
            new_line[j] = value
        new_data.append("".join(new_line))
    new_data = map(list, zip(*new_data)) # FUCK
    return new_data

def looper(data):
    """ Changes the grid until it does not change """
    flag = False
    score = 0
    while not flag:
        score += 1
        temp = step(data)
        if temp == data:
            flag = True
        data = list(temp)
    score = count_occupied(data)
    return score

def count_occupied(data):
    temp = list(data)
    score = 0
    for i in temp:
        for j in i:
            if j == "#":
                score +=1
    return score
  
def main():
    """ main function for part 1 """
    data = read()
    global w
    global h
    w, h = len(data[0]), len(data)
    print(looper(data))

def main2():
    """ main function for part 1 """
    data = read()
    global w
    global h
    w, h = len(data[0]), len(data)
    print(looper2(data))

def looper2(data):
    """ Changes the grid until it does not change """
    flag = False
    score = 0
    while not flag:
        score += 1
        print(score)
        temp = step2(data)
        temp = list(temp)
        if temp == data:
            flag = True
        data = list(temp)
    score = count_occupied(data)
    return score
    
def step2(data):
    """ Changes the grid once """
    new_data = []
    for i in range(w):
        new_line = [0]*h
        for j in range(h):
            current = data[j][i]
            if current == ".":
                value = "."
            elif current == "L":
                b = free2((i, j), data)
                value = "L"*(1-b) + "#"*b
            else:
                b = crowded2((i, j), data)
                value = "#"*(1-b) + "L"*b
            new_line[j] = value
        new_data.append("".join(new_line))
    new_data = map(list, zip(*new_data)) # FUCK
    return new_data

def free2(t, data):
    """ from L coordinate, returns True if it switches """
    cell_score = 0
    cell_score += n_check(t, data)
    cell_score += s_check(t, data)
    cell_score += e_check(t, data)
    cell_score += w_check(t, data)
    cell_score += ne_check(t, data)
    cell_score += nw_check(t, data)
    cell_score += sw_check(t, data)
    cell_score += se_check(t, data)
    if cell_score == 0:
        return True
    return False

def crowded2(t, data):
    """ from # coordinate, returns True if it switches """
    cell_score = 0
    cell_score += n_check(t, data)
    cell_score += s_check(t, data)
    cell_score += e_check(t, data)
    cell_score += w_check(t, data)
    cell_score += ne_check(t, data)
    cell_score += nw_check(t, data)
    cell_score += sw_check(t, data)
    cell_score += se_check(t, data)
    if cell_score >= 5:
        return True
    return False


def n_check(t, data):
        # N CHECK:
    cell_score = 0
    x, y = t[0], t[1]
    flag = False
    while not flag:
        if y == 0:
            flag = True
            break
        y -= 1
        try:
            if data[y][x] == "L":
                break
            elif data[y][x] == "#":
                cell_score += 1
                break
            else:
                pass
        except IndexError:
            flag = True
    return cell_score

def s_check(t, data):
        # S CHECK:
    cell_score = 0
    x, y = t[0], t[1]
    flag = False
    while not flag:
        if y == h-1:
            flag = True
            break
        y += 1
        try:
            if data[y][x] == "L":
                break
            elif data[y][x] == "#":
                cell_score += 1
                break
            else:
                pass
        except IndexError:
            flag = True
    return cell_score

def w_check(t, data):
        # W CHECK:
    cell_score = 0
    x, y = t[0], t[1]
    flag = False
    while not flag:
        if x == 0:
            flag = True
            break
        x -= 1
        try:
            if data[y][x] == "L":
                break
            elif data[y][x] == "#":
                cell_score += 1
                break
            else:
                pass
        except IndexError:
            flag = True
    return cell_score

def e_check(t, data):
        # E CHECK:
    cell_score = 0
    x, y = t[0], t[1]
    flag = False
    while not flag:
        if x == w-1:
            flag = True
            break
        x += 1
        try:
            if data[y][x] == "L":
                break
            elif data[y][x] == "#":
                cell_score += 1
                break
            else:
                pass
        except IndexError:
            flag = True
    return cell_score

def nw_check(t, data):
        # NW CHECK:
    cell_score = 0
    x, y = t[0], t[1]
    flag = False
    while not flag:
        if y == 0 or x == 0:
            flag = True
            break
        y -= 1
        x -= 1
        try:
            if data[y][x] == "L":
                break
            elif data[y][x] == "#":
                cell_score += 1
                break
            else:
                pass
        except IndexError:
            flag = True
    return cell_score

def sw_check(t, data):
        # SW CHECK:
    cell_score = 0
    x, y = t[0], t[1]
    flag = False
    while not flag:
        if y == h-1 or x == 0:
            flag = True
            break
        y += 1
        x -= 1
        try:
            if data[y][x] == "L":
                break
            elif data[y][x] == "#":
                cell_score += 1
                break
            else:
                pass
        except IndexError:
            flag = True
    return cell_score

def se_check(t, data):
        # SE CHECK:
    cell_score = 0
    x, y = t[0], t[1]
    flag = False
    while not flag:
        if y == h-1 or x == w-1:
            flag = True
            break
        y += 1
        x += 1
        try:
            if data[y][x] == "L":
                break
            elif data[y][x] == "#":
                cell_score += 1
                break
            else:
                pass
        except IndexError:
            flag = True
    return cell_score
    
def ne_check(t, data):
        # NE CHECK:
    cell_score = 0
    x, y = t[0], t[1]
    flag = False
    while not flag:
        if y == 0 or x == w-1:
            flag = True
            break
        y -= 1
        x += 1
        try:
            if data[y][x] == "L":
                break
            elif data[y][x] == "#":
                cell_score += 1
                break
            else:
                pass
        except IndexError:
            flag = True
    return cell_score



main2()