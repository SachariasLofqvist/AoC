dict_rules = dict()

rules, instructions = open("Input.txt").read().split(".")

rules = list(rules.strip().split("\n"))
instructions = list(instructions.strip().split("\n"))
total = 0


for rule in rules:
    key, value = rule.split("|")
    
    key = int(key)
    value = int(value)

    if not key in dict_rules.keys():
        dict_rules[key] = [value]
    else:
        dict_rules[key].append(value)


for instruction in instructions:

    safe = False

    instruction = list(map(int, instruction.split(",")))

    for i, keys in enumerate(instruction[:-1]):
        for values in instruction[int(i + 1):]:
            
            if dict_rules.get(keys) == None and i == len(instruction) - 1: continue
            elif dict_rules.get(keys) == None:
                safe = False
                break

            if values in dict_rules.get(keys):
                safe = True
            else:
                safe = False
                break
        else:
            continue
        break


    if safe == True:

        index = len(instruction) - 1
        index = int(index / 2)


        total += instruction[index]

        

