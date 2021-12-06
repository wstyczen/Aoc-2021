from re import compile, findall

def tick(fish):
    fish = [aFish - 1 for aFish in fish]
    new = fish.count(-1)
    fish = [6 if aFish == -1 else aFish for aFish in fish]
    for i in range(new):
        fish.append(8)
    return fish

def part1(fish, days):
    day = 0
    while day < days:
        fish = tick(fish)
        day += 1
    return len(fish)

def getDictFish(fish):
    dict = {}
    for i in range(9):
        dict[i] = 0
    for aFish in fish:
        dict[aFish] += 1
    return dict

def part2(fish, days):
    dictFish = getDictFish(fish)
    day = 0
    while day < days:
        new = dictFish[0]
        for i in range(8):
            dictFish[i] = dictFish[i + 1]
        dictFish[8] = new
        dictFish[6] += new
        day += 1
    print(dictFish)
    return sum(dictFish.values())

with open("Day6.txt") as f:
    pattern = compile("\\d+")
    fish = [int(fish) for fish in findall(pattern, f.readline())]
    print(part2(fish, 256))
    # print(fish)
