from collections import deque

# P 1
p1ScoreTable = {')':3, ']':57, '}':1197, '>':25137}
parenthesisPairs = {'(':')', '[':']', '{':'}', '<':'>'}

def processLine(line):
    open = deque()
    firstIllegal = None
    for par in line:
        # if opening parenthesis
        if par not in p1ScoreTable.keys():
            open.append(par)
        # if closing parenthesis
        else:
            lastOpen = open.pop()
            # if different then the opened one - found corrupted
            if (parenthesisPairs[lastOpen] != par):
                firstIllegal = par
                break
    if firstIllegal is None:
        return 0
    return p1ScoreTable[firstIllegal]

# P 2
p2ScoreTable = {')':1, ']':2, '}':3, '>':4}
def completeALine(line):
    totalScore = 0
    open = deque()
    for par in line:
        # if opening parenthesis
        if par not in p2ScoreTable.keys():
            open.append(par)
        # if closing parenthesis
        else:
            open.pop()

    while len(open) > 0:
        totalScore = totalScore*5 + p2ScoreTable[parenthesisPairs[open.pop()]]
    return totalScore


with open("Day10.txt") as f:
    # P 1
    lines = f.readlines()
    part1 = sum([processLine(line.strip()) for line in lines])
    print(part1)
    # P 2
    uncorruptedLines = [line.strip() for line in lines if processLine(line.strip()) == 0]
    totalScores = sorted([completeALine(line) for line in uncorruptedLines])
    part2 = totalScores[int((len(totalScores) - 1)/2)]
    print(part2)