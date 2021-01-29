with open("d5.txt") as f:
    data = f.readlines()

data = [datum.strip() for datum in data]

data = [int(datum) for datum in data]

def main(star):
	indice = 0
	steps = 0
	
	d_n_off = {n: i for n, i in enumerate(data)}
	
	while True:
		try:
			offset = d_n_off[indice]
			if star == "gold":
				if offset < 3:
					d_n_off[indice] += 1
				else:
					d_n_off[indice] -= 1
			indice += offset
			steps += 1
			
		except KeyError:
			print("out")
			break

	print(star, steps)
	
main("silver")
main("gold")
