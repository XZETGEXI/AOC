import itertools as it

LOW = 172851
HIGH = 675869

doubles = set()

for i in range(10):
    doubles.add(str(i)*2)

triples = set()

for i in range(10):
    triples.add(str(i)*3)

def main():
    score = 0
    for i in range(LOW, HIGH +1):
        flag = True
        s = str(i)
        s_list = list(s)
        s_list_sorted = list(s_list)
        s_list_sorted.sort()
        if s_list != s_list_sorted:
            flag = False
        if not any([j in s for j in doubles]) and flag:
            flag = False
        if any([j in s for j in triples]) and flag:
            triple = [j for j in triples if j in s]
            double = [j for j in doubles if j in s]
            print("triple", triple, "double", double)
            if all([k in triple[0] for k in double]) or len(triple) > 1:
                flag = False
                print("catch", i)
            else:
                print("sus", i)
        score += flag
    return score
        
print(main())
