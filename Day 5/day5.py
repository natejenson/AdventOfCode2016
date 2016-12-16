import hashlib
import time
    
def GetPasswordForDoor(doorId):
    password = ""
    i = 0
    while (len(password) < 8):
        m = hashlib.md5((doorId + str(i)).encode('utf-8'))
        hashed = m.hexdigest()
        if(hashed[:5] == "00000"):
            password += hashed[5]
        i = i + 1
    return password

def GetPasswordForDoorTwo(doorId):
    password = [None for i in range(8)]
    foundChars = 0
    i = 0
    while (foundChars < len(password)):
        m = hashlib.md5((doorId + str(i)).encode('utf-8'))
        hashed = m.hexdigest()
        if(hashed[:5] == "00000"):
            position = ord(hashed[5]) - ord('0')
            newChar = hashed[6]
            if (position < len(password) and password[position] == None):
                password[position] = newChar
                foundChars += 1
        i = i + 1
    return password


doorId = "uqwqemis"

start_time = time.clock()
password = GetPasswordForDoor(doorId)
print('Part 1 - Door Password:', password)
print('Part 1 - %.3f seconds' % (time.clock() - start_time))

start_time = time.clock()
password = GetPasswordForDoorTwo(doorId)
print('Part 2 - Door Password:', password)
print('Part 2 - %.3f seconds' % (time.clock() - start_time))
