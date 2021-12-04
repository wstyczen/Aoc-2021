def getMoreCommonBit(bitStrings, bitIndex, getOpposite = False):
    oneCount = 0
    for index in range(len(bitStrings)):
            if bitStrings[index][bitIndex] == "1":
                oneCount += 1
    bits = ["0", "1"]
    moreCommon = "0"
    lessCommon = "1"
    if oneCount >= len(bitStrings)/2:
        moreCommon = "1"
        lessCommon = "0"
    if (not getOpposite):
        return moreCommon
    return lessCommon

# P1
with open("Day3.txt") as f:
    lines = f.readlines()
    bitNrs = [line.strip() for line in lines]
    gammaRate = ''
    epsilonRate = ''
    for bitIndex in range(len(bitNrs[0])):
        gammaRate += getMoreCommonBit(bitNrs, bitIndex)
        epsilonRate += getMoreCommonBit(bitNrs, bitIndex, True)

    result = int(gammaRate, 2) * int(epsilonRate, 2)
    print(result)

# P2


with open("Day3.txt") as f:
    lines = f.readlines()
    OGRnrs = [line.strip() for line in lines]
    CO2nrs = [line.strip() for line in lines]
    for bitIndex in range(len(OGRnrs[0])):
        # OGR
        if len(OGRnrs) > 1:
            bitRequiredOGR = getMoreCommonBit(OGRnrs, bitIndex)
            OGRnrs = [nr for nr in OGRnrs if nr[bitIndex] == bitRequiredOGR]
        # CO2
        if len(CO2nrs) > 1:
            bitRequiredCO2 = getMoreCommonBit(CO2nrs, bitIndex, True)
            CO2nrs = [nr for nr in CO2nrs if nr[bitIndex] == bitRequiredCO2]

    OGR = OGRnrs[0]
    CO2 = CO2nrs[0]

    print("OGR = " + OGR + " | " + str(int(OGR, 2)))
    print("CO2 SR = " + CO2 + " | " + str(int(CO2, 2)))
    print("Result: " + str(int(OGR, 2)*int(CO2, 2)))
