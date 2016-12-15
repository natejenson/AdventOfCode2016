from collections import defaultdict

class Room:
    def __init__(self, inputStr):
        lastDashIdx = inputStr.rindex('-')
        firstBracketIdx = inputStr.index('[')
        self.encryptedName = inputStr[:lastDashIdx]
        self.sectorId = int(inputStr[lastDashIdx+1:firstBracketIdx])
        self.checksum = inputStr[firstBracketIdx+1:-1]
        
    def isReal(self):
        occurences = defaultdict(int)
        letters = self.encryptedName.replace('-','')
        for letter in letters:
            occurences[letter] = occurences[letter] + 1
        occurences = sorted(occurences.items(), key=lambda x: (-x[1],x[0]))

        realChecksum = ""
        for i in range(5):
            realChecksum += occurences[i][0]
        return realChecksum == self.checksum

def GetRooms():
    with open('day4-input.txt', 'r') as f:
        return [Room(line.strip()) for line in f.readlines()]


rooms = GetRooms()
sumRealRooms = sum(r.sectorId for r in rooms if r.isReal())
print('Part 1 - Sum of sector IDs of real rooms:', sumRealRooms)


    
