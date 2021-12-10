# P 1
def isWithinTheArray(x, y, array2d):
    return (x >= 0 and x < len(array2d[0]) and y >= 0 and y < len(array2d))

def isLowerThan(x1, y1, x2, y2, array):
    if (isWithinTheArray(x1, y1, array) and isWithinTheArray(x2, y2, array)):
        return array[y1][x1] < array[y2][x2]
    return True

def isRiskLevel(x, y, heightmap):
    return (isLowerThan(x, y, x + 1, y, heightmap) and isLowerThan(x, y, x - 1, y, heightmap)
    and isLowerThan(x, y, x, y + 1, heightmap) and isLowerThan(x, y, x, y -1, heightmap))

def getRiskLevel(x, y, heightmap):
    if isRiskLevel(x, y, heightmap):
        return heightmap[y][x] + 1
    return 0

def getRiskMap(heightmap):
    return [[getRiskLevel(i, j, heightmap) for i in range(len(heightmap[j]))] for j in range(len(heightmap))]

def getPart1(heightmap):
    return sum([sum([getRiskLevel(i, j, heightmap) for i in range(len(heightmap[j]))]) for j in range(len(heightmap))])

# P 2

def getLowPoints(heightmap):
    return [(i, j) for j in range(len(heightmap)) for i in range(len(heightmap[j])) if getRiskLevel(i, j, heightmap) != 0]

def getAdjacent(x, y, heightmap):
    adjacent = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(x, y) for (x, y) in adjacent if isWithinTheArray(x, y, heightmap)]

def getBasins(x, y, heightmap, basins):
    for (i, j) in getAdjacent(x, y, heightmap):
        if ((i, j) not in basins):
            if (heightmap[j][i] != 9 and heightmap[y][x] < heightmap[j][i]):
                basins.append((i, j))
                getBasins(i, j, heightmap, basins)
    return basins

from math import prod

def getPart2(heightmap):
    basins = []
    lowPoints = getLowPoints(heightmap)
    for (i, j) in lowPoints:
        basins.append(getBasins(i, j, heightmap, [(i, j)]))
    basinSizes = [len(basin) for basin in basins]
    basinSizes.sort(reverse=True)
    return prod(basinSizes[0:3])

with open("Day9.txt") as f:
    heightmap = [[int(c) for c in line.strip()] for line in f.readlines()]
    print(getPart1(heightmap))
    print(getPart2(heightmap))