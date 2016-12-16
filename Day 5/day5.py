import hashlib

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


doorId = "uqwqemis"
password = GetPasswordForDoor(doorId)
print('Part 1 - Door Password:', password)
