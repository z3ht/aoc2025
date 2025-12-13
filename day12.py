from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from pprint import pprint

from ortools.sat.python.cp_model import CpSolver, OPTIMAL, FEASIBLE, CpModel


@dataclass
class Grid:
    presents: list[int]
    cols: int
    rows: int


def can_fit(grid, shapes):
    model = CpModel()

    present_to_vars = defaultdict(list)
    cord_to_vars = defaultdict(list)

    for present_id, req_presents in enumerate(grid.presents):
        for rot_id, rotation in enumerate(shapes[present_id]):
            for r in range(grid.rows):
                for c in range(grid.cols):
                    rot_var = model.NewBoolVar(f'x_{present_id}_{rot_id}_{r}_{c}')
                    present_to_vars[present_id].append(rot_var)
                    for rr, rc in rotation:
                        cord_to_vars[(r + rr, c + rc)].append(rot_var)

    for present_id, req_presents in enumerate(grid.presents):
        model.Add(sum(present_to_vars[present_id]) >= req_presents)

    for vars in cord_to_vars.values():
        model.Add(sum(vars) <= 1)

    solver = CpSolver()
    return solver.Solve(model) in (OPTIMAL, FEASIBLE)


def go(args):
    i, all, grid, shapes = args
    print(f"{i}/{all}")
    return can_fit(grid, shapes)


if __name__ == "__main__":
    with open("day12.txt", "r") as f:
        lines = list(line.strip() for line in f.readlines())

        grids = []
        for i in range(len(lines) - 1, -1, -1):
            line = lines[i]
            if len(line) == 0:
                break
            dims, presents = line.split(": ")
            rows, cols = tuple(int(dim) for dim in dims.split("x"))
            grids.append(Grid(
                presents=[int(present) for present in presents.split(" ")],
                rows=rows,
                cols=cols
            ))
        print(grids)

        shapes = {}
        i = 0
        while i < len(lines) - len(grids):
            ident = int(lines[i][:-1])
            present = []
            i += 1
            anchor = i
            while i < len(lines):
                line = lines[i]
                if len(line) == 0:
                    break
                present.extend((i - anchor, col) for col, val in enumerate(line) if val == "#")
                i += 1
            i += 1

            rotations = [present]
            for _ in range(3):
                candidate = [(c, -r) for r, c in rotations[-1]]
                if candidate not in rotations:
                    rotations.append(candidate)
            shapes[ident] = rotations
        pprint(shapes)

        with ProcessPoolExecutor() as executor:
            results = list(executor.map(go, [(i, len(grids), g, shapes) for i, g in enumerate(grids)]))

        print(sum(results))
