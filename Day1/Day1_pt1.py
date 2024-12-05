input_list = list()
distans = 0
left = list()
right = list()

with open("input.txt") as file:
    input_list = file.readlines()


for line in input_list:
    numbers = line.strip().split()
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))

left.sort()
right.sort()

for i, number in enumerate(left):

    num = number - right[i]

    if num < 0:
        num = num * -1

    distans = distans + num

print(distans)


