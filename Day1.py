# Day1
with open('Day1.txt', 'r') as f:
    timesIncreased = 0
    lines = f.readlines()
    previous = int(lines[0])
    for line in lines:
        current = int(line)
        if current > previous:
            timesIncreased += 1
        previous = current
        line = f.readline()
    print(timesIncreased)

# Day2
with open('Day1.txt', 'r') as f:
    lines = f.readlines()
    windowIncreased = 0
    count = 0
    window = [0, 0, 0]
    previousWindowSum = 0
    for line in lines:
        window[count % 3] = int(line)
        count += 1
        if count < 3:
            continue
        newWindowSum = sum(window)
        if (previousWindowSum > 0 and newWindowSum > previousWindowSum):
            windowIncreased += 1
        previousWindowSum = newWindowSum
print(windowIncreased)