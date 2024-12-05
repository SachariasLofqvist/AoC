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

    for i, item in enumerate(instruction[:-1]):
        for num in instruction[int(i + 1):]:
            
            if dict_rules.get(item) == None and i == len(instruction) - 1: continue
            elif dict_rules.get(item) == None:
                safe = False
                break

            if num in dict_rules.get(item):
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

        

