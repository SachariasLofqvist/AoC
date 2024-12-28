register, program = open("Day17\\input.txt").read().strip().split("\n\n")

program = [int(char) for char in program.strip().split(":")[1].split(",")]

a, b, c = register.split("\n")

a = (int(a.split(":")[1]))
b = (int(b.split(":")[1]))
c = (int(c.split(":")[1]))

def find(program, ans):
    if program == []: return ans
    for b in range(8):
        a = ans << 3 | b
        b = a % 8
        b = b ^ 2
        c = a >> b
        b = b ^ c
        b = b ^ 3
        if b % 8 == program[-1]:
            sub = find(program[:-1], a)
            if sub is None: continue
            return sub

print(find(program, 0))




'''
b = a % 8
b = b ^ 2
c = a >> b
b = b ^ c
b = b ^ 3
out(b % 8)
a = a >> 3
jmp start if a == 0
'''