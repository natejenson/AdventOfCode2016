def getTriangles():
    with open('day3-input.txt', 'r') as file:
        return [[int(side) for side in l.strip().split()] \
                for l in file.readlines()]

def isTriangleBad(sides):
    sides = sorted(sides)
    return sides[0] + sides[1] <= sides[2]

def numGoodTriangles(triangles):
    count = 0
    for triangle in triangles:
        if(not isTriangleBad(triangle)):
            count += 1
    return count

def numGoodTrianglesVertical(triangles):
    count = 0
    for column in range(len(triangles[0])):
        for row in range(0,len(triangles),3):
            if(not isTriangleBad([triangles[row][column],
                    triangles[row+1][column],
                    triangles[row+2][column]])):
                count += 1
    return count


triangles = getTriangles()
print('Part 1 - Number good triangles:', numGoodTriangles(triangles))
print('Part 2 - Number good triangles vertically:', numGoodTrianglesVertical(triangles))
