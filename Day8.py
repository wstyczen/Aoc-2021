# P1
with open("Day8.txt") as f:
    output = [line.split(" | ")[1].strip().split(" ") for line in f.readlines()]
    print(len([group for groups in output for group in groups if len(group) in [2, 3, 4, 7]]))

from enum import Enum
from re import S
# P2
class Segment(Enum):
    UP = 1
    RIGHT_UP = 2
    LEFT_UP = 3
    MIDDLE = 4
    RIGHT_DOWN = 5
    LEFT_DOWN = 6
    DOWN = 7
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

digits = {
(Segment.UP, Segment.RIGHT_UP ,Segment.LEFT_UP, Segment.RIGHT_DOWN, Segment.LEFT_DOWN, Segment.DOWN):0,
(Segment.RIGHT_UP, Segment.RIGHT_DOWN):1,
(Segment.UP, Segment.RIGHT_UP, Segment.MIDDLE, Segment.LEFT_DOWN, Segment.DOWN):2,
(Segment.UP, Segment.RIGHT_UP, Segment.MIDDLE, Segment.RIGHT_DOWN, Segment.DOWN):3,
(Segment.RIGHT_UP, Segment.LEFT_UP, Segment.MIDDLE, Segment.RIGHT_DOWN):4,
(Segment.UP, Segment.LEFT_UP, Segment.MIDDLE, Segment.RIGHT_DOWN, Segment.DOWN):5,
(Segment.UP, Segment.LEFT_UP, Segment.MIDDLE, Segment.RIGHT_DOWN, Segment.LEFT_DOWN, Segment.DOWN):6,
(Segment.UP, Segment.RIGHT_UP, Segment.RIGHT_DOWN):7,
(Segment.UP, Segment.RIGHT_UP ,Segment.LEFT_UP, Segment.MIDDLE, Segment.RIGHT_DOWN, Segment.LEFT_DOWN, Segment.DOWN):8,
(Segment.UP, Segment.RIGHT_UP ,Segment.LEFT_UP, Segment.MIDDLE, Segment.RIGHT_DOWN, Segment.DOWN):9
}

def findCombination(input):
    combination = {}
    fiveSegmentDigits = []
    sixSegmentDigits = []
    for nr in input:
        if len(nr) == 2:
            # in digit one there are segments RIGHT_UP, RIGHT_DOWN
            one = nr
        elif len(nr) == 3:
            # in digit seven there are segments RIGHT_UP, RIGHT_DOWN, UP
            seven = nr
        elif len(nr) == 4:
            # four contains segments RIGHT_UP, RIGHT_DOWN, MIDDLE, LEFT_UP
            four = nr
        elif len(nr) == 5:
            fiveSegmentDigits.append(nr)
        elif(len(nr) == 6):
            sixSegmentDigits.append(nr)
        elif(len(nr) == 7):
            unmapped = [c for c in nr]
    # up is the segment that occures in seven but not in one
    up = [c for c in seven if c not in one][0]
    combination[up] = Segment.UP
    unmapped.remove(up)
    # in sixSegmentDigits there are 2 occurences of segment RIGHT_UP, 3 of RIGHT_DOWN
    if (len([nr for nr in sixSegmentDigits if one[0] in nr]) == 2):
        # then the first char is RIGHT_UP, second RIGHT_DOWN
        combination[one[0]] = Segment.RIGHT_UP
        combination[one[1]] = Segment.RIGHT_DOWN
    else:
        # the opposite
        combination[one[1]] = Segment.RIGHT_UP
        combination[one[0]] = Segment.RIGHT_DOWN
    unmapped = [el for el in unmapped if el not in one]
    LEFT_UPandMIDDLE = [c for c in four if not c in one]
    # LEFT_UP occures once in fiveSegmentDigits, MIDDLE thrice
    if (len([nr for nr in fiveSegmentDigits if LEFT_UPandMIDDLE[0] in nr]) == 1):
        # then the first element is LEFT_UP, second MIDDLE
        combination[LEFT_UPandMIDDLE[0]] = Segment.LEFT_UP
        combination[LEFT_UPandMIDDLE[1]] = Segment.MIDDLE
    else:
        # the opposite
        combination[LEFT_UPandMIDDLE[1]] = Segment.LEFT_UP
        combination[LEFT_UPandMIDDLE[0]] = Segment.MIDDLE
    unmapped = [el for el in unmapped if el not in LEFT_UPandMIDDLE]
    # at this point all that is left unmapped is LEFT_DOWN and DOWN
    # left down occurs once in fiveSegmentDigits, down thrice
    if (len([nr for nr in fiveSegmentDigits if unmapped[0] in nr]) == 1):
        # then the first element in unmapped is LEFT_DOWN, second DOWN
        combination[unmapped[0]] = Segment.LEFT_DOWN
        combination[unmapped[1]] = Segment.DOWN
    else:
        # the opposite
        combination[unmapped[1]] = Segment.LEFT_DOWN
        combination[unmapped[0]] = Segment.DOWN
    return combination

def processStringToDigit(string, comb):
    segments = tuple(sorted([comb[c] for c in string]))
    return digits[segments]

def getSumOfOutput(input, output):
    comb = findCombination(input)
    outputValue = ""
    for nr in output:
        outputValue += str(processStringToDigit(nr, comb))
    return int(outputValue)

with open("Day8.txt") as f:
    line = f.readline()
    total = 0
    while line:
        input = line.strip().split(" | ")[0].split(" ")
        output = line.strip().split(" | ")[1].split(" ")
        total += getSumOfOutput(input, output)
        line = f.readline()
    print(total)