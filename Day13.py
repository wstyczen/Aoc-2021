from re import compile, search
def getInput(fileName):
    with open(fileName) as f:
        lines = f.readlines()
        points = [tuple([int(x) for x in line.strip().split(",")]) for line in lines if "," in line]
        pattern = compile("(x|y)=(-??\\d+)")
        foldLines = [[search(pattern, line).group(1), int(search(pattern, line).group(2))] for line in lines if "fold" in line]
        return points, foldLines

def foldAlong(pts, foldLine):
    if foldLine[0] == "x":
        folded = [(pt[0] - 2*(pt[0] - foldLine[1]), pt[1]) for pt in pts if pt[0] > foldLine[1]]
        oldPts = [pt for pt in pts if pt[0] < foldLine[1] and pt not in folded]
    else:
        folded = [(pt[0], pt[1] - 2*(pt[1] - foldLine[1])) for pt in pts if pt[1] > foldLine[1]]
        oldPts = [pt for pt in pts if pt[1] < foldLine[1] and pt not in folded]
    return folded + oldPts

def fold(pts, foldLines):
    for foldLine in foldLines:
        pts = foldAlong(pts, foldLine)
    return pts

def showMessage(pts):
    for y in range(min([pt[1] for pt in pts]), max([pt[1] for pt in pts]) + 1):
        for x in range(min([pt[0] for pt in pts]), max(pt[0] for pt in pts) + 1):
            print("#" if (x, y) in pts else " ", end="")
        print()

points, foldLines = getInput("Input//Day13.txt")
# PART 1
points = foldAlong(points, foldLines[0])
del foldLines[0]
print(len(points))
# PART 2
points = fold(points, foldLines)
showMessage(points)