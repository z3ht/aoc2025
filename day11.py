with open("day11.txt", "r") as f:
    raw = list(f.readlines())
    adj_list = {
        key: tuple(values)
        for line in raw
        for key, *values in [line.strip().replace(":", "").split()]
    }

    def backtrack(target):
        can_reach = {target}
        changed = True
        while changed:
            changed = False
            for key, adj in adj_list.items():
                if key not in can_reach:
                    if any(n in can_reach for n in adj):
                        can_reach.add(key)
                        changed = True
        return can_reach

    fft = backtrack("fft")
    dac = backtrack("dac")
    end = backtrack("out")

    def traverse(cur, goal, valid_set):
        if cur == goal:
            return 1
        score = 0
        for nxt in adj_list[cur]:
            if nxt not in valid_set:
                continue
            score += traverse(nxt, goal, valid_set)
        return score

    svr_fft_score = traverse("svr", "fft", fft)
    print(svr_fft_score)

    fft_dac = dac - fft
    fft_dac_score = traverse("fft", "dac", fft_dac)
    print(fft_dac_score)

    dac_end = end - fft - dac
    dac_end_score = traverse("dac", "out", dac_end)
    print(dac_end_score)

    print(svr_fft_score * fft_dac_score * dac_end_score)