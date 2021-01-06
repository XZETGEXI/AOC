import re

file = "input"

def read():
    with open(f"{file}.txt", "r") as f:
        return [datum.strip() for datum in f.readlines()]
    
def parser(datum):
    inst = re.compile(r"\D")
    value = re.compile(r"\d+")
    return inst.search(datum).group(), int(value.search(datum).group())

inst_dict = {"N": 0,"S": 0,"E": 0,"W": 0,"L": 0,"R": 0,"F": 0}

def homot(inst_dict):
    """ Simplifies the dictionary """
    north = inst_dict["N"] - inst_dict["S"]
    east = inst_dict["E"] - inst_dict["W"]
    rot_r = (inst_dict["R"] - inst_dict["L"]) % 360
    fwd = inst_dict["F"]
    return north, east, rot_r, fwd

# The value of facing gives ->
# 0: east
# 1: north
# 2: west
# 3: south

facing = 0

def i_cant_feel_my_face(inst, value):
    """ Changes facing """
    global facing
    if inst == "R":
        value = value // 90
        facing = (facing - value) % 4
    else:
        value = value // 90
        facing = (facing + value) % 4
    
def face_the_truth():
    """ Converts F to the current cardinal """
    if facing == 1:
        return "N"
    if facing == 3:
        return "S"
    if facing == 0:
        return "E"
    if facing == 2:
        return "W"
    else:
        print("Yo what the fuck")

def main():
    data = read()
    for datum in data:
        inst, value = parser(datum)
        if inst == "R" or inst == "L":
            i_cant_feel_my_face(inst, value)
        elif inst == "F":
            inst = face_the_truth()
            inst_dict[inst] += value
        else:
            inst_dict[inst] += value
    north, east, rot_r, fwd = homot(inst_dict)
    print(f"north is {north}, east {east}")

#main2

pos_way_x = 10
pos_way_y = 1
pos_boat_x = 0
pos_boat_y = 0

def you_spin_me_round(inst, value):
    """ Spins the waypoint """
    global pos_way_x # this is ugly
    global pos_way_y
    if inst == "R": # clockwise
        value = value // 90
        for i in range(value):
            temp_y = - pos_way_x
            temp_x = pos_way_y
            pos_way_x = temp_x
            pos_way_y = temp_y
    else: # counter-clockwise
        value = value // 90
        for i in range(value):
            temp_y = pos_way_x
            temp_x = - pos_way_y
            pos_way_x = temp_x
            pos_way_y = temp_y
    
def oh_no_no_no(value):
    """ Moves the boat according to the waypoint """
    global pos_boat_x # that too
    global pos_boat_y
    global pos_way_x
    global pos_way_y
    for i in range(value):
        pos_boat_x += pos_way_x
        pos_boat_y += pos_way_y


def main2():
    global pos_boat_x
    global pos_boat_y
    global pos_way_x
    global pos_way_y
    data = read()
    for datum in data:
        inst, value = parser(datum)
        if inst == "R" or inst == "L":
            you_spin_me_round(inst, value)
        elif inst == "F":
            oh_no_no_no(value)
        elif inst == "N":
            pos_way_y += value
        elif inst == "S":
            pos_way_y -= value
        elif inst == "W":
            pos_way_x -= value
        elif inst == "E":
            pos_way_x += value

main2()
print("east", pos_boat_x)
print("north", pos_boat_y)
print("total", abs(pos_boat_x) + abs(pos_boat_y))