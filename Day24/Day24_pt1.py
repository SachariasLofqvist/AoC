from collections import deque

init_dict = {}

start_dict, instructions = open("Day24\\input.txt").read().strip().split("\n\n")


for line in start_dict.split("\n"):
    key, value = line.split(": ")
    init_dict[key] = int(value)

def calculate(key1, key2, operator):
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


instructions = [instruction for instruction in instructions.split("\n")]

index = 0

while instructions:
    key1, operator, key2, temp, target = instructions[index].split(" ")
    
    if key1 not in init_dict or key2 not in init_dict:
        index += 1
        continue
    else:
        init_dict[target] = calculate(key1, key2, operator)
        instructions.pop(index)
        index = 0


binary_number = deque()

z_keys = [keys for keys in init_dict if keys.startswith("z")]


for keys in sorted(z_keys):
    binary_number.appendleft(str(init_dict[keys]))

print(sorted(z_keys))

tot = "".join(binary_number)
print(tot)
tot = int(tot, 2)
print(tot)