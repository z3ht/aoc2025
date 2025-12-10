from pprint import pprint


def calc_bounds(y, vs):
    active_xs = [x for x, y_min, y_max in vs if y_min <= y <= y_max]
    return min(active_xs), max(active_xs)


with open("day9.txt", "r") as f:
    raw = list(f.readlines())
    points = [tuple(int(c) for c in line.strip().split(",")) for line in raw]

    h_lines = []
    v_lines = []
    for pi in range(len(points)):
        p1 = points[pi]
        p2 = points[(pi + 1) % len(points)]

        if p1[1] == p2[1]:
            h_lines.append((p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])))
        else:
            v_lines.append((p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])))
    h_lines = sorted(h_lines, key=lambda x: x[0])
    v_lines = sorted(v_lines, key=lambda x: x[0])
    pprint((h_lines, v_lines))

    max_area = 0
    for i, (y1, x_min1, x_max1) in enumerate(h_lines):
        the_left, the_right = calc_bounds(y1, v_lines)
        for j in range(i, len(h_lines)):
            y2, x_min2, x_max2 = h_lines[j]

            cur_left, cur_right = calc_bounds(y2, v_lines)
            the_left = max(the_left, cur_left)
            the_right = min(the_right, cur_right)
            if the_left > the_right:
                break


            def area(x1, x2):
                x_min, x_max = min(x1, x2), max(x1, x2)
                if the_left <= x_min and x_max <= the_right:
                    length = x_max - x_min + 1
                    height = y2 - y1 + 1
                    return length * height
                return 0

            max_area = max(
                max_area,
                area(x_min1, x_min2),
                area(x_min1, x_max2),
                area(x_max1, x_min2),
                area(x_max1, x_max2)
            )

    print(max_area)
