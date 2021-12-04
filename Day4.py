from itertools import repeat
from re import compile, findall

boards = {}
queue = []
with open("Day4.txt", 'r') as f:
    drawn = f.readline()
    pattern = compile("\\d+")
    queue = [int(nr) for nr in findall(pattern, drawn)]

    board = []
    line = f.readline()
    while line:
        if (line.isspace()):
            if len(board) > 0:
                boards[tuple(board)] = [[0]*len(row) for row in board]
                board = []
        else:
            row = tuple([int(nr) for nr in findall(pattern, line)])
            board.append(row)
        line = f.readline()
        if (not line):
            boards[tuple(board)] = [[0]*len(row) for row in board]

def checkIfWon(value):
    won = False
    for i in range(len(value)):
        if sum(value[i]) == len(value[0]):
            won = True
            break
    if not won:
        for j in range(len(value[0])):
            if sum([row[j] for row in value]) == len(value):
                won = True
                break
    return won

def getSumOfUnmarked(key, value):
    won = checkIfWon(value)
    if not won:
        return -1
    sumOfUnmarked = 0
    for rowIndex, row in enumerate(key):
        sumOfUnmarked += sum([nr for index, nr in enumerate(row) if value[rowIndex][index] == 0])
    return sumOfUnmarked

def part1(queue, boards):
    for drawnNr in queue:
        for key, value in boards.items():
            # finds indices of all occurences of 'drawnNr' in key
            positions = [(index, row.index(drawnNr)) for index, row in enumerate(key) if drawnNr in row]
            for (i, j) in positions:
                value[i][j] = 1
            if checkIfWon(value):
                result = getSumOfUnmarked(key, value)*drawnNr
                return result


def part2(queue, boards):
    for drawnNr in queue:
        won = []
        for key, value in boards.items():
            # finds indices of all occurences of 'drawnNr' in key
            positions = [(index, row.index(drawnNr)) for index, row in enumerate(key) if drawnNr in row]
            for (i, j) in positions:
                value[i][j] = 1
            if checkIfWon(value):
                won.append(key)

        for key in won:
            if (len(boards) == 1):
                return getSumOfUnmarked(key, value)*drawnNr
            boards.pop(key)

print(part1(queue, boards))
print(part2(queue, boards))