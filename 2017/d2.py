with open("d2.txt", "r") as f:
    data = f.readlines()
    data = [datum.strip().split("\t") for datum in data]
    data = [[*map(int, datum)] for datum in data]

r = {}

for n, datum in enumerate(data):
    r[n] = max(datum) - min(datum)
    
print("silver", sum(r.values()))

r = {}

for n, datum in enumerate(data):
    for i in datum:
        for j in datum:
            if not i % j and i != j:
                r[n] = (i,j)
                continue


o = 0

for b in r.values():
    o += (max(b) / min(b))
    
print("gold", o)
