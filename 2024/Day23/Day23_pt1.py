lines = [line for line in open("Day23\\input.txt").read().strip().split("\n")]
connections = {}

for line in lines:
    key = (line.split("-")[0])
    value = (line.split("-")[1])
    if key not in connections: connections[key] = set()
    if value not in connections: connections[value] = set()
    connections[key].add(value)
    connections[value].add(key)

sets = set()

for x in connections:
    for y in connections[x]:
        for z in connections[y]:
            if x != z and x in connections[z]:
                sets.add(tuple(sorted([x,y,z])))

counter = 0

for tri in sets:
    for cd in tri:
        if cd.startswith("t"):
            counter += 1
            break
        
print(counter)

