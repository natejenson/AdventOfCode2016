def getTriangles():
    with open('day3-input.txt', 'r') as file:
        return [[int(side) for side in l.strip().split()] \
                for l in file.readlines()]

def isTriangleBad(sides):
    sides = sorted(sides)
    return sides[0] + sides[1] <= sides[2]

def getNumberGoodTriangles(triangles):
    count = 0
    for triangle in triangles:
        if(not isTriangleBad(triangle)):
            count += 1
    return count



triangles = getTriangles()
print('Part 1 - Number bad triangles:', getNumberGoodTriangles(triangles))
