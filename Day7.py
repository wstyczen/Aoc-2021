from re import compile, findall

def getCostOfMove(distance):
    return sum(range(1, distance + 1))

def getCheapestPosition(positions):
    minCost = 10**9
    minPosition = -1
    for i in range(min(positions), max(positions) + 1):
        fuelCost = 0
        for pos in positions:
            # PART 1
            # fuelCost += abs(pos - i)
            # PART 2
            fuelCost += getCostOfMove(abs(pos - i))
        if fuelCost < minCost:
            minPosition = i
            minCost = fuelCost
    return minPosition, minCost

with open("Day7.txt") as f:
    pattern = compile("-??\\d+")
    positions = [int(nr) for nr in findall(pattern, f.readline())]
    pos, cost = getCheapestPosition(positions)
    print("Move to " + str(pos) + " for " + str(cost) + " fuel.")