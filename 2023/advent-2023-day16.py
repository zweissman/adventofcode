# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,too-many-arguments
# pylint: disable=duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

from typing import Optional

FILE_NAME = "2023/input/16.txt"


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def show(grid: list[list[str]], debug: bool = False):
    if debug:
        print()
        for y in range(len(grid)):
            print("".join([str(x) for x in grid[y]]))


def show_score(grid: list[list[int]], debug: bool = False):
    if debug:
        print()
        for y in range(len(grid)):
            print("".join([str(x) for x in grid[y]]))


def part1(data: list[str], debug: bool = False) -> int:
    grid = []

    for d in data:
        d = d.strip()
        grid.append(list(d))

    show(grid, debug)

    start = (0, 0, "E")
    return init_run(grid, data, start, debug)


def part2(data: list[str], debug: bool = False) -> int:
    grid = []

    for d in data:
        d = d.strip()
        grid.append(list(d))

    show(grid, debug)

    max_energy = 0
    y = 0
    direction = "S"
    for x in range(len(grid[y])):
        start = (x, y, direction)
        result = init_run(grid, data, start, debug)
        if max_energy < result:
            print(f"({x}, {y}) {direction} {max_energy=}")

            max_energy = result

    y = len(grid) - 1
    direction = "N"
    for x in range(len(grid[y])):
        start = (x, y, direction)
        result = init_run(grid, data, start, debug)
        if max_energy < result:
            print(f"({x}, {y}) {direction} {max_energy=}")

            max_energy = result

    x = 0
    direction = "E"
    for y in range(len(grid)):
        start = (x, y, direction)
        result = init_run(grid, data, start, debug)
        if max_energy < result:
            print(f"({x}, {y}) {direction} {max_energy=}")

            max_energy = result

    x = len(grid[0]) - 1
    direction = "W"
    for y in range(len(grid)):
        start = (x, y, direction)
        result = init_run(grid, data, start, debug)
        if max_energy < result:
            print(f"({x}, {y}) {direction} {max_energy=}")

            max_energy = result

    return max_energy


def init_run(grid, data, start, debug) -> int:
    results = 0

    score = [[0] * len(data[0]) for _ in range(len(grid))]

    to_visit = []
    to_visit.append(start)

    while len(to_visit) > 0:
        x, y, direction = to_visit.pop(0)

        show_score(score, debug)

        try:
            new_direction = move(grid, x, y, direction, score[y][x], debug)
        except IndexError:
            new_direction = None

        if not new_direction:
            continue

        score[y][x] = 1

        for direction in new_direction:
            new_x = x
            new_y = y
            if "N" == direction:
                new_y = y - 1
            elif "S" == direction:
                new_y = y + 1
            elif "W" == direction:
                new_x = x - 1
            elif "E" == direction:
                new_x = x + 1

            to_visit.append((new_x, new_y, direction))

    results = sum(map(sum, score))

    return results


# @functools.cache
def move(
    grid: list[list[str]], x: int, y: int, direction: str, c_score: int, debug: bool
) -> Optional[str]:
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return None

    c = grid[y][x]

    new_direction = ""

    if c == ".":
        new_direction = direction

    elif c == "/":
        if direction == "N":
            new_direction = "E"
        elif direction == "S":
            new_direction = "W"
        elif direction == "W":
            new_direction = "S"
        elif direction == "E":
            new_direction = "N"

    elif c == "\\":
        if direction == "N":
            new_direction = "W"
        elif direction == "S":
            new_direction = "E"
        elif direction == "W":
            new_direction = "N"
        elif direction == "E":
            new_direction = "S"

    elif c == "-":
        if direction in "NS":
            if c_score >= 1:
                # We've been here already. Keep out of a loop
                return None
            new_direction = "WE"
        elif direction in "WE":
            new_direction = direction

    elif c == "|":
        if direction in "NS":
            new_direction = direction
        elif direction in "WE":
            if c_score >= 1:
                # We've been here already. Keep out of a loop
                return None
            new_direction = "NS"

    if debug:
        print(f"({x}, {y}) {direction} -> {new_direction}")

    return new_direction


if __name__ == "__main__":
    print("Test1: ", run(part=1, test_run=True, debug=True))  # 46
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 7884
    print("Test2: ", run(part=2, test_run=True, debug=True))  # 51
    # print("Real2: ", run(part=2, test_run=False, debug=False))  #
