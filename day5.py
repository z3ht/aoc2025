ans = 0
good = []

is_good = True
with open("day5.txt", "r") as f:
    for line in f:
        s = line.strip()
        if s == "":
            is_good = False
            continue

        if is_good:
            left, right = s.split("-")
            good.append((int(left), int(right)))
        else:
            good.sort(key=lambda x: x[0])

            merged = [good[0]]
            prev_start, prev_end = merged[-1]

            for curr_start, curr_end in good[1:]:
                if curr_start <= prev_end:
                    merged[-1] = (prev_start, max(prev_end, curr_end))
                    prev_start, prev_end = prev_start, max(prev_end, curr_end)
                else:
                    merged.append((curr_start, curr_end))
                    prev_start, prev_end = curr_start, curr_end
            for left, right in merged:
                ans += right - left + 1
            break

print(ans)
