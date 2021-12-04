import re

# P1
with open("Day2.txt") as f:
    line = f.readline()
    x = 0
    y = 0
    pattern = re.compile("\\d+")
    while (line):
        nr = pattern.search(line)
        value = int(nr.group())
        if "forward" in line:
            x += value
        elif "up" in line:
            y -= value
        elif "down" in line:
            y += value
        line = f.readline()
    print(x*y)
# P2
with open("Day2.txt") as f:
    line = f.readline()
    x = 0
    y = 0
    aim = 0
    pattern = re.compile("\\d+")
    while (line):
        nr = pattern.search(line)
        value = int(nr.group())
        if "forward" in line:
            x += value
            y += aim*value
        elif "up" in line:
            aim -= value
        elif "down" in line:
            aim += value
        line = f.readline()
    print(x*y)