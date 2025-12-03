num_jolts = 12

with open("day3.txt", "r") as f:
    total = 0
    for raw_line in f.readlines():
        line = raw_line.strip()
        num = 0
        start_ind = 0
        for jolt_ind in range(num_jolts, 0, -1):
            max_ind = 0
            max_num = 0
            for i in range(start_ind, len(line) - jolt_ind + 1):
                if int(line[i]) > max_num:
                    max_num = int(line[i])
                    max_ind = i
            start_ind = max_ind + 1
            num += max_num * (10 ** (jolt_ind - 1))
        print(num)
        total += num
    print(total)
