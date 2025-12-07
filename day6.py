from curses.ascii import isdigit

ans = 0
with open("day6.txt", "r") as f:
    lines = list(f.readlines())
    lines = [line for line in lines]
    # for row in range(len(lines)):
    #     for col in range(len(lines[row])):
    #         val = lines[row][col]
    #         pass
    divs = []
    ct = 0
    for v in lines[-1]:
        if v == " " or v == "\n":
            ct += 1
        else:
            divs.append(ct)
            ct += 1
    max_len = 0
    for line in lines:
        max_len = max(max_len, len(line))
    divs.append(max_len + 1)
    print(divs)
    nums = []
    for line in lines:
        parts = []
        for j in range(1, len(divs)):
            parts.append(line[divs[j - 1]:divs[j] - 1].replace("\n", ""))
        nums.append(parts)
    print(nums)

    for col in range(len(nums[0])):
        new = []
        for row in range(len(nums)):
            v = nums[row][col].strip()
            if v != "+" and v != "*":
                new.append(nums[row][col])
            else:
                max_len = 0
                for num in new:
                    max_len = max(max_len, len(str(num)))

                cur = []
                for j in range(max_len):
                    c = 0
                    for num in new:
                        num = str(num)
                        if j < len(num) and num[j] != " ":
                            c *= 10
                            c += int(num[j])
                    cur.append(c)

                print(cur)

                res = cur[0]
                for j in range(1, len(cur)):
                    if v == "+":
                        res += cur[j]
                    elif v == "*":
                        res *= cur[j]
                ans += res
                print(res)

print(ans)
