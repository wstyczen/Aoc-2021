def addEdge(start, end, edges):
    if start in edges:
        edges[start].append(end)
    else:
        edges[start] = [end]

currentPath = []
paths = []

# DFS
# Took inspiration from:
# https://www.baeldung.com/cs/simple-paths-between-two-vertices

def part1(start, end, edges, visited):
    # if it's a smaller cave and has already been visited in this path - return
    if start.islower() and start in visited:
        return
    visited.append(start)
    currentPath.append(start)
    if start == end:
        paths.append(currentPath.copy())
        visited.remove(start)
        currentPath.pop()
        return
    for adjNode in edges[start]:
        part1(adjNode, end, edges, visited)
    currentPath.pop()
    visited.remove(start)

def part2(start, end, edges, visitedDict):
    if start.islower():
        if start == "start" and visitedDict[start] >= 1:
            return
        # if already visited this cave and visited another small cave twice
        if len([1 for visitedCave in visitedDict if visitedCave.islower() and visitedDict[visitedCave] >= 2]) >= 1:
            if visitedDict[start] >= 1:
                return
    visitedDict[start] += 1
    currentPath.append(start)
    if start == end:
        paths.append(currentPath.copy())
        visitedDict[start] -= 1
        currentPath.pop()
        return
    for adjNode in edges[start]:
        part2(adjNode, end, edges, visitedDict)
    visitedDict[start] -= 1
    currentPath.pop()

with open("Input\\Day12.txt") as f:
    edges = {}
    for line in f.readlines():
        nodes = line.strip().split("-")
        # save an undirected edge as two directed ones - to and from
        addEdge(nodes[0], nodes[1], edges)
        addEdge(nodes[1], nodes[0], edges)
    # P 1
    visited = []
    part1("start", "end", edges, visited)
    print("PART 1: " + str(len(paths)))
    # P 2
    paths.clear()
    visitedDict = {node:0 for node in edges}
    part2("start", "end", edges, visitedDict)
    print("PART 2: " + str(len(paths)))
