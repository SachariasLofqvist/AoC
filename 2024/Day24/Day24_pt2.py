file = open("2024\\Day24\\input.txt")

for line in file:
    if line.isspace(): break

formulas = {}

for line in file:
    x, op, y, z = line.replace(" ->", " ").split()
    formulas[z] = (op, x, y)

def make_wire(char, num):
    return char + str(num).rjust(2, "0")

def verify_z(wire, num):
    print("vz", wire, num)
    op, x, y = formulas[wire]
    if op != "XOR": return False
    if num == 0: return sorted([x, y]) == ["x00", "y00"]
    return ver_int_xor(x, num) and ver_car_bit(y, num) or ver_int_xor(y, num) and ver_car_bit(x, num)

def ver_int_xor(wire, num):
    print("vx", wire, num)
    op, x, y = formulas[wire]
    if op != "XOR": return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def ver_car_bit(wire, num):
    print("vc", wire, num)
    op, x, y = formulas[wire]
    if num == 1:
        if op != "AND": return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR": return False
    return ver_dir_car(x, num - 1) and ver_recar(y, num - 1) or ver_dir_car(y, num - 1) or ver_recar(x, num - 1)

def ver_dir_car(wire, num):
    print("vd", wire, num)
    op, x, y = formulas[wire]
    if op != "AND": return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def ver_recar(wire, num):
    print("vr", wire, num)
    op, x, y = formulas[wire]
    if op != "AND": return False
    return ver_int_xor(x, num) and ver_car_bit(y, num) or ver_int_xor(y, num) and ver_car_bit(x, num)

def verify(num):
    return verify_z(make_wire("z", num), num)

i = 0

while True:
    if not verify(i): break
    i += 1


print("failed on", make_wire("z", i))