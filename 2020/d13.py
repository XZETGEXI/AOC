file = "bigboy"

def read():
    with open(f"{file}.txt", "r") as f:
        data = [datum.strip() for datum in f.readlines()]
        return data

stamp, bus_id = read()

stamp = int(stamp)

bus_id = filter(lambda x: x != "x", [i for i in bus_id.split(",")])

bus_id = map(int, bus_id)

d = {}

def main1():
    for i in bus_id:
        facteur = (stamp // i) + 1
        wait_time = (facteur*i) - stamp
        d[i] = wait_time
    
d = {}
stamp, bus_id = read()

stamp = int(stamp)

new_bus_id = bus_id.split(",")

for n, i in enumerate(new_bus_id):
    try:
       i = int(i)
       d[i] = n
    except:
        pass


lst = []
for i in d.keys():
    lst.append([i, d[i]])

def write(lst):
    with open("result.txt", "w") as f:
        for i in lst:
            f.writelines(str(i)+",")
    f.close()

write(lst)

def solver(d):
    flag = False
    facteur = 0
    key = [*d.keys()][0]
    print(key, "key")
    stamp = key
    while not flag:
        facteur += 1
        current = (facteur * stamp) - d[key]
        flag = True
        for i in d:
            try:
                assert (current + d[i]) % i == 0
            except:
                flag = False
                break
    return current

nombre = 0

def main2(d):
    lst_keys = list(d.keys())
    flag = False
    while not flag:
        try:
            sub_dict = {i: d[i] for i in lst_keys[0:2]}
            start += solver(sub_dict)
            new_step = 1
            for i in sub_dict.keys():
                new_step *= i
        except:
            flag = True
    for i in lst_keys:
#        while d:
        facteur = 1
        facteur *= i
    return facteur
