from datetime import datetime
from collections import defaultdict
import sys
import numpy as np
from queue import PriorityQueue

def getInput(fileName):
    with open(fileName) as f:
        return np.array([[int(digit) for digit in line.strip()] for line in f.readlines()])

def isWithin(map_, pt):
    return 0 <= pt[0] < len(map_[0]) and 0 <= pt[1] < len(map_)

def getAdjacent(map_, pt):
    (x, y) = pt
    return ((i, j) for (i, j) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y -1)) if isWithin(map_, (i, j)))

def getMaxsize():
    return sys.maxsize

# NOTE TO SELF - FUKEN USE PRIORITY QUEUE WITH DJIKSTRA'S AS A DEFAULT
def djikstraWithPriorityQueue(map_, start, end):
    visited = set()
    distances = defaultdict(getMaxsize)
    distances[start] = 0
    toVisit = PriorityQueue()
    toVisit.put((0, start))
    while not toVisit.empty():
        currentRisk, current = toVisit.get()
        visited.add(current)
        for (x, y) in getAdjacent(map_, current):
            if not (x, y) in visited:
                risk = currentRisk + map_[y][x]
                if risk < distances[(x,y)]:
                    distances[(x,y)] = risk
                    toVisit.put((risk, (x, y)))
    return distances[end]

def getExpandedInput(input):
    expanded = [row.tolist().copy() for row in input]
    for i in range(1, 5):
        addition = [[n + i if n + i <= 9 else ((n+i)%10 + 1) for n in row] for row in input]
        for index, row in enumerate(addition):
            expanded[index] += row
    expandedVertically = [row.copy() for row in expanded]
    for i in range(1, 5):
        expandedVertically += [[n + i if n + i <= 9 else ((n+i)%10 + 1) for n in row] for row in expanded]
    return np.array(expandedVertically)

input = getInput("Input//Day15.txt")

start_time = datetime.now()

start = (0,0)
end = (len(input[0]) - 1, len(input) - 1)
print(djikstraWithPriorityQueue(input, start, end))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

start_time = datetime.now()

expandedInput = getExpandedInput(input)
expandedEnd = (len(expandedInput[0]) - 1, len(expandedInput) - 1)
print(djikstraWithPriorityQueue(expandedInput, start, expandedEnd))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))