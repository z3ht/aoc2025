from collections import defaultdict


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py
            return True
        return False


with open("day8.txt", "r") as f:
    conns = 1000

    lines = list(f.readlines())
    points = [tuple(int(c) for c in line.strip().split(",")) for line in lines]

    edges = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i < j:
                dist = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2) ** 0.5
                edges.append((dist, i, j))
    edges = sorted(edges)

    dsu = DSU(len(points))
    ct = 0
    for ct, (dist, i, j) in enumerate(edges):
        dsu.union(i, j)
        print(f"{points[i][0]} {points[j][0]} = {points[i][0] * points[j][0]}")

        num = None
        for p in range(len(points)):
            r = dsu.find(p)
            if num is None:
                num = r
            if num != r:
                break
        else:
            exit()

    rs = defaultdict(int)
    for i in range(len(points)):
        r = dsu.find(i)
        rs[r] = rs[r] + 1
    rs = sorted(rs.values(), reverse=True)
    print(f"{rs[0]} {rs[1]} {rs[2]} = {rs[0] * rs[1] * rs[2]}")
