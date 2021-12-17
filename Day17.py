from re import search
class TargetArea:
    def __init__(self, input):
        self.xBounds, self.yBounds = self.parseInput(input)

    def parseInput(self, input):
        matches = search("(-??\\d+..-??\\d+).*?(-??\\d+..-??\\d+)", input)
        getBounds = lambda i : tuple([int(nr) for nr in matches.group(i).split("..")])
        return getBounds(1), getBounds(2)

class Probe:
    targetArea = []
    def __init__(self, velocity=(0, 0), pos=(0, 0)):
        self.pos = pos
        self.velocity = velocity

    def move(self):
        (x, y) = self.pos
        (velX, velY) = self.velocity
        self.pos = (x + velX, y + velY)
        self.velocity = (velX if velX == 0 else (velX - 1 if velX > 0 else velX + 1), velY - 1)

    def isWithinTargetArea(self):
        return self.targetArea.xBounds[0] <= self.pos[0] <= self.targetArea.xBounds[1] \
            and self.targetArea.yBounds[0] <= self.pos[1] <= self.targetArea.yBounds[1]

    def endsUpInTargetArea(self):
        # if the probe falls below the lower bound of the target area and it's going down,
        # it's y velocity won't change - it will just continue going further down, away from the target
        while (self.velocity[1] > 0 or self.pos[1] >= self.targetArea.yBounds[0]):
            if self.isWithinTargetArea(): return True
            self.move()
        return False

    def getHeightReached(self, vy, initialHeight=0):
        # the probe is shot upwards with a velocity that decrements by one each tick, the target area is below the starting position
        # so the final height reached by a successful sonde will be a sum of elements of the following range:
        return sum(range(vy + 1)) if vy > 0 else 0

    def getPart1(self):
        maxY = 0
        bestVel = (0, 0)
        for vx in range(6, 50):
            for vy in range(5, 150):
                self.velocity = (vx, vy)
                scored = self.endsUpInTargetArea()
                if scored:
                    heightReached = self.getHeightReached(vy)
                    if heightReached > maxY:
                        maxY = heightReached
                        bestVel = (vx, vy)
                self.pos = (0, 0)
        return bestVel, maxY

    def getPart2(self):
        self.pos = (0, 0)
        viableVelocitiesCount = 0
        for vx in range(0, 300):
            for vy in range(-105, 150):
                self.velocity = (vx, vy)
                if self.endsUpInTargetArea():
                    viableVelocitiesCount += 1
                self.pos = (0, 0)
        return viableVelocitiesCount

input = "target area: x=265..287, y=-103..-58"
# input = "target area: x=20..30, y=-10..-5"
Probe.targetArea = TargetArea(input)
# P 1
probe = Probe()
bestVel, highest = probe.getPart1()
print(highest)
# P 2
successfulProbes = probe.getPart2()
print(successfulProbes)
