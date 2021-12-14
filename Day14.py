from collections import defaultdict

def getPairs(template):
    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pairs[template[i:i+2]] += 1
    return pairs

def processPolymer(pairs, modifiedInsertionRules, times = 10):
    for i in range(times):
        newPairs = defaultdict(int)
        for pair, occurences in pairs.items():
            for product in modifiedInsertionRules[pair]:
                newPairs[product] += occurences
        pairs = newPairs
    return pairs

def getPolymerLength(pairs):
    return int(sum(pairs.values()) + 1)

def getOccurences(pairs):
    occurences = defaultdict(int)
    occurences['N'] += 1
    occurences['B'] += 1
    for pair, pairOccurences in pairs.items():
        for letter in pair:
            occurences[letter] += pairOccurences
    return {pair:int(occ/2) for pair, occ in occurences.items()}

def getResult(pairs, modifiedInsertionRules, times = 10):
    pairs = processPolymer(pairs, modifiedInsertionRules, times)
    occurences = getOccurences(pairs)
    # print("H: " + str(occurences["H"]))
    # print("B: " + str(occurences["B"]))
    # print("Result: ", end="")
    return max(occurences.values()) - min(occurences.values())

with open("Input//Day14.txt") as f:
    template = f.readline().strip()
    f.readline()
    splitRule = lambda rule : rule.strip().split(" -> ")
    basicInsertionRules = {splitRule(line)[0]:splitRule(line)[1] for line in f.readlines()}

    # since the order does not seem to matter I am just going to keep track of how many certain pairs there are
    modifiedInsertionRules = defaultdict(list)
    for pair, inserted in basicInsertionRules.items():
        modifiedInsertionRules[pair].append(pair[0] + inserted)
        modifiedInsertionRules[pair].append(inserted + pair[1])
    pairs = getPairs(template)

    # PART 1
    print(getResult(pairs, modifiedInsertionRules))
    # PART 2
    print(getResult(pairs, modifiedInsertionRules, 40))