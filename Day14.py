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

def getOccurences(pairs, template):
    occurences = defaultdict(int)
    occurences[template[0]] += 1 # start character
    occurences[template[-1]] += 1 # end character
    for pair, pairOccurences in pairs.items():
        for letter in pair:
            occurences[letter] += pairOccurences
    return {pair:int(occ/2) for pair, occ in occurences.items()}

def getResult(pairs, modifiedInsertionRules, template, times = 10):
    pairs = processPolymer(pairs, modifiedInsertionRules, times)
    occurences = getOccurences(pairs, template)
    return max(occurences.values()) - min(occurences.values())

with open("Input//Day14.txt") as f:
    template = f.readline().strip()
    f.readline()
    splitRule = lambda rule : rule.strip().split(" -> ")
    basicInsertionRules = {splitRule(line)[0]:splitRule(line)[1] for line in f.readlines()}

    # since the order does not seem to matter I am just going to keep track of each pair separately
    modifiedInsertionRules = defaultdict(list)
    for pair, inserted in basicInsertionRules.items():
        modifiedInsertionRules[pair].append(pair[0] + inserted)
        modifiedInsertionRules[pair].append(inserted + pair[1])
    pairs = getPairs(template)

    # PART 1
    print(getResult(pairs, modifiedInsertionRules, template))
    # PART 2
    print(getResult(pairs, modifiedInsertionRules, template, 40))