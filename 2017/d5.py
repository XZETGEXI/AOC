with open("d5.txt") as f:
    data = f.readlines()

data = [datum.strip() for datum in data]

data = [int(datum) for datum in data]

# data = [0,3,0,1,-3]

d_n_off = {n: i for n, i in enumerate(data)}

indice = 0
steps = 0

while 1:
    try:
        offset = d_n_off[indice]
        #gold
        if offset < 3:
            d_n_off[indice] += 1
        else:
            d_n_off[indice] -= 1
        indice += offset
        steps += 1
    except KeyError:
        print("out")
        break

print(steps)