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

def decode(counts, comparer = max):
    code = ""
    for index in range(len(counts)):
        targetIdx = counts[index].index(comparer(counts[index]))
        code += chr(ord('a') + targetIdx)
    return code

lines = getLines()
counts = count(lines)

print("Part 1 - Decode:", decode(counts))
print("Part 2 - Decode, again:", decode(counts, min))
