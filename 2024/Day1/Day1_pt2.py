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

for lnumber in left:

    alike = 0
    
    for rnumber in right:
        if rnumber == lnumber:
            alike = alike + 1

    distans = distans + (lnumber * alike)

print(distans)
