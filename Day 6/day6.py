def getLines():
    with open('day6-input.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

def count(lines):
    counts = [[0 for letter in range(26)] for index in range(len(lines[0]))]
    for line in lines:
        for i in range(len(line)):
            cIdx = ord(line[i]) - ord('a')
            counts[i][cIdx] += 1

    return counts

def decode(counts):
    code = ""
    for index in range(len(counts)):
        maxIdx = counts[index].index(max(counts[index]))
        code += chr(ord('a') + maxIdx)
    return code

lines = getLines()
counts = count(lines)

print("Part 1 - Decode:", decode(counts))
