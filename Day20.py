import numpy as np
from time import time

def readInput(fileName):
    with open(fileName) as f:
        algorithm = np.array([1 if c == '#' else 0 for c in f.readline().strip()])
        image = np.array([[1 if c == '#' else 0 for c in line.strip()] for line in f.readlines() if not line.isspace()])
    return algorithm, image

def getValue(algorithm, IEAS):
    binaryString = ""
    for row in IEAS:
        for c in row:
            binaryString += "1" if c == 1 else "0"
    return algorithm[int(binaryString, 2)]

def resize(image, size):
    newImage = np.zeros((size, size))
    offset = int((size - len(image))/2)
    newImage[offset:-offset, offset:-offset] = image
    return newImage

def enhance(image, algorithm, nrOfTimes=1):
    enhanced = 0
    image = resize(image, 300)
    while enhanced < nrOfTimes:
        enhanced += 1
        newImage = np.copy(image)
        for i in range(1, len(image) - 1):
            for j in range(1, len(image[0]) - 1):
                newImage[i, j] = getValue(algorithm, image[i-1:i+2, j-1:j+2])
        image = newImage
    image = image[50:-50, 50:-50]
    return np.count_nonzero(image == 1)

algorithm, image = readInput("Input//Day20.txt")
start_time = time()
print(enhance(image, algorithm, nrOfTimes=50))
print("Time of execution: %ss" % (time() - start_time))
