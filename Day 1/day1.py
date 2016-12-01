def GetDirections():
    with open('day1-input.txt', 'r') as inputFile:
        allText = inputFile.read()
        return allText.split(', ')

def ChangeHeadingOnTurn(startHeading, turn):
    if (turn == 'R'):
        return (startHeading + 1) % 4
    else:
        return (startHeading - 1) % 4

def DistanceBetween(startX, startY, endX, endY):
    return abs(endX - startX) + abs(endY - startY)
    
# Part 1
def MoveToEnd(startX, startY, directions):
    heading = 0 # 0,1,2,3 -> N, E, S, W
    x,y = startX, startY
    for direction in directions:
        turn, distance = direction[0], int(direction[1:])
        heading = ChangeHeadingOnTurn(heading, turn)
        x,y = Move(x, y, heading, distance)
    return x,y

def Move(startX, startY, heading, distance):
    x,y = startX, startY
    if (heading == 0):
        y += distance
    elif (heading == 1):
        x += distance
    elif (heading == 2):
        y -= distance
    elif (heading == 3):
        x -= distance
    return (x,y)

# Part 2
def GetPointsOnPath(startX, startY, heading, distance):
    if (heading == 0):
        return [(startX, step) for step in range(startY+1,startY+distance+1)]
    elif (heading == 1):
        return [(step, startY) for step in range(startX+1,startX+distance+1)]
    elif (heading == 2):
        return [(startX, step) for step in range(startY-1,startY-distance-1,-1)]
    elif (heading == 3):
        return [(step, startY) for step in range(startX-1,startX-distance-1,-1)]

def MoveToFirstDuplicate(startX, startY, direction):
    visited = set()
    visited.add((startX,startY))
    heading = 0
    x,y = startX, startY
    for direction in directions:
        turn, distance = direction[0], int(direction[1:])
        heading = ChangeHeadingOnTurn(heading, turn)
        line = GetPointsOnPath(x,y,heading,distance)
        for point in line:
            if point in visited:
                return point
            visited.add(point)
        # set x,y to the last point on the line we just walked.
        x,y = line[-1][0], line[-1][1]
    return None



directions = GetDirections()

x,y = MoveToEnd(0,0,directions)
print("Part 1 - End point:", str((x,y)))
print("Part 1 - Distance:", DistanceBetween(0,0,x,y))
x2,y2 = MoveToFirstDuplicate(0,0,directions)
print("Part 2 - First Duplicate:", str((x2,y2)))
print("Part 2 - Distance:", DistanceBetween(0,0,x2,y2))
