from ortools.sat.python.cp_model import CpModel, CpSolver, OPTIMAL


def solve(buttons, target):
    model = CpModel()

    max_presses_per_slot = max(target)
    the_presses = [model.NewIntVar(0, max_presses_per_slot, f'presses_{i}') for i in range(len(buttons))]
    for i, required_slot_score in enumerate(target):
        the_score_per_slot = sum(the_press * button[i] for the_press, button in zip(the_presses, buttons))
        model.Add(the_score_per_slot == required_slot_score)

    all_presses = model.NewIntVar(0, max_presses_per_slot * len(buttons), 'all_presses')
    model.Add(all_presses == sum(the_presses))
    model.Minimize(all_presses)

    solver = CpSolver()
    result_code = solver.Solve(model)
    assert result_code == OPTIMAL

    return solver.Value(all_presses)


scores = []
with open("day10.txt", "r") as f:
    raw = list(f.readlines())
    sections = [tuple(c for c in line.strip().split(" ")) for line in raw]
    for section in sections:
        in_target = tuple(int(p) for p in section[-1][1:-1].split(","))
        raw_buttons = [set(int(c) for c in str(p[1:-1]).split(",")) for p in section[1:-1]]
        in_buttons = [tuple(int(i in button) for i in range(len(in_target))) for button in raw_buttons]

        result = solve(in_buttons, in_target)
        scores.append(result)

print(sum(scores))
