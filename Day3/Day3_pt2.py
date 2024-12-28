import re

total = 0
multiply = True

with open ("Input.txt") as file:
    instruction = file.read()

result = re.findall((r"mul[(]\d{1,3},\d{1,3}[)]|don't[(][)]|do[(][)]"), instruction)

for item in result:
    if item == "don't()":
        multiply = False
    elif item == "do()":
        multiply = True
    else:
        if multiply == True:

            numbers = re.findall(r'\d{1,3}', item)
    
            numbers = [int (x) for x in numbers]

            pair = tuple(numbers)

            temp = pair[0] * pair[1]

            total += temp

            temp = 1
        else:
            continue

print(total)