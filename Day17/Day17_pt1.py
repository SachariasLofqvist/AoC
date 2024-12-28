jump = False
output = []

register, program = open("Day17\\input.txt").read().strip().split("\n\n")

program = [int(char) for char in program.strip().split(":")[1].split(",")]

a, b, c = register.split("\n")

a = (int(a.split(":")[1]))
b = (int(b.split(":")[1]))
c = (int(c.split(":")[1]))

def comboValue(value):
    new_value = None
    
    match value:
        case 0:
            new_value = 0
        case 1:
            new_value = 1
        case 2:
            new_value = 2
        case 3:
            new_value = 3
        case 4:
            new_value = a
        case 5:
            new_value = b
        case 6:
            new_value = c
    
    return new_value

pointer = 0

while pointer + 1 <= len(program):

    jump = False

    code, value = program[pointer], program[pointer + 1]
    
    match code:
        case 0:
            # value: COMBO
            value = comboValue(value)
            a = int(a // (2 ** value))
        case 1:
            # value: LITERAL
            b = b ^ value
        case 2: 
            # value: COMBO
            value = comboValue(value)
            b = value % 8
        case 3:
            # value: LITERAL
            if not a == 0:
                jump = True
                pointer = value
            # Do not increase
        case 4:
            b = b ^ c
        case 5:
            # value COMBO
            value = comboValue(value)
            value = value % 8
            output.append(value)
        case 6:
            # value COMBO
            value = comboValue(value)
            b = int(a // (2 ** value))
        case 7:
            # value COMBO
            value = comboValue(value)
            c = int(a // (2 ** value))

    if not jump == True:
        pointer += 2

print(output)