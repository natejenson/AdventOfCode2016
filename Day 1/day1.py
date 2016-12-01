def GetDirections():
    with open('day1-input.txt', 'r') as inputFile:
        allText = inputFile.read()
        return allText.split(', ')

def ChangeHeadingOnTurn(startHeading, turn):
    if (turn == 'R'):
        return (startHeading + 1) % 4
    else:
        return (startHeading - 1) % 4

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

def DistanceBetween(startX, startY, endX, endY):
    return abs(endX - startX) + abs(endY - startY)

directions = GetDirections()

(x,y) = MoveToEnd(0,0,directions)
print("Part 1 end point: " + str(x) + "," + str(y))
print("Part 1 distance:", DistanceBetween(0,0,x,y))
