i = 123 # replace with your input


def review(i, star):
	i = str(i)
	LEN_DEC = len(i)
	s = []

	for n, j in enumerate(i):
	
		if star == "silver":
			pointer = (n + 1) % LEN_DEC
		if star == "gold":
			pointer = int((n+ LEN_DEC/2) % LEN_DEC)
		
		if i[pointer] == j:
			s.append(j)
		else:
			pass

	s = [int(i) for i in s]

	r = sum(s)

	print(r)

	
review(i, "silver")
review(i, "gold")
