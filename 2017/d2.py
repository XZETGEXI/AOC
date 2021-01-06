with open("d2.txt", "r") as f:
    data = f.readlines()
    data = [datum.strip().split("\t") for datum in data]
    data = [map(int, datum) for datum in data]

r = {}

for n, datum in enumerate(data):
    to_check = [*datum]
    r[n] = max(to_check) - min(to_check)
    
print(sum(r.values()))

with open("d2.txt", "r") as f:
    data = f.readlines()
    data = [datum.strip().split("\t") for datum in data]
    data = [map(int, datum) for datum in data]

r = {}

for n, datum in enumerate(data):
    to_check = [*datum]
    for i in to_check:
        for j in to_check:
            if not i % j and i != j:
                r[n] = (i,j)
                continue

o = 0

for a,b in r.items():
    o += (max(b) / min(b))
    
print(o)