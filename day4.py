
ans = 0
with open("day4.txt", "r") as f:
    rlines = list(f.readlines())
    lines = []
    for line in rlines:
        lines.append([c for c in line.strip()])

    has_changes = True
    while has_changes:
        has_changes = False
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                if lines[row][col] != "@":
                    continue
                dirs = [
                    (1, 0),
                    (1, 1),
                    (0, 1),
                    (-1, 1),
                    (-1, 0),
                    (-1, -1),
                    (0, -1),
                    (1, -1)
                ]
                ct = 0
                for dir in dirs:
                    try:
                        r = row +dir[0]
                        c = col + dir[1]
                        if r < 0 or c < 0:
                            continue
                        if (lines[r][c] == "@"):
                            ct += 1
                    except:
                        continue
                if (ct < 4):
                    ans += 1
                    lines[row][col] = "."
                    has_changes = True

print(ans)
