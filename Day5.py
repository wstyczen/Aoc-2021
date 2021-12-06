from re import compile, findall

def getAllNrsInBetween(i1, i2):
    lower = min(i1, i2)
    upper = max(i1, i2)
    return range(lower, upper + 1)

def getLine(ventLine):
    line = []
    tickX = 1 if ventLine[0] - ventLine[2] < 0 else (-1 if ventLine[0] - ventLine[2] > 0 else 0)
    tickY = 1 if ventLine[1] - ventLine[3] < 0 else (-1 if ventLine[1] - ventLine[3] > 0 else 0)
    # ticks = (1 if ventLine[0] - ventLine[2] > 0 else -1, 1 if ventLine[1] - ventLine[3] > 0 else -1)
    x = ventLine[0]
    y = ventLine[1]
    line.append((x, y))
    while (x != ventLine[2] or y != ventLine[3]):
        x += tickX
        y += tickY
        line.append((x, y))
    return line

def processVentLine(ventLine, vents):
    for (x, y) in getLine(ventLine):
        vents[y][x] += 1


def printVents(vents):
    for y in range(len(vents)):
        for x in range(len(vents[0])):
            if vents[y][x] >= 1:
                print(vents[y][x], end="")
            else:
                print(".", end="")
        print()

def getPart1(vents):
    total = 0
    for ventLine in vents:
        total += len([vent for vent in ventLine if vent >= 2])
    return total

with open("Day5.txt") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]
    pattern = compile("\\d+")
    input = [[int(item) for item in findall(pattern, line)] for line in lines]
    width = max([max(nrs[0], nrs[2]) for nrs in input]) + 1
    height = max([max(nrs[1], nrs[3]) for nrs in input]) + 1
    vents = [[0 for x in range(width)] for y in range(height)]
    for ventLine in input:
        processVentLine(ventLine, vents)
    # printVents(vents)
    print(getPart1(vents))