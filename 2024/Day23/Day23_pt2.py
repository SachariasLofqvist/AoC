lines = [line for line in open("2024\\Day23\\input.txt").read().strip().split("\n")]
connections = {}

for line in lines:
    key = (line.split("-")[0])
    value = (line.split("-")[1])
    if key not in connections: connections[key] = set()
    if value not in connections: connections[value] = set()
    connections[key].add(value)
    connections[value].add(key)

sets = set()

def serch(node, req):
    key = tuple(sorted(req))
    if key in sets: return
    sets.add(key)

    for neighbor in connections[node]:
        if neighbor in req: continue
        if not all(neighbor in connections[query] for query in req): continue
        serch(neighbor, {*req, neighbor})

for x in connections:
    serch(x, {x})

print(",".join(sorted(max(sets, key=len))))