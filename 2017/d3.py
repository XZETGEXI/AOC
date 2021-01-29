from pprint import pprint
import itertools as it

BIGVALUE = 123 # replace with your input

d_rose_func = {"E": lambda x,y: (x + 1, y),
"N": lambda x,y: (x, y + 1),
"W": lambda x,y: (x - 1, y),
"S": lambda x,y: (x, y - 1),
}

def change_gold(d_coo_values, v_c):
	score = 0
	for i,j in it.product((-1,0,1), repeat = 2):
		if i == 0 and j == 0:
			pass
		try:
			score += d_coo_values[(v_c[0] + i, v_c[1] + j)]
		except:
			pass

	return score

def main(star):
	d_coo_values = {}
	value = 1
	value_coords = (0,0)
	times = 1
	turn = 0
	flag = False

	d_coo_values[value_coords] = value
	
	for rose in it.cycle(d_rose_func):
		
		if turn == 2:
			turn = 0
			times += 1
			
		for i in range(times):
			value_coords = d_rose_func[rose](*value_coords)
			if star == "silver":
				value += 1
			if star == "gold":
				value = change_gold(d_coo_values, value_coords)
			
			d_coo_values[value_coords] = value
			
			if value >= BIGVALUE:
				flag = True
				break
		
		if flag:
			break
		
		turn += 1
	
	if star == "silver":
		inverted = {v:k for k,v in d_coo_values.items()}
		return sum(map(abs, inverted[BIGVALUE]))
	if star == "gold":
		return value


print("silver", main("silver"))

print("gold", main("gold"))
