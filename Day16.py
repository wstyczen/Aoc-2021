from math import prod

class Packet:
    totalVersion = 0
    def __init__(self ,version, id, literal=None, subPackets = []):
        self.version = version
        self.id = id
        self.literal = literal
        self.subPackets = subPackets
        type(self).totalVersion += version

    def getValue(self):
        match self.id:
            case 0:
                return sum([sub.getValue() for sub in self.subPackets])
            case 1:
                return prod([sub.getValue() for sub in self.subPackets])
            case 2:
                return min([sub.getValue() for sub in self.subPackets])
            case 3:
                return max([sub.getValue() for sub in self.subPackets])
            case 4:
                return self.literal
            case 5:
                return 1 if self.subPackets[0].getValue() > self.subPackets[1].getValue() else 0
            case 6:
                return 1 if self.subPackets[0].getValue() < self.subPackets[1].getValue() else 0
            case 7:
                return 1 if self.subPackets[0].getValue() == self.subPackets[1].getValue() else 0


def readAPacket(bitString, index=0):
    (version, id) = (int(bitString[index:index+3], 2), int(bitString[index+3:index+6], 2))
    index += 6
    if id == 4: # literal value
        value = ""
        group = bitString[index:index+5]
        while int(group[0]):
            value += group[1:]
            index += 5
            group = bitString[index:index+5]
        value += group[1:]
        index += 5
        literalValue = int(value, 2)
        return Packet(version, id, literalValue), index
    else: # operator
        lengthTypeId = int(bitString[index], 2)
        index += 1
        if lengthTypeId == 0:
            totalLength = int(bitString[index:index + 15], 2)
            index += 15
            startIndex = index
            subPackets = []
            while index < startIndex + totalLength:
                subPacket, index = readAPacket(bitString, index)
                subPackets.append(subPacket)
            return Packet(version, id, None, subPackets), index
        if lengthTypeId == 1: #
            nrOfSubPackets = int(bitString[index:index+11], 2)
            index += 11
            subPackets = []
            while len(subPackets) < nrOfSubPackets:
                packet, index = readAPacket(bitString, index)
                subPackets.append(packet)
            return Packet(version, id, None, subPackets), index

def getBitString(hexString):
    return str(bin(int(hexString, 16)))[2:].zfill(len(hexString)*4)

with open("Input//Day16.txt") as f:
    input = f.readline().strip()

packet, index = readAPacket(getBitString(input))
#P1
print(Packet.totalVersion)
#P2
print(packet.getValue())