total = 0

def check_combo(target, numbers):
    if len(numbers) == 1:
        return target == numbers[0]
    if target % numbers[-1] == 0 and check_combo(target // numbers[-1], numbers[:-1]):
        return True
    if target > numbers[-1] and check_combo(target-numbers[-1], numbers[:-1]):
        return True
    if len(str(target)) > len(str(numbers[-1])) and str(target).endswith(str(numbers[-1])) and check_combo(int(str(target)[:-len(str(numbers[-1]))]), numbers[:-1]):
        return True
    return False

for line in open("Day7\\input.txt"):
    target, numbers = line.split(": ")
    target = int(target)
    numbers = [int(x) for x in numbers.split()]
    if check_combo(target, numbers):
        total += target

print(total)


