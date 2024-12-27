from collections import deque

index = 0
init_dict = {}

start_dict, instructions = open("Day24\\input.txt").read().strip().split("\n\n")

for line in start_dict.split("\n"):
    key, value = line.split(": ")
    init_dict[key] = int(value)

def findRight(key1, key2, operator, binary_number_x, binary_number_y):
    value = None

    if operator == "AND":
        if init_dict[key1] == init_dict[key2] == 1:
            value = 1
        else:
            value = 0       
    elif operator == "OR":
        if init_dict[key1] == init_dict[key2] == 0:
            value = 0
        else:
            value = 1
    elif operator == "XOR":
        if init_dict[key1]  != init_dict[key2]:
            value = 1
        else:
            value = 0 

    return value

binary_number_x = deque()
binary_number_y = deque()

for key in sorted(init_dict):
    if key.startswith("x"):
        binary_number_x.appendleft(str(init_dict[key]))
    else:
        binary_number_y.appendleft(str(init_dict[key]))

