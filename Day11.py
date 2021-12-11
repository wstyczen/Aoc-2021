from os import times


def isWithinArray(x, y, array):
    return x >= 0 and y >= 0 and x < len(array[0]) and y < len(array)

def getAdjacent(x, y, array):
    return [(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if ((i, j) != (x, y) and isWithinArray(i, j, array))]

def increaseEnergyLevel(array, increment = 1):
    return [[el + increment for el in row] for row in array]

def simulateFlashes(array, flashed):
    newFlashed = []
    [newFlashed.append((i, j)) for j in range(len(array)) for i in range(len(array[0])) if (array[j][i] > 9 and (i, j) not in flashed)]
    for (i, j) in newFlashed:
        for (adjI, adjJ) in getAdjacent(i, j, array):
            if not (adjI, adjJ) in flashed and not (adjI, adjJ) in newFlashed:
                array[adjJ][adjI] += 1
    flashed = flashed + newFlashed
    # if octopuses over 9 energy who haven't flashed yet in the array -> simulate again
    if len([1 for j in range(len(array)) for i in range(len(array[0])) if ((i, j) not in flashed and array[j][i] > 9)]) > 0:
        flashed = simulateFlashes(array, flashed)
    return flashed

def simulateAStep(array):
    flashed = []
    array = increaseEnergyLevel(array)
    flashed = simulateFlashes(array, flashed)
    for (i, j) in flashed:
        array[j][i] = 0
    return (len(flashed)), array

def getPart1(input):
    totalFlashes = 0
    step = 0
    while (step < 100):
        timesFlashed, input = simulateAStep(input)
        totalFlashes += timesFlashed
        step += 1
    return totalFlashes

def getPart2(input):
    fullFlashStep = -1
    step = 1
    while (fullFlashStep == -1):
        timesFlashed, input = simulateAStep(input)
        if timesFlashed == sum([len(row) for row in input]):
            fullFlashStep = step
        step += 1
    return fullFlashStep

with open("Day11.txt") as f:
    input = [[int(c) for c in line.strip()] for line in f.readlines()]
    print(getPart1(input))
    print(getPart2(input))
