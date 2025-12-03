
ct = 0
pos = 50
with open("day1.txt", "r") as f:
    for raw in f:
        line = raw.strip()
        if not line:
            continue

        direction = line[0].upper()
        dist = int(line[1:])
        delta = -dist if direction == "L" else dist

        old_pos = pos
        new_pos = old_pos + delta

        if (old_pos < 0 <= new_pos) or (old_pos > 0 >= new_pos):
            ct += 1

        laps_before = abs(old_pos) // 100
        laps_after = abs(new_pos) // 100
        ct += (laps_after - laps_before)

        if new_pos >= 0:
            pos = new_pos % 100
        else:
            pos = -1 * (abs(new_pos) % 100)

    print(ct)
