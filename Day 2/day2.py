class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Keypad:
    def __init__(self, numbers):
        self.numbers = numbers

    def Number(self, pos):
        return self.numbers[pos.y][pos.x]

    def Move(self, startPos, direction):
        newPos = Position(startPos.x, startPos.y)
        if (direction == "U"):
            newPos.y -= 1
        elif (direction == "D"):
            newPos.y += 1
        elif (direction == "L"):
            newPos.x -= 1
        elif (direction == "R"):
            newPos.x += 1
        else:
            raise "invalid direction: " + str(direction)

        if ((newPos.x < 0 or newPos.x > len(self.numbers[0]) - 1)
            or newPos.y < 0 or newPos.y > len(self.numbers)-1):
            return startPos

        if (self.Number(newPos) == None):
            return startPos

        return newPos

def getCode(keypad, startPos, directions):
    pos = startPos
    code = ""
    for directionSet in directions:
        for direction in directionSet:
            pos = keypad.Move(pos, direction)
        code += str(keypad.Number(pos))
    return code

def getDirections():
    dirs = []
    with open('day2-input.txt', 'r') as file:
        return file.read().splitlines()

pos = Position(1,1)
keypad = Keypad([[1,2,3],[4,5,6],[7,8,9]])
directions = getDirections()

print("Part 1 - Code: ", getCode(keypad, pos, directions))

keypad = Keypad([[None, None, 1, None, None],
                 [None, 2, 3, 4, None],
                 [5,6,7,8,9],
                 [None, "A", "B", "C", None],
                 [None, None, "D", None, None]])

print("Part 2 - Code: ", getCode(keypad, pos, directions))
