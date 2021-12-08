from re import compile, findall

def getDictFish(fish):
    dict = {}
    for i in range(9):
        dict[i] = 0
    for aFish in fish:
        dict[aFish] += 1
    return dict

def getFishAfter(fish, days):
    dictFish = getDictFish(fish)
    day = 0
    while day < days:
        new = dictFish[0]
        for i in range(8):
            dictFish[i] = dictFish[i + 1]
        dictFish[8] = new
        dictFish[6] += new
        day += 1
    return sum(dictFish.values())

with open("Day6.txt") as f:
    pattern = compile("\\d+")
    fish = [int(fish) for fish in findall(pattern, f.readline())]
    print(getFishAfter(fish, 256))