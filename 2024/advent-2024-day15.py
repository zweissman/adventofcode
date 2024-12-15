from copy import deepcopy


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    grid: list[list[str]] = []

    for y, row in enumerate(data):
        if row == "":
            directions = "".join(data[y:])
            break
        grid.append(list(row))

    x, y = find_start(grid)
    if debug:
        print(f"Found start at ({x},{y})")
    # The start should be considered empty
    grid[y][x] = "."

    for direction in directions:
        offset = DIRECTION_MAP[direction]
        if debug:
            show(grid, x, y, debug)
            print(f"Moved {direction} from ({x},{y})")

        dx = x + offset[0]
        dy = y + offset[1]
        if grid[dy][dx] == "#":
            continue
        if grid[dy][dx] == ".":
            grid[y][x] = "."
            x = dx
            y = dy
            continue

        assert grid[dy][dx] == "O", f"unknown character at ({dx},{dy}) {grid[dy][dx]}"

        if move1(grid, direction, dx, dy):
            grid[dy][dx] = "."
            x = dx
            y = dy

    results = score(grid, debug)

    return results


def score(grid, debug) -> int:
    results = 0
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value in "[O":
                if debug:
                    print(f"({x}, {y}) = {y * 100 + x}")
                results += y * 100 + x

    return results


def move1(grid: list[list[str]], direction: str, x: int, y: int) -> bool:
    offset = DIRECTION_MAP[direction]

    dx = x + offset[0]
    dy = y + offset[1]

    while True:
        if grid[dy][dx] == "O":
            dx = dx + offset[0]
            dy = dy + offset[1]
            continue
        if grid[dy][dx] == "#":
            return False

        assert grid[dy][dx] == ".", f"unknown character at ({dx},{dy}) {grid[dy][dx]}"
        while not (x == dx and y == dy):
            grid[dy][dx] = grid[dy - offset[1]][dx - offset[0]]
            dx = dx - offset[0]
            dy = dy - offset[1]

        return True

    return False


DIRECTION_MAP = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    grid: list[list[str]] = []

    for y, row in enumerate(data):
        if row == "":
            directions = "".join(data[y:])
            break
        grid.append(list(row))

    grid = adjust_grid_part_2(grid)

    x, y = find_start(grid)
    if debug:
        print(f"Found start at ({x},{y})")
    # The start should be considered empty
    grid[y][x] = "."

    for direction in directions:
        offset = DIRECTION_MAP[direction]
        if debug:
            show(grid, x, y, debug)
            print(f"Moved {direction} from ({x},{y})")

        dx = x + offset[0]
        dy = y + offset[1]
        if grid[dy][dx] == "#":
            continue
        if grid[dy][dx] == ".":
            grid[y][x] = "."
            x = dx
            y = dy
            continue

        assert grid[dy][dx] in "[]", f"unknown character at ({dx},{dy}) {grid[dy][dx]}"

        if direction in "<>":
            if move_horizontal(grid, direction, dx, dy):
                grid[dy][dx] = "."
                x = dx
                y = dy
        else:
            if can_move_vertical(grid, direction, dx, dy, debug):
                move_vertical(grid, direction, dx, dy, debug)
                x = dx
                y = dy

    results = score(grid, debug)
    show(grid, x, y, debug)

    return results


def move_horizontal(grid: list[list[str]], direction: str, x: int, y: int) -> bool:
    offset = DIRECTION_MAP[direction]

    dx = x
    dy = y

    while True:
        dx = dx + offset[0]
        dy = dy + offset[1]
        if grid[dy][dx] in "[]":
            continue
        if grid[dy][dx] == "#":
            return False

        assert grid[dy][dx] == ".", f"unknown character at ({dx},{dy}) {grid[dy][dx]}"
        while not (x == dx and y == dy):
            grid[dy][dx] = grid[dy - offset[1]][dx - offset[0]]
            dx = dx - offset[0]
            dy = dy - offset[1]

        return True

    return False


def move_vertical(grid: list[list[str]], direction: str, x: int, y: int, debug: bool) -> bool:
    points = []
    points.append((x, y))

    if grid[y][x] == "[":
        points.append((x + 1, y))
    elif grid[y][x] == "]":
        points.append((x - 1, y))
    else:
        raise Exception(f"Should not find {grid[y][x]} at ({x},{y}) for move_vertical")

    offset = DIRECTION_MAP[direction]

    for point in points:
        dx = point[0]
        dy = point[1]

        while True:
            dx = dx + offset[0]
            dy = dy + offset[1]
            if grid[dy][dx] == "#":
                return False
            if grid[dy][dx] in "[]":
                can_move = move_vertical(grid, direction, dx, dy, debug)
                if not can_move:
                    return False

            assert grid[dy][dx] == ".", f"unknown character at ({dx},{dy}) {grid[dy][dx]}"
            while not (point[0] == dx and point[1] == dy):
                grid[dy][dx] = grid[dy - offset[1]][dx - offset[0]]
                dx = dx - offset[0]
                dy = dy - offset[1]
                grid[point[1]][point[0]] = "."

            break

    return True


def can_move_vertical(grid: list[list[str]], direction: str, x: int, y: int, debug: bool) -> bool:
    offset = DIRECTION_MAP[direction]

    dx = x + offset[0]
    dy = y + offset[1]

    if grid[y][x] == "#":
        return False
    if grid[y][x] == "[":
        return can_move_vertical(grid, direction, dx, dy, debug) and can_move_vertical(
            grid, direction, dx + 1, dy, debug
        )
    if grid[y][x] == "]":
        return can_move_vertical(grid, direction, dx, dy, debug) and can_move_vertical(
            grid, direction, dx - 1, dy, debug
        )

    return True


def adjust_grid_part_2(grid: list[list[str]]) -> list[list[str]]:
    new_grid = []
    for y in grid:
        row = "".join(y)
        row = row.replace("#", "##")
        row = row.replace("O", "[]")
        row = row.replace(".", "..")
        row = row.replace("@", "@.")
        new_grid.append(list(row))

    return new_grid


def show(grid: list[list[str]], x: int, y: int, debug: bool = False) -> None:
    if debug:
        grid2 = deepcopy(grid)
        grid2[y][x] = "@"

        print()
        for i, row in enumerate(grid2):
            print(i, "".join([str(x) for x in row]))


def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(grid):
        try:
            x = row.index("@")
        except ValueError:
            x = -1

        if x != -1:
            return (x, y)

    return (-1, -1)


if __name__ == "__main__":
    # print("Test1a: ", run(part=1, test_suffix="-test-a", debug=True))  # 2028
    # print("Test1b: ", run(part=1, test_suffix="-test-b", debug=True))  # 10092
    # print("Real1: ", run(part=1, debug=False))  # 1577255
    # print("Test2a: ", run(part=2, test_suffix="-test-a", debug=True))  # 1751
    # print("Test2b: ", run(part=2, test_suffix="-test-b", debug=True))  #  9021
    # print("Test2c: ", run(part=2, test_suffix="-test2c", debug=True))  # 618
    print("Real2: ", run(part=2, debug=False))  # 1597035
