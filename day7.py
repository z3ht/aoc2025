from pprint import pprint


cache = {}
def traverse(lines, row, col):
    if (row, col) in cache:
        return cache[(row, col)]
    if row + 1 == len(lines):
        return 1
    if lines[row][col] == "^":
        score = 0
        if col - 1 >= 0:
            score += traverse(lines, row, col - 1)
        if col + 1 < len(lines[row]):
            score += traverse(lines, row, col + 1)
        cache[(row, col)] = score
        return score
    else:
        cache[(row, col)] = traverse(lines, row + 1, col)
        return cache[(row, col)]

ans = 0
with open("day7.txt", "r") as f:
    lines = list(f.readlines())
    lines = [[c for c in line.strip()] for line in lines]
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            val = lines[row][col]
            if val == "S":
                print(traverse(lines, row, col))
                exit(0)
            if val == "|" or val == "S":
                if row + 1 == len(lines):
                    continue
                if lines[row + 1][col] == "^":
                    if col - 1 >= 0:
                        lines[row + 1][col - 1] = "|"
                    if col + 1 < len(lines):
                        lines[row + 1][col + 1] = "|"
                elif lines[row + 1][col] == ".":
                    lines[row + 1][col] = "|"
    pprint(lines)
    score = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            val = lines[row][col]
            if val == "|":
                if row + 1 == len(lines):
                    continue
                if lines[row+1][col] == "^":
                    score += 1
    print(score)
