dict_rules = dict()

rules, instructions = open("Input.txt").read().split(".")

rules = list(rules.strip().split("\n"))
instructions = list(instructions.strip().split("\n"))
total = 0

wrong_lists = list()

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
                wrong_lists.append(instruction)
                break

            if values in dict_rules.get(keys):
                safe = True
            else:
                wrong_lists.append(instruction)
                break
        else:
            continue
        break

matches = 0

for wrong_list in wrong_lists:
    matches = 0
    index_temp_list = len(wrong_list) - 1
    temp_list = list(wrong_list)

    for i, keys in enumerate(wrong_list):
        for values in wrong_list[:int(i)] + wrong_list[int(i+1):]:
            if dict_rules.get(keys) == None:
                temp_list[index_temp_list] = keys
                continue
            if values in dict_rules.get(keys):
                matches += 1
        else:
            temp_list[index_temp_list-matches] = keys
            matches = 0
            continue
        break
    

    total += temp_list[int(index_temp_list / 2)]
    
print(total)
            


