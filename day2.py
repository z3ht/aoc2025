ct = 0
with open("day2.txt", "r") as f:
    for line in f.readlines():
        for seq in line.strip().split(","):
            if len(seq) < 2:
                continue
            parts = seq.strip().split("-")
            start = int(parts[0])
            end = int(parts[1])
            for raw_cur in range(start, end + 1):
                cur = str(raw_cur)
                if cur[0] == '0':
                    continue
                for i in range(1, len(cur)):
                    if cur == cur[:i] * (len(cur) // i):
                        ct += raw_cur
                        break

print(ct)
