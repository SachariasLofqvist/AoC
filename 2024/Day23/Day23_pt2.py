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

def serch(node, req):
    pass

